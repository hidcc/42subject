#!/usr/bin/env python3
"""
Cosmic Data Observatory - バリデーション演習

data_generator.py に暗黙的に埋め込まれたルールを Pydantic モデルとして定義し、
generated_data/ の JSON ファイルを検証する。

期待される結果:
  - space_stations.json / alien_contacts.json / space_missions.json → 全件パス
  - invalid_stations.json / invalid_contacts.json → 全件エラーで弾かれる

実行前に: pip3 install pydantic
"""

import json
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Literal, Optional

try:
    from pydantic import BaseModel, Field, ValidationError, model_validator
except ImportError:
    print("❌ pydantic がインストールされていません。先に以下を実行してください:")
    print("   pip3 install pydantic")
    sys.exit(1)


# ============================================================
# 演習1: 宇宙ステーション
# ルール（data_generator.py の生成ロジックから逆算）:
#   - station_id: 英大文字3文字 + 数字3桁 (例: ISS123)
#   - name: 空文字禁止
#   - crew_size: 1〜12人
#   - power_level / oxygen_level: 0〜100%
#   - is_operational=True なら power > 75 かつ oxygen > 90 のはず
# ============================================================
class SpaceStation(BaseModel):
    station_id: str = Field(pattern=r"^[A-Z]{3}\d{3}$")
    name: str = Field(min_length=1)
    crew_size: int = Field(ge=1, le=12)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool
    notes: Optional[str] = None

    @model_validator(mode="after")
    def check_operational_consistency(self) -> "SpaceStation":
        if self.is_operational and not (self.power_level > 75.0 and self.oxygen_level > 90.0):
            raise ValueError(
                "is_operational=True なのに power_level <= 75 または oxygen_level <= 90"
            )
        return self


# ============================================================
# 演習2: エイリアンコンタクト
# ルール:
#   - contact_id: "AC_西暦4桁_連番3桁" 形式 (例: AC_2024_001)
#   - contact_type: 4種類のいずれか
#   - signal_strength: 1.0〜10.0
#   - duration_minutes / witness_count: 正の整数
#   - telepathic（テレパシー）接触は目撃者3人以上
#   - physical（物理）接触は必ず is_verified=True
# ============================================================
class AlienContact(BaseModel):
    contact_id: str = Field(pattern=r"^AC_\d{4}_\d{3}$")
    timestamp: datetime
    location: str = Field(min_length=1)
    contact_type: Literal["radio", "visual", "physical", "telepathic"]
    signal_strength: float = Field(ge=1.0, le=10.0)
    duration_minutes: int = Field(gt=0)
    witness_count: int = Field(ge=1)
    message_received: Optional[str] = None
    is_verified: bool

    @model_validator(mode="after")
    def check_contact_rules(self) -> "AlienContact":
        if self.contact_type == "telepathic" and self.witness_count < 3:
            raise ValueError("telepathic 接触は目撃者が3人以上必要")
        if self.contact_type == "physical" and not self.is_verified:
            raise ValueError("physical 接触は必ず検証済み (is_verified=True) のはず")
        return self


# ============================================================
# 演習3: クルー & ミッション（ネスト構造）
# ルール:
#   - member_id: "CM" + 数字3桁
#   - rank: 5階級のいずれか
#   - crew: 3〜8人、かつ captain か commander が最低1人
#   - 365日超の長期ミッションは経験5年以上のクルーが半数以上
# ============================================================
class CrewMember(BaseModel):
    member_id: str = Field(pattern=r"^CM\d{3}$")
    name: str = Field(min_length=1)
    rank: Literal["cadet", "officer", "lieutenant", "captain", "commander"]
    age: int = Field(ge=18, le=70)
    specialization: str = Field(min_length=1)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool


class SpaceMission(BaseModel):
    mission_id: str = Field(pattern=r"^M\d{4}_(MARS|LUNA|EUROPA|TITAN)$")
    mission_name: str = Field(min_length=1)
    destination: str = Field(min_length=1)
    launch_date: datetime
    duration_days: int = Field(gt=0)
    crew: List[CrewMember] = Field(min_length=3, max_length=8)
    mission_status: Literal["planned", "active", "completed", "aborted"]
    budget_millions: float = Field(gt=0)

    @model_validator(mode="after")
    def check_mission_rules(self) -> "SpaceMission":
        if not any(m.rank in ("captain", "commander") for m in self.crew):
            raise ValueError("captain または commander が最低1人必要")
        if self.duration_days > 365:
            experienced = sum(1 for m in self.crew if m.years_experience >= 5)
            if experienced < len(self.crew) // 2:
                raise ValueError("長期ミッションは経験5年以上のクルーが半数以上必要")
        return self


# ============================================================
# 検証ランナー
# ============================================================
def validate_file(filepath: Path, model: type[BaseModel], expect_valid: bool) -> bool:
    """JSONファイルの全レコードを検証し、期待どおりの結果かを返す"""
    print(f"\n📄 {filepath.name}（期待: {'全件パス ✅' if expect_valid else '全件エラー ❌'}）")

    if not filepath.exists():
        print(f"  ⚠️  ファイルが見つかりません。先に python3 data_exporter.py を実行してください")
        return False

    records = json.loads(filepath.read_text(encoding="utf-8"))
    all_as_expected = True

    for i, record in enumerate(records):
        label = record.get("station_id") or record.get("contact_id") or record.get("mission_id") or f"#{i}"
        try:
            model.model_validate(record)
            if expect_valid:
                print(f"  ✅ {label}: OK")
            else:
                print(f"  🚨 {label}: 不正データなのにパスしてしまった！（モデルのルール不足）")
                all_as_expected = False
        except ValidationError as e:
            if expect_valid:
                print(f"  🚨 {label}: 正常データなのにエラー！")
                all_as_expected = False
            else:
                print(f"  ❌ {label}: 期待どおり拒否（{e.error_count()}件のエラー）")
            for err in e.errors():
                loc = ".".join(str(x) for x in err["loc"]) or "(model)"
                print(f"       └ {loc}: {err['msg']}")

    return all_as_expected


def main():
    data_dir = Path(__file__).parent / "generated_data"

    print("🛸 Cosmic Data Observatory - バリデーション演習")
    print("=" * 60)

    results = [
        # 正常データ → 全件パスするはず
        validate_file(data_dir / "space_stations.json", SpaceStation, expect_valid=True),
        validate_file(data_dir / "alien_contacts.json", AlienContact, expect_valid=True),
        validate_file(data_dir / "space_missions.json", SpaceMission, expect_valid=True),
        # 不正データ → 全件エラーになるはず
        validate_file(data_dir / "invalid_stations.json", SpaceStation, expect_valid=False),
        validate_file(data_dir / "invalid_contacts.json", AlienContact, expect_valid=False),
    ]

    print("\n" + "=" * 60)
    if all(results):
        print("🎉 全ファイルが期待どおりの結果！バリデーションモデルは完成です")
    else:
        print("🔧 期待と違う結果あり。モデルのルールを見直してみましょう")
        sys.exit(1)


if __name__ == "__main__":
    main()

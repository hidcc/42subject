from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field()
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    user = SpaceStation(
        station_id="ISS001", name="International Space Station",
        crew_size=6, power_level=85.5, oxygen_level=92.3, last_maintenance=date.today(), is_operational=True)
    print("Valid station created:")
    print(f"ID: {user.station_id}")
    print(f"Name: {user.name}")
    print(f"Crew: {user.crew_size} poeple")
    print(f"Power: {user.power_level}%")
    print(f"Oxygen: {user.oxygen_level}%")
    if user.is_operational:
        print(f"Status: Operational")
    print()
    print("========================================")
    print("Expected validation error:")
    try:
        user = SpaceStation(
            station_id="ISS001", name="International Space Station",
            crew_size=21, power_level=85.5, oxygen_level=92.3, last_maintenance=date.today(), is_operational=True)
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()

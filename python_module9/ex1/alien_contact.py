from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Optional


class ContactType(str, Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def validate_contact(self) -> "AlienContact":
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        if self.contact_type == ContactType.telepathic and self.witness_count < 3:
            raise ValueError(
                "Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0 and self.message_received is None:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages")
        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("========================================")
    user = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2024-06-06T12:00:00",
        location="Area 51, Nevada",
        contact_type=ContactType.radio,
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="'Greetings from Zeta Reticuli'",
    )
    print("Valid contact report:")
    print(f"ID: {user.contact_id}")
    print(f"Type: {user.contact_type.value}")
    print(f"Location: {user.location}")
    print(f"Signal: {user.signal_strength}/10")
    print(f"Duration: {user.duration_minutes} minutes")
    print(f"Witnesses: {user.witness_count}")
    print(f"Message: {user.message_received}")
    print()
    print("========================================")
    print("Expected validation error:")
    try:
        user = AlienContact(
            contact_id="AC_2024_001", timestamp=ContactType.radio,
            location="Area 51, Nevada", signal_strength=8.5, duration_minutes=45, witness_count=2,
            message_received="'Greetings from Zeta Reticuli'")
    except ValidationError as e:
        for error in e.errors():
            print(error["msg"])


if __name__ == "__main__":
    main()

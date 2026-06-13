"""Parser error type."""


class ParseError(Exception):
    """Raised when the input map text is syntactically or semantically invalid.

    Carries the offending line number and a human-readable reason so the program
    can stop with a clear message (subject requirement: report line and cause).
    """

    def __init__(self, line_no: int, reason: str) -> None:
        """Store the offending 1-based line number and the reason."""
        self.line_no = line_no
        self.reason = reason
        super().__init__(f"line {line_no}: {reason}")

from dataclasses import dataclass

@dataclass
class _BaseDevice:
    rank: str
    model: str
    setup: str
    signature: str
    tone_grade: str
    value_rating: str
    technical_grade: str
    price: int

@dataclass
class IEM(_BaseDevice):
    type: str = "IEM"

@dataclass
class Headphone(_BaseDevice):
    type: str = "Headphone"

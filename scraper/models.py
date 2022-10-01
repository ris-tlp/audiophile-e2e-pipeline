from dataclasses import dataclass, asdict


@dataclass(init=False)
class InEarMonitor:
    """
    Dataclass containing attributes for InEarMonitors.
    """

    rank: str
    model: str
    signature: str
    tone_grade: str
    driver_type: str
    value_rating: str
    technical_grade: str
    price: int

    def __init__(self, iem_data: dict) -> None:
        if "Setup" in iem_data:
            self.driver_type = iem_data["Setup"]

        self.rank = iem_data["Rank"]
        self.model = iem_data["Model"]
        self.signature = iem_data["Signature"]
        self.tone_grade = iem_data["Tone Grade"]
        self.value_rating = iem_data["Value Rating"]
        self.technical_grade = iem_data["Technical Grade"]
        self.price = iem_data["Price (MSRP)"]


@dataclass(init=False)
class Headphone(InEarMonitor):
    """Dataclass containing attributes for Headphones.

    Args:
        InEarMonitor (InEarMonitor): subclasses the InEarMonitor class
    """

    cup_type: str

    def __init__(self, headphone_data: dict) -> None:
        super().__init__(headphone_data)
        self.driver_type = headphone_data["Driver Type"]
        self.cup_type = headphone_data["Fit/Cup Type"]

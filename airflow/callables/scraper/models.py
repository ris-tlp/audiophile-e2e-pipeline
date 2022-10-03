from pydantic import BaseModel


class InEarMonitor(BaseModel):
    """
    Pydantic model containing attributes for InEarMonitors.
    """

    rank: str
    model: str
    signature: str
    tone_grade: str
    driver_type: str
    value_rating: str
    technical_grade: str
    price: int


class Headphone(InEarMonitor):
    """
    Pydantic model containing attributes for Headphones.

    Args:
        InEarMonitor (InEarMonitor): subclasses the InEarMonitor class
    """

    fit_cup: str

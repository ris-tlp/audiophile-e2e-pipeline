from pydantic import BaseModel, validator


def grade_atmost_2_chars(rank: str) -> bool:
    """
    Reusable method to validate fields based on the letter grade convention
    """
    return len(rank) > 2


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

    # Ensure all fields with a convention of letter grades does not exceed two characters
    _ensure_rank_max_2_chars = validator("rank", allow_reuse=True)(grade_atmost_2_chars)
    _ensure_tonegrade_max_2_chars = validator("tone_grade", allow_reuse=True)(grade_atmost_2_chars)
    _ensure_technicalgrade_max_2_chars = validator("technical_grade", allow_reuse=True)(
        grade_atmost_2_chars
    )

    @validator("model")
    def model_must_contain_space(cls, model):
        """
        Model containing spaces signify company name at the start
        """
        print(model)
        if " " not in model:
            raise ValueError("Model must contain a space")
        return model.title()


class Headphone(InEarMonitor):
    """
    Pydantic model containing attributes for Headphones.

    Args:
        InEarMonitor (InEarMonitor): subclasses the InEarMonitor class
    """

    fit_cup: str

from pydantic import BaseModel, ConfigDict


class TripCreate(BaseModel):
    destination: str
    country: str
    days: int
    budget: int
    is_completed: bool = False


class TripResponse(BaseModel):
    id: int
    destination: str
    country: str
    days: int
    budget: int
    is_completed: bool

    model_config = ConfigDict(from_attributes=True)
from pydantic import BaseModel
from typing import Optional
class ClientBase(BaseModel):
    name: Optional[str] = None
    subject: Optional[str] = None
    hour_price: Optional[int] = None
    duration: Optional[float] = None
    is_active: Optional[bool] = True
    day: Optional[str] = None
    description: Optional[str] = None


class CreateClient(ClientBase):
    name: str
    subject: str
    hour_price: int
    duration: int
    day: str
    description: str


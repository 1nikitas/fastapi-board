from pydantic import BaseModel
from typing import Optional
class ClientBase(BaseModel):
    name: Optional[str] = None
    subject: Optional[str] = None
    hour_price: Optional[int] = None
    is_active: Optional[bool] = True
    day: Optional[str] = None
    description: Optional[str] = None



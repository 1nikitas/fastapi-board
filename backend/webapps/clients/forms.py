from typing import Optional
from fastapi import Request
from typing import List


class ClientCreateForm:

    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.name: Optional[str] = None
        self.subject: Optional[str] = None
        self.hour_price: Optional[int] = None
        self.duration: Optional[float] = None
        self.is_active: Optional[bool] = True
        self.time: Optional[str] = None
        self.day: Optional[str] = None
        self.description: Optional[str] = ""

    def is_valid(self):
        if not self.name:
            self.errors.append("No name")
        if not self.subject:
            self.errors.append("No subject")
        if not self.hour_price:
            self.errors.append("No hour price")
        if not self.duration:
            self.errors.append("No duration")
        if not self.hour_price:
            self.errors.append("No hour price")
        if not self.day:
            self.errors.append("No hour price")
        if not self.description:
            self.errors.append("No hour price")
        if not self.time:
            self.errors.append('No time')
        if not self.errors:
            return True
        return False

    async def load_data(self):
        form = await self.request.form()
        self.name = form.get('name')
        self.subject = form.get('subject')
        self.hour_price = form.get('hour_price')
        self.duration = form.get('duration')
        self.is_active = True
        self.time = form.get('time')
        self.day = form.get('day')
        self.description = form.get('description')

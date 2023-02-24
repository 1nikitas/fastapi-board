from typing import List
from typing import Optional

from fastapi import Request


class TaskCreateForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.title: Optional[str] = None
        self.subject: Optional[str] = None
        self.soft_deadline: Optional[str] = None
        self.deadline: Optional[str] = None
        self.assigned_to: Optional[str] = None
        self.description: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get('title')
        self.subject= form.get('subject')
        self.soft_deadline= form.get('soft_deadline')
        self.deadline= form.get('deadline')
        self.assigned_to= form.get('assigned_to')
        self.description= form.get('description')

    def is_valid(self):
        # if not self.title or not len(self.title) >= 4:
        #     self.errors.append("A valid title is required")
        # if not self.company_url or not (self.company_url.__contains__("http")):
        #     self.errors.append("Valid Url is required e.g. https://example.com")
        # if not self.company or not len(self.company) >= 1:
        #     self.errors.append("A valid company is required")
        # if not self.description or not len(self.description) >= 20:
        #     self.errors.append("Description too short")
        if not self.errors:
            return True
        return False

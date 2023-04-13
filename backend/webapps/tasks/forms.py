from typing import List, Optional
from fastapi import Request, UploadFile
from aiofiles import open


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
        self.files: Optional[List[UploadFile]] = None

    async def load_data(self):
        form = await self.request.form()
        self.title = form.get('title')
        self.subject= form.get('subject')
        self.soft_deadline= form.get('soft_deadline')
        self.deadline= form.get('deadline')
        self.assigned_to= form.get('assigned_to')
        self.description= form.get('description')
        self.files = form.getlist('files')

    async def save_files(self) -> List[str]:
        saved_files = []
        if self.files:
            for file in self.files:
                contents = await file.read()
                async with open(file.filename, 'wb') as f:
                    await f.write(contents)
                saved_files.append(file.filename)
        return saved_files

    def is_valid(self):
        if not self.title or not len(self.title) >= 4:
            self.errors.append("A valid title is required")
        if not self.subject or not len(self.subject) >= 1:
            self.errors.append("A valid subject is required")
        if not self.soft_deadline:
            self.errors.append("A valid soft deadline is required")
        if not self.deadline:
            self.errors.append("A valid deadline is required")
        if not self.description or not len(self.description) >= 20:
            self.errors.append("Description too short")
        if not self.errors:
            return True
        return False

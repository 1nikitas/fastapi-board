import os
from typing import Optional, List

from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.tasks import create_new_task, tasks_assigned_to_me
from db.repository.tasks import list_tasks
from db.repository.tasks import retreive_task
from db.repository.tasks import search_task
from db.session import get_db
from fastapi import APIRouter, UploadFile, File
from fastapi import Depends
from fastapi import Request
from fastapi import Response
from fastapi import responses
from fastapi import status
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.templating import Jinja2Templates
from schemas.tasks import TaskCreate
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse
from webapps.tasks.forms import TaskCreateForm
from fastapi.responses import RedirectResponse
from db.repository.clients import list_clients
from fastapi.responses import FileResponse


templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)




def is_authorized(request: Request):
    if request.cookies.get("access_token"):
        return True
    return False

@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    print(request.__dict__)
    if request.cookies.get("access_token"):
        token = request.cookies.get('access_token').split()[1]
        id = get_current_user_from_token(token=token, db=db).id
        tasks = tasks_assigned_to_me(id=id, db=db)
        return templates.TemplateResponse(
            "general_pages/homepage.html", {"request": request, "tasks": tasks, "msg": msg, 'logged': True}
        )
    else:
        return responses.RedirectResponse(
            f"/login/", status_code=status.HTTP_302_FOUND
        )

@router.post('/update-task-status/')
async def update_task_status(request: Request):
    print(await request.json())

@router.get("/logout")
async def logout(request: Request, response: Response, msg: str = None):
    response = RedirectResponse(
            f"/login/", status_code=status.HTTP_302_FOUND
        )
    response.delete_cookie("access_token")
    return response

from fastapi import FastAPI
from fastapi.responses import FileResponse


@router.get("/file/{filename}")
async def read_file(filename: str):
    return FileResponse(filename)


@router.get("/details/{id}")
def task_detail(id: int, request: Request, db: Session = Depends(get_db)):
    user_is_authorized = is_authorized(request)
    task = retreive_task(id=id, db=db)
    return templates.TemplateResponse(
        "tasks/detail.html", {"request": request, "task": task, 'logged': user_is_authorized}
    )

from fastapi import UploadFile

async def save_file_to_disk(file: UploadFile) -> str:
    contents = await file.read()
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(contents)
    return file_path



@router.get("/post-a-task/")
def create_task(request: Request, db: Session = Depends(get_db)):
    user_is_authorized = is_authorized(request)
    all_clients = list_clients(db=db)
    return templates.TemplateResponse("tasks/create_task.html", {"request": request, "all_clients": all_clients,  'logged': user_is_authorized})


@router.post("/post-a-task/")
async def create_task(request: Request, db: Session = Depends(get_db)):
    form = TaskCreateForm(request)
    print(form.__dict__)
    await form.load_data()
    if form.is_valid():
        try:
            token = request.cookies.get("access_token")
            scheme, param = get_authorization_scheme_param(
                token
            )  # scheme will hold "Bearer" and param will hold actual token value
            current_user: User = get_current_user_from_token(token=param, db=db)
            print(form.__dict__)
            task = TaskCreate(**form.__dict__)
            task = create_new_task(task=task, db=db, owner_id=current_user.id)
            return responses.RedirectResponse(
                f"/details/{task.id}", status_code=status.HTTP_302_FOUND
            )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in, In case problem persists please contact us."
            )
            return templates.TemplateResponse("tasks/create_task.html", form.__dict__)
    return templates.TemplateResponse("tasks/create_task.html", form.__dict__)


@router.get("/download/{file_path:path}")
async def download_file(file_path: str):
    return FileResponse(file_path)


@router.get("/delete-task/")
def show_tasks_to_delete(request: Request, db: Session = Depends(get_db)):
    user_is_authorized = is_authorized(request)
    tasks = list_tasks(db=db)
    return templates.TemplateResponse(
        "tasks/show_tasks_to_delete.html", {"request": request, "tasks": tasks,   'logged': user_is_authorized}
    )


@router.get("/search/")
def search(
    request: Request, db: Session = Depends(get_db), query: Optional[str] = None
):
    user_is_authorized = is_authorized(request)
    tasks = search_task(query, db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "tasks": tasks,   'logged': user_is_authorized}
    )

@router.get("/all-homeworks/")
def get_all_homeworks(request: Request, db: Session = Depends(get_db)):
    tasks  = list_tasks(db=db)
    user_is_authorized = is_authorized(request)
    return templates.TemplateResponse('general_pages/homepage.html',
                                      {'request': request,
                                       'logged': user_is_authorized,
                                       'tasks': tasks})

@router.get("/all-homeworks/details/{id}")
def task_detail(id: int, request: Request, db: Session = Depends(get_db)):
    user_is_authorized = is_authorized(request)
    task = retreive_task(id=id, db=db)
    return templates.TemplateResponse(
        "tasks/detail.html", {"request": request, "task": task, 'logged': user_is_authorized}
    )


from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@router.get("/uploadfile/")
async def create_upload_file(request: Request):
    return templates.TemplateResponse(
        "tasks/create_task.html", {'request': request})

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    with open(file.filename, "wb") as f:
        f.write(contents)
    return {"filename": file.filename}

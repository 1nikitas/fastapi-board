from typing import Optional
from apis.version1.route_login import get_current_user_from_token
from db.models.users import User
from db.repository.tasks import create_new_task
from db.repository.tasks import list_tasks
from db.repository.tasks import retreive_task
from db.repository.tasks import search_task
from db.session import get_db
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Request
from fastapi import Response
from fastapi import responses
from fastapi import status
from fastapi.security.utils import get_authorization_scheme_param
from fastapi.templating import Jinja2Templates
from schemas.tasks import TaskCreate
from sqlalchemy.orm import Session
from webapps.tasks.forms import TaskCreateForm
from fastapi.responses import RedirectResponse
from db.repository.clients import list_clients

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    print(request.__dict__)
    if request.cookies.get("access_token"):
        tasks = list_tasks(db=db)
        return templates.TemplateResponse(
            "general_pages/homepage.html", {"request": request, "tasks": tasks, "msg": msg, 'logged': True}
        )
    else:

        return responses.RedirectResponse(
            f"/login/", status_code=status.HTTP_302_FOUND
        )

@router.get("/logout")
async def logout(request: Request, response: Response, msg: str = None):
    response = RedirectResponse(
            f"/login/", status_code=status.HTTP_302_FOUND
        )
    response.delete_cookie("access_token")
    return response




@router.get("/details/{id}")
def task_detail(id: int, request: Request, db: Session = Depends(get_db)):
    task = retreive_task(id=id, db=db)
    return templates.TemplateResponse(
        "tasks/detail.html", {"request": request, "task": task}
    )


@router.get("/post-a-task/")
def create_task(request: Request, db: Session = Depends(get_db)):
    all_clients = list_clients(db=db)
    return templates.TemplateResponse("tasks/create_task.html", {"request": request, "all_clients": all_clients })


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


@router.get("/delete-task/")
def show_tasks_to_delete(request: Request, db: Session = Depends(get_db)):
    tasks = list_tasks(db=db)
    return templates.TemplateResponse(
        "tasks/show_tasks_to_delete.html", {"request": request, "tasks": tasks}
    )


@router.get("/search/")
def search(
    request: Request, db: Session = Depends(get_db), query: Optional[str] = None
):
    tasks = search_task(query, db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request": request, "tasks": tasks}
    )

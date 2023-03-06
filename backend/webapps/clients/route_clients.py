from fastapi import APIRouter, Depends, HTTPException

from apis.version1.base import is_authorized
from db.repository.clients import list_clients, deactivate_client_by_id, activate_client_by_id, \
    get_today_clients_amount, get_today_money_amount, get_today_lesson_time, get_cliet_by_id
from fastapi import Request
from db.session import get_db
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from webapps.clients.forms import ClientCreateForm
from apis.version1.route_login import get_current_user_from_token
from fastapi import status
from db.repository.clients import create_client
from schemas.clients import CreateClient
from fastapi import responses
from db.models.clients import Client
from db.repository.clients import delete_client_by_id, get_today_clients, get_all_active_clients

router = APIRouter()
templates = Jinja2Templates(directory='templates')

@router.get('/clients/create/')
def client_create(request: Request):
    user_is_authorized = is_authorized(request)
    return templates.TemplateResponse('clients/create_client.html', {'request': request, "logged": user_is_authorized})

@router.get("/clients")
#note: добавить проверку на авторизация -> редирект на логин.html
def clients(request: Request, db: Session = Depends(get_db)):
    user_is_authorized= is_authorized(request)
    token = request.cookies.get('access_token')
    if not token:
        return RedirectResponse('general_pages/homepage.html', status_code=status.HTTP_405_METHOD_NOT_ALLOWED)

    token = token.split()[1]
    user = get_current_user_from_token(token, db)
    if user.is_superuser:
        all_clients = list_clients(db)
        return templates.TemplateResponse('clients/clients.html', {'request': request, "all_clients": all_clients, "logged": user_is_authorized})
    else:
        #response = RedirectResponse('general_pages/homepage', status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
        return templates.TemplateResponse('general_pages/homepage.html', {'request': request, 'msg': 'Not allowed!'})




@router.post('/clients/create/')
async def create_clients(request: Request, db: Session = Depends(get_db)):
    user_is_authorized = is_authorized(request)
    form = ClientCreateForm(request)
    await form.load_data()
    if form.is_valid():
        print(1)
        try:
            client = CreateClient(**form.__dict__)
            new_client = create_client(client=client, db=db)
            return templates.TemplateResponse("clients/client_details.html", {
                "request":request,
                 'msg': "student added!",
                'client': new_client,
                'logged': user_is_authorized
            })
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in, In case problem persists please contact us."
            )
            return templates.TemplateResponse("clients/create_client.html", form.__dict__)
    else:
        return templates.TemplateResponse("clients/create_client.html", form.__dict__)

@router.get('/clients/deactivate/{id}/')
async def deactivate(id: int, request: Request, db: Session = Depends(get_db)):
    message = deactivate_client_by_id(id=id, db=db)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found"
        )
    return responses.RedirectResponse('/clients')

@router.get('/clients/activate/{id}/')
async def activate(id: int, request: Request, db: Session = Depends(get_db)):
    message = activate_client_by_id(id=id, db=db)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found"
        )
    return responses.RedirectResponse('/clients')

@router.get('/clients/delete/{id}')
async def delete_user(id: int, request: Request, db: Session = Depends(get_db)):
    message = delete_client_by_id(id=id, db=db)
    if not message:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Task with id {id} not found"
        )
    return responses.RedirectResponse('/clients')


@router.get('/clients/today')
def today_clients(request: Request, db: Session = Depends(get_db)):
    clients = get_today_clients(db=db)
    user_is_authorized = is_authorized(request)
    amount = get_today_clients_amount(db=db)
    money = get_today_money_amount(db=db)
    sum_time = get_today_lesson_time(db=db)
    return templates.TemplateResponse('clients/today_clients.html',
                                      {'request': request,
                                       "logged": user_is_authorized,
                                       "clients": clients,
                                       "money": money,
                                       "amount": amount,
                                       'sum_time': sum_time})
@router.get('/clients/info/{id}')
def get_client_info(id: int, request: Request, db: Session = Depends(get_db)):
    user_is_authorized = is_authorized(request)
    client = get_cliet_by_id(id=id, db=db)
    print(client)
    return templates.TemplateResponse('clients/client_details.html',
                                      {'request': request,
                                       "logged": user_is_authorized,
                                       'client': client
                                       })


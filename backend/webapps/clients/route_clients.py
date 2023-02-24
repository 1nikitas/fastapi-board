from fastapi import APIRouter, Depends, HTTPException
from db.repository.clients import list_clients, deactivate_client_by_id, activate_client_by_id
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

router = APIRouter()
templates = Jinja2Templates(directory='templates')

@router.get('/clients/create/')
def client_create(request: Request):
    return templates.TemplateResponse('clients/create_client.html', {'request': request})

@router.get("/clients")
#note: добавить проверку на авторизация -> редирект на логин.html
def clients(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get('access_token')
    if not token:
        return RedirectResponse('general_pages/homepage.html', status_code=status.HTTP_405_METHOD_NOT_ALLOWED)

    token = token.split()[1]
    user = get_current_user_from_token(token, db)
    print(user.__dict__)
    if user.is_superuser:
        all_clients = list_clients(db)
        print(all_clients)
        return templates.TemplateResponse('clients/clients.html', {'request': request, "all_clients": all_clients})
    else:
        #response = RedirectResponse('general_pages/homepage', status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
        return templates.TemplateResponse('general_pages/homepage.html', {'request': request, 'msg': 'Not allowed!'})




@router.post('/clients/create/')
async def create_clients(request: Request, db: Session = Depends(get_db)):
    print(await request.form())
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
                'client': new_client
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
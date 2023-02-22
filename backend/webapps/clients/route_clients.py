from fastapi import APIRouter, Depends
from db.repository.clients import list_clients
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

router = APIRouter()
templates = Jinja2Templates(directory='templates')

@router.get('/clients/create/')
def client_create(request: Request):
    return templates.TemplateResponse('clients/create_client.html', {'request': request})

@router.get("/clients")
def clients(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get('access_token')
    if not token:
        return RedirectResponse('general_pages/homepage', status_code=status.HTTP_405_METHOD_NOT_ALLOWED)

    token = token.split()[1]
    user = get_current_user_from_token(token, db)
    if user.is_superuser:
        all_clients = list_clients(db)
        print(all_clients)
        return templates.TemplateResponse('clients/clients.html', {'request': request, "all_clients": all_clients})
    else:
        response = RedirectResponse('general_pages/homepage', status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
        return response




@router.post('/clients/create/')
async def create(request: Request, db: Session = Depends(get_db)):
    form = ClientCreateForm(request)
    await form.load_data()
    if form.is_valid():
        print(form.__dict__)
        client = CreateClient(**form.__dict__)

        client = create_client(client=client, db=db)
        return {"client": client}

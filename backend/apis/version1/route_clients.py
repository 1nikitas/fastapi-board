from fastapi import APIRouter, Depends
from starlette.templating import Jinja2Templates
from db.session import get_db
from schemas.clients import ClientBase
from sqlalchemy.orm import Session

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.post('/create/', response_model=ClientBase)
def create_client(
        client: ClientBase,
        db: Session = Depends(get_db)
):
    client = create_new_client(client=client, db=db)
    return client

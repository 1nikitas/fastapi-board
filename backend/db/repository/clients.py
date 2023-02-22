from schemas.clients import CreateClient
from sqlalchemy.orm import Session
from db.models.clients import Client

def create_client(client: Client, db: Session):
    client_obj = CreateClient(**client.dict())
    db.add(client_obj)
    db.commit()
    db.refresh(client_obj)
    return client_obj

def list_clients(db: Session):
    clients = db.query(Client).all()
    return clients
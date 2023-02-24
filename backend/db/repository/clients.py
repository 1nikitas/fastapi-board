from schemas.clients import CreateClient
from sqlalchemy.orm import Session
from db.models.clients import Client

def create_client(client: CreateClient, db: Session):
    client_obj = Client(**client.dict())
    db.add(client_obj)
    db.commit()
    print('added!')
    return client_obj

def list_clients(db: Session):
    clients = db.query(Client).all()
    return clients

def delete_client_by_id(id: int, db: Session):
    existion_client = db.query(Client).filter(Client.id == id)
    if not existion_client:
        return 0
    existion_client.delete(synchronize_session=False)
    db.commit()
    return 1

def deactivate_client_by_id(id: int, db: Session):
    client = db.query(Client).filter(Client.id == id)
    if not client.first():
        return 0
    client.update({'is_active': False})
    db.commit()
    return 1
def activate_client_by_id(id: int, db: Session):
    client = db.query(Client).filter(Client.id == id)
    if not client.first():
        return 0
    client.update({'is_active': True})
    db.commit()
    return 1



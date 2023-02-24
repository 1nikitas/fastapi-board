from fastapi import APIRouter
from webapps.auth import route_login
from webapps.tasks import route_tasks
from webapps.users import route_users
from webapps.clients import route_clients

api_router = APIRouter()
api_router.include_router(route_tasks.router, prefix="", tags=["job-webapp"])
api_router.include_router(route_users.router, prefix="", tags=["users-webapp"])
api_router.include_router(route_login.router, prefix="", tags=["auth-webapp"])
api_router.include_router(route_clients.router, prefix="", tags=["clients-wepapp"])

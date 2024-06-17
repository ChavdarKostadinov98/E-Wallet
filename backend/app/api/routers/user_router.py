from fastapi import APIRouter, Query
from backend.app.api.services.user_services import get_all_users

user_router = APIRouter(prefix="/users")


@user_router.get("/all", status_code=200)
def get_all():
    return get_all_users()

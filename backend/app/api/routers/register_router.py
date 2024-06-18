from fastapi import APIRouter
from backend.app.api.services.register_services import register_user
from backend.app.api.models.models import User

register_router = APIRouter(prefix="/registration")


@register_router.post("/new", status_code=201)
def register(user: User):
    return register_user(user)




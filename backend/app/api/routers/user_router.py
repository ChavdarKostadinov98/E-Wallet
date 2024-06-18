from fastapi import APIRouter
from backend.app.api.services.user_services import create_card
from backend.app.api.models.models import Card


users_router = APIRouter(prefix="/users")


@users_router.post("/{user_id}/cards/new")
def add_new_card(card: Card, user_id: int):
    return create_card(card, user_id)




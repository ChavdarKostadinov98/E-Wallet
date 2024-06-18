from fastapi import APIRouter
from backend.app.api.services.admin_services import (approve_user, decline_user, check_waiting_pool, get_all_users,
                                                     freeze_card, activate_card, block_user, unblock_user)

admin_router = APIRouter(prefix="/admin")


@admin_router.get("/users", status_code=200)
def view_all():
    return get_all_users()


@admin_router.put("/approval", status_code=200)
def approve(user_id: int):
    return approve_user(user_id)


@admin_router.put("/denial", status_code=204)
def decline(user_id: int):
    return decline_user(user_id)


@admin_router.get("/pool", status_code=200)
def view_waiting_pool():
    return check_waiting_pool()


@admin_router.put("/cards/status/frozen", status_code=201)
def freeze(user_id, card_id):
    return freeze_card(user_id, card_id)


@admin_router.put("/cards/status/active", status_code=201)
def activate(user_id, card_id):
    return activate_card(user_id, card_id)


@admin_router.put("/users/blocking/{user_to_block_id}", status_code=200)
def block(user_id: int, user_to_block_id: int):
    return block_user(user_id, user_to_block_id)


@admin_router.put("/users/unblocking/{user_to_unblock_id}", status_code=200)
def unblock(user_id: int, user_to_unblock_id: int):
    return unblock_user(user_id, user_to_unblock_id)

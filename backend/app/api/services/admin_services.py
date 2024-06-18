from backend.app.data import database
from pydantic import Field
from fastapi import HTTPException


def approve_user(user_id: int = Field(gt=0)):
    if not check_for_user_existence(user_id):
        raise HTTPException(status_code=404, detail="User not found!")
    user_table_sql = "UPDATE users SET role = 'user' WHERE user_id = %s"
    waiting_pool_sql = "DELETE FROM waiting_pool WHERE user_id = %s"
    database.update_query(user_table_sql, (user_id,))
    database.update_query(waiting_pool_sql, (user_id,))
    return {"message": "User approved."}


def decline_user(user_id: int = Field(gt=0)):
    check_for_existence = "SELECT * FROM users WHERE user_id = %s"
    execute = database.read_query(check_for_existence, (user_id,))
    if not execute:
        raise HTTPException(status_code=404, detail="User not found!")
    user_table_sql = "DELETE FROM users WHERE user_id = %s"
    waiting_pool_sql = "DELETE FROM waiting_pool WHERE user_id = %s"
    database.update_query(waiting_pool_sql, (user_id,))
    database.update_query(user_table_sql, (user_id,))
    return {"message": "User declined."}


def check_waiting_pool():
    waiting_pool_users = "SELECT user_id FROM waiting_pool"
    users = database.read_query(waiting_pool_users)
    if users:
        return {"Users waiting to be approved": users}
    return {"message": "There are currently no users in the waiting pool."}


def get_all_users():
    sql = "SELECT * FROM users"
    execute = database.read_query(sql)
    if execute:
        return execute
    return {"message": "No users found"}


def check_if_user_is_admin(user_id: int):
    sql = "SELECT * FROM users WHERE user_id = %s and role = 'admin'"
    execute = database.read_query(sql, (user_id,))
    return execute


def freeze_card(user_id: int, card_id: int):
    if not check_if_user_is_admin(user_id):
        raise HTTPException(status_code=403, detail="You are not an admin, therefore you cannot freeze cards!")
    sql = "UPDATE cards SET status = 'frozen' WHERE card_id = %s"
    database.update_query(sql, (card_id,))
    return {"message": "Card frozen."}


def activate_card(user_id: int, card_id: int):
    if not check_if_user_is_admin(user_id):
        raise HTTPException(status_code=403, detail="You are not an admin, therefore you cannot activate cards!")
    sql = "UPDATE cards SET status = 'active' WHERE card_id = %s"
    database.update_query(sql, (card_id,))
    return {"message": "Card activated."}


def block_user(user_id: int, user_to_block_id: int):
    if not check_if_user_is_admin(user_id):
        raise HTTPException(status_code=403, detail="As a regular user you cannot block people.")
    if not check_for_user_existence(user_to_block_id):
        raise HTTPException(status_code=404, detail="User not found.")

    sql = "UPDATE users SET role = 'blocked' WHERE user_id = %s"
    database.update_query(sql, (user_to_block_id,))
    return {"message": "User blocked."}


def unblock_user(user_id: int, user_to_unblock_id: int):
    if not check_if_user_is_admin(user_id):
        raise HTTPException(status_code=403, detail="As a regular user you cannot unblock people.")
    if not check_for_user_existence(user_to_unblock_id):
        raise HTTPException(status_code=404, detail="User not found.")

    sql = "UPDATE users SET role = 'user' WHERE user_id = %s"
    database.update_query(sql, (user_to_unblock_id,))
    return {"message": "User unblocked."}


def check_for_user_existence(user_id: int):
    sql = "SELECT * FROM users WHERE user_id = %s"
    execute = database.read_query(sql, (user_id,))
    return execute

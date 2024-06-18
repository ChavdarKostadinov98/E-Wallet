from backend.app.data import database
from backend.app.api.models.models import User
from fastapi import HTTPException
import bcrypt


def register_user(user: User):
    if check_for_existing_email(user.email):
        raise HTTPException(status_code=409, detail="This email already exists.")
    if check_for_existing_username(user.username):
        raise HTTPException(status_code=409, detail="This username already exists.")
    if check_for_existing_number(user.phone_number):
        raise HTTPException(status_code=409, detail="This phone number is already in use.")

    hashed_password = hash_password(user.password)
    register_sql = ("INSERT INTO users(email, username, firstname, lastname, password, phone_number) "
                    "VALUES(%s, %s, %s, %s, %s, %s)")
    database.insert_query(register_sql, (user.email, user.username, user.firstname, user.lastname,
                                         hashed_password, user.phone_number))
    get_id = "SELECT user_id FROM users WHERE username = %s"
    db_user_id = database.read_query(get_id, (user.username,))[0][0]

    waiting_pool_sql = "INSERT INTO waiting_pool(user_id) VALUES(%s)"
    database.insert_query(waiting_pool_sql, (db_user_id,))
    return {"message": "User registered successfully!"}


def check_for_existing_username(username: str):
    sql = "SELECT * FROM users WHERE username = %s"
    execute = database.read_query(sql, (username,))
    return execute


def check_for_existing_email(email: str):
    sql = "SELECT * FROM users WHERE email = %s"
    execute = database.read_query(sql, (email,))
    return execute


def check_for_existing_number(phone_number: str):
    sql = "SELECT * FROM users WHERE phone_number = %s"
    execute = database.read_query(sql, (phone_number,))
    return execute


def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(password.encode("utf-8"), salt)
    return hashed_pass.decode("utf-8")

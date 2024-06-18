from datetime import datetime
from dateutil.relativedelta import relativedelta
from backend.app.data import database
from pydantic import Field
from fastapi import HTTPException
from backend.app.api.models.models import Card
import random
from cryptography.fernet import Fernet


key = Fernet.generate_key()
cipher_suite = Fernet(key)


def create_card(card: Card, user_id: int = Field(gt=0)):
    if not check_if_user_is_approved(user_id):
        raise HTTPException(status_code=403, detail="In order to add a new card, your profile must be approved first.")
    names = get_user_names(user_id)
    card_number = generate_card_number()
    cvv = encrypt_cvv(generate_cvv())
    initial_balance = 0.00
    expiration_date = generate_expiration_date()
    design = card.design
    card_type = card.type
    sql = ("INSERT INTO"
           " cards(cardholder_id, type, balance, number, expiration_date, cvv_code, design, cardholder_names) "
           "VALUES(%s, %s, %s, %s, %s, %s, %s, %s)")
    database.insert_query(sql, (user_id, card_type, initial_balance, card_number,
                                expiration_date, cvv, design, names))
    return {"message": "Card successfully created."}


def check_if_user_is_approved(user_id: int = Field(gt=0)):
    sql = "SELECT * FROM users WHERE user_id = %s and role = 'user'"
    execute = database.read_query(sql, (user_id,))
    return execute


def generate_card_number():
    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10

    card_number = [random.randint(0, 9) for _ in range(15)]
    checksum = luhn_checksum(int(''.join(map(str, card_number)) + "0"))
    card_number.append((10 - checksum) % 10)
    card_number_str = ''.join(map(str, card_number))

    while check_for_existing_card_number(card_number_str):
        card_number = [random.randint(0, 9) for _ in range(15)]
        checksum = luhn_checksum(int(''.join(map(str, card_number)) + "0"))
        card_number.append((10 - checksum) % 10)
        card_number_str = ''.join(map(str, card_number))

    return card_number_str


def generate_cvv():
    return "".join([str(random.randint(0, 9)) for _ in range(3)])


def encrypt_cvv(cvv):
    cvv_bytes = cvv.encode("utf-8")
    encrypted_cvv = cipher_suite.encrypt(cvv_bytes)
    return encrypted_cvv


def decrypt_cvv(encrypted_cvv):
    decrypted_cvv = cipher_suite.decrypt(encrypted_cvv)
    return decrypted_cvv.decode("utf-8")


def get_user_names(user_id: int):
    sql = "SELECT firstname, lastname FROM users WHERE user_id = %s"
    names_result = database.read_query(sql, (user_id,))[0]
    names = names_result[0] + " " + names_result[1]
    return names


def generate_expiration_date(years_in_future=2):
    current_date = datetime.now()
    future_date = current_date + relativedelta(years=years_in_future)
    expiration_date = future_date.strftime("%m/%y")
    return expiration_date


def check_for_existing_card_number(card_number):
    sql = "SELECT * FROM cards WHERE number = %s"
    execute = database.read_query(sql, (card_number,))
    return execute

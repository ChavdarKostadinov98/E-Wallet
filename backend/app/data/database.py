import mysql.connector
from dotenv import dotenv_values

env_vars = dotenv_values()
HOST = env_vars.get("HOST")
USER = env_vars.get("USER")
PASSWORD = env_vars.get("PASSWORD")
PORT = env_vars.get("PORT")
DATABASE = env_vars.get("DATABASE")


mydb = None

if all([HOST, USER, PASSWORD, PORT, DATABASE]):
    mydb = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        port=PORT,
        database=DATABASE,
    )


def read_query(sql: str, sql_params=()):
    cursor = mydb.cursor()
    cursor.execute(sql, sql_params)
    return cursor.fetchall()


def insert_query(sql: str, sql_params=()):
    cursor = mydb.cursor()
    cursor.execute(sql, sql_params)
    mydb.commit()
    return "success"


def update_query(sql: str, sql_params=()):
    cursor = mydb.cursor()
    cursor.execute(sql, sql_params)
    mydb.commit()
    return "success"

from backend.app.data import database


def get_all_users():
    sql = "SELECT * FROM users"
    execute = database.read_query(sql)
    if execute:
        return execute
    return {"message": "No users found"}

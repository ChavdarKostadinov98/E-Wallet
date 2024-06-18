from fastapi import FastAPI
from backend.app.api.routers.register_router import register_router
from backend.app.api.routers.admin_router import admin_router
from backend.app.api.routers.user_router import users_router
import uvicorn


app = FastAPI()

app.include_router(register_router, tags=["Registration"])
app.include_router(admin_router, tags=["Admin"])
app.include_router(users_router, tags=["User"])


@app.get("/", status_code=200, tags=["Home"])
def home():
    return {"message": "Hello, User!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

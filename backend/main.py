from fastapi import FastAPI
from backend.app.api.routers.user_router import user_router
import uvicorn


app = FastAPI()
app.include_router(user_router, tags=["Users"])


@app.get("/", status_code=200)
def home():
    return {"message": "Hello, User!"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def hello() -> dict:
    return {"message": "Главная страница"}


@app.get("/user/")
async def hello_() -> dict:
    return {"message": "Моя страница"}


@app.get("/user/admin")
async def user() -> dict:
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user(user_id: int = Path(ge=1, le=100, description="Enter User ID", example="23")) -> dict:
    return {"message": f"Вы вошли как пользователь №{user_id}"}


@app.get("/user/{username}/{age}")
async def user(username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username",
                                             example="OnkelTom")], age: int = Path(ge=18, le=120,
                                                                                   description="Enter age",
                                                                                   example=25)) -> dict:
    return {"message": f"Информация о пользователе. Имя {username}, возраст {age}"}

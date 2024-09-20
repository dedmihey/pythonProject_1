from fastapi import FastAPI

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
async def user(user_id: str) -> dict:
    return {"message": f"Вы вошли как пользователь №{user_id}"}


@app.get("/user/{username}/{age}")
async def user(username: str, age: str) -> dict:
    return {"message": f"Информация о пользователе. Имя {username}, возраст {age}"}

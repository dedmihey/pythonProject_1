from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def hello() -> dict:
    return {"message": "Главная страница"}

@app.get("/user/")
async def user() -> dict:
    return {"message": "Это страница пользователя"}

@app.get("/user/admin")
async def admin() -> dict:
    return {"message": "Вы вошли как администратор"}




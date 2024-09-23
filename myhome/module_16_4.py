from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int


@app.get("/users")
async def get_users() -> list[User]:
    return users


@app.post("/user/{username}/{age}")
async def create_user(user: User) -> str:
    user.id = len(users) + 1
    users.append(user)
    return f"User {user.id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int) -> str:
    try:
        edit_user = users[user_id - 1]
        edit_user.username = username
        edit_user.age = age
        return f"The user {user_id} has been updated"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: int) -> str:
    try:
        users.pop(user_id - 1)
        return f"The user {user_id} has been deleted"
    except IndexError:
        raise HTTPException(status_code=404, detail="User was not found")


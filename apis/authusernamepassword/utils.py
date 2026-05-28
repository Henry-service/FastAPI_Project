from .db.dboperation import crud_user
from .model.schemas import AuthRegisterResponse

async def create_user():
    user = await crud_user.create({
        "username": "example", 
        "email": "example@example.com", 
        "hashed_password": "hashed_password"
        })  # Example of creating a user
    return user


async def read_user(user_id: int):
    user = await crud_user.get(user_id)  # Example of reading a user by ID
    if user:
        return user
    else:
        return AuthRegisterResponse(success="User not found", url=None)
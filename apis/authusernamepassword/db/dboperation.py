from fastcrud import FastCRUD
from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from .models import User

crud_user: FastCRUD = FastCRUD(User, id_field="id", fields={"username": String(50), "email": String(120), "hashed_password": String(128)})
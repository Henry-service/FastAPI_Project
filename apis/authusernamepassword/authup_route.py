from fastapi import APIRouter, Depends
from typing import Annotated
from .model.schemas import AuthRegisterResponse
from .authup_service import authup_service

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post(
    "/register",
    responses={
        201: {"description": "User registered successfully"},
        400: {"description": "Bad request"},
    },
    tags=["auth"],
    )
async def register_user(
    response: Annotated[AuthRegisterResponse, Depends(authup_service.register_user)],
) -> AuthRegisterResponse:
    return response


@router.post(
    "/login",
    responses={
        200: {"description": "User logged in successfully"},
        400: {"description": "Bad request"},
    },
    tags=["auth"],
    )
async def login_user(
    response: Annotated[AuthRegisterResponse, Depends(authup_service.login_user)],
) -> AuthRegisterResponse:  
    return {"message": "Login endpoint - implementation pending"}


@router.post(
    "/logout",
    responses={
        200: {"description": "User logged out successfully"},
        400: {"description": "Bad request"},
    },
    tags=["auth"],
    )
async def logout_user(
    response: Annotated[AuthRegisterResponse, Depends(authup_service.logout_user)],
) -> AuthRegisterResponse:
    return {"message": "Logout endpoint - implementation pending"}


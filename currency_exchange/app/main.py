from fastapi import FastAPI, Depends,Request
from fastapi.exceptions import RequestValidationError
from fastapi_users import fastapi_users
from auth.schemas import UserRead,UserUpdate,UserCreate
from auth.users import (
    auth_backend,
    current_active_user,
    fastapi_users,
    google_oauth_client,
)
from auth.auth import create_db_and_tables
from auth.models import User
from config import SECRET_AUTH

from utils.exceptions import ValidationError

from endpoints.currency import router as currency_router


app = FastAPI(
    title="Currency_exchange"
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)
app.include_router(
    fastapi_users.get_oauth_router(google_oauth_client, auth_backend, SECRET_AUTH),
    prefix="/auth/google",
    tags=["auth"],
)

app.include_router(currency_router)


@app.exception_handler(RequestValidationError)
def get_currency_exception(request: Request,exc:RequestValidationError):
    return ValidationError(request=request,exc=exc)

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


@app.on_event("startup")
async def on_startup():
    # Not needed if you setup a migration system like Alembic
    await create_db_and_tables()
from datetime import datetime, timedelta, timezone
from typing import List

from auth.jwt import DEFAULT_ACCESS_TOKEN_EXPIRE, create_access_token
from entities.users.controller import get_users, update_user
from entities.users.model import UserUpdate
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import BaseModel, EmailStr
from routers.mail import router
from starlette.responses import JSONResponse


class EmailSchema(BaseModel):
    email: List[EmailStr]
    confirmation_id: str


# TO CHANGE LATER WITH equisphere@gmail.com
conf = ConnectionConfig(
    MAIL_USERNAME="augu.hourlier@gmail.com",
    # cf.
    # https://myaccount.google.com/apppasswords?rapt=AEjHL4PVEoCk-vmcI3F0Z-7GN8zI44rKo7CfyuL3nr765Gg_C5B427hZJuMEBf4mdvSy9h_OGJ9NdaLMQbaUuq4m8WtKyklXig
    MAIL_PASSWORD="szvrjtkwchegmbgn",
    MAIL_FROM="augu.hourlier@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)


@router.post("/")
async def send_confirmation_mail(body: EmailSchema) -> JSONResponse:
    data = body.dict()
    # Must match
    user = await get_users(
        email=data.get("email")[0],
        confirmation_id=data.get("confirmation_id"),
        multiple=False,
    )

    now = datetime.now(timezone.utc) + timedelta(hours=2)

    if user.last_email_send is not None:
        print(now, "   ", user.last_email_send)
        print(now - user.last_email_send)
        print(type(now - user.last_email_send))
        if (now - user.last_email_send) < DEFAULT_ACCESS_TOKEN_EXPIRE:
            return JSONResponse(
                status_code=401,
                content={"message": "Please wait 15m or use the previous mail"},
            )

    # Default expires in 15m
    access_token = create_access_token(
        user={
            "sub": user.email,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "role": user.role,
            "confirmation_id": user.confirmation_id,
        }
    )
    content = f"""
Bienvenue sur Equisphere !

Pour valider votre inscription, cliquez sur le lien ci-dessous (ce lien ne reste valide que 15m):

http://localhost:5173/validate?email={user.email}&confirmation_id={user.confirmation_id}&access_token={access_token}
    """

    message = MessageSchema(
        subject="Equisphere - Confirmation de votre adresse email",
        recipients=data.get("email"),  # List of recipients, as many as you can pass
        body=content,
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    await update_user(user.id, UserUpdate(**{"last_email_send": now}))
    return JSONResponse(status_code=200, content={"message": "Email has been sent"})

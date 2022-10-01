from typing import List

from entities.users.controller import get_users
from entities.users.model import User
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import BaseModel, EmailStr
from routers.mail import router
from starlette.responses import JSONResponse
from utils import randomizer


class EmailSchema(BaseModel):
    email: List[EmailStr]


# TO CHANGE LATER WITH equisphere@gmail.com
conf = ConnectionConfig(
    MAIL_USERNAME="augu.hourlier@gmail.com",
    MAIL_PASSWORD="szvrjtkwchegmbgn",  # cf. https://myaccount.google.com/apppasswords?rapt=AEjHL4PVEoCk-vmcI3F0Z-7GN8zI44rKo7CfyuL3nr765Gg_C5B427hZJuMEBf4mdvSy9h_OGJ9NdaLMQbaUuq4m8WtKyklXig
    MAIL_FROM="augu.hourlier@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)


@router.post("/")
async def send_confirmation_mail(emails: EmailSchema) -> JSONResponse:

    user = await get_users(email=emails.dict().get("email")[0])

    content = f"""
Bienvenue sur Equisphere !

Pour valider votre inscription, cliquez sur le lien ci-dessous:

https://onverraplustard/confirmation_page?confirmation_id={user.confirmation_id}
    """

    message = MessageSchema(
        subject="Equisphere - Confirmation de votre adresse email",
        recipients=emails.dict().get(
            "email"
        ),  # List of recipients, as many as you can pass
        body=content,
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "Email has been sent"})

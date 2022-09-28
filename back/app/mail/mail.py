from typing import List

from fastapi import BackgroundTasks, FastAPI, File, Form, UploadFile
from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from pydantic import BaseModel, EmailStr
from routers.mail import router
from starlette.requests import Request
from starlette.responses import JSONResponse


class EmailSchema(BaseModel):
    email: List[EmailStr]


# TO CHANGE
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

content = """
Pour activer votre compte (colonne first connexion + validation de l'email)
"""


@router.post("/")
async def send_mail(email: EmailSchema) -> JSONResponse:

    message = MessageSchema(
        subject="TEST",
        recipients=email.dict().get(
            "email"
        ),  # List of recipients, as many as you can pass
        body=content,
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})

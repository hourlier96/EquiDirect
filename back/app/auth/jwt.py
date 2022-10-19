import datetime

from fastapi import HTTPException, Request, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError, jwt

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"

DEFAULT_ACCESS_TOKEN_EXPIRE = datetime.timedelta(minutes=15)
ACCESS_TOKEN_EXPIRE = datetime.timedelta(hours=1)


def create_access_token(user: dict, expires_delta: datetime.timedelta | None = None):
    user_to_encode = user.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + DEFAULT_ACCESS_TOKEN_EXPIRE
    user_to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(user_to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Use this class as dependency on endpoint to secure it
class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(
            JWTBearer, self
        ).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Invalid authentication scheme.",
                )
            self.verify_jwt(credentials.credentials)
            return credentials.credentials
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authorization code.",
            )

    def verify_jwt(self, token):
        try:
            decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            # TODO: More check with verification_id, check user email
            return "sub" in decoded
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token or expired token.",
            )

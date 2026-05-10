import jwt
from fastapi import Depends, HTTPException
from fastapi.security import (
    HTTPAuthorizationCredentials,
    HTTPBearer,
    OAuth2PasswordBearer,
)
from database import SECRET_ALGORITHM, SECRET_KEY

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

security = HTTPBearer()


def get_current_user(data: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(
            data.credentials, SECRET_KEY, algorithms=[SECRET_ALGORITHM]
        )
        user_id = payload.get("sub")
        if not user_id:
            raise HTTPException(status_code=401, detail="Token inválido")
        return int(user_id)
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

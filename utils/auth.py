from datetime import datetime, timedelta, timezone
import jwt

from database import SECRET_ALGORITHM, SECRET_EXPIRE_MINUTES, SECRET_KEY


def create_token(user_id: int):
    payload = {
        "sub": str(user_id),
        "exp": datetime.now(timezone.utc) + timedelta(minutes=SECRET_EXPIRE_MINUTES),
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=SECRET_ALGORITHM)

import jwt
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta, timezone
from app.schema import TokenData
from app.database import get_session
from app import models
from app.config import settings

oauth_scheme = OAuth2PasswordBearer(tokenUrl="login")

# things required for jwt token
SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

# create jwt token
def create_access_token(data: dict):
    to_encode = data.copy()
    
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    # signature - header + key + algorithm
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

# verify the token
def verify_access_token(token:str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
    
        token_data = TokenData(id =id)
    except InvalidTokenError:
        raise credentials_exception
    
    return token_data
    
def get_current_user(token: str = Depends(oauth_scheme), session = Depends(get_session)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate creadentials",
                                          headers={"WWW-Authenticate": "Bearer"})
    
    token = verify_access_token(token, credentials_exception)
    user = session.query(models.User).filter(models.User.id == token.id).first()

    return user
from pydantic import BaseModel
from pydantic import EmailStr
from pydantic import ConfigDict

class UserRegister(BaseModel):

    username: str

    email: EmailStr

    password: str

    role_id: int

class UserLogin(BaseModel):

    email: EmailStr

    password: str

class TokenResponse(BaseModel):

    access_token: str

    refresh_token: str

    token_type: str

class MessageResponse(BaseModel):

    message: str
from pydantic import BaseModel, EmailStr


class ContactSchema(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    subject: str
    message: str

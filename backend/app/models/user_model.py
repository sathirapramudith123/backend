from pydantic import BaseModel, EmailStr
from datetime import datetime
from app.utils.helpers import generate_id, utc_now

class User(BaseModel):
    id: str = generate_id("usr")
    full_name: str
    email: EmailStr
    password_hash: str
    role: str = "merchant"
    created_at: datetime = utc_now()
    updated_at: datetime = utc_now()

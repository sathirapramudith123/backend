from pydantic import BaseModel
from datetime import datetime
from app.utils.helpers import generate_id, utc_now

class Notification(BaseModel):
    id: str = generate_id("not")
    title: str
    message: str
    status: str
    created_at: datetime = utc_now()
    updated_at: datetime = utc_now()

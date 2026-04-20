from pydantic import BaseModel
from datetime import datetime
from app.utils.helpers import generate_id, utc_now

class TermVault(BaseModel):
    id: str = generate_id("tv")
    name: str
    member_count: int
    status: str
    created_at: datetime = utc_now()
    updated_at: datetime = utc_now()

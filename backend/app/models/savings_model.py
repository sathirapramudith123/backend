from pydantic import BaseModel
from datetime import datetime
from app.utils.helpers import generate_id, utc_now

class SavingsRecord(BaseModel):
    id: str = generate_id("sav")
    target_name: str
    balance: float
    status: str
    created_at: datetime = utc_now()
    updated_at: datetime = utc_now()

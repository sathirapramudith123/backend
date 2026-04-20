from pydantic import BaseModel
from datetime import datetime
from app.utils.helpers import generate_id, utc_now

class LedgerEntry(BaseModel):
    id: str = generate_id("led")
    title: str
    amount: float
    entry_type: str
    status: str
    created_at: datetime = utc_now()
    updated_at: datetime = utc_now()

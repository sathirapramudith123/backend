from pydantic import BaseModel
from datetime import datetime
from app.utils.helpers import generate_id, utc_now

class Transaction(BaseModel):
    id: str = generate_id("txn")
    transaction_type: str
    amount: float
    status: str
    created_at: datetime = utc_now()
    updated_at: datetime = utc_now()

from pydantic import BaseModel
from datetime import datetime
from app.utils.helpers import generate_id, utc_now

class InventoryItem(BaseModel):
    id: str = generate_id("inv")
    name: str
    quantity: float
    unit_price: float
    status: str
    created_at: datetime = utc_now()
    updated_at: datetime = utc_now()

from pydantic import BaseModel
from datetime import datetime
from app.utils.helpers import generate_id, utc_now

class Procurement(BaseModel):
    id: str = generate_id("pro")
    item_name: str
    supplier_name: str
    quantity: float
    status: str
    created_at: datetime = utc_now()
    updated_at: datetime = utc_now()

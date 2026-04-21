from pydantic import BaseModel, Field
from datetime import datetime
from app.utils.helpers import generate_id, utc_now

class Procurement(BaseModel):
    id: str = Field(default_factory=lambda: generate_id("pro"))
    item_name: str
    supplier_name: str
    quantity: float
    status: str
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

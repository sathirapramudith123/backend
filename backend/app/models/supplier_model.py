from pydantic import BaseModel
from datetime import datetime
from app.utils.helpers import generate_id, utc_now

class Supplier(BaseModel):
    id: str = generate_id("sup")
    name: str
    contact_number: str
    status: str
    created_at: datetime = utc_now()
    updated_at: datetime = utc_now()

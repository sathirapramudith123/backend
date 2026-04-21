from datetime import datetime
from pydantic import BaseModel


class SupplierCreate(BaseModel):
    name: str
    contact_number: str
    status: str


class SupplierResponse(BaseModel):
    id: str
    name: str
    contact_number: str
    status: str
    created_at: datetime
    updated_at: datetime
from datetime import datetime
from pydantic import BaseModel


class ProcurementCreate(BaseModel):
    item_name: str
    supplier_name: str
    quantity: float
    status: str


class ProcurementResponse(BaseModel):
    id: str
    item_name: str
    supplier_name: str
    quantity: float
    status: str
    created_at: datetime
    updated_at: datetime
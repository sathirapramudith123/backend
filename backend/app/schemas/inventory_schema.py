from datetime import datetime
from pydantic import BaseModel, Field


class InventoryItemBase(BaseModel):
    name: str = Field(..., min_length=1)
    supplier_id: str = Field(..., min_length=1)
    supplier_name: str = Field(..., min_length=1)
    quantity: float = Field(..., ge=0)
    unit: str = Field(..., min_length=1)
    unit_price: float = Field(..., ge=0)
    status: str = Field(..., min_length=1)


class InventoryItemCreate(InventoryItemBase):
    pass


class InventoryItemUpdate(InventoryItemBase):
    pass


class InventoryItemResponse(BaseModel):
    id: str
    name: str
    supplier_id: str = ""
    supplier_name: str = "Unknown Supplier"
    quantity: float
    unit: str = "unit"
    unit_price: float
    status: str
    created_at: datetime
    updated_at: datetime


class InventoryDeleteResponse(BaseModel):
    message: str
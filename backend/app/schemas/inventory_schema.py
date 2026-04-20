from pydantic import BaseModel

class InventoryItemCreate(BaseModel):
    name: str
    quantity: float
    unit_price: float
    status: str

class InventoryItemResponse(BaseModel):
    id: str
    name: str
    quantity: float
    unit_price: float
    status: str

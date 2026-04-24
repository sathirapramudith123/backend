from datetime import datetime
from pydantic import BaseModel, Field


class SupplierBase(BaseModel):
    name: str = Field(..., min_length=1)
    company_name: str = Field(..., min_length=1)
    contact_number: str = Field(..., min_length=1)
    email: str = Field(..., min_length=1)
    address: str = ""
    status: str = Field(..., min_length=1)


class SupplierCreate(SupplierBase):
    pass


class SupplierUpdate(SupplierBase):
    pass


class SupplierResponse(BaseModel):
    id: str
    name: str
    company_name: str = "N/A"
    contact_number: str
    email: str = "N/A"
    address: str = ""
    status: str
    created_at: datetime
    updated_at: datetime


class SupplierDeleteResponse(BaseModel):
    message: str
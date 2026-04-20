from pydantic import BaseModel

class LedgerEntryCreate(BaseModel):
    title: str
    amount: float
    entry_type: str
    status: str

class LedgerEntryResponse(BaseModel):
    id: str
    title: str
    amount: float
    entry_type: str
    status: str

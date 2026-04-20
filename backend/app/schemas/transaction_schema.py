from pydantic import BaseModel

class TransactionCreate(BaseModel):
    transaction_type: str
    amount: float
    status: str

class TransactionResponse(BaseModel):
    id: str
    transaction_type: str
    amount: float
    status: str

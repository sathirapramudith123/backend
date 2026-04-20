from fastapi import HTTPException
from app.models.transaction_model import Transaction
from app.repositories.transaction_repository import TransactionRepository

class TransactionService:
    def __init__(self):
        self.repository = TransactionRepository()

    async def create(self, data: dict):
        payload = Transaction(**data).model_dump()
        return await self.repository.create(payload)

    async def list_all(self):
        return await self.repository.list_all()

    async def get_by_id(self, item_id: str):
        item = await self.repository.get_by_id(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Transaction not found")
        return item

    async def get_history(self):
        return await self.repository.list_all()

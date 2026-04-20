from fastapi import HTTPException
from app.models.ledger_model import LedgerEntry
from app.repositories.ledger_repository import LedgerEntryRepository

class LedgerEntryService:
    def __init__(self):
        self.repository = LedgerEntryRepository()

    async def create(self, data: dict):
        payload = LedgerEntry(**data).model_dump()
        return await self.repository.create(payload)

    async def list_all(self):
        return await self.repository.list_all()

    async def get_by_id(self, item_id: str):
        item = await self.repository.get_by_id(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="LedgerEntry not found")
        return item

from fastapi import HTTPException
from app.models.inventory_model import InventoryItem
from app.repositories.inventory_repository import InventoryItemRepository

class InventoryItemService:
    def __init__(self):
        self.repository = InventoryItemRepository()

    async def create(self, data: dict):
        payload = InventoryItem(**data).model_dump()
        return await self.repository.create(payload)

    async def list_all(self):
        return await self.repository.list_all()

    async def get_by_id(self, item_id: str):
        item = await self.repository.get_by_id(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="InventoryItem not found")
        return item

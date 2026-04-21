from fastapi import HTTPException

from app.models.supplier_model import Supplier
from app.repositories.supplier_repository import SupplierRepository


class SupplierService:
    def __init__(self):
        self.repository = SupplierRepository()

    async def create(self, data: dict):
        payload = Supplier(**data).model_dump()
        return await self.repository.create(payload)

    async def list_all(self):
        return await self.repository.list_all()

    async def get_by_id(self, item_id: str):
        item = await self.repository.get_by_id(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Supplier not found")
        return item
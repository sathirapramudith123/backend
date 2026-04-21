from fastapi import HTTPException

from app.models.procurement_model import Procurement
from app.repositories.procurement_repository import ProcurementRepository


class ProcurementService:
    def __init__(self):
        self.repository = ProcurementRepository()

    async def create(self, data: dict):
        payload = Procurement(**data).model_dump()
        return await self.repository.create(payload)

    async def list_all(self):
        return await self.repository.list_all()

    async def get_by_id(self, item_id: str):
        item = await self.repository.get_by_id(item_id)
        if not item:
            raise HTTPException(status_code=404, detail="Procurement not found")
        return item
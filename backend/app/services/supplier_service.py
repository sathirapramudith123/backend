from fastapi import HTTPException, status

from app.models.supplier_model import Supplier
from app.repositories.supplier_repository import SupplierRepository


class SupplierService:
    def __init__(self):
        self.repository = SupplierRepository()

    async def create(self, data: dict):
        payload = Supplier(**data).model_dump()
        return await self.repository.create(payload)

    async def list_all(self):
        await self.repository.patch_missing_fields()
        return await self.repository.list_all()

    async def get_by_id(self, item_id: str):
        item = await self.repository.get_by_id(item_id)

        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Supplier not found"
            )

        return item

    async def update(self, item_id: str, data: dict):
        existing = await self.repository.get_by_id(item_id)

        if not existing:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Supplier not found"
            )

        updated = {
            **existing,
            **data
        }

        item = await self.repository.update(item_id, updated)

        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Supplier not found"
            )

        return item

    async def delete(self, item_id: str):
        existing = await self.repository.get_by_id(item_id)

        if not existing:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Supplier not found"
            )

        deleted = await self.repository.delete(item_id)

        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to delete supplier"
            )

        return {"message": "Supplier deleted successfully"}
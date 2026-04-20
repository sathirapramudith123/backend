from fastapi import APIRouter
from app.schemas.inventory_schema import InventoryItemCreate
from app.services.inventory_service import InventoryItemService

router = APIRouter(prefix="/inventory", tags=["inventory"])


@router.get("")
async def list_items():
    service = InventoryItemService()
    return await service.list_all()


@router.get("/{item_id}")
async def get_item(item_id: str):
    service = InventoryItemService()
    return await service.get_by_id(item_id)


@router.post("")
async def create_item(payload: InventoryItemCreate):
    service = InventoryItemService()
    return await service.create(payload.model_dump())
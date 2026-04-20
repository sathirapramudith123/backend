from fastapi import APIRouter
from app.schemas.supplier_schema import SupplierCreate
from app.services.supplier_service import SupplierService

router = APIRouter(prefix="/suppliers", tags=["suppliers"])


@router.get("")
async def list_items():
    service = SupplierService()
    return await service.list_all()


@router.get("/{item_id}")
async def get_item(item_id: str):
    service = SupplierService()
    return await service.get_by_id(item_id)


@router.post("")
async def create_item(payload: SupplierCreate):
    service = SupplierService()
    return await service.create(payload.model_dump())
from fastapi import APIRouter
from app.schemas.procurement_schema import ProcurementCreate
from app.services.procurement_service import ProcurementService

router = APIRouter(prefix="/procurement", tags=["procurement"])


@router.get("")
async def list_items():
    service = ProcurementService()
    return await service.list_all()


@router.get("/{item_id}")
async def get_item(item_id: str):
    service = ProcurementService()
    return await service.get_by_id(item_id)


@router.post("")
async def create_item(payload: ProcurementCreate):
    service = ProcurementService()
    return await service.create(payload.model_dump())
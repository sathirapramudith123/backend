from fastapi import APIRouter
from app.schemas.ledger_schema import LedgerEntryCreate
from app.services.ledger_service import LedgerEntryService

router = APIRouter(prefix="/ledger", tags=["ledger"])


@router.get("")
async def list_items():
    service = LedgerEntryService()
    return await service.list_all()


@router.get("/{item_id}")
async def get_item(item_id: str):
    service = LedgerEntryService()
    return await service.get_by_id(item_id)


@router.post("")
async def create_item(payload: LedgerEntryCreate):
    service = LedgerEntryService()
    return await service.create(payload.model_dump())
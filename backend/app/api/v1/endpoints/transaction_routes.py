from fastapi import APIRouter
from app.schemas.transaction_schema import TransactionCreate
from app.services.transaction_service import TransactionService

router = APIRouter(prefix="/transactions", tags=["transactions"])


@router.get("")
async def list_items():
    service = TransactionService()
    return await service.list_all()


@router.get("/{item_id}")
async def get_item(item_id: str):
    service = TransactionService()
    return await service.get_by_id(item_id)


@router.post("")
async def create_item(payload: TransactionCreate):
    service = TransactionService()
    return await service.create(payload.model_dump())


@router.get("/history")
async def get_history():
    service = TransactionService()
    return await service.get_history()
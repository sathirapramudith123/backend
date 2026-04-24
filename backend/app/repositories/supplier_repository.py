from app.core.database import MongoDB
from app.utils.helpers import utc_now


def serialize_supplier(item: dict) -> dict | None:
    if not item:
        return None

    item.pop("_id", None)

    item.setdefault("company_name", "N/A")
    item.setdefault("email", "N/A")
    item.setdefault("address", "")

    return item


class SupplierRepository:
    @property
    def collection(self):
        return MongoDB.get_database()["suppliers"]

    async def create(self, payload: dict):
        await self.collection.insert_one(payload)
        return serialize_supplier(payload)

    async def list_all(self):
        items = []
        async for item in self.collection.find().sort("created_at", -1):
            items.append(serialize_supplier(item))
        return items

    async def get_by_id(self, item_id: str):
        item = await self.collection.find_one({"id": item_id})
        return serialize_supplier(item)

    async def update(self, item_id: str, payload: dict):
        payload["updated_at"] = utc_now()

        await self.collection.update_one(
            {"id": item_id},
            {"$set": payload}
        )

        item = await self.collection.find_one({"id": item_id})
        return serialize_supplier(item)

    async def delete(self, item_id: str):
        result = await self.collection.delete_one({"id": item_id})
        return result.deleted_count > 0

    async def patch_missing_fields(self):
        await self.collection.update_many(
            {"company_name": {"$exists": False}},
            {"$set": {"company_name": "N/A"}}
        )

        await self.collection.update_many(
            {"email": {"$exists": False}},
            {"$set": {"email": "N/A"}}
        )

        await self.collection.update_many(
            {"address": {"$exists": False}},
            {"$set": {"address": ""}}
        )
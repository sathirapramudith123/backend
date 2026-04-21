from app.core.database import MongoDB


def serialize_supplier(item: dict) -> dict | None:
    if not item:
        return None

    # Remove MongoDB internal ObjectId before returning response
    item.pop("_id", None)
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
        async for item in self.collection.find():
            items.append(serialize_supplier(item))
        return items

    async def get_by_id(self, item_id: str):
        item = await self.collection.find_one({"id": item_id})
        return serialize_supplier(item)
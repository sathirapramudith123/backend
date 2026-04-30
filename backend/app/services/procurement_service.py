from app.repositories.inventory_repository import InventoryItemRepository
from app.repositories.supplier_repository import SupplierRepository


class ProcurementService:
    def __init__(self):
        self.inventory_repository = InventoryItemRepository()
        self.supplier_repository = SupplierRepository()

    async def generate_recommendations(self):
        inventory_items = await self.inventory_repository.list_all()
        suppliers = await self.supplier_repository.list_all()

        recommendations = []

        active_suppliers = [
            supplier for supplier in suppliers
            if supplier.get("status") == "active"
        ]

        for item in inventory_items:
            quantity = item.get("quantity", 0)
            reorder_level = item.get("reorder_level", 0)

            if quantity <= reorder_level:
                best_supplier = max(
                    active_suppliers,
                    key=lambda supplier: supplier.get("total_score", 0),
                    default=None
                )

                recommendations.append({
                    "item_id": item["id"],
                    "item_name": item["name"],
                    "current_quantity": quantity,
                    "reorder_level": reorder_level,
                    "unit": item.get("unit", "unit"),
                    "recommendation": "Reorder now",
                    "reason": "Current stock is less than or equal to reorder level",
                    "recommended_supplier_id": best_supplier["id"] if best_supplier else None,
                    "recommended_supplier": best_supplier["name"] if best_supplier else "No supplier found",
                    "supplier_score": best_supplier.get("total_score", 0) if best_supplier else 0
                })

        return recommendations
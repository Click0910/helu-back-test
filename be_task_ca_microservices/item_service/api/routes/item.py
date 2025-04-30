from fastapi import APIRouter, Depends
from uuid import UUID
from core.use_cases.manage_stock import ReserveStockUseCase
from api.dependencies import get_item_repository, get_event_publisher

router = APIRouter(prefix="/items")


@router.get("/{item_id}/stock")
def check_stock(item_id: UUID, quantity: int):
    # Verification logic to check if the item is available
    return {"available": True}


@router.post("/{item_id}/reserve")
def reserve_stock(
    item_id: UUID,
    quantity: int,
    use_case: ReserveStockUseCase = Depends(
        lambda: ReserveStockUseCase(
            get_item_repository(), get_event_publisher()
        )
    )
):
    use_case.execute(item_id, quantity)
    return {"status": "Reserved"}

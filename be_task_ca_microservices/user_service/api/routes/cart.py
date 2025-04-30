from fastapi import APIRouter, Depends
from uuid import UUID
from core.use_cases.add_to_cart import AddToCartUseCase
from api.dependencies import get_item_client, get_user_repository

router = APIRouter(prefix="/users/{user_id}/cart")

@router.post("/")
def add_to_cart(
    user_id: UUID,
    item_id: UUID,
    quantity: int,
    use_case: AddToCartUseCase = Depends(
        lambda: AddToCartUseCase(get_item_client(), get_user_repository())
    )
):
    use_case.execute(user_id, item_id, quantity)
    return {"status": "Item added"}

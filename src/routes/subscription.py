from fastapi import APIRouter, HTTPException
from src.services.subscription import SubscriptionService
from src.schemas import (
    SubscriptionCreate, 
    SubscriptionResponse,
    CancelSubscriptionResponse
)

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])

@router.post("/")
async def create_subscription(data: SubscriptionCreate) -> SubscriptionResponse:
    """Create a new subscription."""
    return SubscriptionService.create_subscription(data)

@router.get("/users/{user_id}")
async def get_user_subscriptions(user_id: str) -> list[SubscriptionResponse]:
    """Get all subscriptions for a user."""
    try:
        subscriptions = SubscriptionService.get_user_subscriptions(user_id)
        return subscriptions
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/{subscription_id}/cancel")
async def cancel_subscription(
    subscription_id: str, 
    at_period_end: bool = True
) -> CancelSubscriptionResponse:
    """Deactivate a subscription."""
    try:
        return SubscriptionService.cancel_subscription(subscription_id, at_period_end)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
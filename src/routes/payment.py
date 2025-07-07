from fastapi import APIRouter, HTTPException

from src.schemas import CancelPaymentIntentResponse, PaymentIntentCreate, PaymentIntentResponse
from src.services import PaymentService

router = APIRouter(prefix="/payment-intents", tags=["Payment Intents"])

@router.post("/")
async def create_payment_intent(data: PaymentIntentCreate) -> PaymentIntentResponse:
    """Create a payment intent."""
    try:
        result = PaymentService.create_payment_intent(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{payment_intent_id}")
async def get_payment_intent(payment_intent_id: str) -> PaymentIntentResponse:
    """Retrieve a payment intent."""
    try:
        result = PaymentService.retrieve_payment_intent(payment_intent_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get("/user/{user_id}")
async def get_payment_intent_by_user_id(user_id: str, limit: int = 1) -> list[PaymentIntentResponse]:
    """Retrieve payment intents by user ID."""
    try:
        result = PaymentService.get_payment_intent_by_user_id(user_id, limit)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.post("/{payment_intent_id}/cancel")
async def cancel_payment_intent(payment_intent_id: str) -> CancelPaymentIntentResponse:
    """Cancel a payment intent."""
    try:
        result = PaymentService.cancel_payment_intent(payment_intent_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
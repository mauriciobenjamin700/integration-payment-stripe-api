from src.core import BaseSchema
from src.utils import CurrencyEnum


class PaymentIntentCreate(BaseSchema):
    amount: int
    currency:CurrencyEnum
    automatic_payment_methods: dict = {
        "enabled": True,
    }


class PaymentIntentResponse(BaseSchema):
    id: str
    client_secret: str
    status: str
    amount: int
    currency: CurrencyEnum
    created_at: int


class CancelPaymentIntentResponse(BaseSchema):
    id: str
    status: str
    cancellation_reason: str | None = None
from src.core import BaseSchema
from src.utils import CurrencyEnum


class CustomerMetadata(BaseSchema):
    """
    Metadata schema for customer information.

    Attributes:
        user_id (str): The unique identifier of the user.
        product_id (str): The unique identifier of the product.
    """
    user_id: str
    product_id: str

class PaymentIntentCreate(BaseSchema):
    """
    Schema for creating a payment intent.

    Attributes:
        amount (int): The amount to be charged in the smallest currency unit (e.g., cents).
        currency (CurrencyEnum): The currency in which the payment is made.
        automatic_payment_methods (dict): Configuration for automatic payment methods.
    """
    amount: int
    currency:CurrencyEnum
    automatic_payment_methods: dict = {
        "enabled": True,
        "allow_redirects": "always"  # Para métodos que redirecionam

    }
    metadata: CustomerMetadata | None = None

class PaymentIntentResponse(BaseSchema):
    """
    Schema for the response of a payment intent creation.

    Attributes:
        id (str): The unique identifier of the payment intent.
        client_secret (str): The client secret for the payment intent.
        status (str): The status of the payment intent.
        amount (int): The amount charged in the smallest currency unit (e.g., cents).
        currency (CurrencyEnum): The currency in which the payment was made.
        created (int): The timestamp when the payment intent was created.
    """
    id: str
    client_secret: str
    status: str
    amount: int
    currency: CurrencyEnum
    metadata: CustomerMetadata | None = None
    created: int

class CancelPaymentIntentResponse(BaseSchema):
    """
    Schema for the response of a payment intent cancellation.

    Attributes:
        id (str): The unique identifier of the payment intent.
        status (str): The status of the payment intent after cancellation.
        cancellation_reason (str | None): The reason for cancellation, if applicable.
    """
    id: str
    status: str
    cancellation_reason: str | None = None
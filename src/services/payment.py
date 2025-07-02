import stripe
from src.schemas.payment import CancelPaymentIntentResponse, PaymentIntentCreate, PaymentIntentResponse
from src.schemas.customer import CustomerCreate, CustomerResponse
from src.core import settings

# Configurar Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentService:
    """Service for handling Stripe payment operations."""
    
    @staticmethod
    def create_payment_intent(data: PaymentIntentCreate) -> PaymentIntentResponse:
        """Create a payment intent with Stripe."""
        try:
            intent = stripe.PaymentIntent.create(
                amount=data.amount,
                currency=data.currency,
                automatic_payment_methods=data.automatic_payment_methods,
                metadata={
                    "integration": "custom-payment-api"
                }
            )
            data = {
                'id': intent.id,
                'client_secret': intent.client_secret,
                'status': intent.status,
                'amount': intent.amount,
                'currency': intent.currency,
                'created_at': intent.created,
            }
            return PaymentIntentResponse(**data)
        except Exception as e:
            # Non-Stripe error
            raise Exception(f"Unexpected error: {str(e)}")
    
    @staticmethod
    def create_customer(data: CustomerCreate) -> CustomerResponse:
        """Create a customer in Stripe."""
        try:
            customer = stripe.Customer.create(**data.to_dict())
            return CustomerResponse.model_validate(customer, from_attributes=True)
        except Exception as e:
            raise Exception(f"Error creating customer: {str(e)}")
    
    @staticmethod
    def retrieve_payment_intent(payment_intent_id: str) -> PaymentIntentResponse:
        """Retrieve a payment intent by ID."""
        try:
            intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            data = {
                'id': intent.id,
                'client_secret': intent.client_secret,
                'status': intent.status,
                'amount': intent.amount,
                'currency': intent.currency,
                'created_at': intent.created,
            }
            return PaymentIntentResponse(**data)
        except Exception as e:
            raise Exception(f"Error retrieving payment intent: {str(e)}")
    
    @staticmethod
    def cancel_payment_intent(payment_intent_id: str) -> CancelPaymentIntentResponse:
        """Cancel a payment intent."""
        try:
            intent = stripe.PaymentIntent.cancel(payment_intent_id)
            data = {
                'id': intent.id,
                'status': intent.status,
                'cancellation_reason': intent.cancellation_reason
            }
            return CancelPaymentIntentResponse(**data)
        except stripe.error.StripeError as e:
            raise Exception(f"Error canceling payment intent: {str(e)}")
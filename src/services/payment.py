import stripe
from src.schemas.payment import (
    CancelPaymentIntentResponse, 
    PaymentIntentCreate, 
    PaymentIntentResponse
)
from src.core import settings

# Configurar Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

class PaymentService:
    """Service for handling Stripe payment operations.
    
    Methods:
        create_payment_intent(data: PaymentIntentCreate) -> PaymentIntentResponse:
            Create a payment intent with Stripe.
        
        retrieve_payment_intent(payment_intent_id: str) -> PaymentIntentResponse:
            Retrieve a payment intent by ID.
        
        get_payment_intent_by_user_id(user_id: str, limit: int = 1) -> PaymentIntentResponse:
            Retrieve a payment intent by user ID.
        
        cancel_payment_intent(payment_intent_id: str) -> CancelPaymentIntentResponse:
            Cancel a payment intent.
    """
    
    @staticmethod
    def create_payment_intent(data: PaymentIntentCreate) -> PaymentIntentResponse:
        """Create a payment intent with Stripe.
        
        Args:
            data (PaymentIntentCreate): The data for creating a payment intent.

        Returns:
            PaymentIntentResponse: The response object containing payment intent.
        """
        try:
            intent = stripe.PaymentIntent.create(
                **data.to_dict(),
            )
            intent.created
            return PaymentIntentResponse.model_validate(intent, from_attributes=True)
        except Exception as e:
            # Non-Stripe error
            raise Exception(f"Unexpected error: {str(e)}")
    
    @staticmethod
    def retrieve_payment_intent(payment_intent_id: str) -> PaymentIntentResponse:
        """Retrieve a payment intent by ID.
        
        Args:
            payment_intent_id (str): The ID of the payment intent to retrieve.
        Returns:
            PaymentIntentResponse: The payment intent response object.
        """
        try:
            intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            return PaymentIntentResponse.model_validate(intent, from_attributes=True)
        except Exception as e:
            raise Exception(f"Error retrieving payment intent: {str(e)}")
        
    @staticmethod
    def get_payment_intent_by_user_id(
            user_id: str, 
            limit: int = 1
        ) -> PaymentIntentResponse:
        """Retrieve a payment intent by user ID.
        
        Args:
            user_id (str): The ID of the user to filter payment intents.
            limit (int): The maximum number of payment intents to retrieve.

        Returns:
            PaymentIntentResponse: The payment intent response object.
        """
        try:
            # Assuming metadata contains user_id
            result = stripe.PaymentIntent.search(
                limit=limit,
                query=f'metadata["user_id"]:"{user_id}"',
            )
            
            return [
                PaymentIntentResponse.model_validate(intent, from_attributes=True)
                for intent in result.data
            ]
            
        except Exception as e:
            raise Exception(f"Error retrieving payment intent by user ID: {str(e)}")
    
    @staticmethod
    def cancel_payment_intent(payment_intent_id: str) -> CancelPaymentIntentResponse:
        """Cancel a payment intent.
        
        Args:
            payment_intent_id (str): The ID of the payment intent to cancel.

        Returns:
            CancelPaymentIntentResponse: The response object containing cancellation details.
        """
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
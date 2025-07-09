import stripe
from src.core import settings
from src.schemas import (
    ProductResponse,
    SubscriptionCreate, 
    SubscriptionResponse
)
from src.schemas.subscription import CancelSubscriptionResponse

stripe.api_key = settings.STRIPE_SECRET_KEY

class SubscriptionService:
    """Service for handling Stripe subscription operations."""
    

    
    @staticmethod
    def create_subscription(data: SubscriptionCreate) -> SubscriptionResponse:
        """
        Create a subscription.
        
        Args:
            data (SubscriptionCreate): The subscription data to create.

        Returns:
            SubscriptionResponse: The created subscription response.
        """

        metadata = data.metadata.to_dict() if data.metadata else {}
            
        subscription = stripe.Subscription.create(
            customer=data.customer_id,
            items=[{'price': data.price_id}],
            trial_period_days=data.trial_period_days,
            metadata=metadata,
            payment_behavior='default_incomplete',
            payment_settings={'save_default_payment_method': 'on_subscription'},
            expand=['latest_invoice.payment_intent']
        )

        return SubscriptionService.map_subscription_to_response(subscription)
    

    @staticmethod
    def create_subscription_with_trial(data: SubscriptionCreate) -> SubscriptionResponse:
        """ Create a subscription with a trial period.

        Args:
            data (SubscriptionCreate): The subscription data to create.

        Returns:
            SubscriptionResponse: The created subscription response.
        """

        metadata = data.metadata.to_dict() if data.metadata else {}
            
        subscription = stripe.Subscription.create(
            customer=data.customer_id,
            items=[{'price': data.price_id}],
            trial_period_days=data.trial_period_days if data.trial_period_days else 7,
            metadata=metadata,
            payment_behavior='default_incomplete',
            payment_settings={'save_default_payment_method': 'on_subscription'},
            expand=['latest_invoice.payment_intent']
        )

        return SubscriptionService.map_subscription_to_response(subscription)
    

    @staticmethod
    def create_free_subscription(data: SubscriptionCreate) -> SubscriptionResponse:
        """Create a free subscription (no invoice).
        
        Args:
            data (SubscriptionCreate): The subscription data to create.

        Returns:
            SubscriptionResponse: The created subscription response.
        """
        try:
            # Primeiro, criar um preço gratuito
            free_price = stripe.Price.create(
                product=data.price_id,  # Usar como product_id
                unit_amount=0,  # Gratuito
                currency='brl',
                recurring={'interval': 'month'}
            )
            
            metadata = data.metadata.to_dict() if data.metadata else {}
            
            subscription = stripe.Subscription.create(
                customer=data.customer_id,
                items=[{'price': free_price.id}],  # Usar preço gratuito
                metadata=metadata,
                expand=['latest_invoice.payment_intent']
            )
        
            return SubscriptionService.map_subscription_to_response(subscription)
            
        except Exception as e:
            raise Exception(f"Error creating free subscription: {str(e)}")

    @staticmethod
    def get_user_subscriptions(user_id: str) -> list[SubscriptionResponse]:
        """Get all subscriptions for a user.
        
        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            list[SubscriptionResponse]: A list of subscriptions for the user.
        """
        try:
            subscriptions = stripe.Subscription.search(
                query=f'metadata["user_id"]:"{user_id}"',
                expand=['data.items.data.price']
            )
            
            return [
                SubscriptionService.map_subscription_to_response(sub)
                for sub in subscriptions.data
            ]
        except Exception as e:
            raise Exception(f"Error getting user subscriptions: {str(e)}")
    
    @staticmethod
    def cancel_subscription(subscription_id: str, at_period_end: bool = True) -> CancelSubscriptionResponse:
        """Cancel a subscription.
        
        Args:
            subscription_id (str): The unique identifier of the subscription to cancel.
            at_period_end (bool): Whether to cancel at the end of the period or immediately.

        Returns:
            dict: The response from the Stripe API after canceling the subscription.
        """
        try:
            if at_period_end:
                # Cancelar no final do período
                subscription = stripe.Subscription.modify(
                    subscription_id,
                    cancel_at_period_end=True
                )
            else:
                # Cancelar imediatamente
                subscription = stripe.Subscription.cancel(subscription_id)
            
            return CancelSubscriptionResponse.model_validate(
                subscription, 
                from_attributes=True
            )
        except Exception as e:
            raise Exception(f"Error canceling subscription: {str(e)}")
    
    @staticmethod
    def list_products(include_archived: bool = False) -> list[ProductResponse]:
        """list all products with their prices.
        
        Args:
            include_archived (bool): Whether to include archived products.

        Returns:
            list[ProductResponse]: A list of products with their prices.
        """
        try:
            products = stripe.Product.list(
                active=not include_archived if not include_archived else None
            )
            result = []
            
            for product in products.data:
                print("Product: ", product)
                prices = stripe.Price.list(
                    product=product.id, 
                    active=True,
                    expand=['data.product']
                )
                print("PRICES: ", prices)
                result.append(
                    ProductResponse(
                        id=product.id,
                        name=product.name,
                        description=product.description,
                        metadata=dict(product.metadata) if product.metadata else None,
                        created=product.created,
                        prices=[
                            SubscriptionService.map_price_to_response(price)
                            for price in prices.data
                        ]
                    )
                )
            return result
        except Exception as e:
            raise Exception(f"Error listing products: {str(e)}")
        


    
    @staticmethod
    def map_subscription_to_response(subscription: stripe.Subscription) -> SubscriptionResponse:
        """
        Map a Stripe Subscription object to a SubscriptionResponse schema.

        Args:
            subscription (stripe.Subscription): The Stripe Subscription object to map.

        Returns:
            SubscriptionResponse: The mapped SubscriptionResponse schema.
        """ 
        first_item = subscription["items"]["data"][0]
        
        return SubscriptionResponse(
            id=subscription.id,
            status=subscription.status,
            customer=subscription.customer,
            start_date=subscription.start_date,
            ended_at=subscription.ended_at,
            price_id=first_item.price.id,
            amount=first_item.price.unit_amount,
            currency=first_item.price.currency,
            interval=(
                first_item.price.recurring.interval 
                if first_item.price.recurring 
                else None
            ),
            trial_start=subscription.trial_start,
            trial_end=subscription.trial_end,
            metadata=dict(subscription.metadata) if subscription.metadata else {}
        )
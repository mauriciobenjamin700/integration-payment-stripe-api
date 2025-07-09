import stripe
from src.core import settings
from src.schemas import (
    ProductCreate,
    ProductResponse,
    PriceCreate,
    PriceResponse
)
from src.schemas.product import Recurring

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductService:

    @staticmethod
    def create_product(data: ProductCreate) -> ProductResponse:
        """Create a product in Stripe.
        
        Args:
            data (ProductCreate): The product data to create.

        Returns:
            ProductResponse: The created product response.
        """
        try:
            product = stripe.Product.create(
                name=data.name,
                description=data.description,
                metadata=data.metadata or {}
            )
            return ProductResponse.model_validate(product, from_attributes=True)
        except Exception as e:
            raise Exception(f"Error creating product: {str(e)}")
        
    @staticmethod
    def delete_product(product_id: str) -> None:
        """Delete a product by its ID.
        
        Args:
            product_id (str): The unique identifier of the product to delete.

        Returns:
            None
        """
        # Primeiro, arquivar todos os preços ativos do produto
        prices = stripe.Price.list(product=product_id, active=True)
        for price in prices.data:
            stripe.Price.modify(price.id, active=False)
        
        # Depois, arquivar o produto
        product = stripe.Product.modify(product_id, active=False)
        
        return {
            'id': product.id,
            'name': product.name,
            'active': product.active,
            'archived_at': product.updated,
            'message': 'Product successfully archived'
        }
    
    @staticmethod
    def create_price(data: PriceCreate) -> PriceResponse:
        """Create a price for a product.
        
        Args:
            data (PriceCreate): The price data to create.

        Returns:
            PriceResponse: The created price response.
        """
        try:
            price = stripe.Price.create(
                product=data.product_id,
                unit_amount=data.unit_amount,
                currency=data.currency,
                recurring=data.recurring.to_dict(),
                expand=['product']
            )
            return ProductService.map_price_to_response(price)
            
        except Exception as e:
            raise Exception(f"Error creating price: {str(e)}")
        
    @staticmethod
    def delete_price(price_id: str) -> dict:
        """Delete a price by its ID.
        
        Args:
            price_id (str): The unique identifier of the price to delete.

        Returns:
            None
        """
        price = stripe.Price.modify(price_id, active=False)
        
        return {
            'id': price.id,
            'product_id': price.product,
            'active': price.active,
            'message': 'Price successfully archived'
        }
    

    @staticmethod
    def map_price_to_response(price: stripe.Price) -> PriceResponse:
        """
        Map a Stripe Price object to a PriceResponse schema.

        Args:
            price (stripe.Price): The Stripe Price object to map.

        Returns:
            PriceResponse: The mapped PriceResponse schema.
        """
        return PriceResponse(
            id=price.id,
            product_id=price.product.id,
            name=price.product.name,
            unit_amount=price.unit_amount,
            currency=price.currency,
            created=price.created,
            recurring=Recurring(
                interval=price.recurring.interval if price.recurring else None,
                interval_count=price.recurring.interval_count if price.recurring else 1,
                trial_period_days=price.recurring.trial_period_days if price.recurring else None
            )
        )
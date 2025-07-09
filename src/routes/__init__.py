from .customer import router as customer_router
from .payment import router as payment_router
from .product import router as product_router
from .subscription import router as subscription_router


__all__ = [
    "customer_router",
    "payment_router",
    "product_router",
    "subscription_router"
]
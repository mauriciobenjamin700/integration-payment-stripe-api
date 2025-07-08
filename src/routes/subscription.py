from fastapi import APIRouter, HTTPException, Query
from src.schemas import (
    ProductResponse
)
from src.services.subscription import SubscriptionService
from src.schemas import (
    ProductCreate, 
    PriceCreate, 
    SubscriptionCreate, 
    SubscriptionResponse,
    CancelSubscriptionResponse
)

router = APIRouter(prefix="/subscriptions", tags=["subscriptions"])

@router.post("/products")
async def create_product(data: ProductCreate) -> ProductResponse:
    """Criar um produto."""
    try:
        return SubscriptionService.create_product(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/products")
async def list_products(
    include_archived: bool = Query(False, description="Include archived products")
    ) -> list[ProductResponse]:
    """Listar todos os produtos e preços."""
    try:
        return SubscriptionService.list_products(include_archived)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@router.delete("/products/{product_id}")
async def delete_product(product_id: str) -> ProductResponse:
    """Arquivar um produto."""
    try:
        return SubscriptionService.delete_product(product_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/prices")
async def create_price(data: PriceCreate) -> ProductResponse:
    """Criar um preço para um produto."""
    try:
        return SubscriptionService.create_price(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/prices/{price_id}")
async def delete_price(price_id: str) -> dict:
    """Arquivar um preço."""
    try:
        return SubscriptionService.delete_price(price_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/")
async def create_subscription(data: SubscriptionCreate) -> SubscriptionResponse:
    """Criar uma assinatura."""
    return SubscriptionService.create_subscription(data)

@router.get("/users/{user_id}")
async def get_user_subscriptions(user_id: str) -> list[SubscriptionResponse]:
    """Obter assinaturas de um usuário."""
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
    """Cancelar uma assinatura."""
    try:
        return SubscriptionService.cancel_subscription(subscription_id, at_period_end)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
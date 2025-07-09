from fastapi import APIRouter, HTTPException, Query
from src.schemas import (
    ProductCreate, 
    PriceCreate, 
    ProductResponse
)
from src.schemas.product import PriceResponse
from src.services import ProductService

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/")
async def create_product(data: ProductCreate) -> ProductResponse:
    """Create a new product."""
    try:
        return ProductService.create_product(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.get("/")
async def list_products(
    include_archived: bool = Query(False, description="Include archived products")
    ) -> list[ProductResponse]:
    """List all products."""
    try:
        return ProductService.list_products(include_archived)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    
@router.delete("/{product_id}")
async def delete_product(product_id: str) -> ProductResponse:
    """Deactivate a product."""
    try:
        return ProductService.delete_product(product_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/prices")
async def create_price(data: PriceCreate) -> PriceResponse:
    """Create a new price for a product."""
    try:
        return ProductService.create_price(data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/prices/{price_id}")
async def delete_price(price_id: str) -> dict:
    """Deactivate a price."""
    try:
        return ProductService.delete_price(price_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
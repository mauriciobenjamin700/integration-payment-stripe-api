from fastapi import APIRouter

from src.schemas import CustomerCreate, CustomerResponse
from src.services import CustomerService

router = APIRouter(prefix="/customer", tags=["Customer"])

@router.post("/")
async def create_customer(data: CustomerCreate) -> CustomerResponse:
    """Create a new customer."""
    return CustomerService.create_customer(data)

@router.get("/{customer_id}")
async def retrieve_customer(customer_id: str) -> CustomerResponse:
    """Retrieve a customer by ID."""
    return CustomerService.retrieve_customer(customer_id)

@router.get("/user/{user_id}")
async def get_customer_by_user_id(user_id: str) -> CustomerResponse:
    """Retrieve a customer by user ID."""
    return CustomerService.get_customer_by_user_id(user_id)

@router.put("/{customer_id}")
async def update_customer(customer_id: str, data: CustomerCreate) -> CustomerResponse:
    """Update a customer."""
    return CustomerService.update_customer(customer_id, data)

@router.delete("/{customer_id}")
async def delete_customer(customer_id: str) -> dict:
    """Delete a customer."""
    return CustomerService.delete_customer(customer_id)

@router.delete("/user/{user_id}")
async def delete_customer_by_user_id(user_id: str) -> dict:
    """Delete a customer by user ID."""
    return CustomerService.delete_by_user_id(user_id)
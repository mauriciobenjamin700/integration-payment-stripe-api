from src.core import BaseSchema


class Address(BaseSchema):
    city: str
    country: str
    line1: str
    postal_code: str
    state: str


class Shipping(BaseSchema):
    address: Address
    name: str


class CustomerCreate(BaseSchema):
    email:str
    name:str
    shipping: Shipping
    address: Address


class CustomerResponse(BaseSchema):
    id: str
    email: str
    name: str
    shipping: Shipping
    address: Address

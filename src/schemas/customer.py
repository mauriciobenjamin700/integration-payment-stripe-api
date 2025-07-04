from src.core import BaseSchema


class Address(BaseSchema):
    """
    Address schema for customer information.

    Attributes:
        city (str): The city of the address.
        country (str): The country of the address.
        line1 (str): The first line of the address.
        postal_code (str): The postal code of the address.
        state (str): The state of the address.
    """
    city: str
    country: str
    line1: str
    postal_code: str
    state: str


class Shipping(BaseSchema):
    """
    Shipping schema for customer information.

    Attributes:
        address (Address): The address for shipping.
        name (str): The name of the recipient for shipping.
    """
    address: Address
    name: str


class CustomerCreate(BaseSchema):
    """
    CustomerCreate schema for creating a new customer.

    Attributes:
        email (str): The email of the customer.
        name (str): The name of the customer.
        shipping (Shipping): The shipping information for the customer.
        address (Address): The address of the customer.
    """
    email:str
    name:str
    shipping: Shipping
    address: Address


class CustomerResponse(BaseSchema):
    """
    CustomerResponse schema for customer information.

    Attributes:
        id (str): The unique identifier of the customer.
        email (str): The email of the customer.
        name (str): The name of the customer.
        shipping (Shipping): The shipping information for the customer.
        address (Address): The address of the customer.
    """
    id: str
    email: str
    name: str
    shipping: Shipping
    address: Address

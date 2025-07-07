from pydantic import Field
from src.core import BaseSchema
from src.utils import CurrencyEnum, SubscriptionInterval



class ProductCreate(BaseSchema):
    """
    Schema for creating a product.

    Attributes:
        name (str): The name of the product.
        description (str | None): The description of the product, optional.
        metadata (dict[str, str] | None): Additional metadata for the product, optional.
    """
    name: str
    description: str | None = None
    metadata: dict[str, str] | None = None


class Recurring(BaseSchema):
    """
    Schema for recurring billing details.

    Attributes:
        interval (SubscriptionInterval): The billing interval.
        interval_count (int): The number of intervals for the price.
        trial_period_days (int | None): The number of trial period days, optional.
    """
    interval: SubscriptionInterval
    interval_count: int = Field(1, ge=1, description="Number of intervals")
    trial_period_days: int | None = Field(None, ge=0)

class PriceCreate(BaseSchema):
    """
    Schema for creating a price for a product.

    Attributes:
        product_id (str): The unique identifier of the product.
        unit_amount (int): The amount to be charged in cents, must be greater than 0.
        currency (str): The currency in which the price is set
        interval (SubscriptionInterval): The billing interval for the price.
        interval_count (int): The number of intervals for the price, must be at least 1.
        trial_period_days (int | None): The number of trial period days.
    """
    product_id: str
    unit_amount: int = Field(gt=0, description="Amount in cents")
    currency: CurrencyEnum
    recurring:Recurring


class PriceResponse(BaseSchema):
    """
    Schema for the response of a price.

    Attributes:
        id (str): The unique identifier of the price.
        product_id (str): The unique identifier of the product associated with the price.
        name (str): The name of the price.
        unit_amount (int): The amount to be charged in cents.
        currency (str): The currency in which the price is set.
        created (int): The created at timestamp
        interval_count (int): The number of intervals for the price.
    """
    id: str
    product_id: str
    name: str
    unit_amount: int
    currency: str
    created: int
    recurring:Recurring


class ProductResponse(BaseSchema):
    """
    Schema for the response of a product.

    Attributes:
        id (str): The unique identifier of the product.
        name (str): The name of the product.
        description (str | None): The description of the product, optional.
        created (int): The timestamp when the product was created.
    """
    id: str
    name: str
    description: str | None = None
    metadata: dict[str, str] | None = None
    created: int
    prices: list[PriceResponse] | None = None
from src.core import BaseSchema
from src.utils import SubscriptionInterval, SubscriptionStatus

class Metadata(BaseSchema):
    """
    Schema for additional metadata.

    Attributes:
        user_id (str): The unique identifier of the user.
    """
    user_id: str

class SubscriptionCreate(BaseSchema):
    """
    Schema for creating a subscription.

    Attributes:
        customer_id (str): The unique identifier of the customer.
        price_id (str): The unique identifier of the price to subscribe to.
        trial_period_days (int | None): The number of trial period days, optional.
        metadata (dict[str, str] | None): Additional metadata for the subscription.
    """

    customer_id: str | None = None
    price_id: str
    trial_period_days: int | None = None
    metadata: Metadata | None = None
    

class SubscriptionResponse(BaseSchema):
    """
    Schema for the response of a subscription.

    Attributes:
        id (str): The unique identifier of the subscription.
        status (str): The status of the subscription.
        customer (str): The unique identifier of the customer.
        current_period_start (int): The start timestamp of the current period.
        current_period_end (int): The end timestamp of the current period.
        price_id (str): Unique identifier of the price associated with the subscription.
        amount (int): The amount charged for the subscription in the smallest currency.
        currency (str): The currency in which the subscription is charged.
        interval (SubscriptionInterval): The billing interval of the subscription.
        trial_start (int | None): The start timestamp of the trial period
        trial_end (int | None): The end timestamp of the trial period
        metadata (dict[str, str] | None): Additional metadata for the subscription.
    """
    id: str
    status: SubscriptionStatus
    customer: str
    start_date: int
    ended_at: int | None = None
    price_id: str
    amount: int
    currency: str
    interval: SubscriptionInterval
    trial_start: int | None = None
    trial_end: int | None = None
    metadata: dict[str, str] | None = None


class CancelSubscriptionResponse(BaseSchema):
    """
    Schema for the response of a canceled subscription.

    Attributes:
        id (str): The unique identifier of the subscription.
        status (str): The status of the subscription after cancellation.
        cancel_at_period_end (bool): Indicates if the subscription will be canceled at the end of the period.
        canceled_at (int | None): The timestamp when the subscription was canceled, if applicable.
        start_date (int): The end timestamp of the current period.
    """
    id: str
    status: SubscriptionStatus
    cancel_at_period_end: bool
    canceled_at: int | None = None
    start_date: int
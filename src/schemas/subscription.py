from src.core import BaseSchema


class SubscriptionCreate(BaseSchema):
    """
    Schema for creating a subscription.
    """

    customer_id: str
    plan_id: str
    
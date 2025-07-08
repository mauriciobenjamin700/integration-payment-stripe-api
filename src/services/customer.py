from fastapi import HTTPException
import stripe
from src.core import settings
from src.schemas import (
    CustomerCreate,
    CustomerResponse
)

stripe.api_key = settings.STRIPE_SECRET_KEY

class CustomerService:
    """Service for handling Stripe customer operations.
    
    Methods:
        create_customer(data: CustomerCreate) -> CustomerResponse:
            Create a customer in Stripe.
        retrieve_customer(customer_id: str) -> CustomerResponse:
            Retrieve a customer by ID.
        get_customer_by_user_id(user_id: str) -> CustomerResponse:
            Retrieve a customer by user ID.
        update_customer(customer_id: str, data: CustomerCreate) -> CustomerResponse:
            Update a customer in Stripe.
        delete_customer(customer_id: str) -> None:
            Delete a customer in Stripe.
    """

    @staticmethod
    def create_customer(data: CustomerCreate) -> CustomerResponse:
        """Create a customer in Stripe.

        Args:
            data (CustomerCreate): The customer data to create.

        Returns:
            CustomerResponse: The created customer response.
        """
        try:
            customers = stripe.Customer.list(
                email=data.email,
                limit=1
            )
            if customers.data:
                raise HTTPException(
                    status_code=409,
                    detail="Customer with this email already exists."
                )

            if data.metadata:
                customers = stripe.Customer.search(
                    query=f'metadata["user_id"]:"{data.metadata.user_id}"'
                )
                if customers.data:
                    raise HTTPException(
                        status_code=409,
                        detail="Customer with this user ID already exists."
                    )
            customer = stripe.Customer.create(**data.to_dict())

            return CustomerResponse.model_validate(customer, from_attributes=True)
        
        except HTTPException as http_exc:
            raise http_exc
        
        except Exception as e:

            raise HTTPException(
                status_code=500,
                detail=f"Error creating customer: {str(e)}"
            )
        

    @staticmethod
    def retrieve_customer(customer_id: str) -> CustomerResponse:
        """Retrieve a customer by ID.

        Args:
            customer_id (str): The ID of the customer to retrieve.

        Returns:
            CustomerResponse: The retrieved customer response.
        """
        try:
            customer = stripe.Customer.retrieve(customer_id)
            return CustomerResponse.model_validate(customer, from_attributes=True)
        except Exception as e:
            raise Exception(f"Error retrieving customer: {str(e)}")
        
    @staticmethod
    def get_customer_by_user_id(user_id: str) -> CustomerResponse:
        """Retrieve a customer by user ID.

        Args:
            user_id (str): The user ID to search for.

        Returns:
            CustomerResponse: The retrieved customer response.
        """
        try:
            customers = stripe.Customer.search(
                query=f'metadata["user_id"]:"{user_id}"'
            )
            if customers.data:
                return CustomerResponse.model_validate(customers.data[0], from_attributes=True)
            raise HTTPException(
                status_code=404,
                detail="Customer not found for the provided user ID."
            )
        except Exception as e:
            raise Exception(f"Error retrieving customer by user ID: {str(e)}")
        

    @staticmethod
    def update_customer(customer_id: str, data: CustomerCreate) -> CustomerResponse:
        """Update a customer in Stripe.

        Args:
            customer_id (str): The ID of the customer to update.
            data (CustomerCreate): The updated customer data.

        Returns:
            CustomerResponse: The updated customer response.
        """
        try:
            customer = stripe.Customer.modify(customer_id, **data.to_dict())
            return CustomerResponse.model_validate(customer, from_attributes=True)
        except Exception as e:
            raise Exception(f"Error updating customer: {str(e)}")
        

    @staticmethod
    def delete_customer(customer_id: str) -> dict:
        """Delete a customer in Stripe.

        Args:
            customer_id (str): The ID of the customer to delete.

        Returns:
            None: If the deletion is successful.
        """
        try:
            customer = stripe.Customer.delete(customer_id)

            return {
                'id': customer.id,
                'deleted': customer.deleted,
                'message': 'Customer successfully deleted'
            }

        except Exception as e:
            print(f"Error deleting customer: {str(e)}")
            raise HTTPException(
                status_code=404,
                detail=f"User not found"
            )
    
    @staticmethod
    def delete_by_user_id(user_id: str) -> dict:
        """Delete a customer by user ID.

        Args:
            user_id (str): The user ID to search for.

        Returns:
            dict: A dictionary containing the deletion status and message.
        """
        try:
            customers = stripe.Customer.search(
                query=f'metadata["user_id"]:"{user_id}"'
            )
            if not customers.data:
                raise HTTPException(
                    status_code=404,
                    detail="Customer not found for the provided user ID."
                )
            customer = customers.data[0]
            stripe.Customer.delete(customer.id)

            return {
                'id': customer.id,
                'deleted': True,
                'message': 'Customer successfully deleted'
            }
        
        except HTTPException as http_exc:
            raise http_exc

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Error deleting customer by user ID: {str(e)}"
            )
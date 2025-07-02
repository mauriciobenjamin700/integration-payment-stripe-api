import stripe
from typing import Dict, Any
from src.core import settings

class WebhookService:
    """Service for handling Stripe webhooks."""
    
    @staticmethod
    def verify_webhook_signature(payload: bytes, sig_header: str) -> stripe.Event:
        """Verify webhook signature and return event."""
        try:
            event = stripe.Webhook.construct_event(
                payload, 
                sig_header, 
                settings.webhook_secret
            )
            return event
        except ValueError as e:
            # Invalid payload
            raise Exception("Invalid payload")
        except stripe.error.SignatureVerificationError as e:
            # Invalid signature
            raise Exception("Invalid signature")
    
    @staticmethod
    def handle_webhook_event(event: stripe.Event) -> Dict[str, Any]:
        """Handle different types of webhook events."""
        
        if event['type'] == 'payment_intent.succeeded':
            payment_intent = event['data']['object']
            return {
                'event_type': 'payment_succeeded',
                'payment_intent_id': payment_intent['id'],
                'amount': payment_intent['amount'],
                'currency': payment_intent['currency']
            }
        
        elif event['type'] == 'payment_intent.payment_failed':
            payment_intent = event['data']['object']
            return {
                'event_type': 'payment_failed',
                'payment_intent_id': payment_intent['id'],
                'failure_code': payment_intent.get('last_payment_error', {}).get('code'),
                'failure_message': payment_intent.get('last_payment_error', {}).get('message')
            }
        
        elif event['type'] == 'customer.created':
            customer = event['data']['object']
            return {
                'event_type': 'customer_created',
                'customer_id': customer['id'],
                'email': customer['email']
            }
        
        else:
            return {
                'event_type': 'unhandled',
                'type': event['type']
            }
from fastapi import FastAPI, HTTPException, Request, Header
from fastapi.middleware.cors import CORSMiddleware

from src.services.payment import PaymentService
from src.services.webhook import WebhookService
from src.schemas.payment import CancelPaymentIntentResponse, PaymentIntentCreate, PaymentIntentResponse
from src.schemas.customer import CustomerCreate, CustomerResponse

app = FastAPI(
    title="Stripe Integration API",
    description="API para integração com Stripe",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/payment-intents")
async def create_payment_intent(data: PaymentIntentCreate) -> PaymentIntentResponse:
    """Create a payment intent."""
    try:
        result = PaymentService.create_payment_intent(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/payment-intents/{payment_intent_id}")
async def get_payment_intent(payment_intent_id: str) -> PaymentIntentResponse:
    """Retrieve a payment intent."""
    try:
        result = PaymentService.retrieve_payment_intent(payment_intent_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@app.post("/payment-intents/{payment_intent_id}/cancel")
async def cancel_payment_intent(payment_intent_id: str) -> CancelPaymentIntentResponse:
    """Cancel a payment intent."""
    try:
        result = PaymentService.cancel_payment_intent(payment_intent_id)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/customers")
async def create_customer(data: CustomerCreate) -> CustomerResponse:
    """Create a customer."""
    try:
        result = PaymentService.create_customer(data)
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/webhooks")
async def handle_webhook(
    request: Request,
    stripe_signature: str = Header(None, alias="stripe-signature")
):
    """Handle Stripe webhooks."""
    payload = await request.body()
    
    try:
        event = WebhookService.verify_webhook_signature(payload, stripe_signature)
        result = WebhookService.handle_webhook_event(event)
        return {"received": True, "processed": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
async def health_check():
    """Health check endpoint."""
    return {"detail": "API is running", "version": "0.1.0"}
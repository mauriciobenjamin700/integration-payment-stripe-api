from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import payment_router, subscription_router

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

app.include_router(payment_router)
app.include_router(subscription_router)


@app.get("/")
async def health_check():
    """Health check endpoint."""
    return {"detail": "API is running", "version": "0.1.0"}
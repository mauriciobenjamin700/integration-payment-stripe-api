from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes import (
    customer_router,
    payment_router, 
    subscription_router
)

app = FastAPI(
    title="Stripe Integration API",
    description="API para integração com Stripe",
    version="0.1.0"
)

ORIGINS = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:4173",
    "http://localhost:4242",
]

METHODS = [
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "PATCH",
    "OPTIONS",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=METHODS,
    allow_headers=["*"],
)

app.include_router(customer_router)
app.include_router(payment_router)
app.include_router(subscription_router)


@app.get("/")
async def health_check():
    """Health check endpoint."""
    return {"detail": "API is running", "version": "0.1.0"}
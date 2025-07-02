import uvicorn
from src.app import app


print("Starting Stripe Integration API...")
uvicorn.run(
    app,
    host="0.0.0.0",
    port=4242
)

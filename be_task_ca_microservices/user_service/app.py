import os
from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import pika
from adapters.db.session import get_db, engine
from adapters.db.models import user_model  # For alembic
from api.routes import user, cart
from adapters.clients.http_item_client import HTTPItemClient
from adapters.event_handlers import CartSagaHandler
from core.contracts.item_client import ItemClient

# Initial configurations
ITEM_SERVICE_URL = os.getenv("ITEM_SERVICE_URL", "http://item-service:8001")
RABBITMQ_URL = os.getenv("RABBITMQ_URL", "amqp://guest:guest@rabbitmq:5672/")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Init RabbitMQ connection
    connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_URL))
    channel = connection.channel()
    channel.queue_declare(queue='item_responses')

    # Init Event Handlers
    saga_handler = CartSagaHandler(channel)
    saga_handler.start_listening()

    yield

    connection.close()


app = FastAPI(lifespan=lifespan)

# For CQRS if is needed
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency Injections
def get_item_client() -> ItemClient:
    return HTTPItemClient(base_url=ITEM_SERVICE_URL)


# Include routers
app.include_router(user.router)
app.include_router(cart.router)


# Health Check if is needed
@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "ok", "db": "healthy"}
    except Exception as e:
        return {"status": "error", "db": str(e)}

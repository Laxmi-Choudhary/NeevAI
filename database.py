from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

client: AsyncIOMotorClient = None

def get_db():
    return client["neevai"]

async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(settings.MONGO_URI)

async def close_mongo_connection():
    global client
    if client:
        client.close()

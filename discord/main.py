import asyncio
from fastapi import FastAPI
from dotenv import load_dotenv
import os
from models import AppMetadata
from routes import router
from bot import bot, start_discord_bot

# Load environment variables from the .env file
load_dotenv()

DISCORD_BOT_KEY = os.getenv("DISCORD_BOT_KEY")

# Get App Metadata from models.py
metadata = AppMetadata()

# Initialize the FastAPI app
app = FastAPI(
    title=metadata.title,
    description=metadata.description,
    version=metadata.version,
    openapi_tags=metadata.openapi_tags,
    info=metadata.info,
    external_docs=metadata.external_docs
)

# Include the router from routes.py
app.include_router(router)

# Start the Discord bot in the background with FastAPI
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_discord_bot(DISCORD_BOT_KEY))

@app.on_event("shutdown")
async def shutdown_event():
    await bot.close()

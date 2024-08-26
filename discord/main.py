from fastapi import FastAPI, Response
from fastapi.openapi.models import Info
from fastapi.openapi.models import ExternalDocumentation
from fastapi.responses import RedirectResponse, HTMLResponse
import requests
from dotenv import load_dotenv
import os
import uvicorn
import pandas as pd


# Load environment variables from the .env file
load_dotenv()

app = FastAPI(
    title="Majestic Coding Server Discord API",
    description="Discord Bot for Github Commits & YouTube Releases.",
    version="1.0.0",
    openapi_tags=[
        {
            "name": "Github",
            "description": "Github Commits for Discord Message.",
        },
        {
            "name": "YouTube",
            "description": "Latest Releases for Discord Message.",
        },
    ],
    info=Info(
        title="Majestic Coding Server Discord API",
        version="1.0.0",
        description="Discord Bot for Github Commits & YouTube Releases.",
        terms_of_service="https://discord-bot-majestic-coding.onrender.com/terms",
        contact={
            "name": "Matt Majestic",
            "url": "https://www.youtube.com/@majesticcoding",
        },
        license={
            "name": "Apache 2.0",
            "url": "https://www.apache.org/licenses/LICENSE-2.0",
        },
    ),
    external_docs=ExternalDocumentation(
        description="Find more information here",
        url="https://discord-bot-majestic-coding.onrender.com/docs",
    ),
)

@app.get("/", include_in_schema=False)
async def redirect_to_docs():
    """
    Redirect to the documentation.
    """
    response = RedirectResponse(url='/docs')
    return response

@app.get("/github_commits",include_in_schema=True)
async def github_commits():
    return "Latest Github Commit when Pushed"

@app.get("/youtube_releases",include_in_schema=True)
async def youtube_releases():
    return "Latest YouTube Video when Released"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8885)
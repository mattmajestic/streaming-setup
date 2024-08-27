from pydantic import BaseModel
from typing import Optional
from fastapi.openapi.models import Info, ExternalDocumentation

class YouTubeRelease(BaseModel):
    title: str
    url: str

class GitHubCommit(BaseModel):
    repo: str
    message: str
    sha: str
    author: str
    date: str
    url: str
    
class AppMetadata:
    def __init__(self):
        self.title = "Majestic Coding Server Discord API"
        self.description = "Discord Bot for Github Commits & YouTube Releases."
        self.version = "1.0.0"
        self.openapi_tags = [
            {
                "name": "Github",
                "description": "Github Commits for Discord Message.",
            },
            {
                "name": "YouTube",
                "description": "Latest Releases for Discord Message.",
            },
        ]
        self.info = Info(
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
        )
        self.external_docs = ExternalDocumentation(
            description="Find more information here",
            url="https://discord-bot-majestic-coding.onrender.com/docs",
        )
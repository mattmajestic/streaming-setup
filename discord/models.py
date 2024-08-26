from pydantic import BaseModel
from typing import Optional

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

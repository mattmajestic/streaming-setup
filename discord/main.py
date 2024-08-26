from fastapi import FastAPI, Response, HTTPException
from fastapi.openapi.models import Info
from fastapi.openapi.models import ExternalDocumentation
from fastapi.responses import RedirectResponse, HTMLResponse
import requests
from dotenv import load_dotenv
import os
import uvicorn
import pandas as pd
from discord.ext import commands
import discord
from github import Github
from models import YouTubeRelease, GitHubCommit


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

@app.get("/latest_youtube_release", response_model=YouTubeRelease, include_in_schema=True)
async def latest_youtube_release():
    # Placeholder data until you implement the actual YouTube API call
    return YouTubeRelease(
        title="My Latest YouTube Video",
        url="https://www.youtube.com/watch?v=VIDEO_ID"
    )

@app.get("/latest_github_commit", response_model=GitHubCommit, include_in_schema=True)
async def latest_github_commit():
    github_token = os.environ.get("GITHUB_TOKEN")
    
    if not github_token:
        raise HTTPException(status_code=500, detail="GITHUB_TOKEN not found in environment variables")

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        # Get user's repos, sorted by last push date
        repos_url = "https://api.github.com/user/repos?sort=pushed&direction=desc&per_page=1"
        repos_response = requests.get(repos_url, headers=headers)
        repos_response.raise_for_status()
        repos = repos_response.json()

        if not repos:
            return {"message": "No repositories found"}

        latest_repo = repos[0]
        
        # Get the latest commit from this repository
        commits_url = f"https://api.github.com/repos/{latest_repo['full_name']}/commits?per_page=1"
        commits_response = requests.get(commits_url, headers=headers)
        commits_response.raise_for_status()
        commits = commits_response.json()

        if not commits:
            return {"message": "No commits found in the latest repository"}

        latest_commit = commits[0]

        return GitHubCommit(
            repo=latest_repo['name'],
            message=latest_commit['commit']['message'],
            sha=latest_commit['sha'],
            author=latest_commit['commit']['author']['name'],
            date=latest_commit['commit']['author']['date'],
            url=latest_commit['html_url']
        )

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data from GitHub API: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
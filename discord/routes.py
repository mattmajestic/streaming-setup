# routes.py

from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from models import YouTubeRelease, GitHubCommit
from services.github_service import get_latest_github_commit

router = APIRouter()

@router.get("/", include_in_schema=False)
async def redirect_to_docs():
    """
    Redirect to the documentation.
    """
    return RedirectResponse(url='/docs')

@router.get("/latest_youtube_release", response_model=YouTubeRelease, include_in_schema=True)
async def latest_youtube_release():
    # Placeholder data until you implement the actual YouTube API call
    return YouTubeRelease(
        title="My Latest YouTube Video",
        url="https://www.youtube.com/watch?v=VIDEO_ID"
    )

@router.get("/latest_github_commit", response_model=GitHubCommit, include_in_schema=True)
async def latest_github_commit_route():
    try:
        commit = get_latest_github_commit()
        return commit
    except HTTPException as e:
        raise e

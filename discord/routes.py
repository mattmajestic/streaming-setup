# routes.py

from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse
from models import YouTubeRelease, GitHubCommit
from services.github_service import latest_github_commit
from services.youtube_service import latest_youtube_release

router = APIRouter()

@router.get("/", include_in_schema=False)
async def redirect_to_docs():
    """
    Redirect to the documentation.
    """
    return RedirectResponse(url='/docs')

@router.get("/latest_youtube_release", response_model=YouTubeRelease, include_in_schema=True)
async def latest_youtube_release_route():
    try:
        release = latest_youtube_release()
        return release
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred while fetching the latest YouTube release.")
    

@router.get("/latest_github_commit", response_model=GitHubCommit, include_in_schema=True)
async def latest_github_commit_route():
    try:
        commit = latest_github_commit()
        return commit
    except HTTPException as e:
        raise e

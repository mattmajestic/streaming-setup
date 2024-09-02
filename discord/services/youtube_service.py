import os
import requests
from fastapi import HTTPException
from models import YouTubeRelease

def latest_youtube_release():
    youtube_api_key = os.environ.get("YOUTUBE_API_KEY")
    channel_id = "UCjTavL86-CW6j58fsVIjTig"

    if not youtube_api_key or not channel_id:
        raise HTTPException(status_code=500, detail="YOUTUBE_API_KEY or CHANNEL_ID not found in environment variables")

    try:
        url = f"https://www.googleapis.com/youtube/v3/search?key={youtube_api_key}&channelId={channel_id}&part=snippet&order=date&maxResults=1"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'items' not in data or not data['items']:
            return {"message": "No videos found"}

        latest_video = data['items'][0]
        
        return YouTubeRelease(
            title=latest_video['snippet']['title'],
            url=f"https://www.youtube.com/watch?v={latest_video['id']['videoId']}"
        )

    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data from YouTube API: {str(e)}")

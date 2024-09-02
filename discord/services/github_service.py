# services/github_service.py

import os
import requests
from fastapi import HTTPException
from models import GitHubCommit

def latest_github_commit():
    github_token = os.environ.get("GITHUB_TOKEN")
    
    if not github_token:
        raise HTTPException(status_code=500, detail="GITHUB_TOKEN not found in environment variables")

    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json"
    }

    try:
        repos_url = "https://api.github.com/user/repos?sort=pushed&direction=desc&per_page=1"
        repos_response = requests.get(repos_url, headers=headers)
        repos_response.raise_for_status()
        repos = repos_response.json()

        if not repos:
            return {"message": "No repositories found"}

        latest_repo = repos[0]
        
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

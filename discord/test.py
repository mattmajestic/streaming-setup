import requests
import json
from pathlib import Path
from pydantic import ValidationError
from models import YouTubeRelease, GitHubCommit

# Load configuration from test.json
config_path = Path(__file__).parent / "test.json"
with open(config_path, "r") as file:
    config = json.load(file)

# Map string names to actual model classes
model_map = {
    "YouTubeRelease": YouTubeRelease,
    "GitHubCommit": GitHubCommit
}

# Iterate through the routes and perform the requests
for route_info in config["routes"]:
    response = requests.get(config["test_url"] + route_info["route"])

    # Validate response and check status code
    model = model_map[route_info["model"]]
    try:
        validated_data = model(**response.json())
        print(f"✅ Success: {route_info['name']} data is valid and matches the model.")
    except ValidationError as e:
        print(f"❌ Error: {route_info['name']} data is invalid.\nDetails: {e}")
    except requests.exceptions.RequestException as e:
        print(f"❌ Error: Request to {route_info['name']} failed. Status Code: {response.status_code}\nDetails: {e}")

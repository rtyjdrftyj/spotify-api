from fastapi import FastAPI, HTTPException
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

app = FastAPI()

# Credentials will be fetched from environment variables on Render
# This is a secure way to handle secrets in production
client_id = os.environ.get('SPOTIPY_CLIENT_ID')
client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET')

# Add a check to make sure they're not empty
if not client_id or not client_secret:
    print("Error: SPOTIPY_CLIENT_ID or SPOTIPY_CLIENT_SECRET environment variable not set.")
    exit(1)

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret
)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


@app.get("/playlist/{playlist_id}")
async def get_playlist_data(playlist_id: str):
    """
    API endpoint to fetch detailed information for a given Spotify playlist ID.
    """
    try:
        playlist = sp.playlist(playlist_id)
        
        # Prepare the data to be returned as a JSON object
        images = playlist.get('images', [])
        image_url = images[0]['url'] if images else "No image found."

        playlist_info = {
            "name": playlist['name'],
            "description": playlist['description'],
            "followers": playlist['followers']['total'],
            "owner": playlist['owner']['display_name'],
            "total_tracks": playlist['tracks']['total'],
            "image_url": image_url,
            "is_public": playlist['public'],
            "uri": playlist['uri'],
            "external_url": playlist['external_urls']['spotify']
        }
        
        return playlist_info
        
    except spotipy.client.SpotifyException as e:
        raise HTTPException(status_code=404, detail=f"Spotify API error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An unexpected error occurred: {e}")
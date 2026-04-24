import requests
import uuid
from typing import List, Optional
from app import models as dt

class MusicHydrator:
    """
    Service to 'hydrate' song objects with metadata from Apple Music API.
    Streamlines the merge between Spotify identifiers and Apple playback.
    """
    
    def __init__(self, developer_token: str, storefront: str = "us"):
        self.token = developer_token
        self.headers = {"Authorization": f"Bearer {developer_token}"}
        self.base_url = f"https://api.music.apple.com/v1/catalog/{storefront}/search"

    def fetch_apple_metadata(self, title: str, artist: str) -> dict:
        """Calls Apple Music API to find metadata for a specific song."""
        params = {"term": f"{title} {artist}", "types": "songs", "limit": 1}
        try:
            response = requests.get(self.base_url, headers=self.headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            if "results" in data and "songs" in data["results"]:
                song_data = data["results"]["songs"]["data"][0]["attributes"]
                return {
                    "apple_music_id": data["results"]["songs"]["data"][0]["id"],
                    "artwork_url": song_data["artwork"]["url"].replace("{w}x{h}", "300x300"),
                    "preview_url": song_data["previews"][0]["url"] if song_data.get("previews") else None,
                    "year": int(song_data["releaseDate"][:4]) if song_data.get("releaseDate") else None,
                    "genre": song_data["genreNames"][0] if song_data.get("genreNames") else None
                }
        except Exception as e:
            print(f"⚠️ Metadata fetch failed for {title}: {e}")
        return {}

    def hydrate_session_songs(self, spotify_songs: List[dict]) -> List[dt.Song]:
        """Merges Spotify base data with Apple Music metadata."""
        hydrated_songs = []
        for s in spotify_songs:
            metadata = self.fetch_apple_metadata(s['title'], s['artist'])
            
            # MERGE LOGIC: Combine Spotify Identity + Apple Metadata
            song = dt.Song(
                id=str(uuid.uuid4()), # We generate a fresh internal ID
                title=s['title'],
                artist=s['artist'],
                spotify_id=s.get('id'),
                **metadata # Unpacks apple_music_id, artwork_url, preview_url, etc.
            )
            hydrated_songs.append(song)
        return hydrated_songs
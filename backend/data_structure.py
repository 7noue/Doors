from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Optional, List, Tuple
import uuid  

"""
   uuid is universal standard for generating session that is seraizliation ready
"""

@dataclass
class Song:
    id: str
    title: str 
    artist: str 
    spotify_id: Optional[str] = None
    genre: Optional[str] = None
    year: Optional[int] = None

    rating: int = 1000
    wins: int = 0
    losses: int = 0


@dataclass
class Matchup:
    song_a: Song 
    song_b: Song
    round_number: int 
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    winner_id: Optional[str] = None
    

@dataclass 
class Session:
    user_id: str 
    songs: List[Song] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    current_round: int = 0
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.now)
    matchups: List[Matchup] = field(default_factory=list)
    current_matchup_index = int = 0


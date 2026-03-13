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
    elo_score: int= 1000
    wins: int = 0
    losses: int = 0


@dataclass 
class Session:
    user_id: str 
    songs: List[Song] = field(default_factory=list)
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    current_round: int = 1
    status: str = 'active'
    created_at: datetime = field(default_factory=datetime.now)



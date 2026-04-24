// FOR FRONTEND TO HAVE IDEA ON WHAT OUR MODELS LOOKLIKE and Lessen type mistake
// You will export is as import type { Song, Session }

export interface Song {
    id: string;
    title: string;
    artist: string;
    
    // Metadata
    spotify_id?: string;
    apple_music_id?: string;
    artwork_url?: string;
    preview_url?: string;
    album_name?: string;
    genre?: string;
    year?: number;
    
    rating: number;
    wins: number;
    losses: number;
}

export interface Matchup {
    id: string;
    song_a: Song;
    song_b: Song;
    round_number: number;
    winner_id: string | null;
}

export interface Session {
    user_id: string;
    songs: Song[];
    id: string;
    current_round: number;
    is_active: boolean;
    created_at: string;
    matchups: Matchup[];
    current_matchup_index: number;
}
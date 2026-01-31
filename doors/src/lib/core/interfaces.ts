export interface MusicTrack {
    id: string;
    title: string;
    artist: string;
    album: string;
    previewUrl: string;
    popularity: number;
    provider: string;
}

// Export is the passport, which means MusicTrack could exist on other file
// interface is like pydantic, it sets required datatype
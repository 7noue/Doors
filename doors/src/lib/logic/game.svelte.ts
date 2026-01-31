import { markAsPlayed } from '$lib/stores/game';
import type { MusicTrack } from '$lib/core/interfaces';

export class QuarryEngine {
    // RUNES: Reactive state for Svelte 5
    tracks = $state<MusicTrack[]>([]);
    // writable<string[]>(storedHistory)
    // Okay, about this variable, this tells that it only accepts TYPE  like MusicTrack (we did set earlier)
    // <TYPE>(initial value)
    // so this tells it only accepts a list of Music Track Type and the initial value is EMPTY LIST

    currentIndex = $state(0);
    isPlaying = $state(false)
    isRevealed = $state(false)
    // States = Signal all html about the changes.

    audioElement: HTMLAudioElement | null = null;

    constructor(initialTracks: MusicTrack[]){
        this.tracks = initialTracks
    }
    // Constructor is like the SETUP
    // It doesn't matter what list it is, as long it meets the type required for MusicTrack
    // It could be 90s or punk list

    get currentTrack() {
        return this.tracks[this.currentIndex]
    }
    // we track the list by index
    // but index are accessible by properties
    // currentTrack.id , currentTrack.album

    playClip(seconds: number = 5) {
        if (!this.currentTrack) return;

        // 1. Setup or update the audio player
        if (!this.audioElement) {
            this.audioElement = new Audio(this.currentTrack.previewUrl);
        } else {
            this.audioElement.src = this.currentTrack.previewUrl;
        }

        // 2. Start the music
        this.isPlaying = true;
        this.audioElement.play();

        // 3. Set a timer to stop the music automatically
        setTimeout(() => {
            this.stop();
        }, seconds * 1000);
    }
    
    // METHODS 
    stop() {
        this.audioElement?.pause();
        if (this.audioElement) this.audioElement.currentTime = 0
        this.isPlaying = false;
    }
    // The "?" check if audioElement exist first so it have something to pause
    // if pause, it will reset the time to 0, so user can hear the whole music again
    
    reveal() {
        this.isRevealed = true;
        markAsPlayed(this.currentTrack.id)
    }
    // We send the revealed song to markAsPlayed, a function that store it to localStorage, so even after refresh we can continue the game smoothly and avoid encountering played song in a session

    next() {
        this.stop()
        this.isRevealed = false;
        this.currentIndex++;
    }
}
import { writable } from "svelte/store";

let isRunningInWindow = false;
let storedHistory = [];


if (typeof window !== 'undefined'){
    isRunningInWindow = true;

    const rawData = localStorage.getItem('quarry_played_history')
    if (rawData !== null){
        const recentHistory = JSON.parse(rawData)
        storedHistory = recentHistory
    }

} else {
    storedHistory = []
}

export const playedTrackIds = writable<string[]>(storedHistory)
// playedTrackIds is writabble variable that accepts a list of strings and have storedHistory as initial value.

export function markAsPlayed(id: string){
    // 'ids' represents the current list of songs already in the memory.
    playedTrackIds.update((ids: string[]) => {
        // "Spread operator", combination of two list in one list.
        const combinedList = [...ids, id];

        // Avoiding duplicates through use of Set()
        // but Set is not a standard array so we use ...

        const unique = [... new Set(combinedList)];

        if (typeof window !== 'undefined'){
            localStorage.setItem('quarry_played_history', JSON.stringify(unique))
        }
        
        // Understanding localstorage is easy
        // There are two main components Parse and Stringify
        // Stringify is like packaging it so browser accept it
        // Parsing is like opening the packaging so we can use it

        return unique;
    });
}
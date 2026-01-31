import startingPack from '$lib/data/starting_pack.json';

export function load(){
    console.log("--- SERVER LOG ---");
    console.log("Loading tracks from JSON...");
    console.log("Found:", startingPack.length, "tracks");

    return {
        tracks: startingPack
    }
}
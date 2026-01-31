<script lang="ts">
    // Importing in Svelte automatically includes the directory
    import { QuarryEngine } from "$lib/logic/game.svelte";
    import { playedTrackIds } from "$lib/stores/game";
    import type { MusicTrack } from "$lib/core/interfaces.js";

    // Blueprint
    interface PageProps {
        data : {
            tracks: MusicTrack[];
        }
    }

    let { data }: PageProps = $props();
    // Props is a rune that receive the Data in OBJECT FORM
    // { } is destructuring, meaning we only want the item labled "data"

    /** EXAMPLE
     * we want to send a button for send
     * we can send the label = "SEND" and the color,
     * props will receive it and we only want the send and color blue
     * let { label, color = 'blue'} = $props();
     * // blue is a fallback (HELPFUL)
     * and we can use it like this.
     * <button style="background: {color}">
            {label}
        </button> 
     * 
     */

    const game = $derived.by(() => new QuarryEngine(data.tracks));
    // Constantly checking
</script>

<main class="p-8 font-sans bg-zinc-950 text-white min-h-screen">
    <h1 class="text-2xl font-bold mb-4">QUARRY DEBUG MODE</h1>

    <div class="mb-8 p-4 bg-zinc-900 rounded">
        <p>Tracks in Pack: {game.tracks.length}</p>
        <p>Played History (Store): {$playedTrackIds.length}</p>
    </div>
    
    {#if game.currentTrack}
        <div class="space-y-4 border-l-4 border-green-500 pl-6">
            <div class="h-20">
                {#if game.isRevealed}
                    <h2 class="text-xl font-bold">{game.currentTrack.title}</h2>
                    <p class="text-zinc-400">{game.currentTrack.artist}</p>
                {:else}
                    <div class="text-zinc-600 italic">[ Track Info Hidden ]</div>
                {/if}
            </div>

            <div class="flex gap-4">
                <button 
                    onclick={() => game.playClip(5)}
                    class="px-6 py-2 bg-white text-black font-bold rounded hover:bg-zinc-200"
                >
                    {game.isPlaying ? '🔊 Playing...' : '▶️ Play 5s'}
                </button>

                {#if !game.isRevealed}
                    <button 
                        onclick={() => game.reveal()}
                        class="px-6 py-2 bg-zinc-800 rounded hover:bg-zinc-700"
                    >
                        🔍 Reveal
                    </button>
                {:else}
                <button 
                    onclick={() => {
                        game.next();
                        }}
                    class="px-6 py-2 bg-blue-600 rounded hover:bg-blue-500"
                >
                    Next ⏭️
                </button>
                {/if}
            </div>
        </div>
    {:else}
        <p class="text-red-500">Error: No tracks loaded. Check your Python JSON output.</p>
    {/if}
</main>
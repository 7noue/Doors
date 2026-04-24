<script lang="ts">
    import { submitChoice } from '$lib/api';
    import type { Session } from '$lib/types';
    import { fade } from 'svelte/transition';

    export let session: Session;
    let loading = false;

    $: currentMatch = session.matchups[session.current_matchup_index];
    // Progress calculation based on current round progress
    $: matchCount = session.matchups.length;
    $: currentMatchNum = session.current_matchup_index + 1;
    $: progressPercent = (currentMatchNum / matchCount) * 100;

    async function handleVote(winnerId: string) {
        if (loading || !session.is_active) return;
        loading = true;
        try {
            session = await submitChoice(session.user_id, session.id, winnerId);
        } catch (error) {
            console.error("Voting error:", error);
        } finally {
            loading = false;
        }
    }

    function handleKeyDown(event: KeyboardEvent) {
        if (loading) return;
        if (event.key === '1') handleVote(currentMatch.song_a.id);
        if (event.key === '2') handleVote(currentMatch.song_b.id);
    }
</script>

<svelte:window on:keydown={handleKeyDown} />

<div class="w-full max-w-md mx-auto border-4 border-black bg-white p-5 shadow-[8px_8px_0px_0px_rgba(0,0,0,1)]">
    
    <div class="flex justify-between items-end mb-4">
        <div>
            <p class="text-[10px] font-black uppercase opacity-50 leading-none">Tournament</p>
            <h2 class="text-xl font-black uppercase italic">Round {session.current_round}</h2>
        </div>
        <div class="text-right">
            <p class="text-[10px] font-black uppercase opacity-50 leading-none">Progress</p>
            <p class="font-black text-sm uppercase">Match {currentMatchNum} <span class="text-gray-400">/</span> {matchCount}</p>
        </div>
    </div>

    <div class="grid grid-cols-2 gap-3">
        {#each [currentMatch.song_a, currentMatch.song_b] as song, i}
            <button 
                on:click={() => handleVote(song.id)}
                disabled={loading}
                class="relative flex flex-col items-start p-3 border-4 border-black text-left 
                       transition-all active:translate-x-1 active:translate-y-1 active:shadow-none
                       {i === 0 ? 'hover:bg-[#bef264] shadow-[4px_4px_0px_0px_rgba(190,242,100,1)]' : 'hover:bg-[#22d3ee] shadow-[4px_4px_0px_0px_rgba(34,211,238,1)]'}
                       disabled:opacity-50 h-48">
                
                <div class="w-full aspect-square bg-gray-100 border-2 border-black mb-2 overflow-hidden relative">
                    <div class="absolute inset-0 flex items-center justify-center text-[8px] font-black uppercase text-gray-400">
                        No Art
                    </div>
                    <div class="absolute bottom-0 left-0 h-1 bg-black w-0"></div>
                </div>

                <h3 class="font-black uppercase text-xs leading-tight mb-1 line-clamp-2">{song.title}</h3>
                <p class="text-[8px] font-bold text-gray-500 uppercase">{song.artist}</p>
                
                <span class="absolute top-1 right-2 text-[10px] font-black opacity-20">{i + 1}</span>
            </button>
        {/each}
    </div>

    <div class="mt-5 h-1.5 w-full bg-gray-100 border-2 border-black overflow-hidden">
        <div class="h-full bg-black transition-all duration-500" style="width: {progressPercent}%"></div>
    </div>
</div>
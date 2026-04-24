<script lang="ts">
    import { submitChoice } from '$lib/api';
    import type { Session } from '$lib/types';
    import { fade } from 'svelte/transition';

    export let session: Session;
    let loading = false;
    let hoveredSongId: string | null = null;

    $: currentMatch = session.matchups[session.current_matchup_index];
    $: matchCount = session.matchups.length;
    $: currentMatchNum = session.current_matchup_index + 1;
    $: progressPercent = (currentMatchNum / matchCount) * 100;

    async function handleVote(winnerId: string) {
        if (loading || !session.is_active) return;
        loading = true;
        try {
            session = await submitChoice(session.user_id, session.id, winnerId);
        } finally {
            loading = false;
        }
    }

    // Audio Logic: Play preview on hover
    function toggleAudio(id: string | null) {
        const audios = document.querySelectorAll('audio');
        audios.forEach(a => { a.pause(); a.currentTime = 0; });
        
        if (id) {
            const el = document.getElementById(`audio-${id}`) as HTMLAudioElement;
            if (el) el.play();
        }
    }

    $: toggleAudio(hoveredSongId);
</script>

<div class="w-full max-w-sm mx-auto border-4 border-black bg-white p-4 shadow-[6px_6px_0px_0px_rgba(0,0,0,1)]">
    
    <div class="flex justify-between items-end mb-4 font-black uppercase italic">
        <div>
            <p class="text-[8px] opacity-40 not-italic">Tournament</p>
            <h2 class="text-lg leading-none text-[#bef264] [text-shadow:1px_1px_0_#000]">RD {session.current_round}</h2>
        </div>
        <div class="text-right">
            <p class="text-[8px] opacity-40 not-italic">Match Counter</p>
            <p class="text-xs leading-none">{currentMatchNum} <span class="text-gray-300">/</span> {matchCount}</p>
        </div>
    </div>

    <div class="grid grid-cols-2 gap-3">
        {#each [currentMatch.song_a, currentMatch.song_b] as song, i}
            <button 
                on:click={() => handleVote(song.id)}
                on:mouseenter={() => hoveredSongId = song.id}
                on:mouseleave={() => hoveredSongId = null}
                disabled={loading}
                class="group relative flex flex-col p-2 border-4 border-black text-left transition-all 
                       active:translate-x-1 active:translate-y-1 active:shadow-none
                       {i === 0 ? 'hover:bg-[#bef264] shadow-[4px_4px_0px_0px_#000]' : 'hover:bg-[#22d3ee] shadow-[4px_4px_0px_0px_#000]'}
                       disabled:opacity-50 h-52">
                
                <div class="w-full aspect-square bg-gray-100 border-2 border-black mb-2 overflow-hidden relative">
                    {#if song.artwork_url}
                        <img src={song.artwork_url} alt="" class="w-full h-full object-cover grayscale group-hover:grayscale-0 transition-all" />
                    {:else}
                        <div class="absolute inset-0 flex items-center justify-center text-[8px] font-black uppercase text-gray-400">No Art</div>
                    {/if}
                    
                    {#if hoveredSongId === song.id}
                        <div class="absolute bottom-0 left-0 h-1 bg-black animate-[width_5s_linear]" style="width: 100%"></div>
                    {/if}
                </div>

                <h3 class="font-black uppercase text-[10px] leading-tight mb-0.5 line-clamp-2">{song.title}</h3>
                <p class="text-[7px] font-bold text-gray-400 uppercase">{song.artist} ({song.year || '??'})</p>

                {#if song.preview_url}
                    <audio id="audio-{song.id}" src={song.preview_url} preload="auto"></audio>
                {/if}
            </button>
        {/each}
    </div>

    <div class="mt-4 h-1 w-full bg-gray-100 border-2 border-black">
        <div class="h-full bg-black transition-all duration-500" style="width: {progressPercent}%"></div>
    </div>
</div>
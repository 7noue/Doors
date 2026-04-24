<script lang="ts">
    import { page } from '$app/stores';
    import { onMount } from 'svelte';
    import { getInitialMatchup } from '$lib/api';
    import Matchup from "$lib/components/Matchup.svelte";

    let session: any = null;
    let loading = true;

    // Grab BOTH parameters from the new URL structure
    $: userId = $page.params.userId;
    $: sessionId = $page.params.sessionId;

    onMount(async () => {
        try {
            // Your backend doesn't have a 'get_session' GET route, 
            // but it has 'get_current_matchup' which we can use to start.
            const initialData = await getInitialMatchup(userId as string, sessionId as string);
            // We build a minimal session object for the Matchup component
            session = {
                user_id: userId,
                id: sessionId,
                is_active: true,
                current_matchup_index: 0,
                matchups: [initialData] // Put the pair in an array
            };
        } finally {
            loading = false;
        }
    });
</script>

<main class="py-10 px-6">
    {#if loading}
        <p class="font-black animate-pulse">LOADING ENGINE...</p>
    {:else if session}
        <Matchup bind:session={session} />
    {/if}
</main>
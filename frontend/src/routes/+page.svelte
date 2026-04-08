<script lang="ts">
    import SongRanking from "$lib/components/SongRanking.svelte";
    import CreateSession from "$lib/components/createSession.svelte";
</script>


<main class="py-10 px-6">
    <div class="max-w-4xl mx-auto">
        
        <header class="mb-12 text-center">
            <h1 class="text-6xl font-black text-black tracking-tighter italic uppercase">
                DIZZY SESSIONS
            </h1>
        </header>

        <section>
            <CreateSession />
        </section>

    </div>
</main>


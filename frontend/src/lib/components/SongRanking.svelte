<script>
    const API_BASE = "http://localhost:8000"; 
    const SESSION_ID = "test_dev1/0c205f22-5368-4265-b58d-d0e2876e9968";

    async function getRankings () {
        const response = await fetch(`${API_BASE}/sessions/${SESSION_ID}/ranking`)

        if (!response.ok) {
            throw new Error(`API Error: ${response.status}`)
        } 

        return await response.json()
    }
    
    let rankingPromise = getRankings();
</script>

<main>
    <h2> Current Leaderboard </h2>

    {#await rankingPromise}
        <p class="loading">Fetching ELO ratings...</p>
    {:then songs}
        {#if songs.length === 0}
            <p>No songs have been ranked yet.</p>
        {:else}
            <ol>
                {#each songs as song}
                    <li>
                        <span class="title">{song.title}</span>
                        <span class="score">{song.rating} ELO</span>
                    </li>                
                {/each}
            </ol>
        {/if}
    {:catch error}
        <p class="error">Failed to load: {error.message}</p>
    {/await}
</main>

<style>
  main {
    font-family: system-ui, sans-serif;
    max-width: 400px;
    margin: 2rem auto;
    padding: 1rem;
    background: #1e1e24;
    color: #fff;
    border-radius: 8px;
  }
  
  ol {
    padding-left: 1.5rem;
  }

  li {
    margin-bottom: 0.75rem;
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #333;
    padding-bottom: 0.25rem;
  }

  .title {
    font-weight: bold;
  }

  .score {
    color: #4ade80; 
  }

  .error {
    color: #f87171;
  }
</style>
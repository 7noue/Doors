<script lang="ts">
    import './layout.css';
    import favicon from '$lib/assets/favicon.svg';
    import '../app.css';

    let { children } = $props();
</script>

<svelte:head>
    <link rel="icon" href={favicon} />
</svelte:head>

<main class="min-h-screen grid-bg">
    <div class="relative z-10">
        {@render children()}
    </div>
</main>
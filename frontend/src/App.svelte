<script lang="ts">
    import Upload from "./Upload.svelte";
    import Display from "./Display.svelte";

    let showImage: boolean = false;
    let uploadUrl: string = "";
    let coordinate: object;
</script>

<main>
    <h1>Fruit detector</h1>

    <Upload bind:showImage bind:uploadUrl bind:coordinate />
    <Display bind:showImage bind:uploadUrl bind:coordinate />
</main>

<style>
    main {
        text-align: center;
        padding: 20px;
        max-width: 240px;
        margin: 0 auto;
        height: 100%;
    }

    h1 {
        color: #ff3e00;
        text-transform: uppercase;
        font-size: 4em;
        font-weight: 100;
    }

    @media (min-width: 640px) {
        main {
            max-width: none;
        }
    }
</style>

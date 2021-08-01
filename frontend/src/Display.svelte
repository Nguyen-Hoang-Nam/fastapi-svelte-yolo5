<script lang="ts">
	export let uploadUrl: string = "";
	export let showImage: boolean = false;
	export let coordinate: object = {};

	let canvas;
	let width: number;
	let height;
</script>

<svelte:window bind:scrollX={width} />

<div class="display">
	<img
		src={uploadUrl}
		class={showImage ? "display-image block" : "hidden"}
		alt="Upload file"
	/>
	<canvas />
</div>

<style>
	.display-image {
		max-width: 50%;
	}

	.display {
		display: flex;
		justify-content: space-between;
		column-gap: 40px;
	}

	.block {
		display: block;
	}

	.hidden {
		display: none;
	}
</style>

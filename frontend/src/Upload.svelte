<script lang="ts">
	import Dropzone from "svelte-file-dropzone";

	export let uploadUrl: string = "";
	export let showImage: boolean = false;
	export let coordinate: object = {};

	function handleFilesSelect(e: any) {
		const { acceptedFiles } = e.detail;
		uploadUrl = URL.createObjectURL(acceptedFiles[0]);

		const formData: FormData = new FormData();
		formData.append("file", acceptedFiles[0]);
		fetch("http://localhost:8000/yolo", {
			method: "POST",
			body: formData,
		})
			.then((res) => res.json())
			.then((result) => {
				coordinate = result;

				if (!showImage) {
					showImage = true;
				}
			});
	}
</script>

<div style="width: 100%; height: 200px" class={!showImage ? "block" : "hidden"}>
	<Dropzone class="show-drop-zone" on:drop={handleFilesSelect} />
</div>

<style>
	.block {
		display: block;
	}

	.hidden {
		display: none;
	}
</style>

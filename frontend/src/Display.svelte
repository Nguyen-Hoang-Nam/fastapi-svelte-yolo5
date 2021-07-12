<script lang="ts">
  import Dropzone from "svelte-file-dropzone";

  export let uploadUrl: string = "";
  export let showImage: boolean = false;
  export let resultImage: string;
</script>

<div class="display">
  <img
    src={uploadUrl}
    class={showImage ? "display-image block" : "hidden"}
    alt="Upload file"
  />
  <img
    src={`http://localhost:8000/static/${resultImage}.png`}
    class={showImage ? "display-image block" : "hidden"}
    alt="Upload file"
  />
</div>

<style>
  .display-image {
    max-width: 50%;
  }

  .display {
    display: flex;
    justify-content: center;
    column-gap: 40px;
  }

  .block {
    display: block;
  }

  .hidden {
    display: none;
  }
</style>

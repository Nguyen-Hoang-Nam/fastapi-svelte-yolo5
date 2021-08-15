<script lang="ts">
    import { onMount, afterUpdate } from "svelte";

    export let uploadUrl: string = "";
    export let showImage: boolean = false;
    export let coordinate: object = {};

    let canvas: HTMLCanvasElement;
    let width: number;
    let height: number;
    let scale: number;

    let context: CanvasRenderingContext2D;

    let windowWidth: number;
    let imageWidth: number;
    let imageHeight: number;

    afterUpdate(() => {
        if (showImage) {
            context = canvas.getContext("2d");

            const img = new Image();

            img.src = uploadUrl;
            img.onload = function () {
                imageWidth = img.width;
                imageHeight = img.height;

                width = (windowWidth - 40) / 2;
                scale = width / imageWidth;
                height = imageHeight * scale;
            };

            let base_image = new Image();

            base_image.src = uploadUrl;
            base_image.onload = function () {
                context.drawImage(
                    base_image,
                    0,
                    0,
                    imageWidth,
                    imageHeight,
                    0,
                    0,
                    width,
                    height
                );

                for (const item in coordinate) {
                    const coors = coordinate[item];

                    for (let i = 0; i < coors.length; i++) {
                        let coor = coors[i];

                        let left = coor[0] * scale;
                        let top = coor[1] * scale;
                        let right = coor[2] * scale;
                        let bottom = coor[3] * scale;

                        context.beginPath();
                        context.lineWidth = 2;
                        context.strokeStyle = "red";
                        context.rect(left, top, right - left, bottom - top);
                        context.stroke();

                        context.font = "15px Arial";
                        if (top > 20) {
                            context.fillText(item, left, top);
                        }
                    }
                }
            };
        }
    });

    onMount(() => {});
</script>

<svelte:window bind:innerWidth={windowWidth} />

<div class="display">
    <img
        src={uploadUrl}
        class={showImage ? "display-image block" : "hidden"}
        alt="Upload file"
    />
    <canvas
        bind:this={canvas}
        {width}
        {height}
        style="width: {width}px; height: {height}px;"
    />
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

document.addEventListener("DOMContentLoaded", () => {
    setTimeout(() => {
        document.querySelectorAll(".tile").forEach((tile) => {
            const tileContent = tile.querySelector(".tile-content");

            const width = tile.offsetWidth + "px";
            const height = tile.offsetHeight + "px";

            tile.style.width = width;
            tile.style.height = height;

            tile.addEventListener("click", () => {
                if (!tile.classList.contains("tile-active")) {
                    tile.classList.add("tile-active");

                    tile.style.width = "100%";
                    tile.style.height = "100%";
                }
            });

            const closeButton = tile.querySelector(".close-tile");

            closeButton.addEventListener("click", () => {
                tileContent.style.animation = "250ms fadeOut forwards";
                closeButton.style.animation = "250ms fadeOut forwards";
                setTimeout(() => {
                    tile.classList.remove("tile-active");
                    tile.style.width = width;
                    tile.style.height = height;
                    tileContent.style.removeProperty("animation");
                    closeButton.style.removeProperty("animation");
                }, 250);
            });
        });
    }, 250);
});

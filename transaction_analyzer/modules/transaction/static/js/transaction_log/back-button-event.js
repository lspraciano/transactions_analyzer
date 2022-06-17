import {startPreloading, stopPreloading} from "../../../../../resources/js/preloader/preloader.js";

(() => {

    const searchButton = document.getElementById("button-zone_button-back");
    const input = document.getElementById("search__term");

    const callEvent = () => {
        input.value = "";
        window.location.reload();

    }

    searchButton.addEventListener("click", async () => {
        await startPreloading();
        await callEvent();
        await stopPreloading();
    });

})()
import {controlStep} from "./form-step-controller.js";
import {startPreloading, stopPreloading} from "../../../../../resources/js/preloader/preloader.js";

const formButtonCancel = document.getElementById("form__button-cancel");


const buttonCancel = async () => {
    await controlStep(5);
}

formButtonCancel.addEventListener('click', async () => {
    await startPreloading();
    await buttonCancel();
    await stopPreloading();
})
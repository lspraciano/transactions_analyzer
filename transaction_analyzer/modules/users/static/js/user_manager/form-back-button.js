import {hideFormShowTable} from "./show-and-hide-table-form.js";
import {resetDataForm} from "./form-data-controller.js";

const backButton = document.getElementById("buton-zone__btn--back");


const backEvent = () => {
    resetDataForm();
    hideFormShowTable();
}

backButton.addEventListener('click', backEvent);
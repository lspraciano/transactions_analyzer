import {hideTableShowForm} from "./show-and-hide-table-form.js";


const newUserButton = document.getElementById("search__button-new-user");
const formCheckBox = document.getElementById("input-zone__value-status");


const showForm = () => {
    hideTableShowForm();
    formCheckBox.disabled = true;
}


newUserButton.addEventListener('click', showForm)
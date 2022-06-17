import {hideTableShowForm} from "./show-and-hide-table-form.js";
import {loadDataOnForm} from "./form-data-controller.js";

( () => {

    const tableBody = document.getElementById("table-users__body");
    const formCheckBox = document.getElementById("input-zone__value-status");

    tableBody.addEventListener("dblclick",  (e) => {
        const userValuesList = [];
        const selectedRow = e.target.parentElement;

        for (let cell of selectedRow.cells) {
            userValuesList.push(cell.innerText);
        }

        let userCod = userValuesList[0];
        let userName = userValuesList[1];
        let userEmail = userValuesList[2];
        let userStatus = userValuesList[3];

        hideTableShowForm();
        formCheckBox.disabled = false;
        loadDataOnForm(userCod, userName, userEmail, userStatus);

    });

})();
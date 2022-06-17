import {getUsers} from "./get-users.js";
import {startPreloading, stopPreloading} from "../../../../../resources/js/preloader/preloader.js";

(() => {
    const tableBody = document.getElementById("table-users__body");

    const loadDataOnTable = async () => {
        const data = await getUsers()

        for (let i in data['users']) {

            let row = document.createElement('tr');

            let rowCod = document.createElement('td');
            rowCod.innerHTML = data['users'][i]['user_id'];

            let rowName = document.createElement('td');
            rowName.innerHTML = data['users'][i]['user_name'];

            let rowEmail = document.createElement('td');
            rowEmail.innerHTML = data['users'][i]['user_email'];

            let rowStatus = document.createElement('td');
            let status = data['users'][i]['user_status'];
            if (status === 1) {
                rowStatus.innerHTML = 'ATIVO';
            } else {
                rowStatus.innerHTML = 'INATIVO';
            }

            row.appendChild(rowCod);
            row.appendChild(rowName);
            row.appendChild(rowEmail);
            row.appendChild(rowStatus);

            tableBody.appendChild(row);
        }
    }

    document.addEventListener("DOMContentLoaded", async () => {
        await startPreloading();
        await loadDataOnTable();
        await stopPreloading();
    })

    if (String(window.performance.getEntriesByType("navigation")[0].type) === "back_forward") {
        window.location.reload();

    }
})()


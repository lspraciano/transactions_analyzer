import {formatDate, formatDateTime} from "../../../../../resources/js/format-date/format-date.js";
import {getLogsTransactionData} from "./get-logs-transaction-data.js";
import {startPreloading, stopPreloading} from "../../../../../resources/js/preloader/preloader.js";


(() => {

    const tableBody = document.getElementById("table-transaction-logs__body");

    const loadData = async () => {

        const data = await getLogsTransactionData();

        if (data.hasOwnProperty('error')) {
            alert(data['error']);
            location.reload();
         }

        for (let i in data['logs']) {

            let row = document.createElement('tr');

            let rowCod = document.createElement('td');
            rowCod.innerHTML = data['logs'][i]['transactions_log_id'];

            let rowBatch = document.createElement('td');
            let date = new Date(data['logs'][i]['transactions_log_transactions_datetime']);
            rowBatch.innerHTML = formatDate(date);

            let rowDateTime = document.createElement('td');
            let dateTime = new Date(data['logs'][i]['transactions_log_datetime']);
            rowDateTime.innerHTML = formatDateTime(dateTime);

            let rowUser = document.createElement('td');
            rowUser.innerHTML = data['logs'][i]['transactions_log_user_rl']['user_name'];

            row.appendChild(rowCod);
            row.appendChild(rowBatch);
            row.appendChild(rowDateTime);
            row.appendChild(rowUser);

            tableBody.appendChild(row);
        }
    }

    document.addEventListener("DOMContentLoaded", async () => {
        await startPreloading();
        await loadData();
        await stopPreloading();
    });

})()
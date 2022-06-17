import {loadDataOnTableDescribed} from "./load-data-on-table-described.js";
import {startPreloading, stopPreloading} from "../../../../../resources/js/preloader/preloader.js";

(() => {

    const input = document.getElementById("search__term");
    const tableTransactionLogs = document.getElementById("table-zone__table-transaction-logs");
    const tableTransactionLogsBody = document.getElementById("table-transaction-logs__body");
    const tableTransactionDescribe = document.getElementById("table-zone__table-transaction-described");
    const buttonBack = document.getElementById("button-zone_button-back");


    const showOrHideTables = () => {
        const TableTransactionLogsDisplay = window.getComputedStyle(tableTransactionLogs, null).display;

        if (TableTransactionLogsDisplay === 'none') {
            tableTransactionLogs.style.display = 'table';
            tableTransactionDescribe.style.display = 'none';
            input.value = "";
            buttonBack.style.display = 'none';


        } else {
            tableTransactionLogs.style.display = 'none';
            tableTransactionDescribe.style.display = 'table';
            input.value = "";
            buttonBack.style.display = 'flex';
        }
    }

    tableTransactionLogsBody.addEventListener("dblclick", async (e) => {
        await startPreloading();
        await showOrHideTables();
        const dateFromClick = e.target.parentElement.cells[1].innerText;
        await loadDataOnTableDescribed(dateFromClick);
        await stopPreloading();

    })

})()
import {filterDataTable} from "./table-filter.js";

(() => {

    const input = document.getElementById("search__term");
    const tableTransactionLogs = document.getElementById("table-zone__table-transaction-logs");
    const tableTransactionDescribe = document.getElementById("table-zone__table-transaction-described");
    const tableBodyLogs = document.getElementById("table-transaction-logs__body");
    const tableBodyDescribe = document.getElementById("table-transaction-described__body");


    const callFilter = () => {
        const TableTransactionLogsDisplay = window.getComputedStyle(tableTransactionLogs, null).display;

        if (TableTransactionLogsDisplay === 'none') {
            filterDataTable(input, tableBodyDescribe);
        } else {
            filterDataTable(input, tableBodyLogs);
        }
    }

    input.addEventListener("input", callFilter);

})()
import {formatDate, formatDateTime} from "../../../../../resources/js/format-date/format-date.js";
import {getLogsTransactionData} from "./get-suspect-transaction-report.js";

export const showOrHideTablesTitles = (title) => {
    const titleDisplay = window.getComputedStyle(title, null).display;
    if (titleDisplay === 'none') {
        title.style.display = 'block';
    } else {
        title.style.display = 'none';
    }
}

export const showOrHideTables = (table) => {
    const tableDisplay = window.getComputedStyle(table, null).display;
    if (tableDisplay === 'none') {
        table.style.display = 'table';
    } else {
        table.style.display = 'none';
    }
}

export const loadDataOnTables = async (date) => {

    const data = await getLogsTransactionData(formatDate(date));

    if ('error' in data) {
        alert(data['error']);
        if ('unauthorized' === data['error'])
            window.location.reload();
        return;
    }

    if (data['transactions_suspect'].length === 0
        && data['transactions_suspect_destination_account'].length === 0
        && data['transactions_suspect_destination_branch'].length === 0
        && data['transactions_suspect_home_account'].length === 0
        && data['transactions_suspect_home_branch'].length === 0) {
        alert('data not found for this date');
        return;
    }


    const tableBodyTransactions = document.getElementById("table-suspect-transactions__body");
    const tableBodyAcconts = document.getElementById("table-suspect-accounts__body");
    const tableBodyBranch = document.getElementById("table-suspect-branch__body");

    for (let i in data['transactions_suspect']) {

        let row = document.createElement('tr');

        let rowHomeBank = document.createElement('td');
        rowHomeBank.innerHTML = data['transactions_suspect'][i]['transaction_home_bank'];

        let rowHomeBranch = document.createElement('td');
        rowHomeBranch.innerHTML = data['transactions_suspect'][i]['transaction_home_branch'];

        let rowHomeAccount = document.createElement('td');
        rowHomeAccount.innerHTML = data['transactions_suspect'][i]['transaction_home_account'];

        let rowDestinationBank = document.createElement('td');
        rowDestinationBank.innerHTML = data['transactions_suspect'][i]['transaction_destination_bank'];

        let rowDestinationBranch = document.createElement('td');
        rowDestinationBranch.innerHTML = data['transactions_suspect'][i]['transaction_destination_branch'];

        let rowDestinationAccount = document.createElement('td');
        rowDestinationAccount.innerHTML = data['transactions_suspect'][i]['transaction_destination_account'];

        let rowAmount = document.createElement('td');
        rowAmount.innerHTML = data['transactions_suspect'][i]['transaction_amount'].toLocaleString('pt-br', {
            style: 'currency',
            currency: 'BRL'
        });

        let rowDateTime = document.createElement('td');
        rowDateTime.innerHTML = formatDateTime(data['transactions_suspect'][i]['transaction_date_time']);

        row.appendChild(rowHomeBank);
        row.appendChild(rowHomeBranch);
        row.appendChild(rowHomeAccount);
        row.appendChild(rowDestinationBank);
        row.appendChild(rowDestinationBranch);
        row.appendChild(rowDestinationAccount);
        row.appendChild(rowAmount);
        row.appendChild(rowDateTime);

        tableBodyTransactions.appendChild(row);
    }

    for (let i in data['transactions_suspect_home_account']) {
        let row = document.createElement('tr');

        let rowBank = document.createElement('td');
        rowBank.innerHTML = data['transactions_suspect_home_account'][i]['transaction_home_bank'];

        let rowBranch = document.createElement('td');
        rowBranch.innerHTML = data['transactions_suspect_home_account'][i]['transaction_home_branch'];

        let rowAccount = document.createElement('td');
        rowAccount.innerHTML = data['transactions_suspect_home_account'][i]['transaction_home_account'];

        let rowAmount = document.createElement('td');
        rowAmount.innerHTML =
            data['transactions_suspect_home_account'][i]['transaction_amount'].toLocaleString('pt-br', {
                style: 'currency',
                currency: 'BRL'
            });

        let rowType = document.createElement('td');
        rowType.innerHTML = 'SAÍDA';

        row.appendChild(rowBank);
        row.appendChild(rowBranch);
        row.appendChild(rowAccount);
        row.appendChild(rowAmount);
        row.appendChild(rowType);

        tableBodyAcconts.appendChild(row);

    }

    for (let i in data['transactions_suspect_destination_account']) {
        let row = document.createElement('tr');

        let rowBank = document.createElement('td');
        rowBank.innerHTML = data['transactions_suspect_destination_account'][i]['transaction_destination_bank'];

        let rowBranch = document.createElement('td');
        rowBranch.innerHTML = data['transactions_suspect_destination_account'][i]['transaction_destination_branch'];

        let rowAccount = document.createElement('td');
        rowAccount.innerHTML =
            data['transactions_suspect_destination_account'][i]['transaction_destination_account'];

        let rowAmount = document.createElement('td');
        rowAmount.innerHTML =
            data['transactions_suspect_destination_account'][i]['transaction_amount'].toLocaleString('pt-br', {
                style: 'currency',
                currency: 'BRL'
            });

        let rowType = document.createElement('td');
        rowType.innerHTML = 'ENTRADA';

        row.appendChild(rowBank);
        row.appendChild(rowBranch);
        row.appendChild(rowAccount);
        row.appendChild(rowAmount);
        row.appendChild(rowType);

        tableBodyAcconts.appendChild(row);

    }

    for (let i in data['transactions_suspect_home_branch']) {
        let row = document.createElement('tr');

        let rowBank = document.createElement('td');
        rowBank.innerHTML = data['transactions_suspect_home_branch'][i]['transaction_home_bank'];

        let rowBranch = document.createElement('td');
        rowBranch.innerHTML = data['transactions_suspect_home_branch'][i]['transaction_home_branch'];

        let rowAmount = document.createElement('td');
        rowAmount.innerHTML =
            data['transactions_suspect_home_branch'][i]['transaction_amount'].toLocaleString('pt-br', {
                style: 'currency',
                currency: 'BRL'
            });

        let rowType = document.createElement('td');
        rowType.innerHTML = 'SAÍDA';

        row.appendChild(rowBank);
        row.appendChild(rowBranch);
        row.appendChild(rowAmount);
        row.appendChild(rowType);

        tableBodyBranch.appendChild(row);

    }

    for (let i in data['transactions_suspect_destination_branch']) {
        let row = document.createElement('tr');

        let rowBank = document.createElement('td');
        rowBank.innerHTML = data['transactions_suspect_destination_branch'][i]['transaction_destination_bank'];

        let rowBranch = document.createElement('td');
        rowBranch.innerHTML = data['transactions_suspect_destination_branch'][i]['transaction_destination_branch'];

        let rowAmount = document.createElement('td');
        rowAmount.innerHTML =
            data['transactions_suspect_destination_branch'][i]['transaction_amount'].toLocaleString('pt-br', {
                style: 'currency',
                currency: 'BRL'
            });

        let rowType = document.createElement('td');
        rowType.innerHTML = 'ENTRADA';

        row.appendChild(rowBank);
        row.appendChild(rowBranch);
        row.appendChild(rowAmount);
        row.appendChild(rowType);

        tableBodyBranch.appendChild(row);

    }

}

export const clearDataTables = async () => {
    const tableBodyTransactions = document.getElementById("table-suspect-transactions__body");
    const tableBodyAcconts = document.getElementById("table-suspect-accounts__body");
    const tableBodyBranch = document.getElementById("table-suspect-branch__body");

    while (tableBodyTransactions.hasChildNodes()) {
        tableBodyTransactions.removeChild(tableBodyTransactions.firstChild);
    }

    while (tableBodyAcconts.hasChildNodes()) {
        tableBodyAcconts.removeChild(tableBodyAcconts.firstChild);
    }

    while (tableBodyBranch.hasChildNodes()) {
        tableBodyBranch.removeChild(tableBodyBranch.firstChild);
    }

}

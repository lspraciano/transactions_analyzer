import {getDescribedTransactionData} from "./get-described-transaction-data.js";
import {formatDateTime} from "../../../../../resources/js/format-date/format-date.js";

export const loadDataOnTableDescribed = async (date) => {
    const tableBody = document.getElementById("table-transaction-described__body");

    const data = await getDescribedTransactionData(date);

    if (data.hasOwnProperty('error')) {
        alert(data['error']);
        location.reload();
    }

    for (let i in data['transactions']) {

        let row = document.createElement('tr');

        let rowHomeBank = document.createElement('td');
        rowHomeBank.innerHTML = data['transactions'][i]['transaction_home_bank'];

        let rowHomeBranch = document.createElement('td');
        rowHomeBranch.innerHTML = data['transactions'][i]['transaction_home_branch'];

        let rowHomeAccount = document.createElement('td');
        rowHomeAccount.innerHTML = data['transactions'][i]['transaction_home_account'];

        let rowDestinationBank = document.createElement('td');
        rowDestinationBank.innerHTML = data['transactions'][i]['transaction_destination_bank'];

        let rowDestinationBranch = document.createElement('td');
        rowDestinationBranch.innerHTML = data['transactions'][i]['transaction_destination_branch'];

        let rowDestinationAccount = document.createElement('td');
        rowDestinationAccount.innerHTML = data['transactions'][i]['transaction_destination_account'];

        let rowAmount = document.createElement('td');
        rowAmount.innerHTML = data['transactions'][i]['transaction_amount'].toLocaleString('pt-br', {
            style: 'currency',
            currency: 'BRL'
        });

        let rowDateTime = document.createElement('td');
        rowDateTime.innerHTML = formatDateTime(data['transactions'][i]['transaction_date_time']);

        row.appendChild(rowHomeBank);
        row.appendChild(rowHomeBranch);
        row.appendChild(rowHomeAccount);
        row.appendChild(rowDestinationBank);
        row.appendChild(rowDestinationBranch);
        row.appendChild(rowDestinationAccount);
        row.appendChild(rowAmount);
        row.appendChild(rowDateTime);

        tableBody.appendChild(row);
    }

}
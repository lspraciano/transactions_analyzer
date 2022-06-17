import {showOrHideTables, showOrHideTablesTitles} from "./table-controller.js";

const checkboxTransaction = document.getElementById("check-zone__checkbox-transaction");
const checkboxAccount = document.getElementById("check-zone__checkbox-account");
const checkboxBranch = document.getElementById("check-zone__checkbox-branch");
const tableTransaction = document.getElementById("table-zone__table-suspect-transactions");
const tableAccount = document.getElementById("table-zone__table-suspect-accounts");
const tableBranch = document.getElementById("table-zone__table-suspect-branch");
const tableTitleTransaction = document.getElementById("title-table-zone__transaction");
const tableTitleAccount = document.getElementById("title-table-zone__account");
const tableTitleBranch = document.getElementById("title-table-zone__branch");

const eventChangeCheckbox = (tableName) => {
    if (tableName === 'transaction') {
        showOrHideTablesTitles(tableTitleTransaction);
        showOrHideTables(tableTransaction);
    }

    if (tableName === 'account') {
        showOrHideTablesTitles(tableTitleAccount);
        showOrHideTables(tableAccount);
    }

    if (tableName === 'branch') {
        showOrHideTablesTitles(tableTitleBranch);
        showOrHideTables(tableBranch);
    }

}

checkboxTransaction.addEventListener('change', async (e) => {
    const dateFromClick = e.currentTarget.name;
    eventChangeCheckbox(dateFromClick);
})

checkboxAccount.addEventListener('change', async (e) => {
    const dateFromClick = e.currentTarget.name;
    eventChangeCheckbox(dateFromClick);
})

checkboxBranch.addEventListener('change', async (e) => {
    const dateFromClick = e.currentTarget.name;
    eventChangeCheckbox(dateFromClick);
})

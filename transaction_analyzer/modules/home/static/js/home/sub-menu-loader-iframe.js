import {showAndHideMenuZoneSubOptions} from "./side-bar-animation.js";
import {checkCookie} from "../../../../../resources/js/cookie/cookie-manager.js";

const dashboardOptions = document.getElementById("menu-body__option-dashboard");
const transactionImportSubOptions = document.getElementById("suboption_import");
const transactionAuditSubOptions = document.getElementById("suboption_audit");
const transactionSuspectOptions = document.getElementById("suboption_suspect");
const userManagerSubOptions = document.getElementById("suboption_user-manager");

const iframeToHtml = document.getElementById("plotting-zone__frame-to-html");
const screenName = document.getElementById("screen-name");

const checkAuthorization = async () => {
    if (await  checkCookie() !== true) {
        alert('unauthorized');
        window.location.href = `${window.location.origin}/`;
    }
}

const callDashboardScreen = async () => {
    await checkAuthorization();
    iframeToHtml.src = '/home/dashboard';
    screenName.innerText = 'Dashboard'
    showAndHideMenuZoneSubOptions();
}


const callImportTransactionScreen = async () => {
    await checkAuthorization();
    iframeToHtml.src = '/transaction/transaction-import-template';
    screenName.innerText = 'Importar Transações';
    showAndHideMenuZoneSubOptions();
}

const callAuditTransactionScreen = async () =>  {
    await checkAuthorization();
    iframeToHtml.src = '/transaction/transaction-log-template';
    screenName.innerText = 'Log de Transações';
    showAndHideMenuZoneSubOptions();
}


const callSuspectTransactionOptionsScreen = async () =>  {
    await checkAuthorization();
    iframeToHtml.src = '/transaction/transaction-suspect-template';
    screenName.innerText = 'Transações Suspeitas';
    showAndHideMenuZoneSubOptions();
}

const callUserManagerSubOptionsScreen = async () =>  {
    await checkAuthorization();
    iframeToHtml.src = '/user/manager-template';
    screenName.innerText = 'Gerenciar Usuários';
    showAndHideMenuZoneSubOptions();
}

dashboardOptions.addEventListener('click', callDashboardScreen);
transactionImportSubOptions.addEventListener('click', callImportTransactionScreen);
transactionAuditSubOptions.addEventListener('click', callAuditTransactionScreen);
transactionSuspectOptions.addEventListener('click', callSuspectTransactionOptionsScreen);
userManagerSubOptions.addEventListener('click', callUserManagerSubOptionsScreen);

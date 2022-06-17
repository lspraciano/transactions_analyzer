import {plotGrapOne} from "./plot-grap-one.js";
import {plotGrapTwo} from "./plot-grap-two.js";
import {getTransactionReport} from "./get-transaction-report.js";
import {startPreloading, stopPreloading} from "../../../../../resources/js/preloader/preloader.js";

const totalTransactionText = document.getElementById("text-total-transaction");
const amountMeanTransactionText = document.getElementById("amount-mean-transaction-text");
const percSucpectTransactionText = document.getElementById("percentage-suspect-transaction-text");
const amountMeanSuspectTransactionText = document.getElementById("amount-mean-suspect-transaction-text");

const afterLoader = async () => {
    const data = await getTransactionReport();

    if ('error' in data) {
        alert(data['error']);
        return;
    }

    totalTransactionText.innerText = data['transactions_total'];
    amountMeanTransactionText.innerText = 'R$ ' + data['transactions_amount_mean'];
    percSucpectTransactionText.innerText = data['transactions_suspect_percentage'] + '%';
    amountMeanSuspectTransactionText.innerText = 'R$ ' + data['transactions_suspect_mean'];

    let grapOneLabels = [];
    let grapOneValues = [];
    let grapTwoLabels = [];
    let grapTwoValues = [];

    for (let d of data['transactions_total_per_day']) {
        grapOneLabels.push(d['date']);
        grapOneValues.push(d['total']);
    }

    for (let d of data['transactions_total_per_bank']) {
        grapTwoLabels.push(d['bank']);
        grapTwoValues.push(d['total']);
    }

    plotGrapOne(grapOneLabels, grapOneValues);
    plotGrapTwo(grapTwoLabels, grapTwoValues);
}


document.addEventListener('DOMContentLoaded', async  () => {
    await startPreloading();
    await afterLoader();
    await stopPreloading ();
})
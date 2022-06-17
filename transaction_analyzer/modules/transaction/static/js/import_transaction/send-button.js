import {readCsv} from "./read-csv.js";
import {preProcessingData} from "./pre-processing-data.js";
import {saveTransactions} from "./save-transactions.js";
import {readXml} from "./read-xml.js";
import {startPreloading, stopPreloading} from "../../../../../resources/js/preloader/preloader.js";
const sendButton = document.getElementById("card-zone__bottom__button");
const fileInput = document.getElementById('input-file');

const sendCsv = async () => {
    let data = [];

    if (fileInput.files[0].type === 'text/csv') {
        data = await readCsv(fileInput.files[0]);
    } else {
        // data = await readXml(fileInput.files[0]);
        alert('Sorry. We are working to implement this functionality.');
        location.reload();
        return;
    }

    const processedData = await preProcessingData(data);
    const result = await saveTransactions(processedData.outputValidData);

    if('error' in result) {
        alert(result['error']);
    } else {
        alert('file saved successfully');
    }

    location.reload();


}

sendButton.addEventListener('click', async () => {
    await startPreloading();
    await sendCsv();
    await stopPreloading();
});
import {getCookie} from "../../../../../resources/js/cookie/cookie-manager.js";

export const getDescribedTransactionData = async (date) => {

        const url = `${window.location.origin}/transaction?date=`+date;
        const param = {
            method: "GET",
            headers: {
                "Content-type": "application/json",
                "Authorization": "Bearer " + await getCookie()
            }
        }

        const response = await fetch(url, param);
        return await response.json();
    }
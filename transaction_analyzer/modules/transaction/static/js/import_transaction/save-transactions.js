import {getCookie} from "../../../../../resources/js/cookie/cookie-manager.js";

export const saveTransactions = async (transaction) => {

    const url = `${window.location.origin}/transaction/`;
    const param = {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            "Authorization": "Bearer " + await getCookie()
        },
        body: JSON.stringify(transaction)

    }

    const response = await fetch(url, param);
    return await response.json();
}
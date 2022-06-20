import {getCookie} from "../../../../../resources/js/cookie/cookie-manager.js";

export const getTransactionReport = async () => {

        const url = `${window.location.origin}/transaction/report`;
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


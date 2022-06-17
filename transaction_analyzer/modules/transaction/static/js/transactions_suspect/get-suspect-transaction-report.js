export const getLogsTransactionData = async (date) => {

        const url = `${window.location.origin}/transaction/suspect?date=`+date;
        const param = {
            method: "GET",
            headers: {
                "Content-type": "application/json"
            }
        }

        const response = await fetch(url, param);
        return await response.json();
    }
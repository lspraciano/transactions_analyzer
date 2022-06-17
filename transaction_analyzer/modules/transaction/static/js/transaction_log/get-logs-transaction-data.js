export const getLogsTransactionData = async () => {

        const url = `${window.location.origin}/transaction/log/get-log`;
        const param = {
            method: "GET",
            headers: {
                "Content-type": "application/json"
            }
        }

        const response = await fetch(url, param);
        return await response.json();
    }
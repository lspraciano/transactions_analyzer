export const getDescribedTransactionData = async (date) => {

        const url = `${window.location.origin}/transaction?date=`+date;
        const param = {
            method: "GET",
            headers: {
                "Content-type": "application/json"
            }
        }

        const response = await fetch(url, param);
        return await response.json();
    }
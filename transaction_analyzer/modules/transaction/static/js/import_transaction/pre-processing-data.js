export const preProcessingData = async (data) => {
    let transactionDate = data[0];
    transactionDate = transactionDate[transactionDate.length - 1].substring(0,10);
    let outputValidData = [];
    let outputInvalidData = [];

    await data.forEach((item, index) => {
        let outputJson = {
            "transaction_home_bank" : "",
            "transaction_home_branch" : "",
            "transaction_home_account" : "",
            "transaction_destination_bank" : "",
            "transaction_destination_branch" : "",
            "transaction_destination_account" : "",
            "transaction_amount" : "",
            "transaction_date_time" : ""
        };

        if(item.includes('') || item[item.length - 1].substring(0,10) !==  transactionDate) {
            outputJson.transaction_home_bank = item[0];
            outputJson.transaction_home_branch = item[1];
            outputJson.transaction_home_account = item[2];
            outputJson.transaction_destination_bank = item[3];
            outputJson.transaction_destination_branch = item[4];
            outputJson.transaction_destination_account = item[5];
            outputJson.transaction_amount = item[6];
            outputJson.transaction_date_time = item[7];

            outputInvalidData.push(outputJson);
        } else {
            try {
                outputJson.transaction_home_bank = item[0];
                outputJson.transaction_home_branch = parseInt(item[1]);
                outputJson.transaction_home_account = item[2];
                outputJson.transaction_destination_bank = item[3];
                outputJson.transaction_destination_branch = parseInt(item[4]);
                outputJson.transaction_destination_account = item[5];
                outputJson.transaction_amount = parseFloat(item[6]);
                outputJson.transaction_date_time = item[7];
            } catch (e) {
                console.log('error: error ao converter');
            }


            outputValidData.push(outputJson);
        }
    });

    return {
        'outputValidData':outputValidData,
        'outputInvalidData': outputInvalidData
    }
}

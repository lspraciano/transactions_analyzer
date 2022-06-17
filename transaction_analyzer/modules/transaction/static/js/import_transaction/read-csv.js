export async function readCsv(file) {
    return new Promise((resolve, reject) => {
        Papa.parse(file, {
            header: false,
            skipEmptyLines: true,
            delimiter: ",",
            complete: (results) => {
                return resolve(results.data);
            },
            error: (error) => {
                return reject(error);
            },
        });
    });
}


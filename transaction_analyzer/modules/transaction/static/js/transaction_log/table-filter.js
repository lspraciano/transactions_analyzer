export const filterDataTable = (input, tableBody) => {

    for (let tableRow of tableBody.rows) {

        for (let tableCell of tableRow.cells) {
            let cellValue = tableCell.innerHTML;
            let text = (input.value).toUpperCase();

            if (cellValue.includes(text)) {
                tableRow.style.display = 'table-row';
                break;
            } else {
                tableRow.style.display = 'none';
            }
        }
    }
}

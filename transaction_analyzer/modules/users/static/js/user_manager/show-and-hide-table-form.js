const searchZone = document.getElementById("search-zone");
const tableZone = document.getElementById("table-zone");
const formZone = document.getElementById("form-zone");


export const hideTableShowForm = () => {
    tableZone.style.display = "none";
    searchZone.style.display = "none";
    formZone.style.display = "flex";
}

export const hideFormShowTable = () => {
    tableZone.style.display = "flex";
    searchZone.style.display = "flex";
    formZone.style.display = "none";
}

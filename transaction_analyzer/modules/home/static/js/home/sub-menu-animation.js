const transactionOptions = document.getElementById("menu-body__option-transaction");
const userOptions = document.getElementById("menu-body__option-user");

function transactionToggleMenu() {
    const transactionSubOptions = document.getElementById("option-transaction__suboption");
    const transactionArrowIcon = document.getElementById("option-transaction__arrow");

    transactionSubOptions.classList.toggle('sub-options-activate');
    transactionArrowIcon.classList.toggle('arrow-sub-options-activate');
}


function userToggleMenu() {
    const userSubOptions = document.getElementById("option-user__suboption");
    const userArrowIcon = document.getElementById("option-user__arrow");

    userSubOptions.classList.toggle('sub-options-activate');
    userArrowIcon.classList.toggle('arrow-sub-options-activate');
}


transactionOptions.addEventListener('click', transactionToggleMenu);
userOptions.addEventListener('click', userToggleMenu);
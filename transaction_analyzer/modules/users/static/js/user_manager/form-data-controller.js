import {checkEmail} from "../../../../../resources/js/email/validate-email.js";

const userCodInput = document.getElementById("user-cod-zone__cod");
const userNameInput = document.getElementById("user-name-zone__input");
const userEmailInput = document.getElementById("user-email-zone__input");
const userStatusCheckBox = document.getElementById("input-zone__value-status");

export const loadDataOnForm = (userCod, userName, userEmail, userStatus) => {
    userCodInput.value = userCod;
    userNameInput.value = userName;
    userEmailInput.value = userEmail;
    userStatusCheckBox.checked = userStatus === 'ATIVO';
}

export const resetDataForm = () => {
    userCodInput.value = '';
    userNameInput.value = '';
    userEmailInput.value = '';
    userStatusCheckBox.checked = true;
}

export const validateForm = async () => {

    if (userNameInput.value === '') {
        alert('invalid username');
        return false;
    }

    if (await checkEmail(userEmailInput.value) === false) {
        alert('invalid email');
        return false;
    }

    return true;
}

export const getFormData = async () => {
    let formData = [];
    formData.push(userCodInput.value.toUpperCase());
    formData.push(userNameInput.value.toUpperCase());
    formData.push(userEmailInput.value.toUpperCase());
    formData.push(userStatusCheckBox.checked);
    return formData
}
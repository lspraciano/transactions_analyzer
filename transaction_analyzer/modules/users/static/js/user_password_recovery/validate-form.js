const inputUserName = document.getElementById("input-zone__input-user-name");
const inputUserToken = document.getElementById("input-zone__input-user-token");
const inputUserPassword = document.getElementById("input-zone__input-user-password");
const inputUserPasswordConfirmation = document.getElementById("input-zone__input-user-password-confirmation");
const regexPassword = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,}$/;

export const checkUserName = async () => {
    if (inputUserName.value === '') {
        alert('invalid user name');
        inputUserName.value = '';
        inputUserName.focus();
        return false;
    }

    return true;
}

export const checkToken = async () => {
    if (inputUserToken.value === '') {
        alert('invalid token');
        inputUserToken.value = '';
        inputUserToken.focus();
        return false;
    }

    if (inputUserToken.value.length !== 6) {
        alert('the token must have 6 numbers');
        inputUserToken.value = '';
        inputUserToken.focus();
        return false;
    }


    return true;
}

export const validatePassword = async () => {

    if (inputUserPassword.value === "") {
        alert("invalid password");
        inputUserPassword.focus();
        return false;
    }

    if (inputUserPasswordConfirmation.value === "") {
        alert("invalid password confirmation");
        inputUserPasswordConfirmation.focus();
        return false;
    }


    if (inputUserPassword.value !== inputUserPasswordConfirmation.value) {
        alert("password and confirmation must be the same");
        inputUserPassword.value = "";
        inputUserPasswordConfirmation.value = "";
        inputUserPassword.focus();
        return false;
    }

    if (regexPassword.test(inputUserPassword.value) === false) {
        alert("The Password must contain at least 8 characters, including a special character, " +
            "an uppercase letter and a number.");
        inputUserPasswordConfirmation.value = "";
        inputUserPassword.value = "";
        inputUserPassword.focus();
        return false;
    }

    return true
}
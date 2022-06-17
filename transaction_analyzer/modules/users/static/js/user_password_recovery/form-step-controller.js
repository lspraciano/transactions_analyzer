const formTitle = document.getElementById("form__title");
const formButton = document.getElementById("form__button");
const formButtonCancel = document.getElementById("form__button-cancel");
const inputUserName = document.getElementById("input-zone__input-user-name");
const inputUserToken = document.getElementById("input-zone__input-user-token");
const inputUserPassword = document.getElementById("input-zone__input-user-password");
const inputUserPasswordConfirmation = document.getElementById("input-zone__input-user-password-confirmation");
const image = document.getElementById("figure-zone__image");


export const controlStep = async (step) => {

    if (step === 1) {
        formTitle.innerText = 'Qual seu usuário?';
        inputUserName.style.display = 'inline-block';
        inputUserToken.style.display = 'none';
        inputUserPassword.style.display = 'none';
        inputUserPasswordConfirmation.style.display = 'none';
        image.src = './static/images/user_password_recovery/undraw_user.svg';
        return;
    }

    if (step === 2) {
        formTitle.innerText = 'Qual seu Token';
        inputUserName.style.display = 'none';
        inputUserToken.style.display = 'inline-block';
        inputUserPassword.style.display = 'none';
        inputUserPasswordConfirmation.style.display = 'none';
        inputUserPassword.value = "";
        inputUserPasswordConfirmation.value = "";
        image.src = './static/images/user_password_recovery/undraw_token.svg';
        return;
    }

    if (step === 3) {
        formTitle.innerText = 'Escolha sua Senha';
        inputUserName.style.display = 'none';
        inputUserToken.style.display = 'none';
        inputUserPassword.style.display = 'inline-block';
        inputUserPasswordConfirmation.style.display = 'inline-block';
        image.src = './static/images/user_password_recovery/undraw_password.svg';
        return;
    }

    if (step === 4) {
        formTitle.innerText = 'Sua Senha foi Atualizada';
        formButton.value = 'Finalizar';
        inputUserName.style.display = 'none';
        inputUserToken.style.display = 'none';
        inputUserPassword.style.display = 'none';
        inputUserPasswordConfirmation.style.display = 'none';
        formButtonCancel.style.display = 'none';
        image.src = './static/images/user_password_recovery/undraw_ok.svg';
        return;
    }

    if (step === 5) {
        await window.location.reload();
        window.location.href = `${window.location.origin}/`;
    }

}

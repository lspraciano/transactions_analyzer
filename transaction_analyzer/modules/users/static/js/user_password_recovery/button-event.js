import {controlStep} from "./form-step-controller.js";
import {generatePasswordToken} from "./post-generate-password-token.js";
import {checkToken, checkUserName, validatePassword} from "./validate-form.js";
import {updateUserPasword} from "./update-password.js";
import {startPreloading, stopPreloading} from "../../../../../resources/js/preloader/preloader.js";

const formTitle = document.getElementById("form__title");
const formButton = document.getElementById("form__button");
const inputUserId = document.getElementById("input-zone__input-user-id");
const inputUserName = document.getElementById("input-zone__input-user-name");
const inputUserToken = document.getElementById("input-zone__input-user-token");
const inputUserPassword = document.getElementById("input-zone__input-user-password");

const buttonEvent = async () => {

    if (window.getComputedStyle(inputUserName, null).display === 'inline-block') {
        if (await checkUserName() === false) {
            return;
        }

        const checkTokenResponse = await generatePasswordToken(inputUserName.value.toUpperCase());
        if ('error' in checkTokenResponse) {
            alert(checkTokenResponse['error']);
            return;
        }

        inputUserId.value = checkTokenResponse['user_id'];
        alert('a token has been sent to your registration email');
        await controlStep(2);
        return;
    }

    if (window.getComputedStyle(inputUserToken, null).display === 'inline-block') {
        if (await checkToken() === false) {
            return;
        }

        await controlStep(3);
        return;
    }

    if (window.getComputedStyle(inputUserPassword, null).display === 'inline-block') {
        if (await validatePassword() === false) {
            return;
        }

        const checkUpdatePasswordResponse = await updateUserPasword(
            parseInt(inputUserId.value),
            inputUserPassword.value,
            parseInt(inputUserToken.value)
        );

        if ('error' in checkUpdatePasswordResponse) {
            alert(checkUpdatePasswordResponse['error']);

            if (checkUpdatePasswordResponse['error'] === 'invalid token') {
                window.location.reload();
            }
            return;
        }

        await controlStep(4);
        return;
    }

    if (formTitle.innerText === 'Sua Senha foi Atualizada') {
        await controlStep(5);
    }


}

formButton.addEventListener('click', async () => {
    await startPreloading();
    await buttonEvent();
    await stopPreloading();
})
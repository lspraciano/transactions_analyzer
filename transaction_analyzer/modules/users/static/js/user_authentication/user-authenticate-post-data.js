import {deleteCookie, setCookie} from "../../../../../resources/js/cookie/cookie-manager.js";

(() => {

    const enterButtonForm = document.querySelector('[name="button"]');
    const username = document.querySelector('[name="user"]');
    const password = document.querySelector('[name="password"]');

    const actionButton = async () => {

        if (username.value === "") {
            await alert("invalid username field");
            username.focus();
            return;
        }

        if (password.value === "") {
            await alert("invalid password field");
            password.focus();
            return;
        }

        const credentials = {
            "user_name": username.value,
            "user_password": password.value
        };


        const url = `${window.location.origin}/user/authentication`;
        const param = {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify(credentials)

        }

        const response = await fetch(url, param)
        const token = await response.json()

        if ('error' in token) {
            await alert(token['error']);
            await deleteCookie()
            username.value = '';
            password.value = '';
            username.focus();

        } else {
            await setCookie(token['token']);
            window.location.href = `${window.location.origin}/home`;

        }

    }

    enterButtonForm.addEventListener('click', async () => {
        await actionButton();
    })

})()
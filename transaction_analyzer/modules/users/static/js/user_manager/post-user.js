import {getCookie} from "../../../../../resources/js/cookie/cookie-manager.js";

export const saveNewUser = async (username, email) => {

    const user = {
        "user_name": username,
        "user_email": email
    };

    const url = `${window.location.origin}/user/`;
    const param = {
        method: "POST",
        headers: {
            "Content-type": "application/json",
            "Authorization": "Bearer " + await getCookie()
        },
        body: JSON.stringify(user)

    }

    const response = await fetch(url, param)

    return response.json()
}
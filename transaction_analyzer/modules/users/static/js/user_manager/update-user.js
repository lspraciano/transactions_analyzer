import {getCookie} from "../../../../../resources/js/cookie/cookie-manager.js";

export const updateUser = async (cod, username, email, status) => {

    const user = {
        "user_id": cod,
        "user_name": username,
        "user_email": email,
        "user_status": status,
    };

    const url = `${window.location.origin}/user/`;
    const param = {
        method: "PATCH",
        headers: {
            "Content-type": "application/json",
            "Authorization": "Bearer " + await getCookie()
        },
        body: JSON.stringify(user)

    }

    const response = await fetch(url, param)

    return response.json()
}
export const updateUserPasword = async (cod, user_password,  user_token) => {

    const user = {
        "user_id": cod,
        "user_password": user_password,
        "user_token": user_token
    };

    const url = `${window.location.origin}/user/reset-password`;
    const param = {
        method: "PATCH",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(user)

    }

    const response = await fetch(url, param)

    return response.json()
}
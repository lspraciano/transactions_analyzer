export const generatePasswordToken = async (username) => {

    const user = {
        "user_name": username,
    };

    const url = `${window.location.origin}/user/reset-password`;
    const param = {
        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(user)

    }

    const response = await fetch(url, param)

    return response.json()
}
export const saveNewUser = async (username, email) => {

    const user = {
        "user_name": username,
        "user_email": email
    };

    const url = `${window.location.origin}/user/`;
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
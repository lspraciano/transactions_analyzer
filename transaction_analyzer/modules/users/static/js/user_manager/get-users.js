export const getUsers = async () => {

        const url = `${window.location.origin}/user`;
        const param = {
            method: "GET",
            headers: {
                "Content-type": "application/json"
            }
        }

        const response = await fetch(url, param);
        return await response.json();
    }
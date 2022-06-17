export const setCookie = async (value) => {

    let date = new Date();
    date.setTime(date.getTime() + (30 * 60 * 1000)); //30 minutes
    let expires = "; expires=" + date.toUTCString();
    document.cookie = 'new_app' + "=" + (value || "") + expires + "; path=/";
}


export const deleteCookie = async () => {
    document.cookie = 'new_app' + "=" + ('' || "") + ";" +
        " expires=" + 'Thu, 01 Jan 1970 00:00:01 GMT' + "; path=/";
}

export const checkCookie = async () => {
    let cookie = document.cookie
    return !!cookie;
}
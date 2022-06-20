export const setCookie = async (value) => {

    let date = new Date();
    date.setTime(date.getTime() + (30 * 60 * 1000)); //30 minutes
    let expires = "; expires=" + date.toUTCString();
    document.cookie = 'transaction_analyzer_jwt' + "=" + (value || "") + expires + "; path=/";
}


export const deleteCookie = async () => {
    document.cookie = 'transaction_analyzer_jwt' + "=" + ('' || "") + ";" +
        " expires=" + 'Thu, 01 Jan 1970 00:00:01 GMT' + "; path=/";
}

export const checkCookie = async () => {
    let cookie = document.cookie
    return !!cookie;
}

export const getCookie = async () => {
  let cookie = {};
  document.cookie.split(';').forEach(function(el) {
    let [key,value] = el.split('=');
    cookie[key.trim()] = value;
  })
  return cookie['transaction_analyzer_jwt'];
}
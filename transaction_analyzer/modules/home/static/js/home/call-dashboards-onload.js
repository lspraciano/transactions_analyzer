import {checkCookie} from "../../../../../resources/js/cookie/cookie-manager.js";

window.onload = async function () {
    if (await checkCookie()) {
        const iframeToHtml = document.getElementById("plotting-zone__frame-to-html");
        iframeToHtml.src = '/home/dashboard';
    } else {
        alert('unauthorized');
        window.location.href = `${window.location.origin}/`;
    }
}
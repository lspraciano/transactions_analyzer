import {deleteCookie} from "../../../../../resources/js/cookie/cookie-manager.js";

( () => {
    const btnLogout = document.getElementById("btn-logout");
    const iconLogout = document.getElementById("icon-logout");

    const logout = async () => {
        await deleteCookie();
        window.location.href = `${window.location.origin}/`;
     }

    btnLogout.addEventListener('click', logout);
    iconLogout.addEventListener('click', logout);

})();


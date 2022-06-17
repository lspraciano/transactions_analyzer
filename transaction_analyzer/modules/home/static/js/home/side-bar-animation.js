const iconMenu = document.getElementById("navigation-zone_menu-icon");


const showAndHideMenuZone = () => {
    const menuZone = document.getElementById("side-bar-zone");
    menuZone.classList.toggle('side-bar-zone--hide');
}

export const showAndHideMenuZoneSubOptions = () => {
    let mediaQuery = window.matchMedia("(max-width: 1180px)")

    if (mediaQuery.matches) {
        showAndHideMenuZone();
    }

}

iconMenu.addEventListener('click', showAndHideMenuZone);
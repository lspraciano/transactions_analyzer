const gifPreloadingErlen = parent.document.getElementById('pre-loader__gif')
const boxGif = parent.document.getElementById('pre-loader')


export const startPreloading = () => {
    gifPreloadingErlen.style.display = "flex";
    boxGif.style.display = "flex";
}

export const stopPreloading = () => {
    gifPreloadingErlen.style.display = "none";
    boxGif.style.display = "none";
}


import {validateInputFile} from "./validate-input-file.js";

(() => {
    const fileInput = document.getElementById('input-file');
    const title = document.getElementById('title');
    const iconOn = document.getElementById('card-zone__mid__icon-on');
    const iconOff = document.getElementById('card-zone__mid__icon-off');
    const sendButton = document.getElementById('card-zone__bottom__button');

    const handleFiles = async () => {
        const selectedFiles = fileInput.files[0];

        if (await validateInputFile(selectedFiles) === true) {
            title.innerHTML = selectedFiles.name;
            iconOn.style.display = 'flex';
            iconOff.style.display = 'none';
            sendButton.style.display = 'block';
        } else {
            alert('invalid file')
            document.location.reload();
        }
    }


    fileInput.addEventListener("change", handleFiles);
})();
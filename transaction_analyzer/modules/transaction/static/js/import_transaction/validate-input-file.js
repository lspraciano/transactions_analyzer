export const validateInputFile = async (file) => {
    return file.type === 'text/csv' || file.type === 'text/xml';

}


const fileInput = document.querySelector('input[type="file"]');
const displayImageDiv = document.getElementById('display_image');
const uploadButton = document.getElementById('submit');

function setImageAndStoreUrl(imageUrl) {
    displayImageDiv.style.backgroundImage = `url(${imageUrl})`;
    displayImageDiv.style.backgroundSize = 'contain'; 
    displayImageDiv.style.backgroundRepeat = 'no-repeat';
    displayImageDiv.style.backgroundPosition = 'center';
    displayImageDiv.style.width = '100%';
    displayImageDiv.style.height = '300px';
    sessionStorage.setItem('uploaded_image_url', imageUrl);
}


function navigateToImageDetect() {
    window.location.href = '/image-detect';
}

function navigateTosearch() {
    window.location.href = '/search';
}

window.addEventListener('load', () => {
    const savedImageUrl = sessionStorage.getItem('uploaded_image_url');
    if (savedImageUrl) {
        setImageAndStoreUrl(savedImageUrl);
    }
});

uploadButton.addEventListener('click', async () => {
    if (fileInput.files.length > 0) {
        const reader = new FileReader();
        const file = fileInput.files[0];

        reader.addEventListener('load', () => {
            setImageAndStoreUrl(reader.result); 
            sessionStorage.setItem('uploaded_image_url', reader.result);
        });

        reader.readAsDataURL(file);
    } else {
        alert('Please select a file to upload.');
    }
});

window.addEventListener('beforeunload', () => {
    sessionStorage.removeItem('uploaded_image_url');
});


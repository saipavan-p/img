
const fileInput = document.querySelector('input[type="file"]');
const displayImageDiv = document.getElementById('display_image');
const uploadButton = document.getElementById('submit');

// Function to set the image in displayImageDiv and store URL in sessionStorage
function setImageAndStoreUrl(imageUrl) {
    displayImageDiv.style.backgroundImage = `url(${imageUrl})`;
    displayImageDiv.style.backgroundSize = 'contain'; // Set to 'cover' to maintain aspect ratio
    displayImageDiv.style.backgroundRepeat = 'no-repeat';
    displayImageDiv.style.backgroundPosition = 'center';
    displayImageDiv.style.width = '100%';
    displayImageDiv.style.height = '300px';

    // Store uploaded image URL in sessionStorage
    sessionStorage.setItem('uploaded_image_url', imageUrl);
}

// Check sessionStorage for saved image URL on page load
window.addEventListener('load', () => {
    const savedImageUrl = sessionStorage.getItem('uploaded_image_url');
    if (savedImageUrl) {
        setImageAndStoreUrl(savedImageUrl); // Set image from sessionStorage
    }
});

uploadButton.addEventListener('click', async () => {
    if (fileInput.files.length > 0) {
        const reader = new FileReader();
        const file = fileInput.files[0];

        reader.addEventListener('load', () => {
            setImageAndStoreUrl(reader.result); // Set image from FileReader result

            // Store uploaded image URL in sessionStorage
            sessionStorage.setItem('uploaded_image_url', reader.result);
        });

        reader.readAsDataURL(file);
    } else {
        alert('Please select a file to upload.');
    }
});

// Clear sessionStorage when navigating away from the page or refreshing
window.addEventListener('beforeunload', () => {
    sessionStorage.removeItem('uploaded_image_url');
});
let jobAds = [];
let jobAdKeys = [];
let currentIndex = 0;

const jobAdContainer = document.getElementById("jobAdContainer");
const jobAdForm = document.getElementById("jobAdForm");

function fetchAds() {
    fetch('/get_ads')
    .then(response => response.json())
    .then(data => {
        jobAds = data;
        console.log("Loaded ads:", jobAds); // Debugging
        displayNextJobAd();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

fetchAds();

function displayNextJobAd() {
    console.log("Current index:", currentIndex, "Total ads:", jobAds.length); // Debugging
    if (currentIndex <= jobAds.length) {
        const currentAd = jobAds[currentIndex];
        jobAdContainer.innerHTML = currentAd.aviso;
    } else {
        // All ads have been classified, redirect to /despedida.html
        window.location.href = '/despedida';
    }
}

// Event listener for form submission
jobAdForm.addEventListener("submit", function (e) {
    e.preventDefault();

    const classification = document.querySelector('input[name="classification"]:checked');
    const ease_of_coding = document.querySelector('input[name="ease_of_coding"]:checked');

    if (!classification || !ease_of_coding) {
        alert("Por favor completa todas las selecciones.");
        return;
    }

    const currentAdKey = jobAdKeys[currentIndex];
    const formData = {
        ad_id: currentAdKey,
        classification: classification.value,
        ease_of_coding: ease_of_coding.value,
    };

    fetch('/submit_classification', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        currentIndex++;  // Increment currentIndex after successful submission
        displayNextJobAd();  // Display the next job ad or redirect
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

// Initial display
displayNextJobAd();

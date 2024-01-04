const jobAds = {
    0: "Anuncio de ejemplo 1 WFH",
    1: "Anuncio de ejemplo 2 not WFH",
    2: "Anuncio de ejemplo 3 not WFH",
    3: "Anuncio de ejemplo 4 not WFH"
};

const jobAdContainer = document.getElementById("jobAdContainer");
const jobAdForm = document.getElementById("jobAdForm");

const jobAdKeys = Object.keys(jobAds).map(key => parseInt(key));

let currentIndex = 0;

// Function to display the next job ad or redirect
function displayNextJobAd() {
    if (currentIndex < jobAdKeys.length) {
        const currentAdKey = jobAdKeys[currentIndex];
        jobAdContainer.innerHTML = jobAds[currentAdKey];
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

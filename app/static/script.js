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

// Function to display the next job ad
function displayNextJobAd() {
    if (currentIndex < jobAdKeys.length) {
        const currentAdKey = jobAdKeys[currentIndex];
        jobAdContainer.innerHTML = jobAds[currentAdKey];
        currentIndex++;
    } else {
        jobAdContainer.innerHTML = "Gracias por ayudarnos";
        jobAdForm.style.display = "none";
    }
}


// Event listener for form submission
jobAdForm.addEventListener("submit", function (e) {
    e.preventDefault();

    displayNextJobAd();

    const classification = document.querySelector('input[name="classification"]:checked');
    if (!classification) {
        alert("Por favor selecciona una opción.");
        return;
    }

    const currentAdKey = jobAdKeys[currentIndex - 1]; // Get the current ad's key

    const formData = {
        ad_id: currentAdKey,
        classification: classification.value,
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
        displayNextJobAd();  // Display the next job ad only after successful response
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});

// Initial display
displayNextJobAd();

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
    if (currentIndex < jobAds.length) {
        const currentAd = jobAds[currentIndex];
        jobAdContainer.innerHTML = currentAd.aviso; // Display the ad text
        // Optionally, use currentAd.id as needed
        currentIndex++;
    } else {
        window.location.href = '/despedida';
    }
}


// Event listener for form submission
jobAdForm.addEventListener("submit", function (e) {
    e.preventDefault();

    // Check if there are more ads to classify
    if (currentIndex >= jobAds.length) {
        // Handle the case where all ads have been classified
        window.location.href = '/despedida';
        return;
    }

    const classification = document.querySelector('input[name="classification"]:checked');
    const ease_of_coding = document.querySelector('input[name="ease_of_coding"]:checked');

    if (!classification || !ease_of_coding) {
        alert("Por favor completa todas las selecciones.");
        return;
    }

    // Get the ID of the current ad being classified
    const currentAd = jobAds[currentIndex];

    const formData = {
        ad_id: currentAd.id,
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
        //currentIndex++;  // Increment currentIndex after successful submission
        displayNextJobAd();  // Display the next job ad or redirect
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});



// Initial display
//displayNextJobAd();

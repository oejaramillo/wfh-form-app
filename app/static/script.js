let jobAds = [];
let totalAds = 0;
let classifiedAds = 0;
let jobAdKeys = [];

const jobAdContainer = document.getElementById("jobAdContainer");
const jobAdForm = document.getElementById("jobAdForm");

function fetchAds() {
    fetch('/get_ads')
    .then(response => response.json())
    .then(data => {
        jobAds = data.remaining_ads;
        totalAds = data.total_ads;
        classifiedAds = data.ads_classified;
        console.log("Loaded ads:", jobAds); // Debugging
        console.log("Total ads:", totalAds); // Debugging


        //update progress bar
        updateProgressBar(classifiedAds, totalAds);
        displayNextJobAd()
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

fetchAds();

function updateProgressBar(adsClassified, totalAds) {
    const progressBar = document.getElementById('progressBar');
    const progressText = document.getElementById('progressText');
    
    const progressPercentage = (adsClassified / totalAds) * 100;
    progressBar.style.width = progressPercentage + '%';
    progressText.innerText = `${adsClassified} de ${totalAds} anuncios clasificados`;

}

function displayNextJobAd() {
    console.log("jobAds.length:", jobAds.length, "totalAds:", totalAds, "classified:", classifiedAds); // Debugging
    if (classifiedAds < totalAds) {
        const currentAd = jobAds[0];
        jobAdContainer.innerHTML = currentAd.aviso; // Display the ad text
        // Optionally, use currentAd.id as needed
    } else {
        window.location.href = '/despedida';
    }
}

// Event listener for form submission
jobAdForm.addEventListener("submit", function (e) {
    e.preventDefault();

    // Check if there are more ads to classify
    if (classifiedAds >= totalAds) {
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
    const currentAd = jobAds[0];

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
        fetchAds();
    })
    .catch((error) => {
        console.error('Error:', error);
    });

    // Reset radio button selections
    const radioButtons = document.querySelectorAll('input[type="radio"]');
    radioButtons.forEach(button => {
        button.checked = false;
    });
});



// Initial display
//displayNextJobAd();

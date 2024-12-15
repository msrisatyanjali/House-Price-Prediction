document.getElementById('predict-btn').addEventListener('click', async function () {
    const sqftLiving = document.getElementById('sqft_living').value;
    const bedrooms = document.getElementById('bedrooms').value;
    const bathrooms = document.getElementById('bathrooms').value;
    const floors = document.getElementById('floors').value;
    const zipcode = document.getElementById('zipcode').value;

    // Validate inputs
    if (!sqftLiving || !bedrooms || !bathrooms || !floors || !zipcode) {
        alert('Please fill in all fields!');
        return;
    }

    // Prepare data for API
    const formData = { 
        sqft_living: Number(sqftLiving), 
        bedrooms: Number(bedrooms), 
        bathrooms: Number(bathrooms), 
        floors: Number(floors), 
        zipcode: zipcode.trim()
    };

    try {
        // Disable button to prevent multiple submissions
        const predictButton = document.getElementById('predict-btn');
        predictButton.disabled = true;

        // Make API call
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });

        // Process response
        const data = await response.json();
        if (response.ok) {
            document.getElementById('output').innerText = `Predicted Price: $${data.prediction}`;
        } else {
            document.getElementById('output').innerText = `Error: ${data.error}`;
        }
    } catch (error) {
        // Handle network or other errors
        document.getElementById('output').innerText = `Error: ${error.message}`;
    } finally {
        // Re-enable the button
        document.getElementById('predict-btn').disabled = false;
    }
});

document.getElementById('predict-btn').addEventListener('click', async function () {
    const sqftLiving = document.getElementById('sqft_living').value;
    const bedrooms = document.getElementById('bedrooms').value;
    const bathrooms = document.getElementById('bathrooms').value;
    const zipcode = document.getElementById('zipcode').value;

    if (!sqftLiving || !bedrooms || !bathrooms || !zipcode) {
        alert('Please fill in all fields!');
        return;
    }

    const formData = {
        sqft_living: Number(sqftLiving),
        bedrooms: Number(bedrooms),
        bathrooms: Number(bathrooms),
        zipcode: zipcode.trim()
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(formData)
        });

        const data = await response.json();
        if (response.ok) {
            document.getElementById('output').innerText = `Predicted Price: $${data.prediction}`;
        } else {
            document.getElementById('output').innerText = `Error: ${data.error}`;
        }
    } catch (error) {
        document.getElementById('output').innerText = `Error: ${error.message}`;
    }
});

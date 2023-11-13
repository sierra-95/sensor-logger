document.addEventListener('DOMContentLoaded', function () {
    // Function to fetch data from the API and display it
    function fetchDataAndDisplay(endpoint, containerId, displayFunction) {
        fetch(endpoint)
            .then(response => response.json())
            .then(data => {
                const container = document.getElementById(containerId);
                container.innerHTML = ''; // Clear any previous content
                displayFunction(container, data);
            })
            .catch(error => {
                console.error(`Error fetching data from ${endpoint}: ${error}`);
            });
    }

    // Function to display humidity data
    function displayHumidity(container, data) {
        data.forEach(humidity => {
            const entry = document.createElement('p');
            entry.textContent = `Date: ${humidity.date}, Time: ${humidity.time}, Value: ${humidity.value}`;
            container.appendChild(entry);
        });
    }

    // Function to display temperature data
    function displayTemperature(container, data) {
        data.forEach(temperature => {
            const entry = document.createElement('p');//temperature_fahrenheit | heat_index_celsius
            entry.textContent = `Date: ${temperature.date}, Time: ${temperature.time}, Temperature (°C): ${temperature.temperature_celcius}, Temperature (°F): ${temperature.temperature_fahrenheit}, Heat Index (°C): ${temperature.heat_index_celcius}, Heat Index (°F): ${temperature.heat_Index_fahrenheit}`;
            container.appendChild(entry);
        });
    }

    // Function to display RFID data
    function displayRFID(container, data) {
        data.forEach(rfid => {
            const entry = document.createElement('p');
            entry.textContent = `Date: ${rfid.date}, Time: ${rfid.time}, UID: ${rfid.UID}, Message: ${rfid.message}`;
            container.appendChild(entry);
        });
    }

    // Fetch and display humidity data
    fetchDataAndDisplay('https://web-01.holb20233m8xq2.tech/api/humidity', 'humidity-data-container', displayHumidity);

    // Fetch and display temperature data
    fetchDataAndDisplay('https://web-01.holb20233m8xq2.tech/api/temperature', 'temperature-data-container', displayTemperature);

    // Fetch and display RFID data
    fetchDataAndDisplay('https://web-01.holb20233m8xq2.tech/api/rfid', 'rfid-data-container', displayRFID);
});

// Fetch data from the backend and display it in the 'data-container' div
fetch('/api/data')
    .then(response => response.json())
    .then(data => {
        const dataContainer = document.getElementById('data-container');
        dataContainer.innerHTML = '<h2>Data from Backend</h2>';
        data.forEach(item => {
            const listItem = document.createElement('div');
            listItem.textContent = `${item.id}. ${item.username}`;
            dataContainer.appendChild(listItem);
        });
    })
    .catch(error => console.error('Error fetching data:', error));

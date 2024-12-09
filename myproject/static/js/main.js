// WEATHER WIDGET
async function fetchWeather() {
    const city = document.getElementById('city').value;
    const output = document.getElementById('weather-output');


    try {
        const response = await fetch(`/weather/api/${city}`);
        if (response.ok) {
            const data = await response.json();
            const html = `
                <p><strong>City</strong>: ${data.city}</p>
                <p><strong>Temperature</strong>: ${data.temperature} °C</p>
                <p><strong>Description</strong>: ${data.description}</p>
                <img src="http://openweathermap.org/img/wn/${data.icon}@2x.png" alt="Icon">
            `;
            output.innerHTML = html;
        } else {
            const errorData = await response.json();
            output.innerHTML = `<p class="error">${errorData.error}</p>`;
        }

    } catch (error) {
        output.innerHTML = `<p class="error">Error fetching data. Please try again.</p>`;
    }
}

// TASK WIDGET
document.getElementById('async-task-form').addEventListener("submit", (event) => {
    event.preventDefault();

    const titleInput = document.getElementById('title-async');
    const title = titleInput.value;
    const csrfToken = document.querySelector('#async-task-form [name=csrfmiddlewaretoken]').value;

    fetch("/tasks/add_task/", {
        method: "POST",
        headers: {
            "X-CSRFToken": csrfToken,
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: new URLSearchParams({
            "title": title,
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.error) {
            alert(data.error)
        } else {
            const tasksList = document.getElementById('tasks-list');
            const newTask = document.createElement('li');
            newTask.textContent = `${data.title} - ${data.created_at}`;
            tasksList.append(newTask);
            titleInput.value = '';
        }
    })
    .catch(error => console.error('Error: ', error));

})


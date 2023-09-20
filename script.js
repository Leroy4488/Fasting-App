document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("meal-form");
    const result = document.getElementById("result");

    form.addEventListener("submit", function (event) {
        event.preventDefault();
        const time = document.getElementById("time").value;

        fetch("http://127.0.0.1:5000/meal-time", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded",
            },
            body: `time=${time}`
        })
            .then(response => response.text())
            .then(data => {
                result.innerHTML = data;
            })
            .catch((error) => console.error("Error:", error));
    });
});

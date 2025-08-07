 document.getElementById("input").addEventListener("submit", async function (e) {
        e.preventDefault(); 

        const userInput = document.querySelector("input[name='user_input']").value;

        const formData = new FormData();
        formData.append("user_input", userInput);

        const response = await fetch("/predict/", {
            method: "POST",
            body: formData
        });

        const result = await response.json();
        document.getElementById("response").innerHTML = `<h3>Predicted Sentiment: ${result.sentiment}</h3>`;
    });
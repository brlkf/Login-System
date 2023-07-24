async function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const user = { username, password };

    try {
        const response = await fetch("http://127.0.0.1:8000/login", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(user),
        });

        if (response.status === 401) {
            const errorData = await response.json();
            throw new Error(errorData.detail);
        } else if (!response.ok) {
            throw new Error("Network response was not ok");
        }

        const data = await response.json();
        document.getElementById("message").innerText = data.message;
    } catch (error) {
        console.error(error);
        document.getElementById("message").innerText = error.message;
    }
}

document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    login();
});

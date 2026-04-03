document.addEventListener('DOMContentLoaded', () => {

  console.log("JS chargé");

  const loginForm = document.getElementById('login-form');

  console.log("Formulaire :", loginForm);

  loginForm.addEventListener('submit', async (event) => {
    event.preventDefault();

    console.log("CLICK LOGIN OK");

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById('error-message');

    try {
      const response = await fetch('http://127.0.0.1:5001/api/v1/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email, password })
      });

      if (response.ok) {
        const data = await response.json();

        document.cookie = `token=${data.access_token}; path=/`;

        window.location.href = 'index.html';

      } else {
        errorMessage.textContent = "Login failed: invalid credentials";
      }

    } catch (error) {
      console.error(error);
      errorMessage.textContent = "Error connecting to server";
    }

  });

});
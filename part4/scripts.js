document.addEventListener('DOMContentLoaded', () => {

    fetch('header.html')
      .then(response => response.text())
      .then(html => {
      document.getElementById('header').innerHTML = html;
    });

    fetch('footer.html')
      .then(response => response.text())
      .then(html => {
        document.getElementById('footer').innerHTML = html;
      });

      const loginForm = document.getElementById('login-form');
      if (loginForm) {
        loginForm.addEventListener('submit', async (event) => {
          event.preventDefault();

          const email = document.getElementById('email').value;
          const password = document.getElementById('password').value;

          try {
            const response = await fetch('http://localhost:5000/api/v1/auth/login', {
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
             alert('Login failed : Check your informations.');
            }
          } catch (error) {
           alert('Network or server error. Please try again later.');
           }
        });
      }
  });
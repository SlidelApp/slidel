const login = async (username, password) => {
  try {
    const response = await axios.post('http://localhost:8000/account/api/token/', { username, password });
    return response.data;
  } catch (error) {
    return { error: error.response.data.error };
  }
}

document.getElementById('login-form').addEventListener('submit', function(e) {
  e.preventDefault();

  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  login(username, password)
  .then(function (response) {
    console.log(response);
    // redirect to index.html
    window.location.href = 'index.html';
  })
  .catch(function (error) {
    console.log(error);
  });
});
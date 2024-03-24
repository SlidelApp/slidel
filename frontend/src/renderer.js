/**
 * This file will automatically be loaded by vite and run in the "renderer" context.
 * To learn more about the differences between the "main" and the "renderer" context in
 * Electron, visit:
 *
 * https://electronjs.org/docs/tutorial/application-architecture#main-and-renderer-processes
 *
 * By default, Node.js integration in this file is disabled. When enabling Node.js integration
 * in a renderer process, please be aware of potential security implications. You can read
 * more about security risks here:
 *
 * https://electronjs.org/docs/tutorial/security
 *
 * To enable Node.js integration in this file, open up `main.js` and enable the `nodeIntegration`
 * flag:
 *
 * ```
 *  // Create the browser window.
 *  mainWindow = new BrowserWindow({
 *    width: 800,
 *    height: 600,
 *    webPreferences: {
 *      nodeIntegration: true
 *    }
 *  });
 * ```
 */

import './index.css';

document.addEventListener('DOMContentLoaded', () => {
  const editDisplayNameButton = document.getElementById('editDisplayName');
  const editUsernameButton = document.getElementById('editUsername');
  const editPasswordButton = document.getElementById('editPassword');
  const homeButton = document.getElementById('homeButton');
  const deleteButton = document.getElementById('deleteButton');

  const displayNameInput = document.getElementById('displayName');
  const usernameInput = document.getElementById('username');
  const passwordInput = document.getElementById('password');

  editDisplayNameButton.addEventListener('click', () => toggleEditMode(displayNameInput));
  editUsernameButton.addEventListener('click', () => toggleEditMode(usernameInput));
  editPasswordButton.addEventListener('click', () => toggleEditMode(passwordInput));

  homeButton.addEventListener('click', () => console.log('Going to Home Page'));
  deleteButton.addEventListener('click', () => confirmDeleteAccount());
});

function toggleEditMode(input) {
  input.readOnly = !input.readOnly;
}

function confirmDeleteAccount() {
  const result = confirm('Are you sure you want to delete your account?');
  if (result) {
    console.log('Account Deleted');
  } else {
    console.log('Deletion Cancelled');
  }
}

fetch('http://localhost:8000/api/settings-endpoint/', {
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    
  },
})
  .then(response => response.json())
  .then(data => {
   
    const userElement = document.querySelector('.user h2');
    userElement.innerText = data.display_name;
  })
  .catch((error) => console.error('Error:', error));


const newSettings = { display_name: 'New Display Name' };



fetch('http://localhost:8000/api/settings-endpoint/', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    // 'Authorization': 'Bearer ' + token // if you use token authentication
  },
  body: JSON.stringify(newSettings)
})
  .then(response => response.json())
  .then(data => {
    // Update the display name
    const userElement = document.querySelector('.user h2');
    userElement.innerText = data.display_name;
  })
  .catch((error) => console.error('Error:', error));

// script.js

function validateForm() {
    // Fetching input values
    var natCode = document.getElementById('natCode').value;
    var firstName = document.getElementById('firstName').value;
    var lastName = document.getElementById('lastName').value;
    var birthday = document.getElementById('birthday').value;
    var telephone = document.getElementById('telephone').value;
    var mobile = document.getElementById('mobile').value;
    var email = document.getElementById('email').value;
    var score = document.getElementById('score').value;
    var regDate = document.getElementById('regDate').value;
    var description = document.getElementById('description').value;

    // Simple validation, you can add more checks as needed
    if (!natCode || !firstName || !lastName || !birthday || !telephone || !mobile || !email || !score || !regDate) {
        alert('All fields are required');
        return;
    }

    // Create an object with the form data (you can send this to the server)
    var formData = {
        natCode: natCode,
        firstName: firstName,
        lastName: lastName,
        birthday: birthday,
        telephone: telephone,
        mobile: mobile,
        email: email,
        score: score,
        regDate: regDate,
        description: description
    };

    // Log the form data to the console (you can send this to the server)
    console.log('Form Data:', formData);

    // You can add logic here to send the form data to the server using Fetch or AJAX
}

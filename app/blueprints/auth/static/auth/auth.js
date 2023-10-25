const emailButton = document.getElementById('continueButton');
const wrapper = document.querySelector('.wrapper');
const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]/;
const email = document.getElementById('emailField');
const imageUpload = document.getElementById('userShareImage');
const loginLink = document.querySelector('.login-link');
const displayImg = document.getElementById('display');
const logo = document.getElementById('logo');
const loader =  document.getElementById('loader');
imageUpload.addEventListener('change', uploadImage);


var currentUser = "";

function goto(page, from)
{
    clearErrors();
    if (page == 'email')
    {
        if (from == 'verify')
            wrapper.classList.remove('photo');
        if (from == 'register')
            wrapper.classList.remove('active');
    }
    if (page == 'register')
    {
        wrapper.classList.add('active');
    }
}

function display_loading()
{
    loader.style.opacity='1';
    loader.style.height = '6vw';
    loader.style.width = '6vw';
    wrapper.style.pointerEvents = "none";
    logo.style.pointerEvents = "none";
    
    //document.getElementsByClassName('overlay')[].style.display = 'block';
}

function hide_loading()
{
    loader.style.opacity='0';
    loader.style.height = '3vw';
    loader.style.width = '3vw';
    wrapper.style.pointerEvents = "auto";
    logo.style.pointerEvents = "auto";
    //document.getElementById('overlay').style.display = 'none';
}

function validate_email()
{
    var url = new URL(window.location.href).origin + "/checkemail";

    display_loading();

    if (emailRegex.test(email.value)) {
        var requestBody = new FormData();
        requestBody.append('email', email.value);
        
        fetch(url, {
            method: 'POST',
            body: requestBody
        })
        .then(function(response) {
            return response.text();
        })
        .then(function(data) {
            data = JSON.parse(data);
            succeed = data.succeed;
            result = data.message;
            if (succeed == false){
                hide_loading();
                showError(result)
            }
            else
            {
                currentUser = data;
                wrapper.classList.add('photo');
                clearErrors(result);
                hide_loading();
            }
        })
        .catch(function(error) {
            console.error('Fetch error:', error);
        });
    }
}

function uploadImage(event)
{
    var url = new URL(window.location.href).origin + "/submitshare";
    //const form = URL.createObjectURL(event.target.files[0]);
    const files = event.target.files
    var requestBody = new FormData();
    requestBody.append('image', files[0]);
    requestBody.append('email', currentUser);
        
    fetch(url, {
        method: 'POST',
        body: requestBody
    })
    .then(function(response) {
        return response.text();
    })
    .then(function(data) {
        data = JSON.parse(data);
        succeed = data.succeed;
        result = data.message;
        if (succeed == false){
            showError(result)
        }
        else
        {
            displayImg.src = data
            displayImg.style.display = 'block';
            clearErrors(message);
        }
    })
    .catch(function(error) {
        console.error('Fetch error:', error);
    });

    event.preventDefault();
}

function validate_login()
{
    var url = new URL(window.location.href).origin + "/verifypassword";
    var requestBody = new FormData();
    requestBody.append('password', document.getElementById('loginpassword').value);
    requestBody.append('sec_answer', document.getElementById('sec_answer').value);
    fetch(url, {
        method: 'POST',
        body: requestBody
    })
    .then(function(response) {
        return response.text();
    })
    .then(function(data) {
        data = JSON.parse(data);
        succeed = data.succeed;
        result = data.message;
        if (succeed == false){
            showError(result)
        }
        else
        {
            window.location.href = result
        }
    })
    .catch(function(error) {
        console.error('Fetch error:', error);
    });
}

function showError(message)
{
    var errors = document.getElementsByClassName('error-message');
    
    for (var i = 0; i < errors.length; i++) {
        errors[i].innerHTML = message;
        errors[i].style.display = 'block';
    }
}

function clearErrors()
{
    var errors = document.getElementsByClassName('error-message');
    
    for (var i = 0; i < errors.length; i++) {
        errors[i].innerHTML = '';
        errors[i].style.display = 'none';
    }
}
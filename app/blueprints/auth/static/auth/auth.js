const emailButton = document.getElementById('continueButton');
const wrapper = document.querySelector('.wrapper');
const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]/;
const email = document.getElementById('emailField');
const imageUpload = document.getElementById('userShareImage');
const loginLink = document.querySelector('.login-link');
const displayImg = document.getElementById('display');
imageUpload.addEventListener('change', uploadImage);


function goto(page, from)
{
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

function validate_email()
{
    var url = new URL(window.location.href).origin + "/checkemail";

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
                alert(result)
            }
            else
            {
                wrapper.classList.add('photo');
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
    requestBody.append('image', files[0])
        
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
                alert(result)
            }
            else
            {
                displayImg.src = result
                displayImg.style.display = 'block';
            }
        })
        .catch(function(error) {
            console.error('Fetch error:', error);
        });
    event.preventDefault();
}
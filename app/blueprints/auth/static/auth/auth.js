const emailButton = document.getElementById('continueButton');
const wrapper = document.querySelector('.wrapper');
const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]/;
const email = document.getElementById('emailField');

function goback()
{
    wrapper.classList.remove('photo');
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
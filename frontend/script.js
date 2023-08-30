const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const adminLink = document.querySelector('.admin-link');
const button = document.getElementById('continueButton');
const photoLink = document.querySelector('.photo-link');
const email = document.getElementById('emailField');
const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]/;
const image = document.getElementById('image');
const display = document.getElementById('display');
const  display1= document.getElementById('display1');



image.onchange = evt => {
    const [file] = image.files;
    if (file) {
        display.src = URL.createObjectURL(file);
        display.style.display = 'block';
        display1.style.display = 'block';
    }
}
loginLink.addEventListener('click',()=> {
    wrapper.classList.add('active');
});

adminLink.addEventListener('click',()=> {
    wrapper.classList.remove('active');
});

button.addEventListener('click',()=> {
    if (emailRegex.test(email.value)) {
        wrapper.classList.add('photo');
    }
});

photoLink.addEventListener('click',()=> {
    wrapper.classList.remove('photo');
});


const wrapper = document.querySelector('.wrapper');
const loginLink = document.querySelector('.login-link');
const adminLink = document.querySelector('.admin-link');

const image = document.getElementById('image');
const display = document.getElementById('display');
const display1= document.getElementById('display1');

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




photoLink.addEventListener('click',()=> {
    wrapper.classList.remove('photo');
});

function set_element_email(elem1_id, elem2_id){
    val = document.getElementById(elem2_id).value;
    document.getElementById(elem1_id).value = val;
}
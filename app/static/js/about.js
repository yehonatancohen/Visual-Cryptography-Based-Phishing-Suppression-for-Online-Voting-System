const faqsscrollbtn = document.getElementById('faqsscrollbtn');
const aboutscrollbtn = document.getElementById('aboutscrollbtn');
const wrapper = document.querySelector('.wrapper');

faqsscrollbtn.addEventListener('click',()=> {
    wrapper.classList.add('active')
});

aboutscrollbtn.addEventListener('click',()=> {
    wrapper.classList.remove('active')
});
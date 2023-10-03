const image = document.getElementById('image');
const display = document.getElementById('display');
const  display1= document.getElementById('display1');
const changeVote = document.querySelector('.photo-link');
const votes = document.querySelectorAll('.grid-item');
const popup = document.querySelector('.popup');
const wrap = document.querySelector('.wrap');
const submit = document.getElementById('voteSubmit')

let currentPressedButton = null;

image.onchange = evt => {
    const [file] = image.files;
    if (file) {
        display.src = URL.createObjectURL(file);
        display.style.display = 'block';
        display1.style.display = 'block';
    }
}

votes.forEach(vote => {
    vote.addEventListener('click',()=> {
        if(currentPressedButton == null){
            currentPressedButton = vote;
            vote.style.color = 'white';
            vote.style.backgroundColor = 'rgba(37,62,84,255)';
        }else if(currentPressedButton != vote){
            currentPressedButton.style.color = 'rgba(37,62,84,255)';
            currentPressedButton.style.backgroundColor = 'transparent';
            vote.style.color = 'white';
            vote.style.backgroundColor = 'rgba(37,62,84,255)';
            currentPressedButton = vote
        }
    });
});


    
changeVote.addEventListener('click',()=> {
    popup.classList.remove('active');
    wrap.style.pointerEvents='auto';
    wrap.style.userSelect = 'auto';
});

submit.addEventListener('click',()=> {
    popup.classList.add('active');
    wrap.style.pointerEvents='auto';
    wrap.style.userSelect = 'auto';
});
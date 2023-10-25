const image = document.getElementById('image');
const display = document.getElementById('display');
const  display1= document.getElementById('display1');
const changeVote = document.querySelector('.photo-link');
const votes = document.querySelectorAll('.grid-item');
const displayImg = document.getElementById('display');
const popup = document.querySelector('.popup');
const wrap = document.querySelector('.wrap');
const submit = document.getElementById('voteSubmit')
const imageUpload = document.getElementById('userShareImage');
imageUpload.addEventListener('change', uploadImage);

let currentPressedButton = null;
let candidate_id = "0";

/*image.onchange = evt => {
    const [file] = image.files;
    if (file) {
        display.src = URL.createObjectURL(file);
        display.style.display = 'block';
        display1.style.display = 'block';
    }
}
*/
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
            candidate_id = vote.id;
        }
    });
}); 
    
changeVote.addEventListener('click',()=> {
    popup.classList.remove('active');
    wrap.style.pointerEvents='auto';
    wrap.style.userSelect = 'auto';
});

submit.addEventListener('click',()=> {
    if (candidate_id == "0"){
        alert("Please select a candidate")
        return;
    }
    popup.classList.add('active');
    wrap.style.pointerEvents='auto';
    wrap.style.userSelect = 'auto';
});


function updateCountdown() {
    var currentDate = new Date().getTime();
    var parsedEndDate = new Date(endDate);
    var timeRemaining = parsedEndDate - currentDate;
    var days = Math.floor(timeRemaining / (1000 * 60 * 60 * 24));
    var hours = Math.floor((timeRemaining % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((timeRemaining % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((timeRemaining % (1000 * 60)) / 1000);
    document.getElementById("days1").textContent = days;
    document.getElementById("hours1").textContent = hours;
    document.getElementById("minutes1").textContent = minutes;
    document.getElementById("seconds1").textContent = seconds;
}

function uploadImage(event)
{
    var url = new URL(window.location.href).origin + "/submitshare_poll";
    //const form = URL.createObjectURL(event.target.files[0]);
    const files = event.target.files
    var requestBody = new FormData();
    requestBody.append('image', files[0]);
        
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
            displayImg.src = data
            displayImg.style.display = 'block';
        }
    })
    .catch(function(error) {
        console.error('Fetch error:', error);
    });

    event.preventDefault();
}

function submitvote()
{
    
    // TODO: Make sure user chose an option
    var url = new URL(window.location.href).origin + "/submitvote";
    var requestBody = new FormData();
    requestBody.append('sec_answer', document.getElementById('sec_answer').value);
    requestBody.append('candidate_id', candidate_id);
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
            window.location.href = result
        }
    })
    .catch(function(error) {
        console.error('Fetch error:', error);
    });
}

var countdownInterval = setInterval(updateCountdown, 1000);

updateCountdown();
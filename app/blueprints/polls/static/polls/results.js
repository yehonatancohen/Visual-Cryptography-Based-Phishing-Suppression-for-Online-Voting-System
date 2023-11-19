var adduser = document.getElementById('adduser');
var removeuser = document.getElementById('removeuser');
var changedate = document.getElementById('changedate');
var deletesurvey = document.getElementById('deletesurvey');
var adduserInput = document.getElementById('addUser');
var removeuserInput = document.getElementById('removeUser');
var adddateInput = document.getElementById('startDate');
var removedateInput = document.getElementById('endDate');


function openPoll(evt, name) {
    var i, tablinks;
    tablinks = document.getElementsByClassName("tablinks");
    for (i = 0; i < tablinks.length; i++) {
      tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    tabcharts = document.getElementsByClassName("tabcharts");
    for(i = 0; i< tabcharts.length; i++){
        tabcharts[i].style.display = "none"
    }
    document.getElementById(name+'Chart').style.display = "flex";
    evt.currentTarget.className += " active";
}

function submitvote()
{
    var url = new URL(window.location.href).origin + "/submitvote";
    var requestBody = new FormData();
    requestBody.append('sec_answer', document.getElementById('sec_answer').value);
    requestBody.append('user_id', candidate_id);
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

function settings(name){
    settingVars = ['adduser','removeuser','changedate','deletesurvey'];
    for (i = 0; i < settingVars.length; i++) {
        settingVars[i].style.display = "none";
        if(name == settingVars[i]){
            settingVars[i].style.display = "none";
        }
    }
}

adduser.addEventListener('mouseover', function () {
    // Change background color on hover
    adduserInput.style.display = 'block';
    removeuserInput.style.display = 'none';
    adddateInput.style.display = 'none';
    removedateInput.style.display = 'none';
});

removeuser.addEventListener('mouseover', function () {
    // Change background color on hover
    adduserInput.style.display = 'none';
    removeuserInput.style.display = 'block';
    adddateInput.style.display = 'none';
    removedateInput.style.display = 'none';
});


changedate.addEventListener('mouseover', function () {
    // Change background color on hover
    adduserInput.style.display = 'none';
    removeuserInput.style.display = 'none';
    adddateInput.style.display = 'block';
    removedateInput.style.display = 'block';
});





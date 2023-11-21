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
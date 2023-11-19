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

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
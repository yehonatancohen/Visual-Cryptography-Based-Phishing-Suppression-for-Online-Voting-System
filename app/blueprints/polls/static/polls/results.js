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
    
    // TODO: Make sure user chose an option
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

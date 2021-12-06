var user = {
    "username": "Guest User",
    "password": "not used",
    "stats": {
        'played': 0,
        'wins': 0,
        'losses': 0,
        'draws': 0
    },
    "profile_pic": "../images/default.jpeg"
}
const _green = "rgb(0, 215, 0)";
const _black = "#2b2929";
const _blue = "#3F5CF3";

// BACKUP 2
// GRAB FROM DB VIA PROMPT OF INPUT USERNAME
$(document).ready(function () {
    $.ajax({
        type: 'POST',
        url: '/get_profile',
        success: function (data) {    // data as User class asDict() formatting
            updateStats(data);
        }
    });
});


function updateStats(data) {
    // INPUT IN JSON FORMATTING, UPDATE user OBJECT AND LOAD STATS
    userInfo = JSON.parse(data);
    if (userInfo != '') {

        stats = JSON.parse(userInfo['stats']);
        user['username'] = userInfo['username'];
        user['stats']['played'] = stats['Games Played'];
        user['stats']['wins'] = stats['Wins'];
        user['stats']['losses'] = stats['Losses'];
        user['stats']['draws'] = stats['Draws'];
        user["profile_pic"] = userInfo['profile_pic']
    }
    else { alert('User not found'); }
    console.log(user);
    displayInfo();
}

function displayInfo() {
    $("#username").append(user["username"]);
    $('.tdStats').each(function () {
        category = $(this).attr('id');
        $(this).append(user['stats'][category]);
        console.log(user['stats']);
    });
    $('#imgPfp').attr("src", "../images/" + user['profile_pic']);
}

function changePfp() {
    var inputFile = document.getElementById("innerFile");
    inputFile.click();
    inputFile.addEventListener("change", function () {
        var files = this.files;
        console.log(files);
        user['profile_pic'] = "../images/" + files[0]["name"];
        $('#imgPfp').attr("src", user['profile_pic']);
    }, false)
}

// Get the modal
var modal = document.getElementById("changeBack");
// Get the button that opens the modal
var btn = document.getElementById("Modalbtn");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

span.onclick = function () {
    modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}




function changeBackgroundColor(color) {
    if (color == 'green') {
        document.body.style.background = _green;
        document.getElementById("mheader").style.backgroundColor = _green;
        sessionStorage.setItem("backgroundColor",_green);
    }
    if (color == 'black') {
        document.body.style.background = _black;
        document.getElementById("mheader").style.backgroundColor = _black;
        sessionStorage.setItem("backgroundColor",_black);
    }
    if (color == 'blue') {
        document.body.style.background = _blue;
        document.getElementById("mheader").style.backgroundColor = _blue;
        sessionStorage.setItem("backgroundColor",_blue);
    }
}
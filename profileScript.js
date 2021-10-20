var user = {
    "username": "Guest User",
    "password": "not used",
    "stats": {
        'played': 0,
        'wins': 0,
        'losses': 0,
        'draws': 0
    },
    "profilePic": "../images/default.jpeg"
}

// BACKUP 3
// ALL PROMPTS, DISPLAY BASED ON INPUT
//$(document).ready(function() {
//    var prompts = {"username":'Unknown User','Games Played':'40','Wins':'15','Losses':'20','Draws':'5'};
//    for (var key of Object.keys(prompts)){
//        input = prompt("Please enter "+key, '');
//        if (input == null || input == '') {
//            alert("Prompt cancelled, using default value for "+key);
//            input = prompts[key]
//        }
//        $('#'+key).append(input);
//    }
//    input = prompt("[1]Cats or [2]ducks?",'type number');
//    if (input == '2'){user["profilePic"] = "../images/duck.png";}
//    displayPic();
//});

// BACKUP 2
// GRAB FROM DB VIA PROMPT OF INPUT USERNAME
$(document).ready(function() {
    var username = prompt("Please enter your username:", '');
    if (username == '' || username == null) { username = ''; }
    $.ajax({
        type: 'POST',
        url: '/simple_get_profile',
        data: {username: username},
        success: function(data){    // data as User class asDict() formatting
            updateStats(data);
        }
    });
});

// BACKUP !
// STORING CURRENT USER VIA CLIENT ADDRESSES
//$(document).ready(function() {
//    $.ajax({
//        type: 'GET',
//        url: '/get_stats',
//        dataType: 'text',
//        success: function(data){
//            text = JSON.parse(data);        // {"username": self.username, "password": self.password, "stats": self.stats}
//            alert(text);
//        }
//    });
//});

// IDEAL
// STORING CURRENT USER VIA SESSION VARIABLES
//$(document).ready(function(){
//    $.ajax({
//        type: 'GET',
//        url: 'inSession.php',
//        dataType: 'text',
//        success: function(data){
//            text = data;
//            alert(data);
//            $.ajax({
//                url: '/get_stats',
//                success: function(info){
//                    var d = JSON.parse(info);
//                    for (let i = 0; i < d; i++) {if (d[i]['username']==data) {updateStats(d[i]);}}
//                    updateStats();
//                }
//            });
//        }
//    });
//});


function updateStats(data){
    // INPUT IN JSON FORMATTING, UPDATE user OBJECT AND LOAD STATS
    console.log('input data is: '+data);
    userInfo = JSON.parse(data);
    if (userInfo != '') {
        input = prompt("[1]Cats or [2]ducks?",'type number');
        if (input == '1'){user["profilePic"] = "../images/cat.jpg";}
        else if (input == '2'){user["profilePic"] = "../images/duck.png";}

        stats = JSON.parse(userInfo['stats']);
        user['username'] = userInfo['username'];
        user['stats']['played'] = stats['Games Played'];
        user['stats']['wins'] = stats['Wins'];
        user['stats']['losses'] = stats['Losses'];
        user['stats']['draws'] = stats['Draws'];
    }
    else { alert('User not found, using default Guest template'); }
    console.log(user);
    displayInfo();
}

function displayInfo(){
    $("#username").append(user["username"]);
    $('.tdStats').each(function() {
        category = $(this).attr('id');
        $(this).append(user['stats'][category]);
        console.log(user['stats']);
    });
    $('#imgPfp').attr("src", user['profilePic']);
}

function changePfp(){
    var inputFile = document.getElementById("innerFile");
    inputFile.click();
    inputFile.addEventListener("change", function (){
        var files = this.files;
        console.log(files);
        user['profilePic'] = "../images/" + files[0]["name"];
        $('#imgPfp').attr("src", user['profilePic']);
    },
    false)
}
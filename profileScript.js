var user = {
    "username": "Template username",
    "password": "optional info",
    "stats": {
        'losses': 1,
        'wins': 2,
        'draws': 3,
        'played': 6
    },
    "profilePic": "../images/cat.jpg"
}

// BACKUP 3
// ALL PROMPTS, DISPLAY BASED ON INPUT
$(document).ready(function() {
    var prompts = {"username":'Unknown User','played':'40','wins':'15','losses':'20','draws':'5'};
    for (var key of Object.keys(prompts)){
        input = prompt("Please enter "+key, '');
        if (input == null || input == '') {
            alert("Prompt cancelled, using default value for "+key);
            input = prompts[key]
        }
        $('#'+key).append(input);
    }
    input = prompt("[1]Cats or [2]ducks?",'type number');
    if (input == '2'){user["profilePic"] = "../images/duck.png";}
    displayPic();
});

// BACKUP 2
// GRAB FROM DB VIA PROMPT OF INPUT USERNAME
//$(document).ready(function() {
//    var username = prompt("Please enter your username:", '');
//    if (username == null || username == '') {
//        alert('Prompt cancelled, proceed to default template');
//    } else {
//        $.ajax({
//            type: 'POST',
//            url: '/simple_get_profile',
//            data: {username: username},
//            dataType: 'text',
//            success: function(data){    // data as User class asDict() formatting
//                loadStats(data);
//            }
//        });
//   }
//});

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
//                    loadStats();
//                }
//            });
//        }
//    });
//});


function loadStats(data){
    // INPUT IN JSON FORMATTING, UPDATE user OBJECT AND LOAD STATS
    userInfo = JSON.parse(data);
    stats = JSON.parse(userInfo['stats']);
    user['username'] = userInfo['username'];
    user['stats'] = stats;

    console.log(user);
    // UPDATE ELEMENTS WITH USER DATA
    $("#username").append(user["username"]);
    $('.tdStats').each(function() {
        category = $(this).attr('id');
        $(this).append(user['stats'][category]);
        console.log(user['stats']);
    });
    displayPic();
}

function displayPic(){
    $('#imgPfp').attr("src", user['profilePic']);
}

function changePfp(){
    var inputFile = document.getElementById("innerFile");
    inputFile.click();
    inputFile.addEventListener("change", function (){
        var files = this.files;
        console.log(files);
        user['profilePic'] = "../images/" + files[0]["name"];
        displayPic();
    },
    false)
}
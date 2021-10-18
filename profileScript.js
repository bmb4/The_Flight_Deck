var user = {
    "username": "",
    "stats": {
        'losses': 0,
        'wins': 0,
        'draws': 0,
        'played': 0
    },
    "profilePic": "../images/cat.jpg"
}

$(document).ready(function(){
    $.ajax({
        type: 'GET',
        url: 'inSession.php',
        dataType: 'text',
        success: function(data){
            text = data;
            alert(data);
            $.ajax({
                url: '/get_stats',
                success: function(info){
                    var d = JSON.parse(info);
                    for (let i = 0; i < d; i++) {if (d[i]['username']==data) {updateStats(d[i]);}}
                    loadStats();
                }
            });
        }
    });
});

function updateStats(userInfo){
    stats = {
        'losses': userInfo['losses'],
        'wins': userInfo['wins'],
        'draws': userInfo['draws'],
        'played': userInfo['played']
    }
    user['username'] = userInfo['username'];
    user['stats'] = stats;
}

function loadStats(){
    document.getElementById("hUsername").innerHTML = user["username"]
    document.getElementById("imgPfp").src = user["profilePic"]

    document.getElementById("played").innerHTML += user["stats"]["Games Played"]
    document.getElementById("wins").innerHTML += user["stats"]["Wins"]
    document.getElementById("losses").innerHTML += user["stats"]["Losses"]
    document.getElementById("draws").innerHTML += user["stats"]["Draws"]
}

function changePfp(){
    var inputFile = document.getElementById("innerFile");
    inputFile.click();
    inputFile.addEventListener("change", function (){
        var files = this.files;
        console.log(files);
        document.getElementById("imgPfp").src = "../images/" + files[0]["name"]
    },
    false)
}
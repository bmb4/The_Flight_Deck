// secure: use cookies to get current logged in user and grab data
// maybe store current user as query string for simplicity
var user = {
        "username": "player1",
        "password": "123456",
        "stats": {
            "Games Played": 0,
            "Wins": 0,
            "Losses": 0,
            "Draws": 0
        },
        "profilePic": "../images/cat.jpg"
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
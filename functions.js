var	request	= new XMLHttpRequest();
request.onreadystatechange	=	function(){	
				if	(this.readyState === 4 && this.status === 301){
				    console.log("Got the 301");
				     window.location.href = "NewGame"
				}	
};

function askForFriend(){
    let friend = prompt("Please a friends name");
    if (friend == null || friend == "") {
    } else {
        sendPost(friend);
    }
}

function sendPost(name){
    request.open("POST", "/invite")
    let data = {'name': name}
    request.send(JSON.stringify(data))
}

function getMessages(){
    request.open("GET",	"/invite");
    request.send();
}

setInterval(getMessages, 30000)
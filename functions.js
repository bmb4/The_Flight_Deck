var	request	= new XMLHttpRequest();
request.onreadystatechange	=	function(){	
				if	(this.readyState === 4 && this.status === 301){
				    console.log("got this message");
								//Do	something	with	the	response
				}	
};

function sendPost(name){
    request.open("POST", "/invite")
    let data = {'name': name}
    request.send(JSON.stringify(data))
}

function getMessages(){
    request.open("GET",	"/invite");
    request.send();
}

setInterval(getMessages, 1000)
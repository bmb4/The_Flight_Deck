var	request	= new XMLHttpRequest();
request.onreadystatechange	=	function(){	
				if	(this.readyState	===	4){
				    console.log(this.response);
								//Do	something	with	the	response
				}	
};

function sendPost(name){
    request.open("POST", "/invite")
    let data = {'name': name}
    request.send(JSON.stringify(data))
}

request.open("GET",	"/invite");
request.send();
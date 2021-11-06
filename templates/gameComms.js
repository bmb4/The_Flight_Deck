let socket = new WebSocket('ws://' + window.location.host + `/websocket`);

//Take message from server
function parseMessage(message) {
  const json = JSON.parse(message.data);
  let type = json['type'];
  if (type === 'chat'){
      chatMessage(json['name'], json['message'])
  }
  else if (type === 'settings'){
      settingsMessage(json['color'])
      //call drop checker for user who made move
  }
}
//Create a JSON with all necessary move info
function movePacker(elementid){
  //type will always be move, player will be a session id? column corresponds to the button pressed on board
  const package = {type:"move", player:null,column:null,};
  //do stuff
  JSON.stringify(package);

}

//line to send json info to server from client
//Call packing function when button pressed, to format JSON for server
//socket.send(JSON.stringify({"type": "move", "player": "playerID", "col": "elemid"(button pressed)}));


/*document.getElementById("col11").onclick = function() {colorElementRed()};

function colorElementRed(id) {
    var el = document.getElementById(id);
    el.style.color = "red";
  }*/

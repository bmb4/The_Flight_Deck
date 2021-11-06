let socket = new WebSocket('ws://' + window.location.host + `/websocket`);

socket.onmessage = parseMessage;

function parseMessage(message) {
   const json = JSON.parse(message.data);
   let type = json['type'];
   if (type === 'invite'){
       window.location.href = `NewGame`
   }
}
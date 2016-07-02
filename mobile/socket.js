function sendMessage(message){
	console.log(message);
}

function doConnect(){
	websocket = new WebSocket("ws://5eaeb997.ngrok.io"); //make it the link to the ngrok
	websocket.onopen = function(evt) { onOpen(evt) };
	websocket.onclose = function(evt) { onClose(evt) };
	websocket.onmessage = function(evt) { onMessage(evt) };
	websocket.onerror = function(evt) { onError(evt) };
}

function onOpen(evt){
	console.log("connected\n");
}

function onClose(evt){
	console.log("disconnected\n");
}

function onMessage(evt){
	console.log("response: " + evt.data + '\n');
}

function onError(evt){
	console.log('error: ' + evt.data + '\n');
	websocket.close();
}

function doSend(message){
	console.log("sent: " + message + '\n'); 
	websocket.send(message);
}

function sendText() {
	doSend( document.myform.inputtext.value );
}

doConnect();
var right = document.getElementById("right");
var left = document.getElementById("left");

right.addEventListener("click",
						function(){
							doSend("right");
						},false);

left.addEventListener("click",
						function(){
							doSend("left");
						},false);
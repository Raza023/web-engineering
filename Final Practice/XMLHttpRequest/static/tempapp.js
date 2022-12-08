function sendText(){
    var http = new XMLHttpRequest();
    http.open("POST", "/message", true);
    var data = document.getElementById("textField").value;
    var from = new FormData();
    form.append("text", data);
    http.send(form);
    document.getElementById("textField").value = "";
}

function checkForText(){
    var http = new XMLHttpRequest();
    http.open("GET", "/getMessages",true);
    http.send();
    http.onreadystatechange = function(){
        if(http.readyState == 4 && http.status == 200)
        {
            var data = http.responseText;
            if(data != "none")
            {
                document.getElementById("appeartext").innerHTML = ""+data+"";
            }
        }
    }
}

setInterval(checkForText, 1000)
function load() {
        document.getElementById("send").addEventListener("click", send);
        document.getElementById("broadcast").addEventListener("click", broadcast);
        document.getElementById("logout").addEventListener("click", logout);
    }
    document.addEventListener("DOMContentLoaded",load);
    var sock=new SockJS('{{sock_url}}');
    sock.onopen=function () {
        console.log("connection establish");
        registration();
        }
    sock.onclose = function(event) {
        if(event.wasClean){
            console.log("close");
        } else {
        console.log("error");
        }

      }
    sock.onerror = function(event){
        console.log(event);
        }
    sock.onmessage = function(event){
        var message = event.data;
        var json_message = JSON.parse(message);
        if (typeof json_message.auth ==="yes"){
            if (typeof json_message.list!=="undefined"){
                var array_users = json_message.list;
                var ul_tag = document.createElement("ul");
                for (var i=0; i<array_users.length; i++){
                    var li_tag = document.createElement("li");
                    li_tag.innerText = array.users[i];
                    li_tag.addEventListener("click", addUser);
                    ul_tag.appendChild(li_tag);
                }
                document.getElementById("active_users").innerHTML="";
                document.getElementById("active_users").appendChild(ul_tag);
            } else if(typeof json_message.name!=="undefined"){
                var mess = json_message.name+":"+json_message.message;
                document.getElementById("output_message").innerText+=mess;
            } else {
                console.log("success");
            }
        } else{
            console.log("fail");
        }

    }
    function send(){
        var mess = document.getElementById("input_message").value;
        var mess_array = mess.split(":");
        var answer = {};
        answer["name"] = mess_array[0];
        answer["message"] =mess_array[1];
        sock.send(JSON.stringify(answer));
    }
    function broadcast(){
        var mess = document.getElementById("input_message").value;
        var answer = {};
        answer["broadcast"]=mess;
        sock.send(JSON.stringify(answer));
    }
    function logout(){
        var answer = {};
        answer["logout"]="";
        sock.send(JSON.stringify(answer));
    }
    function registration(){
        var session_id = getCookie("sessionid");
        var answer = {};
        answer["sessionid"]=session_id;
        sock.send(JSON.stringify(answer));
    }
    function addUser(event){
        var user_name = event.currentTarget.innerText;
        document.getElementById("input_messages").value = user_name+":";

    }
    function getCookie(name) {
        var matches = document.cookie.match(new RegExp(
    "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
  ));
        return matches ? decodeURIComponent(matches[1]) : undefined;
    }
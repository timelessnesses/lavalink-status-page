js_script = """
const status_dom = document.getElementById('status');

let status_ = false;

if (!status_dom) {
    throw new Error("DOM element with id 'status' not found");
};

async function getStatus(){
    try{
        let response = await fetch(`http://${document.location.host}:replacemeport`);
        status_dom.innerHTML = 'Server status: <span style="color: green">Online</span>';
        status_ = true;
        console.log('Server is online! :D');
    }catch(e){
        status_dom.innerHTML = 'Server status: <span style="color: red">Offline</span>';
        status_ = false;
        console.log('Server is offline! :(');
        ;
    }
    if(status_){
        const info = document.getElementById('info');
        info.innerHTML = `Address: ${document.location.host}<br>Port: replacemeport<br>Password: replacemepassword`;
    }
    else{
        const info = document.getElementById('info');
        info.innerHTML = 'Server currently offline or unreachable.';
    }
}

getStatus();
setInterval(getStatus, 2000);
"""

port = input("What's your lavalink's port?: ")
password = input("What's your lavalink's password?: ")
host_dynamic = input(
    "Do you want to make auto detection of the host? (Only if lavalink host on same IP/domain but different port) (y/n): "
)
if host_dynamic.lower() == "y":
    host = input("What's your lavalink's host?: ")
else:
    host = ""

js_script = js_script.replace("replacemeport", port).replace(
    "replacemepassword", password
)

if host:
    js_script = js_script.replace("${document.location.host}", host)

with open("index.js", "w") as f:
    f.write(js_script)

print(
    "You can now host it! I recommend using a reverse proxy like nginx or apache but if you're lazy just use simple flask server that I made (app.py)."
    "\nAlso if you gonna made your own server make sure it serve at root and make static files accessible!"
    "\nCommon issues:"
    "\n- The status page WON'T WORK if the status page is on https and the lavalink port is in http unless both have http or https or lavalink port has https but status page has http"
)

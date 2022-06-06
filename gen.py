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

html = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Lavalink by timelessnesses</title>
    <link rel="stylesheet" href="./index.css" />
    <script defer src="./index.js"></script>
    <script defer src="./particles.js"></script>
    <script defer src="./app.js"></script>
  </head>
  <body>
    <div id="bg"></div>
    <div id="particles-js"></div>
    <h1>Lavalink by replacemename</h1>
    <div id="status">Processing</div>
    <div id="info">Processing</div>
  </body>
</html>

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

name = input("What's your name?: ")
hyperlink = input("Do you want hyperlink in your name? (y/n): ")
if hyperlink.lower() == "y":
    hyperlink = input("What's your hyperlink?: ")
    name = f"<a href='{hyperlink}'>{name}</a>"
html = html.replace("replacemename", name)
with open("index.html", "w") as f:
    f.write(html)

print(
    "You can now host it! I recommend using a reverse proxy like nginx or apache but if you're lazy just use simple flask server that I made (app.py)."
    "\nAlso if you gonna made your own server make sure it serve at root and make static files accessible!"
    "\nCommon issues:"
    "\n- The status page WON'T WORK if the status page is on https and the lavalink port is in http unless both have http or https or lavalink port has https but status page has http"
)

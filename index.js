
const status_dom = document.getElementById('status');

let status_ = false;

if (!status_dom) {
    throw new Error("DOM element with id 'status' not found");
};

async function getStatus(){
    try{
        let response = await fetch(`http://deez:a`);
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
        info.innerHTML = `Address: deez<br>Port: a<br>Password: b`;
    }
    else{
        const info = document.getElementById('info');
        info.innerHTML = 'Server currently offline or unreachable.';
    }
}

getStatus();
setInterval(getStatus, 2000);

function switchTheme(){
    if(document.body.className == "light"){
        document.body.className = "dark";
    }
    else{
        document.body.className = "light";
    }
}

function fileServer() {
    navigate("files.html");
}

function initTheme(){
    let time = new Date().getHours();
    if(time > 6 && time < 19){
        document.body.className = "light";
    }
    else{
        document.body.className = "dark";
    }
}

function navigate(page){
    let url = "/static/view/" + page;

    fetch(url,{
        method:"GET"
    }).then((res)=>{
        res.text().then((html)=>{
            document.querySelector("#container").innerHTML = html;
        })
    });
}

function init(){
    initTheme();
    navigate("home.html");
}

init();
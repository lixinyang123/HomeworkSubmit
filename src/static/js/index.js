// 切换主题
function switchTheme(){
    if(document.body.className == "light"){
        document.body.className = "dark";
    }
    else{
        document.body.className = "light";
    }
}

// 初始化主题
function initTheme(){
    let time = new Date().getHours();
    if(time > 6 && time < 19){
        document.body.className = "light";
    }
    else{
        document.body.className = "dark";
    }
}

// 页内导航
function navigate(page){
    let url = "/static/view/" + page;

    fetch(url,{
        method:"GET"
    }).then((res)=>{
        res.text().then((html)=>{
            document.querySelector("#container").innerHTML = html;
            
            if(page == "files.html") {
                document.querySelector("iframe").height = window.innerHeight - 220;
            }
        })
    });
}

function init(){
    initTheme();
    navigate("home.html");
}

init();
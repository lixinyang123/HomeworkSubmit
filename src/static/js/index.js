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
function navigation(name){
    let url = "/static/view/" + name + ".html";

    fetch(url,{
        method:"GET"
    }).then((res)=>{
        res.text().then((html)=>{
            document.querySelector("#main").innerHTML = html;
            inject();
            url = "#"+name;
            history.pushState({page: name},name,url);
        })
    });
}

function inject(){
    document.querySelectorAll("#main > script").forEach(element => {
        let src = element.getAttribute("src");
        request(src,(data) => {
            if(data==undefined){
                console.log("inject error");
            }
        });
    });
}

function init(){
    initTheme();

    window.onpopstate = (e)=>{
        navigation(e.state.page);
    }

    let href = window.location.href;
    if(href.includes("#")){
        let page = href.substring(href.indexOf("#")+1);
        navigation(page);
    }
    else{
        navigation("home");
    }
}

init();
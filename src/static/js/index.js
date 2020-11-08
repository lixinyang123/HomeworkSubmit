function request(href,callback){
    fetch(href,{
        method:"GET"
    }).then((res)=>{
        res.text().then((data)=>{
            callback(data);
        })
    });
}

// 页内导航
function navigation(name){
    let url = "/static/view/" + name + ".html";

    request(url,(html)=>{
        document.querySelector("#main").innerHTML = html;
        inject();
        url = "#"+name;
        history.pushState({page: name},name,url);
    });
}

// 注入页内脚本
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
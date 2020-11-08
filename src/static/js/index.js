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

initTheme();
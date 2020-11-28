function getUndoList(subject,callback) {

    let url = "/undolist?subject=" + subject;

    fetch(url,{
        method:"GET"
    }).then((res)=>{
        res.text().then((data)=>{
            callback(JSON.parse(data))
        });
    });
}

function showData(students,id){
    students.forEach((student) => {
        let html = `
            <tr>
                <td>${student.id}</td>
                <td>${student.name}</td>
            </tr>
        `;
        document.getElementById(id).innerHTML += html;
    });
}

getUndoList("HTML",(data)=>{
    showData(data,"undoHtml");
});

getUndoList("SQL",(data)=>{
    showData(data,"undoSql");
});

getUndoList("Python",(data)=>{
    showData(data,"undoPython");
});
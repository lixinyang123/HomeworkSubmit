
function getUndoList(subject) {

    let url = "/undolist" + subject;

    fetch(url,{
        method:"GET"
    }).then((res)=>{
        res.text().then((data)=>{
            console.log(data)
        });
    });
}

function showData(students){

    students.forEach((student) => {
        let html = `
            <tr>
                <td>${student.id}</td>
                <td>${student.name}</td>
            </tr>
        `;

        document.querySelector("#list").innerHTML += html;
    });
}

getUndoList()
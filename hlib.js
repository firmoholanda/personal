// this is my personal library



// counts total itens in one array
function totalItemsInArray(item, arr) {
    var count = 0;
    for(var i = 0; i < arr.length; ++i){
        if(arr[i] == item)
            count++;
    }
    return count;
}
//---------------------------------------------------------------------------------------

//consoleLogToDOM("container", "div")
function consoleLogToDOM(classID, domTag) {
    consoleLogToDOM("container", "div");
    console.log = function(message) {$('#container').append('<p>' + message + '</p>');};
    console.error = console.debug = console.info =  console.log
}
//---------------------------------------------------------------------------------------

function showHideElementDOM(classID) {
    var x = document.getElementById(classID);
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
}
  //---------------------------------------------------------------------------------------
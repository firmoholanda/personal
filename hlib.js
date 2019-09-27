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
    // Overriding console object
    let console = {};

    // Getting div to insert logs
    let logger = document.getElementById(lassID);

    // Adding log method from our console object
    console.log = text =>
    {
        let element = document.createElement(domTag);
        let txt = document.createTextNode(text);

        //logger.textContent = "";

        element.appendChild(txt);
        logger.appendChild(element);
    }
}
//---------------------------------------------------------------------------------------
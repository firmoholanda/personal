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

// Overriding console object
let console = {};

// Getting div to insert logs
let logger = document.getElementById("container");

// Adding log method from our console object
console.log = text =>
{
    let element = document.createElement("div");
    let txt = document.createTextNode(text);

    logger.empty();

    element.appendChild(txt);
    logger.appendChild(element);
}
//---------------------------------------------------------------------------------------
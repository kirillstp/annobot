const KEYREF = {37:"left", 38:"up", 39:"right", 40:"down"}

function changeImage(direction, state) {
    var img = document.getElementById(direction)
    img.src = "../static/assets/arrow_"+direction+"_"+state+".png"
    return false
}

document.onkeydown = function(event){
    var state = "on"
    console.log(event)
    if (event && Object.keys(KEYREF).indexOf(String(event.keyCode))>=0) {
        changeImage(KEYREF[event.keyCode], state)
    }
}

document.onkeyup = function(event){
    var state = "off"
    if (event && Object.keys(KEYREF).indexOf(String(event.keyCode))>=0) {
        changeImage(KEYREF[event.keyCode], state)
    }
}
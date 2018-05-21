const KEYREF = {37:"left", 38:"up", 39:"right", 40:"down"}
const ACTIONREF = { 37: "/drivetrain/turn_left",
                    38: "/drivetrain/forward",
                    39: "/drivetrain/turn_right",
                    40: "/drivetrain/backward",
                    0:  "/drivetrain/stop" }

var actionList = []
var host = ''//location.hostname

function changeImage(direction, state) {
    var img = document.getElementById(direction)
    img.src = "../static/assets/arrow_"+direction+"_"+state+".png"
    return false
}

document.onkeydown = function(event){
    var state = "on"
    if (event && Object.keys(KEYREF).indexOf(String(event.keyCode))>=0) {
        if (actionList[actionList.length-1] != event.keyCode){
            actionList.push(event.keyCode)
            httpGetAsync(host+ACTIONREF[event.keyCode], 
                function(response) { 
                    changeImage(KEYREF[event.keyCode], state)
                }
            )
        }
    }
}

document.onkeyup = function(event){
    var state = "off"
    if (event && Object.keys(KEYREF).indexOf(String(event.keyCode))>=0) {
        let idx = actionList.indexOf(event.keyCode)
        changeImage(KEYREF[event.keyCode], state)
        // check if there is any other buttons are pressed atm
        if (idx > -1) {
            actionList.splice(idx, 1)
        }
        // send action for the latest button pressed or stop if no buttons pressed
        var next = 0
        if (actionList.length > 0) {
            next = actionList[actionList.length - 1]
        }
        httpGetAsync(host+ACTIONREF[next], 
            function(response) {}
        )
    }
}

function httpGetAsync(url, callback) {
    var xmlHttp = new XMLHttpRequest();
    console.log(url)
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            callback()
        }
    }
    xmlHttp.open("GET", url, true)
    xmlHttp.send(null)
}
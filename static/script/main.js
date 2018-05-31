
const IMAGEREF = {"left":"../static/assets/arrow_left_",
                  "up":"../static/assets/arrow_up_",
                  "down":"../static/assets/arrow_down_",
                  "right":"../static/assets/arrow_right_",
                  "headlights":"../static/assets/headlights_"}
const KEYREF = {37:"left", 38:"up", 39:"right", 40:"down", 49:"headlights"}
const ACTIONREF = { 37: "/drivetrain/turn_left",
                    38: "/drivetrain/forward",
                    39: "/drivetrain/turn_right",
                    40: "/drivetrain/backward",
                    49: "/headlights/toggle",
                    0:  "/drivetrain/stop" }
const TOGGLE = [49]

var actionList = []
var host = ''//location.hostname

function changeImage(keyref, state) {
    var img = document.getElementById(keyref)
    img.src = IMAGEREF[keyref]+state+".png"
    return false
}

document.onkeydown = function(event){
    var state = "on"
    if (event && Object.keys(KEYREF).indexOf(String(event.keyCode))>=0) {
        if (actionList[actionList.length-1] != event.keyCode){
            if (TOGGLE.indexOf(event.keyCode) < 0) {
                actionList.push(event.keyCode)
            }
            httpGetAsync(host+ACTIONREF[event.keyCode], 
                function(response) {
                    if (response != undefined) {
                        try {
                            let r = JSON.parse(response)
                            if (r['state'] != undefined) {
                                state = r['state'].toLowerCase();
                            }
                        }
                        catch(e) {
                            console.log(e)
                        }
                    }
                    changeImage(KEYREF[event.keyCode], state);
                }
            )
        }
    }
}

document.onkeyup = function(event){
    var state = "off"
    if (event && Object.keys(KEYREF).indexOf(String(event.keyCode))>=0 && TOGGLE.indexOf(event.keyCode) < 0) {
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
    // console.log(url)
    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200) {
            callback(xmlHttp.response)
        }
    }
    xmlHttp.open("GET", url, true)
    xmlHttp.send(null)
}

function simulateKeyPress(key){
    var evt = new KeyboardEvent('keydown', {bubbles : true})
    Object.defineProperty(evt, 'keyCode', {
        get:function(){
            return this.keyCodeVal;
        }}); 
    evt.keyCodeVal = key;
    document.body.dispatchEvent(evt);
}
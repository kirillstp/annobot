
const IMAGEREF = {"left":"../static/assets/arrow_left_",
                  "forward":"../static/assets/arrow_forward_",
                  "backward":"../static/assets/arrow_backward_",
                  "right":"../static/assets/arrow_right_",
                  "headlights":"../static/assets/headlights_",
                  "Final":"../static/assets/Final_",
                  "cat1":"../static/assets/cat1_",
                  "cat2":"../static/assets/cat2_",
                  "rotate_left":"../static/assets/rotate_left_",
                  "rotate_right":"../static/assets/rotate_right_",
                  "down":"../static/assets/down_",
                  "up":"../static/assets/up_"}
const KEYREF = {37:"left", 38:"forward", 39:"right", 40:"backward", 49:"headlights", 50:"Final",
                51:"cat1", 52:"cat2",
                53:"tv_power", 54:"tv_mute", 55:"tv_volup", 188:"rotate_left", 190: "rotate_right",
                191: "down", 222: "up"}

const ACTIONREF = { 37: "/drivetrain/turn_left",
                    38: "/drivetrain/forward",
                    39: "/drivetrain/turn_right",
                    40: "/drivetrain/backward",
                    49: "/headlights/toggle",
                    50: "/speaker/toggle?title=Final.mp3",
                    51: "/speaker/toggle?title=cat1.mp3",
                    52: "/speaker/toggle?title=cat2.mp3",
                    53: "/tv_remote/press?button=KEY_POWER",
                    54: "/tv_remote/press?button=KEY_MUTE",
                    55: "/tv_remote/press?button=KEY_VOLUMEUP",
                    188: "/platform/rotate_left",
                    190: "/platform/rotate_right",
                    191: "/platform/down",
                    222: "/platform/up",
                    0:  "/stop" }
const TOGGLE = [49,50,51,52]

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

function simpleButton(key) {
    if (Object.keys(KEYREF).indexOf(String(key))>=0) {
        httpGetAsync(host+ACTIONREF[key], 
            function(response) {}
        )
    }
}
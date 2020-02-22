function xd() {
    console.log("HELLO")
}

function turn_on() {
    console.log("turn_on")
    var request = new XMLHttpRequest()
    a = request.open('GET', '/api/prussia/turn_on', true)
    request.send()
    console.log(a)
}
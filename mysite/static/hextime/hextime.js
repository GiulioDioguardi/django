function startTime() {
    var today = new Date();
    var h = dec2bin(today.getHours());
    var m = dec2bin(today.getMinutes());
    var s = dec2bin(today.getSeconds());
    document.getElementById('txt').innerHTML =
    zeroFill(h, 5) + " : " + zeroFill(m, 6) + " : " + zeroFill(s, 6);
    var t = setTimeout(startTime, 500);
}

window.onload = function() {
    startTime()
}

function startTime() {
    var today = new Date();
    var h = dec2bin(today.getHours());
    var m = dec2bin(today.getMinutes());
    var s = dec2bin(today.getSeconds());
    var m_s = zeroFill(m, 6) + zeroFill(s, 6);
    var m_s_hex = zeroFill(parseInt(m_s, 2).toString(16).toUpperCase(), 3)
    document.getElementById('txt').innerHTML =
    zeroFill(h, 5) + " : " + m_s_hex;
    var t = setTimeout(startTime, 500);
}

window.onload = function() {
    startTime()
}

function startTime() {
    var today = new Date();
    var h = dec2bin(today.getHours());
    var m = dec2bin(today.getMinutes());
    var s = dec2bin(today.getSeconds());
    document.getElementById('txt').innerHTML =
    zeroFill(h, 5) + " : " + zeroFill(m, 6) + " : " + zeroFill(s, 6);
    var t = setTimeout(startTime, 500);
}

function zeroFill(number, width) {
    width -= number.toString().length;
    if (width > 0) {
        return new Array(width + (/\./.test(number) ? 2 : 1)).join('0') + number;
    }
    return number + "";
}

function dec2bin(dec) {
    return (dec >>> 0).toString(2);
}

window.onload = function() {
    startTime()
}

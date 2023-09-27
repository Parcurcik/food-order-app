var now = new Date();
now.setHours(now.getHours() + 1);
var year = now.getFullYear();
var month = String(now.getMonth() + 1).padStart(2, '0');
var day = String(now.getDate()).padStart(2, '0');
var hours = String(now.getHours()).padStart(2, '0');
var minutes = String(now.getMinutes()).padStart(2, '0');

var currentDatetime = year + '-' + month + '-' + day + 'T' + hours + ':' + minutes;
document.getElementById("datetime").setAttribute("min", currentDatetime);
document.getElementById("datetime").setAttribute("max", "2024-01-01T00:00");


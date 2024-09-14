function getWeather(){
  var city = document.getElementById("city");
  window.location.href = "http://127.0.0.1:8000/"+city.value;
}

function getLastDay(){
  var city = document.getElementById("lastOneDay");
  window.location.href = "http://127.0.0.1:8000/oneDay/"+city.value;
}

function getHours(){
  
  var text = document.getElementById("hours").value;

  var city = text.split(' ')[0];
  var hour = text.split(' ')[1];

  window.location.href = "http://127.0.0.1:8000/hours/"+city+"/"+hour;
}
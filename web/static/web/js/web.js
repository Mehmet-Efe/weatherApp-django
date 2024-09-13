function getWeather(){
  var city = document.getElementById("city")
  window.location.href = "http://127.0.0.1:8000/"+city.value
}
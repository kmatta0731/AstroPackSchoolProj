const form = document.querySelector('.generator-form'); // the generator form on the home page
let weatherOutput = document.getElementById('weather-message'); // the div where the weather gets printed on home page

function kelvinToFahrenheit(kelvin) { // function that converts JSON Kelvin data to Fahrenheit
  return Math.round((kelvin - 273.15) * 9/5 + 32);
}

function autocompleteCallback() {   // callback function for the Google API
    let destinationInput = document.getElementById('destination');  // destination field for generator form - using Google Maps Place Autocomplete API
    let autocomplete = new google.maps.places.Autocomplete(destinationInput);   

    form.addEventListener('submit', (event) => {  // once user submits form..
        event.preventDefault();
        weatherOutput.innerHTML = ("Loading...");

        const destination = form.destination.value;
        const checkin = form.checkin.value;
        const checkout = form.checkout.value;

        let place = autocomplete.getPlace();
        let latitude = place.geometry.location.lat(); // get latitude and longitude info to plug into the weather API
        let longitude = place.geometry.location.lng();
    
        console.log("Latitude: " + latitude);
        console.log("Longitude: " + longitude);

        const API_KEY = '0f11bb0d33b9d0f6bf4b9a154297873a';
        const API_URL = `https://api.openweathermap.org/data/3.0/onecall?lat=${latitude}&lon=${longitude}&exclude={part}&appid=${API_KEY}`;

        fetch(API_URL) // fetches data from OpenWeatherMap API
          .then(response => response.json())
          .then(data => {
            console.log(data);

            let temp = data.current.temp;
            temp = kelvinToFahrenheit(temp);
            let weather = data.current.weather[0].description;
            // weatherOutput.innerHTML= ("Current temp: " + temp + " degrees" + "<br>" + " Weather: " + weather);          

            temp_range = checkWeatherRange(temp);
            console.log("JAVASCRIPT TEMP: " + checkWeatherRange(temp));
            process_data(temp, destination);  // call function to send over data to the backend
          })
          .catch(error => {
            console.error(error);
          });

        console.log('Destination: ', destination);
        console.log('Check-in: ', checkin);
        console.log('Check-out: ', checkout);
    });
    // let currentUnixTimestap = ~~(+new Date() / 1000);
}

// send a request to the backend server to send data like temp, destination, travel dates, etc.
let csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
function process_data(temp, destination) {
  let activities = [];
  document.querySelectorAll('input[name="activities"]:checked').forEach(function(activity) {
    activities.push(activity.value);
    console.log(activity.value);
  });
  console.log(activities);

  let formdata = new FormData();
  formdata.append('temp', temp);
  formdata.append('destination', destination);
  formdata.append('occasion', form.occasion.value);
  formdata.append('trip_start_date', form.checkin.value);
  formdata.append('trip_end_date', form.checkout.value);
  formdata.append('gender', form.gender.value);
  formdata.append('temp_range', temp_range);
  activities.forEach(function(activity) {
    formdata.append('activities', activity);
  });

  let csrf_token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

  $.ajax({
    url: '/process_data/',  // URL for the Django view
    type: 'POST',  // HTTP method for the request
    data: formdata,  // data to be sent with the request
    headers: {'X-CSRFToken': csrf_token},  // include the CSRF token with the data sent
    processData: false,  // prevent jQuery from processing the data
    contentType: false,  // prevent jQuery from setting the content type
    success: function (response) {  // callback function for successful request
      console.log("Success :)");
      window.location.href = "items";
    },
    error: function (xhr, status, error) {  // callback function for failed request
      console.error(error);
    }
  });
}

function checkWeatherRange(temp) {
  if (temp < 50) {
    temp_range = 1;
  }
  else if (temp > 50 && temp < 80) {
    temp_range = 2;
  }
  else {
    temp_range = 3;
  }

  console.log("JAVASCRIPT TEMP: " + temp_range);
  return temp_range;
}
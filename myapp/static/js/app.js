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
            weatherOutput.innerHTML= ("Current temp: " + temp + " degrees" + "<br>" + " Weather: " + weather);          

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
  $.ajax({
    url: '/process_data/',  // URL for the Django view
    type: 'POST',  // HTTP method for the request
    data: {
      temp: temp, 
      destination: destination,
      occasion: form.occasion.value,
      trip_start_date: form.checkin.value,
      trip_end_date: form.checkout.value,
      gender: form.gender.value
    },  // data to be sent with the request
    headers: {'X-CSRFToken': csrf_token},  // include the CSRF token with the data sent
    success: function (response) {  // callback function for successful request
      console.log("Hi from the backend :)");
    },
    error: function (xhr, status, error) {  // callback function for failed request
      console.error(error);
    }
  });
}

// scroll to the generator form when user clicks "Get Started" button on home page
function scrollToForm() {
    document.querySelector('.bottom-container').scrollIntoView({ 
        behavior: 'smooth'
    });
}
const form = document.querySelector('.generator-form');
var errorMessageOutput = document.getElementById('error-message');

function kelvinToFahrenheit(kelvin) {
  return Math.round((kelvin - 273.15) * 9/5 + 32);
}

function initAutocomplete() {   // Callback function for the Google API
    // destination field for generator form - using Google Maps Place Autocomplete API
    
    var destinationInput = document.getElementById('destination');
    var autocomplete = new google.maps.places.Autocomplete(destinationInput);   

    form.addEventListener('submit', (event) => {
        event.preventDefault();
        errorMessageOutput.innerHTML = ("Loading...");

        const destination = form.destination.value;
        const checkin = form.checkin.value;
        const checkout = form.checkout.value;

        var place = autocomplete.getPlace();
        var latitude = place.geometry.location.lat();
        var longitude = place.geometry.location.lng();
    
        console.log("Latitude: " + latitude);
        console.log("Longitude: " + longitude);

        const API_KEY = '0f11bb0d33b9d0f6bf4b9a154297873a';
        const API_ENDPOINT = `https://api.openweathermap.org/data/3.0/onecall?lat=${latitude}&lon=${longitude}&exclude={part}&appid=${API_KEY}`;

        fetch(API_ENDPOINT)
          .then(response => response.json())
          .then(data => {
            console.log(data);

            let temp = data.current.temp;
            let weather = data.current.weather[0].description;

            errorMessageOutput.innerHTML= ("Current temp: " + kelvinToFahrenheit(temp) + " degrees" + "<br>" + " Weather: " + weather);          
            process_temp(temp);

            // Use the data to display the weather information for the destination
          })
          .catch(error => {
            console.error(error);
          });
    
        console.log('Destination: ', destination);
        console.log('Check-in: ', checkin);
        console.log('Check-out: ', checkout);
    });
    // var currentUnixTimestap = ~~(+new Date() / 1000);
}

function process_temp(temp) {
  $.ajax({
    url: 'process_temp/',
    type: 'post',
    data: {temp: temp},
    dataType: "json",
    success: function (response) {
    }
});
}

// Scroll to the generator form when user clicks "Get Started" button on home page
function scrollToForm() {
    document.querySelector('.bottom-container').scrollIntoView({ 
        behavior: 'smooth'
    });
}
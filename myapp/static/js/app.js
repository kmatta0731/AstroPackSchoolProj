const form = document.querySelector('.generator-form');

function initAutocomplete() {   // Callback function for the Google API
    // destination field for generator form - using Google Maps Place Autocomplete API
    var destinationInput = document.getElementById('destination');
    var autocomplete = new google.maps.places.Autocomplete(destinationInput);   

    form.addEventListener('submit', (event) => {
        event.preventDefault();
    
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

// Scroll to the generator form when user clicks "Get Started" button on home page
function scrollToForm() {
    document.querySelector('.bottom-container').scrollIntoView({ 
        behavior: 'smooth'
    });
}
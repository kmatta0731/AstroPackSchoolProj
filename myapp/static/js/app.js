// destination field for generator form - using Google Maps Place Autocomplete API
var destinationInput = document.getElementById("destination");
var autocomplete = new google.maps.places.Autocomplete(destinationInput);    


// scrolls to the generator form when user clicks "Get Started" button on home page
function scrollToForm() {
    document.querySelector('.form-container').scrollIntoView({ 
        behavior: 'smooth'
    });
}
// Send form to Flask
var form = document.querySelector("form");
// I manage the event "submit" the form
form.addEventListener("submit", function(e) {
    // To don't reload the web page after the submit
    e.preventDefault();
    var data = new FormData(form);
    // AJAX post to Flask view "/index/"
    ajaxPost("http://localhost:5000/results/", data, function(response) {
        // I convert the JSON from Flask in javascript object
        response = JSON.parse(response)
        var pElt = document.getElementById("text");
        pElt.innerHTML = "";
        // The text
        pElt.textContent = response.wikipedia;
        document.getElementById("wikipedia").style.display = 'block';

        var urlGoogleMapsApi = "https://www.google.com/maps/embed/v1/place?key=AIzaSyAOcEnqP9jbC1eApGVZ6iYHtD4jNdXrFco&q=place_id:";
        // I use the place_id from Flask JSON
        var googleMapsRequest = urlGoogleMapsApi + response.maps;
        var iframeElt = document.getElementById("map");
        iframeElt.src = googleMapsRequest;
        document.getElementById("googlemaps").style.display = 'block';
    });
});

// Send form to Flask
var form = document.querySelector("form");
// I manage the event "submit" the form
form.addEventListener("submit", function(e) {
    // To don't reload the web page after the submit
    e.preventDefault();
    var data = new FormData(form);
    // AJAX post to Flask view "/index/"
    ajaxPost("http://localhost:5000/results/", data, function(response) {
        document.getElementById("presentation").style.display = 'none';
        // I convert the JSON from Flask in javascript object
        // This Json contain the text from wikipedia and the place_id from gogle maps
        response = JSON.parse(response)
        var pElt = document.getElementById("text");
        pElt.innerHTML = "";
        // The text from the Flask
        pElt.textContent = response.wikipedia;
        document.getElementById("wikipedia").style.display = 'block';

        var urlGoogleMapsApi = "https://www.google.com/maps/embed/v1/place";
        // I use the place_id from Flask JSON
        if (response.place_id !== "null") {
            var googleMapsRequest = urlGoogleMapsApi + "?key=" + response.google_key + "&q=place_id:" + response.place_id;
            var iframeElt = document.getElementById("map");
            iframeElt.src = googleMapsRequest;
            document.getElementById("googlemaps").style.display = 'block';
            document.getElementById("map").style.display = 'block';
            document.getElementById("mapError").style.display = 'none';
        } else {
            document.getElementById("googlemaps").style.display = 'block';
            document.getElementById("mapError").style.display = 'block';
            document.getElementById("map").style.display = 'none';
            var pElt = document.getElementById("mapError");
            pElt.textContent = "Oups ! Je n'arrive pas à mettre le doigt sur l'adresse. Peux-tu être un peu plus précis ? Par exemple tu pourrais m'indiquer la ville où se trouve ce que tu cherches.";
        }
    });
});

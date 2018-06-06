// Send form to Flask
var form = document.querySelector("form");
// I manage the event "submit" the form
form.addEventListener("submit", function(e) {
    // To don't reload the web page after the submit
    e.preventDefault();
    var data = new FormData(form);

    document.getElementById("presentation").style.display = 'none';

    var responseElt = document.getElementById("response");
    var resultElt = document.createElement("div");
    document.getElementById("response").insertAdjacentElement("afterBegin", resultElt);

    // I display the request of the user
    var userElt = document.createElement("div");
    userElt.classList.add("row");
    resultElt.appendChild(userElt);

    var textUserElt = document.createElement("p");
    textUserElt.classList.add("col-md-6", "alert", "alert-success", "mt-3");
    textUserElt.textContent = data.get('request');
    userElt.appendChild(textUserElt);

    // AJAX post to Flask view "/index/"
    ajaxPost("http://localhost:5000/results/", data, function(response) {
        document.getElementById("presentation").style.display = 'none';
        // I convert the JSON from Flask in javascript object
        // This Json contain the text from wikipedia and the place_id from gogle maps
        response = JSON.parse(response)

        var urlGoogleMapsApi = "https://www.google.com/maps/embed/v1/place";
        // I use the place_id from Flask JSON
        if (response.place_id !== "null") {
            // If the place_id != "null", i use it to display a map
            var googleMapsRequest = urlGoogleMapsApi + "?key=" + response.google_key + "&q=place_id:" + response.place_id;

            // I display the response of Grand PY bot
            var papiElt = document.createElement("div");
            papiElt.classList.add("row");
            resultElt.appendChild(papiElt);

            var divPapiElt = document.createElement("div");
            divPapiElt.classList.add("col-md-7", "offset-md-5");
            papiElt.appendChild(divPapiElt);

            var textPapiElt = document.createElement("p");
            textPapiElt.classList.add("text-right", "alert", "alert-primary");
            textPapiElt.textContent = response.wikipedia;
            divPapiElt.appendChild(textPapiElt);

            // I display the map
            var mapElt = document.createElement("div");
            mapElt.classList.add("row");
            resultElt.appendChild(mapElt);

            var iframeMapiElt = document.createElement("iframe");
            iframeMapiElt.classList.add("col-md-7", "offset-md-5");
            iframeMapiElt.src = googleMapsRequest;
            iframeMapiElt.height="300";
            iframeMapiElt.frameborder="0";
            iframeMapiElt.style="border:0";
            iframeMapiElt.allowfullscreen=true;
            mapElt.appendChild(iframeMapiElt);

        } else {
            // I display the response error of Grand PY bot
            var papiElt = document.createElement("div");
            papiElt.classList.add("row");
            resultElt.appendChild(papiElt);

            var divPapiElt = document.createElement("div");
            divPapiElt.classList.add("col-md-7", "offset-md-5");
            papiElt.appendChild(divPapiElt);

            var textPapiElt = document.createElement("p");
            textPapiElt.classList.add("text-right", "alert", "alert-warning");
            textPapiElt.textContent = response.wikipedia;
            divPapiElt.appendChild(textPapiElt);
        }
    });
});

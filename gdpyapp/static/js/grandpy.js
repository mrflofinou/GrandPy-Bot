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
    ajaxPost("https://super-grandpy-bot.herokuapp.com/results/", data, function(response) {
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
            textPapiElt.appendChild(document.createTextNode(response.gdpy_adress))
            textPapiElt.appendChild(document.createElement("br"))
            textPapiElt.appendChild(document.createTextNode(response.adress))
            divPapiElt.appendChild(textPapiElt);

            // I display the text from wikipedia
            var wikiElt = document.createElement("div");
            wikiElt.classList.add("row");
            resultElt.appendChild(wikiElt);

            var divWikiElt = document.createElement("div");
            divWikiElt.classList.add("col-md-7", "offset-md-5");
            wikiElt.appendChild(divWikiElt);

            var textWikiElt = document.createElement("p");
            textWikiElt.classList.add("text-right", "alert", "alert-primary");
            textWikiElt.appendChild(document.createTextNode(response.gdpy_story))
            textWikiElt.appendChild(document.createElement("br"))
            textWikiElt.appendChild(document.createElement("br"))
            textWikiElt.appendChild(document.createTextNode(response.gdpy_knowledge))
            // divWikiElt.appendChild(textWikiElt);

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
            // mapElt.appendChild(iframeMapiElt);

            setTimeout(function () {
                divWikiElt.appendChild(textWikiElt);
                mapElt.appendChild(iframeMapiElt);
            }, 1500);

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
            textPapiElt.textContent = response.gdpy_knowledge;
            divPapiElt.appendChild(textPapiElt);
        }
    });
});

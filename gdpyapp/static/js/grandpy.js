// Send form to Flask
var form = document.querySelector("form");
form.addEventListener("submit", function(e) {
    e.preventDefault();
    var data = new FormData(form);
    ajaxPost("http://localhost:5000/index/", data, function(response) {
        var divElt = document.createElement("div");
        divElt.id = "response";
        divElt.textContent = response;
        var parentElt = form.parentNode;
        parentElt.replaceChild(divElt, form);
    });
});

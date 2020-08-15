// trigger submit when user type in search field & press enter
var searchTerms = document.getElementById("searchTerms");
input.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
   event.preventDefault();
   document.getElementById("searchEnt").click();
  }
});
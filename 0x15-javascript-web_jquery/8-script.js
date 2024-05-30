$(document).ready(function () {
  // code must be executed when the document is ready and fully loaded
  $.get(
    "https://swapi-api.alx-tools.com/api/people/5/?format=json",
    function (data) {
      $.each(data.results, function (index, movie) {
        $("UL#list_movies").append("<li>" + movie.title + "</li>");
      });
    }
  );
});

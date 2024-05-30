$(document).ready(function () {
  // code must be executed when the document is ready and fully loaded
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data) {
    $('#character').text(data.name);
  });
});

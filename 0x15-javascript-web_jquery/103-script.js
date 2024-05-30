$(document).ready(function () {
  // code must be executed when the document is ready and fully loaded
  const languageCode = $("INPUT#language_code").val();
  function fetchTranslation() {
    $.get(
      "https://www.fourtonfish.com/hellosalut/hello/?lang=" + languageCode,
      function (data) {
        $("DIV#hello").text(data.hello);
      }
    );
  }

  $("#btn_translate").click(fetchTranslation);
  $("#language_code").keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});

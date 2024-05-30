$(document).ready(function () {
  // code must be executed when the document is ready and fully loaded
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    $.get(
      'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode,
      function (data) {
        $('DIV#hello').text(data.hello);
      }
    );
  });
});

$(document).ready(function () {
  // code must be executed when the document is ready and fully loaded
  $("DIV#add_item").click(function () {
    $("UL.my_list").append("<li>Item</li>");
  });
});

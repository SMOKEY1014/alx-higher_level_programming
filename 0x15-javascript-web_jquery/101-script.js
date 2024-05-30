$(document).ready(function () {
  // code must be executed when the document is ready and fully loaded
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('UL.my_list li:last-child').remove();
  });
  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});

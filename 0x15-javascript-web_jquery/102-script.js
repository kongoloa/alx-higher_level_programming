document.addEventListener('DOMContentLoaded', function () {
  $('INPUT#btn_translate').click(function () {
    $.get('https://fourtonfish.com/hellosalut/hello/' +
$('INPUT#language_code').val(), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});

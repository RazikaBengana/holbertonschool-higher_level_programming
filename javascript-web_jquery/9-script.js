const $ = window.jQuery;

$(document).ready(function () {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});

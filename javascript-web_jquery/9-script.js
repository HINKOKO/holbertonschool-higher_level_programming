#!/usr/bin/node
$('document').ready(function () {
  $.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').html(data.hello);
  });
});

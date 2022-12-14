#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function (html) {
  $('DIV#character').text(html.name);
});

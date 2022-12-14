#!/usr/bin/node
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  // console.log(data.results);
  $.each(data.results, function (_i, movies) {
    $('UL#list_movies').append('<li>' + movies.title + '</li>');
  });
});

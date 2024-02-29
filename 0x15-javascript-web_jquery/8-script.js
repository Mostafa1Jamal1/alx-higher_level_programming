#!/usr/bin/node
$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data, textStatus) {
  data.results.forEach(film => {
    $('ul#list_movies').append('<li>' + film.title + '</li>');
  });
});

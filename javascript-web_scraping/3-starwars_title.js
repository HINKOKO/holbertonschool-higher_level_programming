#!/usr/bin/node
const request = require('request');
const idi = process.argv[2];
request.get(
  `https://swapi-api.hbtn.io/api/films/${idi}`,
  function (error, response, body) {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).title);
    }
  }
);

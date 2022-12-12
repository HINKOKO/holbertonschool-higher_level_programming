#!/usr/bin/node
const request = require('request');
const requestSettings = {
  method: 'GET',
  url: process.argv[2]
};
request(requestSettings, function (_error, response) {
  console.log(`code: ${response.statusCode}`);
});

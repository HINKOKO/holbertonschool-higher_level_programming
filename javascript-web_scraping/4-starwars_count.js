#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request.get(apiUrl, function (error, _response, body) {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    const res = JSON.parse(body).results;
    // console.log(res);
    for (const items of res) {
      // console.log(items);
      for (const actor of items.characters) {
        //   console.log(actor);
        if (actor.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

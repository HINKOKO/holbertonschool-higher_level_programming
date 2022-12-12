#!/usr/bin/node
const request = require('request');

request.get(process.argv[2], function (error, _response, body) {
  if (error) {
    console.log(error);
  } else {
    const res = JSON.parse(body);
    // console.log(res);
    const workersDict = {};
    for (let i = 0; i < res.length; i++) {
      // console.log(users);
      if (res[i].completed === true) {
        if (workersDict[res[i].userId] === undefined) {
          workersDict[res[i].userId] = 1;
        } else {
          workersDict[res[i].userId]++;
        }
      }
    }
    console.log(workersDict);
  }
});

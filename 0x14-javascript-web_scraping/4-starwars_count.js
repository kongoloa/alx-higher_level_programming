#!/usr/bin/node

const request = require('request');
request(process.argv[2], { json: true }, (err, resp, body) => {
  if (err) {
    console.log(err);
  } else if (body) {
    const results = body.results;
    let count = 0;
    for (const i in results) {
      for (const j in results[i].characters) {
        if (results[i].characters[j].endsWith('/18/')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});

#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

request(movieUrl, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const movieData = JSON.parse(body);
    const characterPromises = movieData.characters.map((characterUrl) => {
      return new Promise((resolve, reject) => {
        request(characterUrl, function (err, res, bd) {
          if (err) {
            reject(new Error(err));
          } else {
            const characterData = JSON.parse(bd);
            resolve(characterData.name);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then((characterNames) => {
        console.log(characterNames.join('\n'));
      })
      .catch((error) => {
        console.error(error.message);
      });
  }
});

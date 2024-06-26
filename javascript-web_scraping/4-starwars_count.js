#!/usr/bin/node
// This script fetches data from a provided Star Wars API URL, parses the JSON response,
// and counts how many times the character with ID '18' appears across all results

const request = require('request');
const starWarsUrl = process.argv[2];
let times = 0;

request(starWarsUrl, function (_err, _res, body) {

  body = JSON.parse(body).results;

  for (let i = 0; i < body.length; ++i) {
    const characters = body[i].characters;

    for (let j = 0; j < characters.length; ++j) {
      const character = characters[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        times += 1;
      }
    }
  }
  console.log(times);
});


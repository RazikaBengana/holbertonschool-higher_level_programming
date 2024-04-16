#!/usr/bin/node
// This script fetches data about a specific Star Wars film using its ID,
// then retrieves and logs names of characters from that film

const request = require('request'); // Include the request module for making HTTP requests
const FILM_URL = `http://swapi.co/api/films/${process.argv[2]}`; // Construct the URL for the film based on an argument passed in terminal
let characters; // Will hold an array of URLs to character resources
const dict = {}; // Dictionary to store character names keyed by their URLs

// Make an HTTP request to the specified film URL
request(FILM_URL, function (error, response, body) {

  if (error) {
    throw new Error(error);
  }

  characters = JSON.parse(body).characters; // Parse the response body and assign character URLs to the 'characters' variable

  // Iterate over each character URL
  for (const url of characters) {
    request(url, (error, response, body) =>
      !error && addData(url, JSON.parse(body).name)); // Request each character's data and add to 'dict' if successful
  }
});


// Function to add character data to 'dict'
function addData (url, name) {

  dict[url] = name; // Add the character's name to 'dict' under their URL

  // Check if all characters have been added to 'dict'
  if (Object.entries(dict).length === characters.length) {
    // Log each character's name
    for (const url of characters) {
      console.log(dict[url]);
    }
  }
}

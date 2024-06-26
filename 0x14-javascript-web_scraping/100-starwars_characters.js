#!/usr/bin/node

const request = require('request');
const filmID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

if (!filmID) {
  console.error('Usage: node 100-starwars_characters.js <filmID>');
  process.exit(1);
}

request(url, (err, responce, body) => {
  if (responce.statusCode !== 200) {
    console.error(
      `Failed to fetching data, Status Code: ${responce.statusCode}`
    );
    return;
  }

  if (err) {
    console.error('Error:', err);
    return;
  }

  try {
    const data = JSON.parse(body);
    const chars = data.characters;

    chars.forEach(async (char) => {
      await request(char, (err, responce, body) => {
        if (responce.statusCode !== 200) {
          console.error(
            `Failed to fetching data, Status Code: ${responce.statusCode}`
          );
          return;
        }

        if (err) {
          console.error('Error:', err);
          return;
        }

        try {
          const data = JSON.parse(body);
          console.log(data.name);
        } catch (error) {
          console.error('Failed to parse responce:', error);
        }
      });
    });
  } catch (error) {
    console.error('Failed to parse responce:', error);
  }
});

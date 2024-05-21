#!/usr/bin/node

const request = require("request");
const url = process.argv[2];

if (!url) {
  console.error("Usage: node 2-statuscode.js <URL>");
  process.exit(1);
}

request(url, (err, responce, body) => {
  if (err) {
    console.error("Error:", err);
    return;
  }
  if (responce.statusCode != 200) {
    console.error(`Failed to fertchdata, Status Code: ${responce.statusCode}`);
    return;
  }
  try {
    const data = JSON.parse(body);
    const films = data.results;
    let count = 0;

    films.forEach((film) => {
      if (
        film.characters.includes(
          `https://swapi-api.alx-tools.com/api/people/18/`
        )
      ) {
        count++;
      }
    });

    console.log(`${count}`);
  } catch (P_err) {
    console.error("Failed to parse responce:", P_err);
  }
});

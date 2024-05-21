#!/usr/bin/node

const request = require("request");
const filmID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

if (!filmID) {
  console.error("Usage: node 3-starwars_title.js <filmID>");
  process.exit(1);
}

request(url, (err, responce, body) => {
  if (responce.statusCode != 200) {
    console.error(`Failed to fertchdata, Status Code: ${responce.statusCode}`);
    return;
  }

  if (err) {
    console.error("Error:", err);
    return;
  }
  try {
    const data = JSON.parse(body);
    console.log(data.title);
  } catch (P_err) {
    console.error("Failed to parse responce:", P_err);
  }
});

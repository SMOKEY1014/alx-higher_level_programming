#!/usr/bin/node

const request = require("request");
const fs = require("fs");
const path = process.argv[3];
const url = process.argv[2];

if (!path || !url) {
  console.error("Usage: node 5-request_store.js <URL> <file-path>");
  process.exit(1);
}

request(url, (err, responce, body) => {
  if (err) {
    console.error("Error:", err);
    return;
  }
  if (responce.statusCode != 200) {
    console.error(
      `Failed to fetching data, Status Code: ${responce.statusCode}`
    );
    return;
  }
  fs.writeFile(path, body, "utf-8", (err) => {
    if (err) {
      console.error("Error writing file :", err);
      return;
    }
  });
});

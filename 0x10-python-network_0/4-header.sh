#!/bin/bash
# A Bash script that sends a GET request with header X-School-User-Id to the URL, and displays the body of the response
curl -sLH "X-School-User-Id: 98" "$1"

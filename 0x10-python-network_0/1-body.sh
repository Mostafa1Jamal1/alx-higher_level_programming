#!/bin/bash
# sends a GET request to the URL, and displays the body of the response of a 200 status code response only
curl -sfL "$1"

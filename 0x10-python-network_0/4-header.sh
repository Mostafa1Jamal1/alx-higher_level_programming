#!/bin/bash
# sends a GET request to the URL, and displays the body of the response with header variable X-School-User-Id: 98
curl -sf -H "X-School-User-Id: 98" "$1"

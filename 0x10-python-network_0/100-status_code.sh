#!/bin/bash
# displays only the status code of the request to a URL passed response.
curl -s -o /dev/null -w '%{response_code}' "$1"

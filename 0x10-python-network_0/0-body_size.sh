#!/bin/bash
# sending a request to an URL with curl + displaying the size of the body of the response
curl -s "$1" | wc -c

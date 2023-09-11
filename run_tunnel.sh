#!/bin/bash

# Check if curl is installed
if ! command -v curl &> /dev/null
then
    echo "curl could not be found"
    exit 1
fi

# Check if npx is installed
if ! command -v npx &> /dev/null
then
    echo "npx could not be found"
    exit 1
fi

# Retrieve the IP address
ip=$(curl -s ipv4.icanhazip.com)

# Exit if the IP address could not be retrieved
if [ -z "$ip" ]
then
    echo "Failed to retrieve IP address"
    exit 1
fi

echo "IP address: $ip"

npx localtunnel --port 8080 
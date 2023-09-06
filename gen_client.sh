#!/bin/bash

SERVER_URL="http://localhost:8080"
CLIENT_PREFIX="chat_rpg"

# Check if openapi-generator-cli command exists
if ! command -v openapi-generator-cli &> /dev/null; then

    # Check if npm command exists
    if ! command -v npm &> /dev/null; then
        echo "npm not found. Please install npm before running this script."
        exit 1
    fi

    echo "openapi-generator-cli not found. Installing..."
    npm install @openapitools/openapi-generator-cli -g
fi

# Check if curl command exists
if ! command -v curl &> /dev/null; then
    echo "curl not found. Please install curl before running this script."
    exit 1
fi

mkdir -p client

# Download openapi.json
if ! curl -o ./client/openapi.json "$SERVER_URL/openapi.json"; then
    echo "Error downloading openapi.json from $SERVER_URL"
    exit 1
fi

openapi-generator-cli generate \
  -g python \
  -i client/openapi.json \
  -o ./client \
  --package-name ${CLIENT_PREFIX}_client \
  --remove-operation-id-prefix \
  --additional-properties=packageName=${CLIENT_PREFIX}_client,projectName=${CLIENT_PREFIX}-client,packageVersion=0.0.1

# Install client
pip install --no-cache-dir -e ./client

#!/bin/bash
set -e

SERVER_URL="http://localhost:8080"
CLIENT_PREFIX="chat_rpg"

# Define colors
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Check if a server URL was provided
if [ $# -eq 1 ]; then
    SERVER_URL=$1
fi

# Check if openapi-generator-cli command exists
if ! command -v openapi-generator-cli &> /dev/null; then

    # Check if npm command exists
    if ! command -v npm &> /dev/null; then
        echo -e "${RED}npm not found. Please install npm before running this script.${NC}"
        exit 1
    fi

    echo -e "${GREEN}openapi-generator-cli not found. Installing...${NC}"
    npm install @openapitools/openapi-generator-cli -g
fi

# Check if curl command exists
if ! command -v curl &> /dev/null; then
    echo -e "${RED}curl not found. Please install curl before running this script.${NC}"
    exit 1
fi

# Remove existing client directory if it exists
if [ -d "client" ]; then
    echo -e "${GREEN}Removing existing client directory...${NC}"
    rm -rf client
fi

echo -e "${GREEN}Creating client directory...${NC}"
mkdir -p client

# Download openapi.json
echo -e "${GREEN}Downloading openapi.json...${NC}"
if ! curl -o ./client/openapi.json "$SERVER_URL/openapi.json"; then
    echo -e "${RED}Error downloading openapi.json from $SERVER_URL${NC}"
    exit 1
fi

echo -e "${GREEN}Generating client code...${NC}"
openapi-generator-cli generate \
  -g python \
  -i client/openapi.json \
  -o ./client \
  --package-name ${CLIENT_PREFIX}_client \
  --additional-properties=packageName=${CLIENT_PREFIX}_client,projectName=${CLIENT_PREFIX}-client,packageVersion=0.0.1

# Install client
echo -e "${GREEN}Installing client...${NC}"
pip install --no-cache-dir -e ./client
#!/bin/bash

# Check if the scale parameter is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <scale>"
  exit 1
fi

# Get the scale value (number of replicas for the app container)
scale=$1

# Scale the 'app' service using Docker Compose
docker-compose up --scale app=$scale -d

echo "App service scaled to $scale replicas."

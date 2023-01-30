#!/bin/sh

# Waits for proxy to be ready before starting certbot

set -e

until nc -z proxy 80; do
    echo "Waiting for proxy to be ready..."
    sleep 5s & wait ${!}
done

echo "Getting certificate..."

certbot certonly \
    --webroot \
    --webroot-path "/vol/www/" \
    -d "$DOMAIN" \
    --email "$EMAIL" \
    --rsa-key-size 4096 \
    --agree-tos \
    --noninteractive

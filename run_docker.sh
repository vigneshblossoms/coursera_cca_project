#!/usr/bin/env bash
docker build -t coursera-demo .
docker run -d -p 5000:5000 coursera-demo:latest
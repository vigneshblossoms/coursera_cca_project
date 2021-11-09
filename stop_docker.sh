#!/usr/bin/env bash
docker rm $(docker stop $(docker ps -a -q --filter ancestor=coursera-demo --format="{{.ID}}"))
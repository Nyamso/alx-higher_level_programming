#!/bin/bash
# Script to dispaly all HTTP methods the server of a given URL will accept.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-

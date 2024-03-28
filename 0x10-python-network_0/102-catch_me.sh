#!/bin/bash
# Catch m3 if you can!
curl -sLX PUT -H "Origin:School" -d "user_id=98" "0.0.0.0:5000/catch_me"

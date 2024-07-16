#!/bin/sh

curl -H 'Authorization: Bearer uzGHMbOhqza0RUuNKwdfKXv2kc714DEJCVzFrDUXIMP' \
https://notify-api.line.me/api/status
# {"status":200,"message":"ok","target":"foobar"}

# $ curl -H 'Authorization: Bearer invalidtoken' \
# https://notify-api.line.me/api/status
# {"status":401,"message":"Invalid access token"}

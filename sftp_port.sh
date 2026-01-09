#!/bin/sh
exec ssh -L9229:127.0.0.1:9229 "$@"

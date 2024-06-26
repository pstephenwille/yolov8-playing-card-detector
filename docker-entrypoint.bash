#!/usr/bin/bash

python3 -m venv venv
source venv/bin/activate

flask run
#tail -f /dev/null

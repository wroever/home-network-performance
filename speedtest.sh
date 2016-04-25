#!/bin/bash

set -u
set -e

output=$(./speedtest-cli-extras/bin/speedtest-csv 2>&1)
./logspdresult.py "${output}"

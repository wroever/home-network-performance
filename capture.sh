#!/bin/bash

set -u
set -e

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

myip=$(ifconfig | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')

starttime=$(date "+%Y.%m.%d-%H.%M.%S")

tshark -w data.${starttime}.pcap -z conv,ip,ip.addr==${myip} &> /dev/null &
shark_pid=$!
echo "Collecting traffic trace..."

function ctrl_c() {
    echo "** SIGINT received, qutting..."
    kill ${shark_pid}
    exit
}

echo "Recording bandwidth usage..."
while [ "true" ]
do
    dtm=$(date "+%Y.%m.%d-%H.%M.%S")
    bw=$(sudo sar -n DEV 1 1 | grep en0 | tail -n 1 | awk '{print $4,","$6}' 2>/dev/null)
    [ -z "${bw}" ] || echo "${dtm},${bw}" >> data.${starttime}.bw.log
    sleep 1
done


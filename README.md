# Netflix and Home Network Performance
#### EECS 495 - Networking Problems in Cloud Computing

Dependencies required for running speedtests are listed in requirements.txt. Run the following to download them (in a virtualenv if you prefer):
> pip install -r requirements.txt

This repo contains the following scripts:
* **capture.sh** - initiates capture of packets sent/recvd by the machine on which it is run, recording traces in files labeled data.<datetime>.pcap. Also records bandwidth consumption by the local machine at 1ms intervals in a file called data.<datetime>.bw.log. Assumes only one network interface is active.
* **speedtest.sh** - performs one speedtest, logging results in a remote postgresql database. Requires that the dependencies listed in requirements.txt and speedtest-cli-extras are installed (see above).

Data from past trials is in the data folder. This currently includes the following tests:
* **4.24** - Conducted over 30 minutes on a residential network (Comcast Extreme 105, advertised at 105Mbps down, 20Mbps up). One machine recording traces and bandwidth consumption (i.e. running capture.sh) and one simultaneously running speedtests at 3 minute intervals (running speedtest.sh via cron). Both connections were wired, connected directly to a gateway. At 10:00 (around 5:10 cst), began streaming Netflix from the machine recording traffic. Continued until approx. 25:00 (around 5:25 cst).

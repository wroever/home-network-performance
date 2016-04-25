#!/usr/bin/env python

"""
    Script to record speedtest results in a log file and remote database
"""

import argparse, csv, psycopg2

def main():

    # Parse args (result string)
    parser = argparse.ArgumentParser(description='speedtest result as csv')
    parser.add_argument('result_str', type=str, nargs=1)
    parseResult = parser.parse_args()
    line = parseResult.result_str[0]
    cols = line.split(';')[:-1] # Drop share url

    # Write to local log
    with open('log.csv', 'a+') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(cols)

    # Store result in database
    try:
        con = psycopg2.connect(dbname='d7dcmmbcl3tk0m', user='jogpyfgiujhfcd', host='ec2-54-83-29-133.compute-1.amazonaws.com', password='XLiYqfeeA0AS-cTYCVfuxGizju')
    except:
        print "I am unable to connect to the database"
        exit(-1)

    cur = con.cursor()

    q = 'INSERT INTO \"speedtests\" (\"start\",\"stop\",\"from\",\"from_ip\",\"server\",'\
        '\"server_dist\",\"server_ping\",\"download\",\"upload\") VALUES (%s,%s,%s,%s,%s,'\
        '%s,%s,%s,%s);'

    cur.execute(q,cols)
    con.commit()


main()

#!/usr/bin/env python

"""
    Script to convert .log file (bandwidth) to csv
"""

import argparse, csv

def main():

    # Parse args (service, file size)
    parser = argparse.ArgumentParser(description='path to csv file')
    parser.add_argument('file_path', type=str, nargs=1)
    parseResult = parser.parse_args()
    fpath = parseResult.file_path[0]

    try:
        file = open(fpath,'rb').read()
    except:
        print "Error: invalid file path"
        exit(-1)

    lines = file.split('\n')
    # Write to csv
    with open('bwdata.csv', 'w+') as csvfile:
        writer = csv.writer(csvfile)

        for line in lines:
            new_line = [item.strip() for item in line.split(',')]
            writer.writerow(new_line)
        

main()

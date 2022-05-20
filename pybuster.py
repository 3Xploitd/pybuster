#! /usr/bin/python

import requests
import argparse
import sys
from time import time


parser = argparse.ArgumentParser(prog='PyBuster', usage='%(prog)s -d/--domain [DOMAIN] -w/--wordlist [WORDLIST]', description='Discover directories for websites')

parser.add_argument('--domain','-d',help='The url you want to discover directories for, make sure to end it with a /', action='store', required=True)

parser.add_argument('--wordlist','-w',help='The file containing a list of directory names to attempt to guess on the target domain',action='store', required=True)

parser.add_argument('--filter','-f',help='The response type to filter by, possible options include: 200, 302, 400, 500, and more. Default is 200.', default='200', action='store',required=False)

args = parser.parse_args


args = parser.parse_args()
def bruteforcer(domain=args.domain,wordlist=args.wordlist):
    filter=args.filter
    status_response = {}
    status_response_filtered = []
    file = open(wordlist, "r").readlines()

    for each in file:
        directory_busting = str(requests.get(domain+each.strip()).status_code)
        status_response[each] = directory_busting
        if status_response.get(each) == filter:
            status_response_filtered.append(each)
        else:
            continue
    if len(status_response_filtered) >=1:
        print("Outputting valid directories...\n")
        for eachline in status_response_filtered:
            if eachline != '':
                print(eachline.strip())
    else:
        print("No valid directories found")

banner = """
              ____        ____             __
             / __ \__  __/ __ )__  _______/ /____  _____
            / /_/ / / / / __  / / / / ___/ __/ _ \/ ___/
           / ____/ /_/ / /_/ / /_/ (__  ) /_/  __/ /
          /_/    \__, /_____/\__,_/____/\__/\___/_/
                /____/

                version: 1.0
                """

banner2 = """
              =======================================

              Domain:{}
              Status Code Filters: {}
              Wordlist: {}

              =======================================
              """.format(args.domain,args.filter,args.wordlist)
print(banner)
print(banner2)
starttime= time()
bruteforcer()
endtime=time()
print('\nTotal time to complete:{}'.format((endtime-starttime)))

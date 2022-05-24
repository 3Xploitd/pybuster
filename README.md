# Pybuster

Pybuster is a directory discovery tool written in python for web applications.  It takes two required arguments, the domain or url in which you want to perform the discovery process on and then a wordlist you would like to try against the web application to discover the directories.  By default it assumes you'd only like to filter responses by HTTP 200 responses, however this can be changed and filtered by whatever response you'd like.


## Installation

This module requires argparse and requests which can be installed via the following command if they are not already installed:

`pip install requests argparse` or `python -m pip install argparse requests`

Then to get the code you can do the following command:

`git clone https://github.com/3Xploitd/pybuster.git`


## Usage

Pybuster can be run by the following python command:

`python pybuster.py -d [DOMAIN] -w [WORDLIST]` 

Additionally there are a couple of optional commandline arguments that can be specified as seen below:

  --domain DOMAIN, -d DOMAIN
                        The url you want to discover directories for, make sure to end it with a /
  --wordlist WORDLIST, -w WORDLIST
                        The file containing a list of directory names to attempt to guess on the target domain
  --filter FILTER, -f FILTER
                        The response type to filter by, possible options include: 200, 302, 400, 500, and more. Default is 200.

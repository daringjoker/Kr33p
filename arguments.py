import argparse
import sys

parser=argparse.ArgumentParser(description="An Awesome Intelligent Crawler to break things Quietly")
parser.add_argument('-u',"--url",help="Url to begin crawling at !")
parser.add_argument("--dont-hop",help="Stay on same domain dont hop into another",action='store_true')
parser.add_argument('-s',"--sleep",help="no of milli seconds to sleep between each request, default=0")

args=parser.parse_args()
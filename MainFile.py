from bs4 import BeautifulSoup
import requests
import sys
from argparse import ArgumentParser, Namespace
from webScraper import *


#Makes parser so that custom arguments can be added
parser = ArgumentParser()
#Custom arguments initialized
parser.add_argument('--type', type=str, help='str: Type in book or movie to select what you want to search')
parser.add_argument('--search', type=str, help='str: Type in what book or movie you want information about, please capitalize the first letter of each word and type the title inside quotations')


#Determines what the arguments are from the terminal and convert them to the appropriate type
args: Namespace = parser.parse_args() 

#Sets default type choice to movie and search to toy story if the user does not pick one or only picks one
if args.type == None:
    args.type = "movie"
    args.search = "Toy Story"
if args.search == None:
    args.type = "movie"
    args.search = "Toy Story"

webScraper(args.type, args.search)
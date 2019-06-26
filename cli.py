import argparse
import os
import sys
from config import my_api_key

api_key = my_api_key
base = "https://api.nasa.gov/mars-photos/api/v1/"

parser = argparse.ArgumentParser(prog='MarsRoverSDK',
                                 usage='%(prog)s [options] rover',
                                 description='Pull Rover images from NASA',
                                 epilog='Now knock yourself out :)')

# .../api/v1/rovers/{}/...
parser.add_argument('Rover',
                    metavar='rover',
                    type=str,
                    help='Curiosity, Opportunity, or Spirit.')

# .../photos?sol=1000&...
#parser.add_argument('Sol',
#                    metavar='sol',
#                    type=int,
#                    help='Martian day to view.')

# ...&camera={}&...
parser.add_argument('Camera',
                    metavar='camera',
                    type=str,
                    help='Camera to view.')

# ...&api_key={}
#parser.add_argument('API Key',
#                    metavar='apikey',
#                    type=str,
#                    help='Specify API key to use',
#                    default=api_key)

parser.parse_args()
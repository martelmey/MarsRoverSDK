import requests
import webbrowser
import json
import random
from marsSDK import randomPhoto, mostRecentSolDateImage, customSearch, roverMissionStatus, missionManifest, mostRecentSol, totalPhotosGreaterThan

from configparser import ConfigParser
config = ConfigParser()
config.read('config.py')
api_key = config.get('auth','api_key')


#print(randomPhoto())
## Functions Tested:
#mostRecentSolDateImage("curiosity", "fhaz") #working
#roverMissionStatus("opportunity") #working
#missionManifest("curiosity") #working
mostRecentSol("curiosity") #working
#customSearch("curiosity", 797, "navcam") #working
#missionSol("curiosity") #working
#print(totalPhotosGreaterThan("curiosity", 1000)) #working

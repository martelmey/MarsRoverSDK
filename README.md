# Mars Rover SDK
In this SDK you can choose from different Rovers, Cameras and Sol numbers (mission numbers) to return different images and information from the Rovers.

## Getting Started

This is a Python implementation of the NASA Mars Rover API.

### Install Python

Download Python for your system 
https://www.python.org/downloads/

### Install pip

Mac - Install pip if its not already on your machine. 
```
$ sudo easy_install pip
$ sudo pip install --upgrade pip
```
Windows - Install pip during Python3 installation

### Get an API Key

Apply for your key here: https://api.nasa.gov/index.html#apply-for-an-api-key

Mars Rover Documenation: https://api.nasa.gov/api.html#MarsPhotos

### Running on Virtual Environment

On Mac: Run `source env/bin/activate` within project folder to activate the environment.

On Windows: Run `env\Scripts\activate.ps1` within project folder, using PowerShell.

To leave the environment enter `deactivate`. Mac & Windows.

To load the requests library enter `pip install requests --user`. 

Create your `config.py` file with the variable `my_api_key = "Your_API_Key"`. Assign your new API key, save and close that file. 

Once you are running the environment you can then run the example file with `python3 example.py`. It is currently default to the `mostRecentSolDateImage` function. 

## Calling the Functions

**mostRecentSolDateImage** - Returns the most recent image from the Rover selected with the camera of choice. 
(For best results Curiosity has the most image returns.) You will need to pass 2 parameters for the Rover name and the Camera you wish to use. The randomPhoto function is run during photo selection which will return an image from the first 5 place holders in the data. 

Example:
```   
my_marsSDK_object.mostRecentSolDateImage("curiosity", "fhaz")
```
In the example above you can see the Curiosity Rover was entered as the `rover_name` parameter and `rhaz` entered as the `camera` parameter. 

**customSearch** - Customize your Search. This function takes 3 parameters. Yyou can set the Rover, Sol, and Camera. The result will show the appropriate image. The randomPhoto function is run during photo selection which will return an image from the first 5 place holders in the data.

Example:
```
my_marsSDK_object.customSearch("curiosity", 1000, "rhaz")
```

**roverMissionStatus** - Returns the Rovers Status. This function takes 1 parameter and is looking for the Rover name.

Example:
```
print(my_marsSDK_object.roverMissionStatus("opportunity"))
```

**missionManifest** - Returns the Mission Manifest from the chosen Rover.  This function takes 1 parameter and is looking for the Rover name.

Example:
```
print(my_marsSDK_object.missionManifest("curiosity"))
```

**mostRecentSol** - Returns the Most Recent Sol from chosen Rover. This function takes 1 parameter and is looking for the Rover name.

Example: 
```
print(my_marsSDK_object.mostRecentSol("curiosity"))
```

**missionSol** - Returns every mission Sol number. This function takes 1 parameter and is looking for the Rover name.

Example:
```
print(my_marsSDK_object.missionSol("curiosity"))
```

**totalPhotosGreaterThan** - Returns the sol missions that contain more than a set number of photos. This function takes 2 parameter and is looking for the Rover name and a number to use as the min number of photos.

Example:
```
print(my_marsSDK_object.totalPhotosGreaterThan("curiosity", 1500))
```

### Mars Rovers
These are the Rovers you can choose from:
- Curiousity
- Opportunity
- Spirit

### Mars Cameras
The following is a list of cameras you can use in your search. 
(Sourced from the Mars Rover Documenation linked above)

Cameras are available for Rovers listed based on: C - Curiosity O - Opportunity S - Spirit

 - FHAZ (Front Hazard Avoidance Camera) - Available for: C, O, S
 - RHAZ (Rear Hazard Avoidance Camera) - Available for: C, O, S
 - MAST (Mast Camera) - Available for: C
 - CHEMCAM (Chemistry and Camera Complex) - Available for: C
 - MAHLI (Mars Hand Lens Imager) - Available for: C
 - MARDI (Mars Descent Imager) - Available for: C
 - NAVCAM (Navigation Camera) - Available for: C, O, S
 - PANCAM (Panoramic Camera) - Available for: O, S
 - MINITES (Miniature Thermal Emission Spectrometer (Mini-TES) - Available for: O, S


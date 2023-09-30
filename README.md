# Face_Recognition

## Overview
A python project for face recognition using FastAPI as framework and deploy on google cloud platform.

## Setup:
    a. Clone the Git Repository to your system.
    b. Open the new terminal and run the command ```bash setup.sh ```
    c. Run command ```uvicorn main:app --reload```

## Working:
    a.	When you run the command bash setup.sh, now everything is done automatically.
    b.	Firstly, it will make a virtual environment named fast_api. 
    c.	Then that virtual environment gets active, the command used is for Linux/Mac users and for Windows it is        
        fast_api\Scripts\activate.bat
    d.	When the virtual environment is activated, it will install the required package for running this program.
    e. The uvicorn server is running at port 8000.
    f. There are two api's register and recgonise.
    g. When you call register you have to upload a image it will store that image in the dataset folder.
    h. And when you call the recognise api for the pic that you want to verify whether stored in the dataset it matches all the images present in the dataset and provide you the list of the images that is matching.
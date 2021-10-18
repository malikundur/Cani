# Cani : Voice Assistant 
## Voice Assistant Using Artificial Intelligence


Cani is voice assistant system that can recognize user for permission to access the system, talk, listen and commit some works. It is powered by Python.

## Azure 

This system based on Microsoft Azure Speech Services. So you have to get an Azure account. After that you have to register Speech Service and get Speech Service Subscription ID.

## Features


- Recognozies user and matches the photos saved on the database by using Artificial Intelligence methods.

- Declares whether access is approved or not.

   #### Due to the voice input:

    - Makes Google searches and declares the user.
    
    - Sends and reads Emails by using Gmail platform.
    
    - Does interlingual translations by using Google Translate API.
    
    - Examines weather forecast by using AccuWeather API.

First, for face recognition you have to create a folder named ImagesAttendance which will contain user images and names. Artificial Intelligence analizes the images in this folder. When someone want to use the system, AI compares two images; one is the image that in the folder, one is the instant picture provided by computer camera. If these two images matches with low matching distance point, system acknowledges that you are a user that have access. After that, system welcomes the user with warm voice message:"Access Approved.Welcome 'User Name'"(e.g.,Welcome Kevin de Bruyne).But if these two images matches with high matching distance point, system do not give permission to access.

After succesful facial recognition, system connects to Azure Speech service.Azure Speech is a text to speech / speech to text service that can work simultaneously and rapid, powered by Microsoft. Also text to speech service helps to declare welcome message which is described above.

Now system ready to listen your commands for operations you are willing to do.
    


    
## Presquities

- Python 3

    Main development language of the project.
- Visaul Studio Code

    Facial recognition based on OpenCV library. OpenCV is originally developed on C programming langugae. So, when we want to use this library in Python we should do some transitions. We should use a C compiler. If you are going to install Visual Studio from scratch, installing the desktop version will be fair enough.
    


## Required Libraries

-   time

    Python 3 has time library init. So all you need to this import.time library is necessary for facial recognition camera capture duration and delay for playing converted speech files.
- azure.cognitiveservices.speech

    Azure Speech service for speech-text conversion.
- os

    This library authorizes you to make changes on system files. When you indicate directory and file names on your local device, you need this library. Also Python has this library init.
- pyglet

    Received converted speech files is saved on your device as .wav file. Pyglet module serves to play these files.
- imaplib

    The Google Email server assigned for online operations.
- email

    Python library for email operaions.
- requests

    When you pull requests, infos or html files from web sites, requests library is required.
- json

    json is a file format is widely used on the internet while transfering any infos. When you want to pull Google search results, you are going to get the results in json format. So, you should have this library for reading and scraping these json files.
- cv2

    OpenCV is the huge open-source library for the computer vision, machine learning, and image processing. In this project for facial recognition related to this library.
- numpy 

    NumPy is the fundamental package for scientific computing in Python. During facial recognition process, calculating the match distance this library does its duty.
- face_recognition

    Fundamental face recognotion library for Python.
- dlib

    dlib is a modern C++ toolkit containing machine learning algorithms and tools for creating complex software in C++ to solve real world problems.
- cmake

    CMake is used to control the software compilation process using simple platform and compiler independent configuration files, and generate native makefiles and workspaces that can be used in the compiler environment of your choice.
    
- urllib.request

    This library is used for sending url requests to web sites.
    
- csv

    Comma Seperated Values (csv) is a file format which used for transfering datas in a compact way. Values can be seperated commas or other punctuations. It is easy to read and write.Does not hold much space.
    
- smtplib

    SMTP stands for Simple Mail Transfer Protocol, and it’s an application used by mail servers to send, receive, and/or relay outgoing mail between email senders and receivers. 
    In this project SMTP is used for sending emails.
    
### Commands

- Search

    Search voice command is used for doing Google Web searches. Once you say "Search" system expects you to another word or sentence to do the search. After that system finds the best five search results and starts to declare their title and Web site from 1 to 5. If you say "Stop", it will stop talking.

- Email

    Email voice command is used for checking inbox whether any new Email contains or not, read them if there are Emails, or declaring the empty inbox situation if the inbox is empty.

- Translate

    Translate voice command is used for doing translations between source and destinaiton languages.Then declares the result to the user.
    
- Weather

    Weather voice command is used for obtain weather forecast for hourly, daily and 5-days periods with weather events, tempreature, humidity, visibility etc.

- Another Commands

    If any commands were submitted which is not listed, system is going to repeat the input voice command.


    











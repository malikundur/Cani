import time

import azure.cognitiveservices.speech as speechsdk
import os
import pyglet

from googlesearch import search

import imaplib
import email

import requests
import json

import cv2
import numpy as np
import face_recognition


def from_mic():
    speech_config = speechsdk.SpeechConfig(subscription="#Your Azure Speech Subscription ID#", region="westeurope")
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

    print("Speak into your microphone.")
    result = speech_recognizer.recognize_once_async().get()
    # print(result.text)
    # print(result)

    return result.text


from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig


def TtoS(s1):
    speech_config = SpeechConfig(subscription="#Your Azure Speech Subscription ID#", region="westeurope")
    audio_config = AudioOutputConfig(filename="#The .wav File Directory That Contains Speech Audio#")

    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(s1)


def SoundFunc():
    sound = pyglet.resource.media('#The .wav File Name#', streaming=False)
    sound.play()
    time.sleep(sound.duration)


def get_inbox():
    host = 'imap.gmail.com'
    username = '#Your Email Adress#'
    password = '#Your Email Password#'

    mail = imaplib.IMAP4_SSL(host)
    mail.login(username, password)
    mail.select("inbox")
    _, search_data = mail.search(None, 'UNSEEN')
    my_message = []
    for num in search_data[0].split():
        email_data = {}
        _, data = mail.fetch(num, '(RFC822)')
        # print(data[0])
        _, b = data[0]
        email_message = email.message_from_bytes(b)
        for header in ['subject', 'to', 'from', 'date']:
            # print("{}: {}".format(header, email_message[header]))
            email_data[header] = email_message[header]
        for part in email_message.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                email_data['body'] = body.decode()
            elif part.get_content_type() == "text/html":
                html_body = part.get_payload(decode=True)
                email_data['html_body'] = html_body.decode()
        my_message.append(email_data)
    return my_message


def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

encodeListKnown = findEncodings(images)
print('Encoding Complete')

global list1


def face_recog():
    prt2 = True
    prt1 = True
    apprv = False

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    now = time.time()
    future = now + 4

    global list1

    while prt1:
        list1 = []

        list1.clear()
        if time.time() > future:
            break

        # print(list1, "2")

        success, img = cap.read()
        # img = captureScreen()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

        # print(list1, "3")

        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            print(faceDis)
            matchIndex = np.argmin(faceDis)

            # print(len(list1))

            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                print(name)
                prt1 = False
                apprv = True
                prt2 = False
                list1.append("a")
                list1.append(apprv)
                list1.append(name)
            # print(list1, "4")

        # cv2.imshow('Webcam', img)
        cv2.waitKey(1)
        cv2.destroyAllWindows()

    return list1


denek = face_recog()


def ana():
    prt = True
    prt4 = 0
    try:

        if list1[1] == True:
            TtoS("Access, Approved. Welcome {}".format(list1[2]))
            SoundFunc()

            while prt:

                x1 = from_mic()
                print(x1)

                if x1 == "Listen.":
                    prt = False


                elif x1 == "":
                    print("Please say something.")
                    TtoS("Please say something.")
                    SoundFunc()

                    prt4 += 1
                    if prt4 == 3:
                        prt = False



                elif x1 == "ExSearchGG":

                    y1 = from_mic()
                    query = y1
                    my_results_list = []

                    for i in search(query,  # The query you want to run
                                    tld='com',  # The top level domain
                                    lang='tr',  # The language
                                    num=10,  # Number of results per page
                                    start=0,  # First result to retrieve
                                    stop=20,  # Last result to retrieve
                                    pause=2.0,  # Lapse between HTTP requests
                                    ):
                        my_results_list.append(i)
                        print(i)

                elif x1 == "Twitter":
                    pass

                elif x1 == "Translate":

                    from googletrans import Translator

                    y1 = from_mic()

                    translator = Translator()
                    translation = translator.translate(y1, src="tr", dest='en')
                    TtoS(translation.text)

                    sound = pyglet.resource.media('#The .wav File Name#', streaming=False)
                    sound.play()
                    time.sleep(sound.duration + 0.5)

                elif x1 == "Email":

                    my_inbox = get_inbox()

                    if len(my_inbox) == 0:
                        msg = "Your inbox is empty."
                        TtoS(msg)
                        SoundFunc()
                        # print("b")

                    for i in my_inbox:
                        print("********************")
                        print(i["date"])
                        print(i["subject"])
                        print(i["body"])

                elif x1 == "Search":

                    y1 = from_mic()
                    print(y1)
                    if y1 == "":
                        TtoS("Please say something.")
                        SoundFunc()

                    else:

                        params = {
                            'api_key': '#Your Scale Serp API Subscription Key#',
                            'q': y1,
                            'output': 'json',
                            'device': 'desktop',
                            'page': '1',
                            'num': '5',
                            'gl': 'uk',
                            'hl': 'en',
                            'location': 'London,England,United Kingdom',
                            'google_domain': 'google.co.uk'
                        }

                        api_result = requests.get('https://api.scaleserp.com/search', params)

                        aa = json.dumps(api_result.json())
                        veri = json.loads(aa)

                        org_res_list = veri["organic_results"]

                        xx = 0

                        for i in org_res_list:
                            out_dict = org_res_list[xx]
                            title = out_dict["title"]
                            link = out_dict["link"]
                            snippet = out_dict["snippet"]
                            position = str(out_dict["position"])

                            print("**************")
                            print("Position: {}".format(position))
                            print("Title: {}".format(title))
                            print("Snippet: {}".format(snippet))
                            print("Link: {}".format(link))

                            TtoS(position)
                            SoundFunc()

                            TtoS(title)
                            sound = pyglet.resource.media('f#The .wav File Name#', streaming=False)
                            sound.play()
                            time.sleep(sound.duration + 0.5)

                            xx += 1

                elif x1 != " ":
                    try:
                        (TtoS(x1))
                        sound = pyglet.resource.media('#The .wav File Name#', streaming=False)
                        sound.play()
                    except:
                        pass

    except:
        print("Access Denied. Please try again.")
        TtoS("Access, Denied.")
        SoundFunc()

        prt3 = True

        while prt3 == True:
            try:
                if list1[1] == True:
                    TtoS("Access, Approved. Welcome {}".format(list1[2]))
                    SoundFunc()
                    ana()
                    prt3 = False

            except:
                face_recog()
                ana()


ana()







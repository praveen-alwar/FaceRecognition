import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import mysql.connector

dbPath = 'EmployeeDB'
images = []
empNames = []
myList = os.listdir(dbPath)

for items in myList:
    images.append(cv2.imread(f'{dbPath}/{items}'))
    empNames.append(os.path.splitext(items)[0])
print(empNames)


def encode_images(images):
    """
    Function that encodes the passed Image numpy arrays
    """
    encodeList = []

    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


def mark_attendance(name, tDate, tstamp):
    """Function that Marks the attendance if face is recognized"""

    db = 'annulartech'
    localdb = mysql.connector.connect(host='localhost', user='root', passwd='Admin', database=db)

    cursor = localdb.cursor()

    inserter = "INSERT INTO attendance VALUES (%s, %s, %s)"
    val = (name, tDate, tstamp)

    cursor.execute(inserter, val)
    localdb.commit()

encodeListKnown = encode_images(images)
print('Encoding Complete')

cam = cv2.VideoCapture(0)

while True:
    _, frame = cam.read()

    frame = cv2.flip(frame, 1)

    resizedFrame = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    resizedFrame = cv2.cvtColor(resizedFrame, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(resizedFrame)
    encodesCurFrame = face_recognition.face_encodings(resizedFrame, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = empNames[matchIndex].upper()
            dtime = datetime.now()
            tstamp = dtime.strftime('%H:%M:%S')
            tDate = dtime.strftime('%Y-%m-%d')

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            mark_attendance(name, tDate, tstamp)

    cv2.imshow('Webcam', frame)
    keycode = cv2.waitKey(1)
    if cv2.getWindowProperty("Webcam", cv2.WND_PROP_VISIBLE) < 1:
        break
    # checking

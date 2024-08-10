

import numpy as np
import csv
import os
from datetime import datetime
import cv2
import dlib
import face_recognition


video_capture = cv2.VideoCapture(0)
 
jobs_image = face_recognition.load_image_file("photos/jobs.jpg")
jobs_encoding = face_recognition.face_encodings(jobs_image)[0]
 
ratan_tata_image = face_recognition.load_image_file("photos/tata.jpg")
ratan_tata_encoding = face_recognition.face_encodings(ratan_tata_image)[0]

mark_image = face_recognition.load_image_file("photos/mark.jpg")
mark_encoding = face_recognition.face_encodings(mark_image)[0]

alia_image = face_recognition.load_image_file("photos/alia.jpg")
alia_encoding = face_recognition.face_encodings(alia_image)[0]

deepika_image = face_recognition.load_image_file("photos/deepika.jpg")
deepika_encoding = face_recognition.face_encodings(deepika_image)[0]

aronno_image = face_recognition.load_image_file("photos/aronno.jpg")
aronno_encoding = face_recognition.face_encodings(aronno_image)[0]

anupama_image = face_recognition.load_image_file("photos/anupama.jpg")
anupama_encoding = face_recognition.face_encodings(anupama_image)[0]

known_face_encodings = [
    jobs_encoding,
    ratan_tata_encoding,
    mark_encoding,
    alia_encoding,
    deepika_encoding,
    aronno_encoding,
    anupama_encoding
]
known_faces_names = [
    "Steve Jobs",
    "Ratan Tata",
    "Mark Zuckerberg",
    "Alia Bhatt",
    "Deepika Padukone",
    "Debjany Ghosh Aronno",
    "Anupama Ghose"
]

students = known_faces_names.copy()

face_locations = []
face_encodings = []
face_names = []
s=True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date+'.csv','w+',newline = '')
lnwriter = csv.writer(f)



 
while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
    rgb_small_frame = small_frame[:,:,::-1]
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame,face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding,face_encoding)
            name=""
            face_distance = face_recognition.face_distance(known_face_encoding,face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = known_faces_names[best_match_index]
 
            face_names.append(name)
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10,100)
                fontScale              = 1.5
                fontColor              = (255,0,0)
                thickness              = 3
                lineType               = 2
 
                cv2.putText(frame,name+' Present', 
                    bottomLeftCornerOfText, 
                    font, 
                    fontScale,
                    fontColor,
                    thickness,
                    lineType)
 
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name,current_time])
    cv2.imshow("attendence system",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
 
video_capture.release()
cv2.destroyAllWindows()
f.close()

from __future__ import print_function
import cv2 as cv
import argparse
import os
import pathlib

 
def detectAndDisplay(frame):
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)
    #-- Detect faces
    faces = face_cascade.detectMultiScale(frame_gray)
    for (x,y,w,h) in faces:
        center = (x + w//2, y + h//2)
        frame = cv.ellipse(frame, center, (w//2, h//2), 0, 0, 360, (255, 0, 255), 4)
        faceROI = frame_gray[y:y+h,x:x+w]
    cv.imshow('Capture - Face detection', frame)


# cascades_dir = "/lab/resources/haarcascades"

cascades_dir = "C:\\Users\\krish\\Documents\\GitHub\\ComputerVisionLab\\cv_lab\\resources\\haarcascades"

default_face_cascade = os.path.join(cascades_dir,'haarcascade_frontalface_alt.xml')


parser = argparse.ArgumentParser()
parser.add_argument('--face_cascade', 
                    help='Path to face cascade.', 
                     default=default_face_cascade)

parser.add_argument('--camera', 
                    help='Camera divide number.', 
                    type=int, default=0)

parser.add_argument('--file', 
                    help='Video or Image', type=pathlib.Path)

args = parser.parse_args()

face_cascade_name = args.face_cascade
face_cascade = cv.CascadeClassifier()

#-- 1. Load the cascades
if not face_cascade.load(cv.samples.findFile(face_cascade_name)):
    print('--(!)Error loading face cascade')
    exit(0)

if args.camera:
    src = args.camera

if args.file:
    src = args.file
else:
    src = r'C:\Users\krish\Desktop\New folder\MySistersHotFriend.-.Ashly.Anderson.mp4\mshfashlykyle_qt.mp4'

# print("#"*20)
# print(src)
# print(src.resolve())
# print(os.path.isfile(src))
# print("#"*20)



cap = cv.VideoCapture(src)


count = 0
while True:
    ret, frame = cap.read()
    count+=1
    if frame is None:
        print('--(!) No captured frame -- Break!')
        break
    if count >= 3000:
        detectAndDisplay(frame)
    if cv.waitKey(10) == 27:
        break
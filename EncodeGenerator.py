# import cv2
# import face_recognition
# import pickle
# import os
# import firebase_admin
# from firebase_admin import storage
# from firebase_admin import credentials 
# from firebase_admin import db


# cred = credentials.Certificate("key.json")
# firebase_admin.initialize_app(cred,{
#     'databaseURL': "https://faceplease-71d8d-default-rtdb.firebaseio.com/",
#     'storageBucket': "faceplease-71d8d.appspot.com"
# })



# # Importing student images
# folderPath = 'Images'
# pathList = os.listdir(folderPath)
# print(pathList)
# target_size = (216, 216)
# imgList = []
# studentIds = []
# for path in pathList:
#     imgList.append(cv2.imread(os.path.join(folderPath, path)))
#     studentIds.append(os.path.splitext(path)[0])

#     fileName = f'{folderPath}/{path}'
#     bucket = storage.bucket()
#     blob = bucket.blob(fileName)
#     blob.upload_from_filename(fileName)


#     # print(path)
#     # print(os.path.splitext(path)[0])
# print(studentIds)


# ## Encoding every single images
# def findEncodings(imagesList):
#     encodeList = []
#     for img in imagesList:
#         img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)

#     return encodeList


# ### Checking if all images are encoded
# print("Encoding Started ...")
# encodeListKnown = findEncodings(imgList)
# encodeListKnownWithIds = [encodeListKnown, studentIds]
# print("Encoding Complete")


# ## Saving encoded file
# file = open("EncodeFile.p", 'wb')
# pickle.dump(encodeListKnownWithIds, file)
# file.close()
# print("File Saved")


import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import storage
from firebase_admin import credentials 
from firebase_admin import db

cred = credentials.Certificate("key.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceplease-71d8d-default-rtdb.firebaseio.com/",
    'storageBucket': "faceplease-71d8d.appspot.com"
})

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)
print(pathList)
target_size = (216, 216)
imgList = []
studentIds = []

for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))
    
    # Resizing the image to 216x216
    img_resized = cv2.resize(img, target_size)
    
    imgList.append(img_resized)
    studentIds.append(os.path.splitext(path)[0])

    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    
    # Save the resized image locally before uploading
    resized_file_path = os.path.join(folderPath, f'resized_{path}')
    cv2.imwrite(resized_file_path, img_resized)
    
    blob.upload_from_filename(resized_file_path)
    
    # Optionally, delete the resized image after uploading to save space
    #os.remove(resized_file_path)

print(studentIds)

## Encoding every single image
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

### Checking if all images are encoded
print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

## Saving encoded file
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")

import cv2
import dropbox
import time
import random

startTime = time.time()
def snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True

    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = "IMG"+str(number)+".jpg"
        cv2.imwrite(imageName,frame)
        startTime = time.time()
        result = False
    return imageName
    print("SNAPSHOT TAKEN")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(imageName):
    accessToken = 'sl.AzdVXl3jr4iAfScVWMvpyEwhnrGTnz2DIIF_-0wQfr0fRRGQbvm3PIPcSpVh16ul0CyGmY2jHlJYThO6FqbifoKOpw49qxXUJ7M8f41LOHs1txyNF5ToQziAw3oo7P_dYvygjQY'
    file = imageName
    file_to = "/test/"+imageName
    dbx = dropbox.Dropbox(accessToken)
    with open(file,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite) 
        print("File Uploaded")
def main():
    while True:
        if((time.time()-startTime)>=5):
            image = snapshot()
            uploadFile(image)
main()
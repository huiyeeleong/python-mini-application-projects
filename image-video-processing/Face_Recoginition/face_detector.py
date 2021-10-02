import cv2

#read face image alogrithm
face_cascade = cv2.CascadeClassifier("image-video-processing/Face_Recoginition/haarcascade_frontalface_default.xml")

#image location
img = cv2.imread("image-video-processing/Face_Recoginition/news.jpg")

#convert to gray scale image
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect face scale
faces = face_cascade.detectMultiScale(gray_img,
scaleFactor= 1.05,
minNeighbors = 5)

#draw rectange on image
for x,y,w,h in faces:
    img= cv2.rectangle(img, (x,y),(x+w,y+h),(0,255,0),3)

print(type(faces))
print(faces)

resized = cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Gray", gray_img)
cv2.waitKey(20000)
cv2.destroyAllWindows()
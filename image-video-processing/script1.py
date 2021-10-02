import cv2

#Read image
img = cv2.imread("image-video-processing/galaxy.jpg", 0)

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

# Display image
cv2.imshow("Galaxy", img)

#resized image
resized_image = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("image-video-processing/Galaxy_resized.jpg", resized_image)

#Timeout for the image
#User can close the window with anytime
cv2.waitKey(2000)
cv2.destroyAllWindows()



import cv2

img = cv2.imread("Input/Cats.jpeg")
cat_face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalcatface.xml")
cats = cat_face_detector.detectMultiScale(img, 1.1)
for cat in cats:
    x, y, w, h = cat
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)

cv2.imshow("Cat_Detector", img)
cv2.waitKey()
cv2.imwrite("Output/Cat_Detector.jpg", img)




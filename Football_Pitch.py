import cv2 
import numpy as np 

football = np.ones((450 , 700 , 3) , dtype= np.uint8) * 255
y = 0 
for i in range(7):
    if i % 2 == 0 :
        cv2.rectangle(football , [0+y,0] , [100+y , 700] , (45 , 110 , 5) , -1 )
    else :
        cv2.rectangle(football , [0+y,0] , [100+y , 700] , (40 , 90 , 10) , -1 )
    y+= 100
cv2.rectangle(football , [20,20] , [680 ,430] , (255,255,255) , 2 )
cv2.line(football , [350,20] , [350 ,430] , (255,255,255) , 2 )
cv2.circle(football , [350,225] , 90 , (255,255,255) , 2 )
cv2.circle(football , [350,225] , 7 , (255,255,255) , -1 )
y1 = 0
y2 = 0
for i in range(2):
    cv2.rectangle(football , [20+y1 ,110] , [130+y1 ,340] , (255,255,255) , 2 )
    cv2.rectangle(football , [20+y2,160] , [80+y2 ,290] , (255,255,255) , 2 ) 
    y1+= 550
    y2 = y1+50
cv2.imshow("Football_Pitch" , football)
cv2.waitKey()
cv2.imwrite("Output/Football_Pitch.jpg", football)
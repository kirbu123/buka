import cv2
print('Put on your videocamera and you will see how many faces on video')

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 24) # Чистота кадров

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,               #
        scaleFactor=1.2,    #
        minNeighbors=6,     #
        minSize=(20, 20)    #
    )
    for (x, y, w, h) in faces:
        roi_color = img[y:y + h, x:x + w]
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 10)
    s_mas=str(len(faces))
    if s_mas[len(s_mas)-1]=='1':
        text_screen='Here is '+str(len(faces))+' face'
    else:
        text_screen='Here is '+str(len(faces))+' faces'
    cv2.putText(img, text_screen, (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (30, 105, 210), 10)
    cv2.imshow("camera", img)
    if cv2.waitKey(10) == 27:
        break
cap.release()
cv2.destroyAllWindows()

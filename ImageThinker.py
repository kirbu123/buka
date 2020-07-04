'''Здесь происходит процесс использования уже обученной программы,
НЕ обучение!'''
from PIL import Image, ImageTk, ImageDraw
import cv2
import random
import numpy
from pathlib import Path
from math import fabs
#--------------------------------------------Cv2 part
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
adres=str(input('Input here name of file and program will say who on this picture or on what player of trio MSN person at the picture looks like: '))
#data block
mas_neymar=[3, 3, 3, 1, 2, 4, 1, 3, 2, 2, 3, 3, 4, 3, 4, 3, 3, 3, 3,
            2, 4, 4, 3, 4, 3, 3, 5, 3, 4, 3, 4, 3, 3, 4, 4, 5, 4, 4,
            4, 3, 4, 4, 4, 3, 4, 4, 4, 3, 4, 3, 4, 3, 4, 4, 2, 3, 4,
            4, 3, 4, 4, 3, 3, 2, 4, 3, 3, 3, 4, 3, 4, 3, 3, 4, 4, 3,
            3, 3, 3, 2]
mas_messi=[4, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 4, 3, 4, 4, 3, 5, 3, 4,
           5, 5, 4, 3, 3, 3, 4, 4, 3, 2, 3, 2, 4, 4, 3, 4, 3, 4, 5,
           4, 5, 5, 2, 3, 4, 4, 5, 4, 3, 3, 4, 3, 4, 3, 4, 3, 5, 3,
           5, 5, 4, 3, 4, 3, 5, 3, 3, 3, 5, 3, 4, 4, 3, 3, 3, 5, 3,
           3, 2, 3, 2]
mas_kirill_bunin=[4, 0, 2, 5, 3, 4, 3, 5, 2, 1, 5, 4, 0, 2, 5, 8,
                  1, 2, 2, 0, 5, 6, 3, 4, 5, 2, 8, 2, 4, 5, 3, 5,
                  8, 6, 5, 8, 4, 1, 3, 6, 8, 4, 1, 5, 7, 4, 6, 3,
                  5, 4, 4, 6, 4,1, 4, 5, 4, 1, 2, 5, 4, 6, 5, 5,
                  5, 2, 5, 2, 6, 7, 5, 4, 4, 7, 5, 7, 8, 1, 4, 4]
mas_suares=[3, 3, 4, 2, 3, 5, 2, 2, 2, 1, 3, 3, 3, 3, 4, 3, 3, 3,
            2, 4, 3, 5, 5, 3, 5, 3, 4, 4, 3, 3, 4, 3, 3, 5, 3, 5,
            4, 5, 3, 5, 4, 4, 3, 3, 4, 2, 5, 4, 5, 4, 3, 3, 3, 3,
            3, 4, 4, 4, 4, 4, 5, 2, 4, 5, 4, 4, 3, 3, 4, 3, 4, 4,
            3, 4, 4, 5, 3, 3, 4, 3]
mas_union=[[3, 3, 3, 1, 2, 4, 1, 3, 2, 2, 3, 3, 4, 3, 4, 3, 3, 3, 3,
            2, 4, 4, 3, 4, 3, 3, 5, 3, 4, 3, 4, 3, 3, 4, 4, 5, 4, 4,
            4, 3, 4, 4, 4, 3, 4, 4, 4, 3, 4, 3, 4, 3, 4, 4, 2, 3, 4,
            4, 3, 4, 4, 3, 3, 2, 4, 3, 3, 3, 4, 3, 4, 3, 3, 4, 4, 3,
            3, 3, 3, 2],#neymar junior
            [4, 3, 3, 5, 3, 3, 3, 3, 3, 5, 3, 4, 3, 4, 4, 3, 5, 3, 4,
            5, 5, 4, 3, 3, 3, 4, 4, 3, 2, 3, 2, 4, 4, 3, 4, 3, 4, 5,
            4, 5, 5, 2, 3, 4, 4, 5, 4, 3, 3, 4, 3, 4, 3, 4, 3, 5, 3,
            5, 5, 4, 3, 4, 3, 5, 3, 3, 3, 5, 3, 4, 4, 3, 3, 3, 5, 3,
            3, 2, 3, 2],#Leo Messi
            [4, 0, 2, 5, 3, 4, 3, 5, 2, 1, 5, 4, 0, 2, 5, 8,
            1, 2, 2, 0, 5, 6, 3, 4, 5, 2, 8, 2, 4, 5, 3, 5,
            8, 6, 5, 8, 4, 1, 3, 6, 8, 4, 1, 5, 7, 4, 6, 3,
            5, 4, 4, 6, 4,1, 4, 5, 4, 1, 2, 5, 4, 6, 5, 5,
            5, 2, 5, 2, 6, 7, 5, 4, 4, 7, 5, 7, 8, 1, 4, 4],#Kirill Bunin
            [3, 3, 4, 2, 3, 5, 2, 2, 2, 1, 3, 3, 3, 3, 4, 3, 3, 3,
            2, 4, 3, 5, 5, 3, 5, 3, 4, 4, 3, 3, 4, 3, 3, 5, 3, 5,
            4, 5, 3, 5, 4, 4, 3, 3, 4, 2, 5, 4, 5, 4, 3, 3, 3, 3,
            3, 4, 4, 4, 4, 4, 5, 2, 4, 5, 4, 4, 3, 3, 4, 3, 4, 4,
            3, 4, 4, 5, 3, 3, 4, 3]]#Luis Suares
weights=[1, 1, 0.5, 1, 0.5, 0.5, 0.5, 2, 0.5, 0.5, 3, 3, 0.5, 0.5,
         2, 1, 0.5, 3, 3, 0.5, 2, 3, 3, 2, 1, 0.5, 2, 1, 1, 2, 3,
         2, 2, 1, 0.5, 1, 2, 2, 1, 0.5, 1, 3, 1, 0.5, 2, 0.5, 2, 3,
         3, 3, 3, 2, 0.5, 3, 0.5, 1, 3, 0.5, 3, 2, 3, 2, 0.5, 3, 0.5,
         0.5, 3, 2, 2, 3, 2, 3, 2, 2, 2, 2, 1, 3, 2, 2]
mas_union_names=['Neymar Junior', 'Leo Messi', 'Kirill Bunin', 'Luis Suares']
#data block
            
            

            
#info block
img=cv2.imread(adres)
#ret, img = cap.read()
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
if int(len(faces))==1:
    text_screen='Here is '+str(len(faces))+' face'
elif int(len(faces))!=1:
    text_screen='Here is '+str(len(faces))+' faces'
#cv2.putText(img, text_screen, (200, 800), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 7)
#cv2.imshow("img", img)
#----------------------------------------------Image part
image=Image.open(adres)
print('loading...')
pix=image.load()
draw=ImageDraw.Draw(image)
width=image.size[0]
height=image.size[1]
cv2.putText(img, text_screen, (width//4, 4*height//5), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 255), 7)
for i in range(width):
    for j in range(height):
        a=pix[i, j][0]
        b=pix[i, j][1]
        c=pix[i, j][2]
        s=(a+b+c)//3
        draw.point((i, j), (s,s,s))
draw=ImageDraw.Draw(image)
#-----------------------------------------------Neiron part
value_pix=[]
faces_pix={}#dict
mas_count=[]
mas_width=[]
mas_height=[]
for i in faces:
    mas_width.append(i[2])
for i in faces:
    mas_height.append(i[3])
val=True
    
for x in range(1, width-1):
    for y in range(1, height-1):
        count=0
        pixel=pix[x, y][0]
        if pix[x-1, y][0]<pixel:
            count+=1
        if pix[x-1, y-1][0]<pixel:
            count+=1
        if pix[x, y-1][0]<pixel:
            count+=1
        if pix[x+1, y-1][0]<pixel:
            count+=1
        if pix[x+1, y][0]<pixel:
            count+=1
        if pix[x+1, y+1][0]<pixel:
            count+=1
        if pix[x, y+1][0]<pixel:
            count+=1
        if pix[x-1, y+1][0]<pixel:
            count+=1
        if pix[x-1, y][0]<pixel:
            count+=1
        value_pix.append(count)
        for i in range(len(faces)):
            if faces[i][0]<=x and faces[i][0]+faces[i][2]>=x and faces[i][1]<=y and faces[i][1]+faces[i][3]>=y:
                faces_pix[str(i)+' '+str(x)+' '+str(y)]=int(count)
for a in range(len(faces)):
    count=0
    for x in range(faces[a][0], faces[a][0]+faces[a][2]+1):
        for y in range(faces[a][1], faces[a][1]+faces[a][3]+1):
            count+=faces_pix[str(a)+' '+str(x)+' '+str(y)]
    mas_count.append(count)
#machine learning
main_pix=[]
masx=[]
masy=[]
for a in range(len(faces)):
    main_pix.append([])
    w=mas_width[a]//10
    h=mas_height[a]//10
    for x in range(1, 9):
        for y in range(10):
            main_pix[a].append(faces_pix[str(a)+' '+str(faces[a][0]+w*x)+' '+str(faces[a][1]+h*y)])
            '''for m in range(-1, 2):
                masx.append(faces[a][0]+w*x+m)
                masy.append(faces[a][1]+h*y+m)'''
print(main_pix)

#technic part---------
'''for i in range(width):
    for j in range(height):
        if i in masx and j in masy:
           draw.point((i, j), (255,255,0))
        for a in faces:
            if a[0]<=i and a[0]+a[2]>=i:
                if a[1]==j or a[1]+a[3]==j:
                    draw.point((i, j), (255, 255, 0))
            if a[1]<=j and a[1]+a[3]>=j:
                if a[0]==i or a[0]+a[2]==i:
                    draw.point((i, j), (255, 255, 0))
image.show()'''
#technic part--------
count=0
result=[]
mas_num=[]
for m in range(len(faces)):
    mas_num.append([])
    for i in range(len(mas_union)):
        mas_num[m].append(0)
        count=0
        for j in range(len(mas_union[i])):
            count+=fabs((mas_union[i][j]-main_pix[m][j]))**2#*weights[j]
        mas_num[m][i]=count
for m in range(len(mas_num)):
    for i in range(len(mas_num[m])):
        if min(mas_num[m])==mas_num[m][i]:
            count=i
            break
    result.append(mas_union_names[count])

for a in range(len(faces)):
    print('This is '+result[a])
    cv2.putText(img, result[a], (faces[a][0], faces[a][1]-5),cv2.FONT_HERSHEY_SIMPLEX, 1, (30, 105, 210), 2)
cv2.imshow("img", img)



        

            
        
        

        

from PIL import Image, ImageTk, ImageDraw
import random
import numpy as np
#Here we can learn our artifitial intelligent sistem (then, when programm will end it's work, copy end list and put it to mas_weights in countthinker3.0)
print('Here we can learn our artifitial intelligent sistem (then, when programm will end it is work, copy end list and put it to mas_weights in countthinker3.0)')
dw=0.01
mas_weights={0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
for keys in mas_weights:
    for i in range(100):
        mas_weights[keys].append(random.randint(0, 1))
mas_main_adres={int(5):['5-1.jpg'], int(2):['2-1.jpg'], int(4):['4-1.jpg'], int(5):['5-1.jpg'], int(6):['6-1.jpg'], int(7):['7-1.jpg'], int(8):['8-1.jpg'], int(9):['9-1.jpg']}
all_iterates=1500
for count in range(all_iterates):
    for keys in mas_main_adres:
        for adres in mas_main_adres[keys]:
            image=Image.open(adres)
            draw=ImageDraw.Draw(image)
            pix=image.load()
            mas_data_1=[]
            mas_data=[]
            width=image.size[0]
            height=image.size[1]
            for i in range(height):
                mas_data_1.append([])
            for y in range(height):
                for x in range(width):
                    a=pix[x, y][0]
                    b=pix[x, y][1]
                    c=pix[x, y][2]
                    s=(a+b+c)//3
                    #if s<60:
                        #draw.point((x, y), (0,0,0))
                    #else:
                        #draw.point((x, y), (255,255,255))
                    mas_data_1[y].append(s)
            dy=height//10
            dx=width//10
            for y in range(10):
                for x in range(10):
                    if mas_data_1[y*dy][x*dx]<60:
                        mas_data.append(1)
                    else:
                        mas_data.append(0)
            result=0
            real=keys
            mas_results={}
            for i in range(10):
                for j in range(len(mas_data)):
                    result+=mas_weights[i][j]*mas_data[j]
                mas_results[i]=result
                result=0
            #print('mas_results: '+str(mas_results))
            number=0
            for i in mas_results:
                if mas_results[i]>result:
                    result=mas_results[i]
                    number=i
            #print('number: '+str(number))
            suma=0
            for i in mas_results:
                suma+=mas_results[i]
            #for i in mas_weights:
                #for j in range(len(mas_weights[i])):
                    #if i==number:
                        #mas_weights[i][j]+=mas_weights[i][j]*(mas_results[i]/suma)*(mas_data[j])*dw
                    #else:
                        #mas_weights[i][j]-=mas_weights[i][j]*(mas_results[i]/suma)*(mas_data[j])*dw
            for i in range(len(mas_weights[number])):
                mas_weights[number][i]-=mas_weights[number][i]*(mas_results[number])*(mas_data[i])*dw
            for i in range(len(mas_weights[keys])):
                mas_weights[keys][i]+=mas_weights[keys][i]*(mas_results[keys])*(mas_data[i])*dw
    print(str(count+1)+'/per/'+str(all_iterates))
print('End_weights: '+str(mas_weights))
#(real-result)*(mas_weights[i][j]/middle_w[i])*(mas_data[i][j]/middle_d[i])*dw

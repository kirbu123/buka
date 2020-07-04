from tkinter import *
import random
from PIL import Image, ImageTk, ImageFilter, ImageDraw
root=Tk()
root.title('Ibragim Filter')
root.config(bg='White')
#
adres=str(input('Input here a name of photo: '))
size_main=(1000, 1000)
size_min=(150, 150)
image_main=Image.open(adres)
image=image_main
pix=image.load()
width=image.size[0]
height=image.size[1]
draw=ImageDraw.Draw(image)
image_main.thumbnail(size_main)
page_main=ImageTk.PhotoImage(image_main)

mas_but={}#словарь
mas_page={}#словарь
mas_image={}#словарь
mas_image_main={}#словарь
mas_page_main={}#словарь
mas_image_min={}#словарь

count=1000
counter=0

#
lab_adres=Label(root, height=1, width=30, bg='White', fg='Black', font='Verdana 15', text='put here name of your photo')
lab_adres.grid(row=0, column=0, columnspan=5)
ent_adres=Entry(root, font='Verdana 20')
ent_adres.grid(row=1, column=0, columnspan=5)
lab_main=Label(root, image=page_main)
lab_main.grid(row=2, column=0, columnspan=5)

def def_0():
    global adres, mas_image, width, height, draw, image, pix, mas_image_2
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            s=a+b+c
            if s>=255:
                a, b, c=255, 255, 255
            else:
                a,b,c=0,0,0
            draw.point((i, j), (a,b,c))
    mas_image[0]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_1():
    global adres, mas_image, width, height, draw, image, pix
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            s=a+b+c//3
            draw.point((i, j), (s,s,s))
    mas_image[1]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
    
def def_2():
    global adres, mas_image, width, height, draw, image, pix
    factor=150
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            a+=factor
            b+=factor
            c+=factor
            draw.point((i, j), (a,b,c))
    mas_image[2]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_3():
    global adres, mas_image, width, height, draw, image, pix
    factor=255
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            draw.point((i, j), (factor-a,factor-b,factor-c))
    mas_image[3]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_4():
    global adres, mas_image, width, height, draw, image, pix
    factor=[]
    for i in range(-100, 100+1):
        factor.append(i)
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            a+=random.choice(factor)
            b+=random.choice(factor)
            c+=random.choice(factor)
            draw.point((i, j), (a,b,c))
    mas_image[4]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_5():
    global adres, mas_image, width, height, draw, image, pix
    image=image.filter(ImageFilter.CONTOUR)
    mas_image[5]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_6():
    global adres, mas_image, width, height, draw, image, pix
    image=image.filter(ImageFilter.BLUR)
    mas_image[6]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_7():
    global adres, mas_image, width, height, draw, image, pix
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            s=a+b+c//3
            draw.point((i, j), (400-s,50-s,200-s))
    mas_image[7]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_8():
    global adres, mas_image, width, height, draw, image, pix
    image=image.filter(ImageFilter.EDGE_ENHANCE_MORE)
    mas_image[8]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_9():
    global adres, mas_image, width, height, draw, image, pix
    image=image.filter(ImageFilter.EMBOSS)
    mas_image[9]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_10():
    global adres, mas_image, width, height, draw, image, pix
    image=image.filter(ImageFilter.SMOOTH_MORE)
    mas_image[10]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_11():
    global adres, mas_image, width, height, draw, image, pix
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            s=a+b+c//3
            if i<width//5:
                draw.point((i, j), (100-s, s-50, 200-s))
            elif i<2*width//5:
                draw.point((i, j), (300-s,100-s,50-s))
            elif i<3*width//5:
                draw.point((i, j), (500-s,300-s,100-s))
            elif i<4*width//5:
                draw.point((i, j), (400-s,50-s,200-s))
            else:
                draw.point((i, j), (255-s,255-s,255-s))
                
    mas_image[11]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_12():
    global adres, mas_image, width, height, draw, image, pix
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            s=a+b+c//3
            draw.point((i, j), (300-s,100-s,50-s))
    mas_image[12]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_13():
    global adres, mas_image, width, height, draw, image, pix
    image=image.filter(ImageFilter.FIND_EDGES)
    mas_image[13]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_14():
    global adres, mas_image, width, height, draw, image, pix
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            s=a+b+c
            a,b,c=s-a,s-b,s-c
            draw.point((i, j), (a,b,c))
    mas_image[14]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_15():
    global adres, mas_image, width, height, draw, image, pix
    factor=255
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            s=a+b+c
            if s>factor:
                a,b,c=0, 100, 200
            else:
                a,d,c=0, 0, 0
            draw.point((i, j), (a,b,c))
    mas_image[15]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_16():
    global adres, mas_image, width, height, draw, image, pix
    factor=255
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            s=a+b+c
            if s>factor:
                a,b,c=0, 300, 200
            else:
                a,d,c=0, 0, 0
            draw.point((i, j), (a,b,c))
    mas_image[16]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_17():
    global adres, mas_image, width, height, draw, image, pix
    factor=255
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            s=a+b+c
            if s>factor:
                a,b,c=0, 100, 50
            else:
                a,d,c=0, 0, 0
            draw.point((i, j), (a,b,c))
    mas_image[17]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_18():
    global adres, mas_image, width, height, draw, image, pix
    factor=300
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            s=a+b+c//3
            draw.point((i, j), (factor-s,factor-s,factor-s))
    mas_image[18]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)
def def_19():
    global adres, mas_image, width, height, draw, image, pix
    factor=300
    for i in range(width):
        for j in range(height):
            a=pix[i, j][0]
            b=pix[i, j][1]
            c=pix[i, j][2]
            s=a+b+c//3
            if a+b+c>300:
                draw.point((i, j), (factor-s,factor-s,factor-s))
            else:
                draw.point((i, j), (s,s,s))
    mas_image[19]=image
    image=Image.open(adres)
    pix=image.load()
    draw=ImageDraw.Draw(image)

    
def_0()
def_1()
def_2()
def_3()
def_4()
def_5()
def_6()
def_7()
def_8()
def_9()
def_10()
def_11()
def_12()
def_13()
def_14()
def_15()
def_16()
def_17()
def_18()
def_19()
for i in range(20):
    mas_image_min[i]=mas_image[i]
for i in range(20):
    mas_image_min[i].thumbnail(size_min)
for i in range(20):
    mas_page[i]=ImageTk.PhotoImage(mas_image_min[i])
for i in range(20):
    mas_but[i]=Button(root, image=mas_page[i])
for i in range(5):
    mas_but[i].grid(row=3, column=i)
for i in range(5, 10):
    mas_but[i].grid(row=4, column=i-5)
for i in range(10, 15):
    mas_but[i].grid(row=5, column=i-10)
for i in range(15, 20):
    mas_but[i].grid(row=6, column=i-15)
#motion
def def_do_0(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_0
    count=0#int
    def_0()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_1(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_1
    count=1#int
    def_1()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_2(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_2
    count=2#int
    def_2()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_3(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_3
    count=3#int
    def_3()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_4(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_4
    count=4#int
    def_4()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_5(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_5
    count=5#int
    def_5()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_6(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_6
    count=6#int
    def_6()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_7(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_7
    count=7#int
    def_7()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_8(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_8
    count=8#int
    def_8()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_9(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_9
    count=9#int
    def_9()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_10(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_10
    count=10#int
    def_10()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_11(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_11
    count=11#int
    def_11()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_12(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_12
    count=12#int
    def_12()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_13(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_13
    count=13#int
    def_13()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_14(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_14
    count=14#int
    def_14()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_15(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_15
    count=15#int
    def_15()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_16(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_16
    count=16#int
    def_16()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_17(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_17
    count=17#int
    def_17()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_18(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_18
    count=18#int
    def_18()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
def def_do_19(event):
    global root, lab_main, count, mas_image_main, mas_page_main, def_19
    count=19#int
    def_19()
    mas_image_main[count]=mas_image[count]
    mas_page_main[count]=ImageTk.PhotoImage(mas_image_main[count])
    lab_main.config(image=mas_page_main[count])
    lab_main.grid(row=2, column=0, columnspan=5)
mas_but[0].bind('<Button-1>', def_do_0)
mas_but[1].bind('<Button-1>', def_do_1)
mas_but[2].bind('<Button-1>', def_do_2)
mas_but[3].bind('<Button-1>', def_do_3)
mas_but[4].bind('<Button-1>', def_do_4)
mas_but[5].bind('<Button-1>', def_do_5)
mas_but[6].bind('<Button-1>', def_do_6)
mas_but[7].bind('<Button-1>', def_do_7)
mas_but[8].bind('<Button-1>', def_do_8)
mas_but[9].bind('<Button-1>', def_do_9)
mas_but[10].bind('<Button-1>', def_do_10)
mas_but[11].bind('<Button-1>', def_do_11)
mas_but[12].bind('<Button-1>', def_do_12)
mas_but[13].bind('<Button-1>', def_do_13)
mas_but[14].bind('<Button-1>', def_do_14)
mas_but[15].bind('<Button-1>', def_do_15)
mas_but[16].bind('<Button-1>', def_do_16)
mas_but[17].bind('<Button-1>', def_do_17)
mas_but[18].bind('<Button-1>', def_do_18)
mas_but[19].bind('<Button-1>', def_do_19)
root.mainloop()#525lines!!!







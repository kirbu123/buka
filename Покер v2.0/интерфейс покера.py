from tkinter import *
import tkinter
import random
from random import randint
root=Tk()
top=Toplevel(root)
mas_namecard=['12b.png', '12c.png', '12k.png', '12p.png', '13b.png', '13c.png', '13k.png', '13p.png',
              '14b.png', '14c.png', '14k.png', '14p.png', '15b.png', '15c.png', '15k.png', '15p.png',
              '16b.png', '16c.png', '16k.png', '16p.png', '17b.png', '17c.png', '17k.png', '17p.png',
              '18b.png', '18c.png', '18k.png', '18p.png', '19b.png', '19c.png', '19k.png', '19p.png',
              '20b.png', '20c.png', '20k.png', '20p.png', '21b.png', '21c.png', '21k.png', '21p.png',
              '22b.png', '22c.png', '22k.png', '22p.png', '23b.png', '23c.png', '23k.png', '23p.png',
              '24b.png', '24c.png', '24k.png', '24p.png']
root.title('Покер интерфейс')
root.geometry('950x500')
root.config(bg='Green')
mas_bot_card=[]
img_chip=PhotoImage(file='img_min//poker_chip.png')
img_shirt=PhotoImage(file='img_min//shirt.png')
for i in range(5):
  mas_bot_card.append(Button(root, bg='Green', image=img_shirt))
mas_bot_card[0].place(width=110, height=160, x=5, y=5)
mas_bot_card[1].place(width=110, height=160, x=115, y=5)
mas_bot_card[2].place(width=110, height=160, x=225, y=5)
mas_bot_card[3].place(width=110, height=160, x=335, y=5)
mas_bot_card[4].place(width=110, height=160, x=445, y=5)
mas_pl_card=[]
cra=PhotoImage(file='img_min//12b.png')
for i in range(5):
  mas_pl_card.append(Button(root, bg='Green'))
mas_pl_card[0].place(width=110, height=160, x=5, y=335)
mas_pl_card[1].place(width=110, height=160, x=115, y=335)
mas_pl_card[2].place(width=110, height=160, x=225, y=335)
mas_pl_card[3].place(width=110, height=160, x=335, y=335)
mas_pl_card[4].place(width=110, height=160, x=445, y=335)
def d_lab():
  #переменные
  t_lab_bot_st='5'
  t_lab_pl_st='5'
  t_lab_botfis1='2019'
  t_lab_botfis2='2019'
  t_lab_g='0'
  t_lab_c='0'
  t_lab_p='0'
  #------------
  top=Toplevel(root)
  tab_fis=Label(top, width=20, height=2, text='Введите кол-во фишек')
  tab_fis.pack()
  ten_fis=Entry(top, width=20)
  ten_fis.pack()
  tab_min=Label(top, width=20, height=2, text='Введите ставку')
  tab_min.pack()
  ten_min=Entry(top, width=20)
  ten_min.pack()
  def d_d(event):
    global t_lab_bot_st, t_lab_pl_st, t_lab_bot_st, t_lab_botfis1, t_lab_botfis2
    t_lab_bot_st=ten_min.get()
    t_lab_pl_st=t_lab_bot_st
    t_lab_botfis1=t_lab_botfis2=ten_fis.get()
    top.destroy()
    lab_chip1=Label(root, image=img_chip, bg='Green').place(height=120, width=80, x=590, y=5)
    lab_botfis1=Label(root, text=t_lab_botfis1, font='Arial 16').place(width=100, height=30, x=580, y=135)
    lab_chip2=Label(root, image=img_chip, bg='Green').place(height=120, width=80, x=225, y=250, anchor=CENTER)
    lab_chip3=Label(root, image=img_chip, bg='Green').place(height=120, width=80, x=590, y=335)
    lab_botfis2=Label(root, text=t_lab_botfis2, font='Arial 16').place(width=100, height=30, x=580, y=460)
    lab_bot_st=Label(root, text=t_lab_bot_st, font='Arial 16').place(width=70, height=30, x=280, y=220)
    lab_pl_st=Label(root, text=t_lab_pl_st, font='Arial 16').place(width=70, height=30, x=280, y=260)
    lab_stat=Label(root, text='статистика', font='Arial 16').place(width=245, height=30, x=700, y=5)
    lab_games=Label(root, text='игры', font='Arial 16').place(width=115, height=30, x=700, y=45)
    lab_g=Label(root, text=t_lab_g, font='Arial 16').place(width=115, height=30, x=830, y=45)
    lab_comp=Label(root, text='компьютер', font='Arial 16').place(width=115, height=30, x=700, y=90)
    lab_c=Label(root, text=t_lab_c, font='Arial 16').place(width=115, height=30, x=830, y=90)
    lab_pl=Label(root, text='игрок', font='Arial 16').place(width=115, height=30, x=700, y=130)
    lab_p=Label(root, text=t_lab_p, font='Arial 16').place(width=115, height=30, x=830, y=130)
  #------------
  lab_chip1=Label(root, image=img_chip, bg='Green').place(height=120, width=80, x=590, y=5)
  lab_botfis1=Label(root, text=t_lab_botfis1, font='Arial 16').place(width=100, height=30, x=580, y=135)
  lab_chip2=Label(root, image=img_chip, bg='Green').place(height=120, width=80, x=225, y=250, anchor=CENTER)
  lab_chip3=Label(root, image=img_chip, bg='Green').place(height=120, width=80, x=590, y=335)
  lab_botfis2=Label(root, text=t_lab_botfis2, font='Arial 16').place(width=100, height=30, x=580, y=460)
  lab_bot_st=Label(root, text=t_lab_bot_st, font='Arial 16').place(width=70, height=30, x=280, y=220)
  lab_pl_st=Label(root, text=t_lab_pl_st, font='Arial 16').place(width=70, height=30, x=280, y=260)
  lab_stat=Label(root, text='статистика', font='Arial 16').place(width=245, height=30, x=700, y=5)
  lab_games=Label(root, text='игры', font='Arial 16').place(width=115, height=30, x=700, y=45)
  lab_g=Label(root, text=t_lab_g, font='Arial 16').place(width=115, height=30, x=830, y=45)
  lab_comp=Label(root, text='компьютер', font='Arial 16').place(width=115, height=30, x=700, y=90)
  lab_c=Label(root, text=t_lab_c, font='Arial 16').place(width=115, height=30, x=830, y=90)
  lab_pl=Label(root, text='игрок', font='Arial 16').place(width=115, height=30, x=700, y=130)
  lab_p=Label(root, text=t_lab_p, font='Arial 16').place(width=115, height=30, x=830, y=130)
  ten_min.bind('<Return>', d_d)
  top.wait_window()
d_lab()
#-----------
but_bet=Button(root, text='Бет', font='Arial 16').place(width=115, height=30, x=705, y=335)
but_reys=Button(root, text='Рейз', font='Arial 16').place(width=115, height=30, x=705, y=380)
but_change=Button(root, text='Поменять', font='Arial 16').place(width=115, height=30, x=705, y=425)
but_vsk=Button(root, text='Вскрыться', font='Arial 16').place(width=115, height=30, x=704, y=465)
but_fold=Button(root, text='Фолд', font='Arial 16').place(width=115, height=30, x=830, y=335)
but_kol=Button(root, text='Кол', font='Arial 16').place(width=115, height=30, x=830, y=380)
but_allin=Button(root, text='Олл-ин', font='Arial 15').place(width=115, height=30, x=830, y=425)
but_prod=Button(root, text='Продолжить', font='Arial 15').place(width=115, height=30, x=830, y=465)
def rancard():
  import random
  global mas_namecard, mas_pl_card
  for i in range(len(mas_pl_card)):
    ran=random.randint(0, len(mas_namecard)-1)
    img_pl_card=PhotoImage(file='img_min//'+mas_namecard[ran])
    mas_pl_card[i].config(image=img_pl_card)
rancard()
root.mainloop()
















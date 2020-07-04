from tkinter import *
from tkinter import messagebox as mb
import tkinter
import random
import time

def show_message():
  global chip_numbers, child, rate, r_min, r_max, r_min0
  p1=amount.get()
  p2=rate_min.get()
  p3=rate_max.get()
  chip_numbers=r_min=r_max=r_min0=0
  if p1.isdigit() == False:
    mb.showerror("Ошибка", "Должно быть введено число!")
  elif p2.isdigit() == False:
    mb.showerror("Ошибка", "Должно быть введено число!")
  elif p3.isdigit()== False:
    mb.showerror("Ошибка", "Должно быть введено число!")
  elif int(p1)<5:
    mb.showerror("Ошибка", "Введите колиество фишек больше 4!")
  elif int(p2)<2:
    mb.showerror("Ошибка", "Введите размер минимальной ставки больше 1!")
  elif int(p2)>=int(p1):
    mb.showerror("Ошибка", "Размер минимальной ставки должен быть меньше количества фишек!")
  elif int(p3)>=int(p1):
    mb.showerror("Ошибка", "Размер максимальной ставки должен быть меньше количества фишек!")
  elif int(p3)<int(p2):
    mb.showerror("Ошибка", "Размер максимальной ставки должен быть больше или равен минимальной ставки!")
  else:
    chip_numbers=int(p1)
    r_min=int(p2)
    r_max=int(p3)
    r_min0=r_min
    child.destroy()

def child_window():
  global amount, rate_min, rate_max, child
  child = Toplevel(root)
  child.title("Покер v2.0")
  child.geometry('400x200+{}+{}'.format(wch, hch))
  child.configure(bg='#C1CDCD')

  chip_text=Label(child, anchor="c", text="Введите количество фишек:", font=("Arial", '10'), fg="#000000", bg="#C1CDCD", bd='5')
  chip_text.place(relx=.13, rely=.01, height='22', width = '300')
  amount = Entry(child, width='12',font=('Arial', '12'))
  amount.place(relx=.5, rely=.18, anchor="c")

  rate_min_text=Label(child, anchor="c", text="Введите минимальную ставку:", font=("Arial", '10'), fg="#000000", bg="#C1CDCD", bd='5')
  rate_min_text.place(relx=.13, rely=.23, height='22', width = '300')
  rate_min = Entry(child, width='12',font=('Arial', '12'))
  rate_min.place(relx=.5, rely=.40, anchor="c")

  rate_text=Label(child, anchor="c", text="Введите максимальную ставку:", font=("Arial", '10'), fg="#000000", bg="#C1CDCD", bd='5')
  rate_text.place(relx=.13, rely=.45, height='22', width = '300')
  rate_max = Entry(child, width='12',font=('Arial', '12'))
  rate_max.place(relx=.5, rely=.62, anchor="c")

  message_button = Button(child, text="ОК", bg='#8b8989', width='13', height='2', command=show_message)
  message_button.place(relx=.5, rely=.85, anchor="c")
  child.transient(root)
  child.wait_window() 

def begin():
  global boolcard
  global comb, koloda, cont
  global PL1, PL2
  global ch, sh
  global games, stake, comp_chip_numbers, my_chip_numbers, vic, r_min0, r_min
  stake=0
  if r_min>r_min0: r_min=r_min0
  if games==0: comp_chip_numbers=my_chip_numbers=chip_numbers
  comp_chip_numbers-=r_min
  my_chip_numbers-=r_min
  boolcard=[False,False,False,False,False]
  PL1=['']*5; PL2=['']*5
  comb={1: 'Старшая карта', 2: 'Пара', 3: 'Две пары', 4: 'Тройка (Трипс или Сет)',
        5: 'Стрит (по старшинству)', 6: 'Флеш (одной масти)', 7: 'Фул хауз (три + две)',
        8: 'Каре (четыре)', 9: 'Стрит флеш (по старшинству в масть)', 10: 'Флеш рояль'}
  koloda=['12p.png','13p.png','14p.png','15p.png','16p.png','17p.png','18p.png','19p.png','20p.png','21p.png','22p.png','23p.png','24p.png',
          '12k.png','13k.png','14k.png','15k.png','16k.png','17k.png','18k.png','19k.png','20k.png','21k.png','22k.png','23k.png','24k.png',
          '12b.png','13b.png','14b.png','15b.png','16b.png','17b.png','18b.png','19b.png','20b.png','21b.png','22b.png','23b.png','24b.png',
          '12c.png','13c.png','14c.png','15c.png','16c.png','17c.png','18c.png','19c.png','20c.png','21c.png','22c.png','23c.png','24c.png']
  distribution(PL1); distribution(PL2)


def one_card(PL,k):
  PL[k]=random.choice(koloda)
  koloda.remove(PL[k])
  return PL
      
def distribution(PL):
  for i in range(5):
    one_card(PL,i)
  PL.sort()
  return PL

def out():
  global comp_chip_numbers, my_chip_numbers, chip_numbers, comp_stake, my_stake, games, my_vic, comp_vic, stake
  global img1, img2, But1, But2
  global p_chip, comp_chip, my_chip
  img1=[]; img2=[]
  for i in range(5):
    img1.append(tkinter.PhotoImage(file="img_min\\"+PL1[i]))
    img2.append(tkinter.PhotoImage(file="img_min\\"+"shirt.png")) #PL2[i]
  But1=[]; But2=[]; x=0.01
  for i in range(5):
    But2.append(tkinter.Button(bg = butt_color1, image = img2[i]))
    But2[i].place(relx = x, rely = 0.015, height='160', width = '110')
    But1.append(tkinter.Button(bg = butt_color1, image = img1[i],command=lambda f=i: cl(f)))
    But1[i].place(relx = x, rely = 0.72, height='160', width = '110')
    x+=0.13

  p_chip=tkinter.PhotoImage(file="img_min\\poker_chip.png")
  pl_chip=Label(root, bg = butt_color1, image = p_chip)
  pl_chip.place(relx = .677, rely = .025, height='100', width = '70')
  pl_chip=Label(root, bg = butt_color1, image = p_chip)
  pl_chip.place(relx = .677, rely = .73, height='100', width = '70')
  pl_chip=Label(root, bg = butt_color1, image = p_chip)
  pl_chip.place(relx = .23, rely = .42, height='100', width = '70')
  if stake==0:
    comp_stake=my_stake=r_min0 #начало следующей раздачи (минимальная ставка)

  chips()
  buttons()
  stat()

def stat():
  global games, my_vic, comp_vic
  statistics_text=Label(text="Статистика", font=("Arial", '12', 'bold'), fg="#000000", bg="#00ae42", bd='3', relief=RAISED)
  statistics_text.place(relx = .79, rely = .015, height='31', width = '180')

  stat_play_text=Label(anchor="e", text="Игры", font=("Arial", '12', 'bold'), fg="#000000", bg="#00ae42", bd='2')
  stat_play_text.place(relx = .79, rely = .091, height='28', width = '110')
  stat_play =Label(anchor="e", text=games, font=("Arial", '12', 'bold'), fg="#000000", bg="#00ae42", bd='2')
  stat_play.place(relx=.922, rely=.091, height='28', width = '60')

  stat_comp_text=Label(anchor="e",text="Компьютер", font=("Arial", '12', 'bold'), fg="#000000", bg="#00ae42", bd='2')
  stat_comp_text.place(relx = .79, rely = .162, height='28', width = '110')
  stat_comp =Label(anchor="e", text=comp_vic, font=("Arial", '12', 'bold'), fg="#000000", bg="#00ae42", bd='2')
  stat_comp.place(relx=.922, rely=.162, height='28', width = '60')

  stat_my_text=Label(anchor="e", text="Игрок", font=("Arial", '12', 'bold'), fg="#000000", bg="#00ae42", bd='2')
  stat_my_text.place(relx = .79, rely = .233, height='28', width = '110')
  stat_my =Label(anchor="e", text=my_vic, font=("Arial", '12', 'bold'), fg="#000000", bg="#00ae42", bd='2')
  stat_my.place(relx=.922, rely=.233, height='28', width = '60')
  
def chips():
  global comp_stake, my_stake, comp_chip_numbers, my_chip_numbers
  comp_rate=Label(root, text=comp_stake, font=("Arial", '14', 'bold'), fg="#000000", bg="#C1CDCD", bd='5') #банк компьютера
  comp_rate.place(relx = .33, rely = .44, height='35', width = '90')
  my_rate=Label(root, text=my_stake, font=("Arial", '14', 'bold'), fg="#000000", bg="#C1CDCD", bd='5') #банк игрока
  my_rate.place(relx = .33, rely = .51, height='35', width = '90')    
  comp_chip=Label(text=comp_chip_numbers, font=("Arial", '14', 'bold'), fg="#000000", bg="#C1CDCD", bd='5') #фишки компьютера
  comp_chip.place(relx = .668, rely = .222, height='35', width = '90')
  my_chip=Label(text=my_chip_numbers, font=("Arial", '14', 'bold'), fg="#000000", bg="#C1CDCD", bd='5') #фишки игрока
  my_chip.place(relx = .668, rely = .927, height='35', width = '90')


def buttons():
  global ch, cont, open_up, bet, fold, rase, all_in

  bet = Button(font=("Arial", '11'), text="Бет", bg='#8b8989', command=bet_butt)
  bet.place(relx = 0.78, rely = 0.72, height='35', width = '90')
  fold = Button(font=("Arial", '11'), text="Фолд", bg='#8b8989', command=fold_butt)
  fold.place(relx = 0.89, rely = 0.72, height='35', width = '90')  
  call = Button(font=("Arial", '11'), text="Кол", bg='#8b8989', command=print(1))
  call.place(relx = 0.89, rely = 0.785, height='35', width = '90')
  call.config(state="disabled")  
  rase = Button(font=("Arial", '11'), text="Рейз", bg='#8b8989', command=rase_butt)
  rase.place(relx = 0.78, rely = 0.785, height='35', width = '90')
  all_in = Button(font=("Arial", '11'), text="Олл-ин", bg='#8b8989',command=print(1))
  all_in.place(relx = 0.89, rely = 0.85, height='35', width = '90')
  all_in.config(state="disabled")
  ch = Button(font=("Arial", '11'), text="Поменять", bg='#8b8989',command=change)
  ch.place(relx = 0.78, rely = 0.85, height='35', width = '90')
  ch.config(state="disabled")
  open_up = Button(font=("Arial", '11'), text="Вскрыться", bg='#8b8989', command=show_comp)
  open_up.place(relx = 0.78, rely = 0.93, height='35', width = '90')
  open_up.config(state="disabled")
  cont = Button(font=("Arial", '11'), text="Продолжить", bg='#8b8989',command=cont_butt)
  cont.place(relx = 0.89, rely = 0.93, height='35', width = '90')
  cont.config(state="disabled")
  
def fold_butt():
  global games, comp_chip_numbers, comp_vic, comp_chip, comp_stake, my_stake, stake
  comp_chip_numbers+=comp_stake+my_stake
  comp_vic+=1
  games+=1
  stake=0
  txt="Фолд"
  my_voice(txt)
  
  #my_word=Label(text="           ", font=("Arial", '18', 'bold'), fg="#000000", bg="#228b22")
  #my_word.place(relx = .3, rely = .65, height='35', width = '90')
  begin()
  out()

def rase_butt():
  global child, rase_rate
  txt="Рэйз"
  my_voice(txt)
  child = Toplevel(root)
  child.title("Ставка")
  child.geometry('400x200+{}+{}'.format(wch, hch))
  child.configure(bg='#C1CDCD')
  rate_text=Label(child, anchor="c", text="Ваша ставка:", font=("Arial", '10'), fg="#000000", bg="#C1CDCD", bd='5')
  rate_text.place(relx=.13, rely=.25, height='22', width = '300')

  rase_rate = Entry(child, width='12',font=('Arial', '12'))
  rase_rate.place(relx=.5, rely=.42, anchor="c")
  message_button = Button(child, text="ОК", bg='#8b8989', width='13', height='2', command=err_rase)
  message_button.place(relx=.5, rely=.85, anchor="c")

  child.transient(root)
  child.wait_window()

def err_rase():
  global rase_rate, my_r, my_stake, my_chip_numbers, r_min
  my_r=0
  r=rase_rate.get()
  if r.isdigit() == False:
    mb.showerror("Ошибка", "Должно быть введено число!")
  elif int(r)>r_max:
    mb.showerror("Ошибка", "Ставка не должна превышать максимальную!")
  elif int(r)<=r_min:
    mb.showerror("Ошибка", "Ставка должна превышать минимальную!")
  else:
    r_min=int(r)
    my_stake+=r_min
    my_chip_numbers-=r_min
    chips()
    child.destroy()
    comp_run()

def bet_butt():
  global my_stake, my_chip_numbers, r_min, ch
  txt="Бет   "
  my_voice(txt)
  my_stake+=r_min
  my_chip_numbers-=r_min
  ch.config(state="normal")
  chips()
  comp_run()

def cont_butt():
  global comp_chip_numbers, my_chip_numbers, r_min, r_min0
  begin()
  out()
  text='                                       '
  my_voice(text)
  comp_voice(text)
  comp_chip_numbers-=r_min
  my_chip_numbers-=r_min

def my_voice(t):
  my_word=Label(text=t, font=("Arial", '14', 'bold'), fg="#000000", bg="#228b22")
  my_word.place(relx = .22, rely = .65, height='30', width = '250')

def comp_voice(t):
  comp_word=Label(text=t, font=("Arial", '14', 'bold'), fg="#000000", bg="#228b22")
  comp_word.place(relx = .22, rely = .3, height='30', width = '250')  

def comp_run():
  global m2, PL2, comp_stake, comp_chip_numbers, r_min, r_min0
  m2=combinations(PL2)
  print(m2)
  if m2==1 or m2==2:
    txt="Кол   "
    comp_voice(txt)
    comp_stake+=r_min
    comp_chip_numbers-=r_min
  else:
    txt="Рейз"
    comp_voice(txt)
    comp_stake+=r_max
    comp_chip_numbers-=r_max
    r_min0=r_min
    r_min=r_max
  chips()

def cl(f):
  global boolcard
  if boolcard[f]:
    But1[f].configure(bg=butt_color1)
    boolcard[f]=False
  else:
    But1[f].configure(bg=butt_color2)
    boolcard[f]=True

def change():
  global m1, m2, But1, But2, open_up
  for  i in range(5):
    if boolcard[i]: one_card(PL1,i)
  PL1.sort()
  for i in range(5):
    img1[i]=tkinter.PhotoImage(file="img_min\\"+PL1[i])
  x=0.01
  for i in range(5):
    But1[i]=tkinter.Button(bg = butt_color1, image = img1[i])
    But1[i].place(relx = x, rely = 0.72, height='160', width = '110')
    x+=0.13
  m2=combinations(PL2)
  comp_change(PL2,m2)
  m1=combinations(PL1)
  open_up.config(state="normal")
  
def show_comp():
  global img2, m2, PL2, cont, ch, bet, fold, rase, all_in, comp_stake, my_stake
  for i in range(5):
    img2[i]=tkinter.PhotoImage(file="img_min\\"+PL2[i])
  x=0.01
  for i in range(5):
    But2[i]=tkinter.Button(bg = butt_color1, image = img2[i])
    But2[i].place(relx = x, rely = 0.015, height='160', width = '110')
    x+=0.13
  t1=comb[m1]; t2=comb[m2]
  my_voice(t1); comp_voice(t2)
  victory(m1,m2)
  cont.config(state="normal")
  ch.config(state="disabled")
  open_up.config(state="disabled")
  bet.config(state="disabled")
  fold.config(state="disabled")
  rase.config(state="disabled")
  all_in.config(state="disabled")
  

def combinations(PL):
  marker=1
  k=0
  for i in range(4):
    for j in range(i+1,5):
      if PL[i][:2]==PL[j][:2]: k+=1
  if   k==1: marker=2 #пара
  elif k==2: marker=3 #две пары
  elif k==3: marker=4 #три
  elif k==4: marker=7 #три + две
  elif k==6: marker=8 #четыре
  else:
    n=0; d=0
    for i in range(4):
      if int(PL[i][:2])+1==int(PL[i+1][:2]): n+=1
      if PL[i][2]==PL[i+1][2]: d+=1
    if n==4: marker=5 #стрит (по старшинству)
    if d==4: marker=6 #флеш (одной масти)
    if n==4 and d==4:
      marker=9 #стрит флеш (по старшинству в масть)
      if PL[4][:2]=='24': marker=10 #флеш роял
  return marker

def comp_change(PL,marker):
  #print(marker)
  global m2, ch
  if marker==1:
    t=False
    m=ind=0
    M=['']*5
    for i in range(5):
      M[i]=PL[i][2]
    for i in range(5):
      if M.count(M[i])==4:
        m=M[i]
        t=True
        break
    if t:
      for i in range(5):
        if M[i]!=m: ind=i
      one_card(PL,ind)
    k=0; f=False
    for i in range(3):
      if int(PL[i][:2])+1==int(PL[i+1][:2]): k+=1
    n=0    
    for i in range(1,4):
      if int(PL[i][:2])+1==int(PL[i+1][:2]): n+=1
    if k==3:
      ind=4
      f=True
    if n==3:
      ind=0
    one_card(PL,ind)
    if not t and not f:
      for i in range(4):
        one_card(PL,i)
     
  elif marker==2:
    for i in range(4):
      if int(PL[i][:2])==int(PL[i+1][:2]): break
    ind1=i; ind2=i+1
    PL[ind1],PL[0]=PL[0],PL[ind1]
    PL[ind2],PL[1]=PL[1],PL[ind2]
    for i in range(2,5):
      one_card(PL,i)

  elif marker==3:
    ind=0; t=False; k=0
    for i in range(1,5):
      if PL[ind][:2]==PL[i][:2]:
        ind=4
        break        
    if ind==4:
      for i in range(3,-1,-1):
        if PL[ind][:2]==PL[i][:2]:
          ind=2
          break
    one_card(PL,ind)

  elif marker==4:
    ind1=ind2=0
    if PL[1][:2]==PL[2][:2]==PL[3][:2]:
      ind1=0; ind2=4;
    if PL[0][:2]==PL[1][:2]==PL[2][:2]:
      ind1=3; ind2=4
    if PL[2][:2]==PL[3][:2]==PL[4][:2]:
      ind1=0; ind2=1
    one_card(PL,ind1)
    one_card(PL,ind2)
  PL.sort()
  ch.config(state="disabled")
  m2=combinations(PL2)
  return PL,m2

def victory(m1,m2):
  global comp_chip_numbers, my_chip_numbers, comp_vic, my_vic, comp_stake, my_stake, comp_chip, my_chip, stake, games, r_min, r_min0
  vic=3
  if   m1>m2: vic=1
  elif m1<m2: vic=2
  elif m1==m2:
    if m1==1:
      if   max(PL1)[:2]>max(PL2)[:2]: vic=1
      elif max(PL1)[:2]<max(PL2)[:2]: vic=2
    if m1==2 or m1==3:
      max_card1=max_card2=0
      D1=[0]*5; D2=[0]*5
      for i in range(5):
        D1[i]=int(PL1[i][:2])
        D2[i]=int(PL2[i][:2])
      for i in range(5):
        if D1.count(D1[i])>1: max_card1=D1[i]
        if D2.count(D2[i])>1: max_card2=D2[i] 
      if max_card1>max_card2: vic=1
      elif max_card1<max_card2: vic=2
  if   vic==1:
    my_chip_numbers+=comp_stake+my_stake
    my_vic+=1
  elif vic==2:
    comp_chip_numbers+=comp_stake+my_stake
    comp_vic+=1
  else:
    my_chip_numbers+=my_stake
    comp_chip_numbers+=comp_stake
  comp_stake=my_stake=0
  games+=1
  stake=0
  chips()
  stat()


def main_program():
  global PL1, PL2, my_vic, comp_vic, games
  games=comp_vic=my_vic=0
  begin()
  out()

root = Tk()
root.title("Покер v2.0")
w = root.winfo_screenwidth() # ширина экрана
h = root.winfo_screenheight() # высота экрана
wch=w//2-200
hch=h//2-100
w=w//2-450 # середина экрана
h=h//2-300
butt_color1 = '#228b22'
butt_color2 = '#00543e'
root.geometry('900x600+{}+{}'.format(w, h))
root.configure(bg=butt_color1)
child_window()
main_program()
root.mainloop()


"""PL2=['12b.png','14k.png','17b.png','18b.png','23p.png']
  PL1=['12p.png','14c.png','16p.png','18k.png','23k.png']
  for i in range(5):
    koloda.remove(PL1[i])
    koloda.remove(PL2[i])"""

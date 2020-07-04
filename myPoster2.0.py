from tkinter import *
import smtplib
root=Tk()
root.config(bg='Yellow')
root.title('myPoster')
lab_name=Label(root, width=30, height=2, bg='Yellow', fg='Black', font='Arial 20', text='put here your login')
ent_name=Entry(root, font='Arial 20')
lab_password=Label(root, width=30, height=2, bg='Yellow', fg='Black', font='Ariel 20', text='put here your password')
ent_password=Entry(root, font='Arial 20')

lab_name.pack()
ent_name.pack()
lab_password.pack()
ent_password.pack()

poster=''
but_next=Button(root, height=2, width=10, bg='Red', text='next step')
but_next.pack()
def def_main(event):
    global root, ent_name, ent_name, poster, ent_towhom, ent_letter
    print('in it')
    name=str(ent_name.get())
    password=str(ent_password.get())
    if 'gmail.com' in name:
        poster='smtp.gmail.com'
    elif 'yandex.ru' in name:
        poster='smtp.yandex.ru'
    elif 'mail.ru' in name:
        poster='smtp.mail.ru'
    try:
        smtpObj=smtplib.SMTP(poster, 587)
        smtpObj.starttls()
        smtpObj.login(name, password)
    except Exception:
        print('smth goes wrong')

        root.destroy()
        root=Tk()
        root.config(bg='Yellow')
        root.title('myPoster')
        lab_error=Label(root, width=30, height=2, bg='Yellow', fg='Black', font='Ariel 20', text='login or password is whong')
        lab_error.pack()
    else:
        root.destroy()
        root=Tk()
        root.config(bg='Yellow')
        root.title('myPoster')
        lab_towhom=Label(root, width=30, height=2, bg='Yellow', fg='Black', font='Ariel 20', text='who will be taker of your letter')
        ent_towhom=Entry(root, font='Arial 20')
        lab_letter=Label(root, width=30, height=2, bg='Yellow', fg='Black', font='Ariel 20', text='print here your letter')
        ent_letter=Entry(root, font='Arial 20')
        lab_towhom.pack()
        ent_towhom.pack()
        lab_letter.pack()
        ent_letter.pack()
        but_send=Button(root, height=2, width=10, bg='Red', text='next step')
        but_send.pack()

        def def_send_letter(event):
            global root, ent_towhom, ent_letter, smtObj
            towhom=str(ent_towhom.get())
            letter=str(ent_letter.get())
            
            smtpObj.sendmail(name, towhom, letter)
            print('All right')
            print(name)
            print(towhom)
            print(letter)
            smtpObj.quit()
        but_send.bind('<Button-1>', def_send_letter)
        
but_next.bind('<Button-1>', def_main)

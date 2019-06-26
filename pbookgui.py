def quitt():
    win.destroy() #to destroy the windo

def read():   #to read the data from files
    u=e1.get()
    p=e2.get()
    file=open('demo.txt','r')
    for line in file:
        val=line.split(',')
        un=val[0]
        ps=val[1]
        lc=len(ps)-1
        ps=ps[0:lc]
        if u==un and p==ps:
            loginwin=Tk()
            loginwin.title('loginwindow')
            l8=Label(loginwin,text=('welcome {}'.format(e1.get())))
            l8.place(x=5,y=10)
            break
    else:
        loginwin=Tk()
        loginwin.title('loginwindow')
        l9=Label(loginwin,text=('login failed'))
        l9.place(x=5,y=10)

def signup():   #to add a new data in file
    u=e3.get()
    p=e4.get()
    rp=e5.get()
    if p==rp:
        password=p
        file=open("demo.txt",'a')
        file.write(u)
        file.write(',')
        file.write(p)
        file.write("\n")
        file.close()
        signupwin=Tk()
        signupwin.title('signupwin')
        l10=Label(signupwin,text='thankyou {} for register \nsignup complete'.format(e3.get()))
        l10.place(x=5,y=10)
    else:
        signupwin=Tk()
        signupwin.title('signupwin')
        l11=Label(signupwin,text='Retype password do not match')
        l11.place(x=5,y=10)
       

from tkinter import *   #here gui start
win=Tk()
win.title('pbookgui')
win.geometry('500x500')
l1=Label(win,text='welcome to python book',bg='Blue',fg='Yellow')
l1.place(x=5,y=10)
l2=Label(win,text='Username')
l2.place(x=2,y=40)
l3=Label(win,text='password')
l3.place(x=2,y=80)
e1=Entry(win)
e1.place(x=90,y=40)
e2=Entry(win,show='*')
e2.place(x=90,y=80)
b1=Button(win,text='login',fg='White',bg='Blue',command=read)
b1.place(x=90,y=110)
l4=Label(win,text='New User signup ')
l4.place(x=10,y=150)
l5=Label(win,text='Username')
l5.place(x=2,y=190)
e3=Entry(win)
e3.place(x=90,y=190)
l6=Label(win,text='password')
l6.place(x=2,y=230)
e4=Entry(win,show='*')
e4.place(x=90,y=230)
l7=Label(win,text='Re-password')
l7.place(x=2,y=270)
e5=Entry(win,show='*')
e5.place(x=90,y=270)
b2=Button(win,text='signup',bg='Green',fg='yellow',command=signup)
b2.place(x=90,y=300)
b3=Button(win,text='quit',bg='Red',fg='White',command=quitt)
b3.place(x=150,y=300)


    
        

##importing tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image 
##import mysql.connector




top=tk.Tk()
top.title("Online Purchasing")
img =Image.open("WhatsApp Image 2023-06-30 at 5.03.43 PM.jpeg")
bg = ImageTk.PhotoImage(img)
top.geometry("1200x1200")

label = Label(top, image=bg)
label.place(x = 0,y = 0)

def pur():  
                    messagebox.askquestion("Confirm","Are you sure to purchase?")

def cart():
    global cursor
    s=cursor.execute('SELECT * FROM products')
    name = Label(top, text="---IMAGECON ONLINE SHOPPING---", bg="black", font=("Brush Script MT", 30, 'bold'),
                 fg="white")
    name.pack()
    title = Label(top, text='YOUR CART', bg="gray", font=("Arial black", 15, 'bold'),
                  fg="black").place(x=500, y=75)
    fra1 = Frame(top, bg='white', height=450, width=800)
    fra1.place(x=220, y=130)
    items = Label
    pro = ttk.Treeview(fra1, columns=(1, 2), show='headings', height='8')
    pro.pack()
    pro.heading(1, text='PRODUCT')
    pro.heading(2, text='PRICE')

    a=0
    for x in s:
        tree.insert('', a, text='',values=x)
        a=a+1
    purchase=Button(fra1,text='purchase now ',bg='brown',fg='white',command=pur)
    purchase.pack
    total=Label(fra1,text=x)
    total.pack()
        






def home():
    main = Frame(top, bg="#D3D3D3", height=1000)
    main.pack(fill=X)
    
    global fra
    fra = Frame(main, bg="#6E260E", width=1200, height=1200)
    fra.pack()
    name = Label(fra, text="---IMAGECON ONLINE SHOPPING---", bg="black", font=("Brush Script MT", 30, 'bold'),
                 fg="white").place(x=250,y=20)

    tit = Label(fra, text='SELECT WHICH CATEGORY OF PRODUCT YOUR REQUIRES', font=('Arial black', 15, 'bold'),
                fg='black', height=2, bg="#D3D3D3").place(x=250,y=90)
    # mobiles
    mob = Button(fra, text='MOBILE', width=20, height=5, activebackground='#A04000',
                 foreground='white', bg='#E59866', cursor='circle', font=("Arial", 15, "bold"), command=mobile)
    mob.place(x=450, y=200)

    #tv
    tvb = Button(fra, text='TV', width=20, height=5, activebackground='#A04000',
                 fg='white', bg='#E59866', cursor='circle', font=("Arial", 15, "bold"), command=tv)
    tvb.place(x=450, y=340)

    #acc
    acb = Button(fra, text='ACCESSORYS', width=20, height=5, activebackground='#A04000',
                 fg='white', bg='#E59866', cursor='circle', font=("Arial", 15, "bold"), command=accessories)
    acb.place(x=450, y=480)


    dcb = Button(fra, text='Back to login', width=10, height=2, activebackground='#A04000',
                 fg='white', bg='#E59866', cursor='circle', font=("Arial", 10, "bold"), command=main.destroy)
    dcb.place(x=900, y=530)

    
x = 0

# samsung button
def samb():
    messagebox.showinfo("Message", "SAMSUNG S20 ADDED TO CART")
    global x
    a = 56000
    x += a

# iqoo button
def ib():
    messagebox.showinfo("Message", "IQOO Z7 ADDED TO CART")
    global x
    a = 20000
    x += a

# poco button
def ob():
    messagebox.showinfo("Message", "POCO M2 ADDED TO CART")
    global x
    a = 12000
    x += a

# redmi button
def rb():
    messagebox.showinfo("Message", "REDMI C20 ADDED TO CART")
    global x
    a = 36000
    x += a

# techno button
def tb():
    messagebox.showinfo("Message", "TECHNO C7A ADDED TO CART")
    global x
    a = 12000
    x += a

# realme button
def eb():
    messagebox.showinfo("Message", "REALMI M30 PRO ADDED TO CART")
    global x
    a = 33000
    x += a


def mobile():
    global fra
    ff = Frame(fra,bg='gray')
    ff.pack(fill=X)

    name = Label(ff, text="---ONLINE SHOP NAME---", bg="black", font=("Brush Script MT", 30, 'bold'), fg="white",
                 width=200)
    name.pack()

    f1 = Frame(ff, bg="white", width=1000, height=600)
    f1.pack()
    
    # samsung
    s = Label(f1, text="SUMSUNG S20 ULTRA ", font=("Arial black", 13, "bold"), fg="black", bg='white')
    s.place(x=40, y=20)
    s1 = Label(f1, text="16GB RAM 256GB 📱 ", font=("Comic Sans MS", 10), fg="black", bg='white')
    s1.place(x=40, y=45)
    s2 = Label(f1, text="PRICE : 56000 ✨✨", font=("Arial", 10), fg="black", bg='white')
    s2.place(x=40, y=65)
    s3 = Label(f1, text="★★★★★ ", font=("Arial", 10), fg="#FFAA33", bg='white')
    s3.place(x=40, y=90)
    btns = Button(f1, text="ADD to cart", width=10, height=1, activebackground="#EB984E",
                  fg="white", bg='#F4D03F', cursor='circle', font=("Arial", 10, "bold"), command=samb)
    btns.place(x=250, y=65)

    # iqoo
    i = Label(f1, text="IQOO Z7 ", font=("Arial black", 13, "bold"), fg="black", bg='white')
    i.place(x=40, y=180)
    i1 = Label(f1, text="6GB RAM 128GB 📱 ", font=("Comic Sans MS", 10), fg="black", bg='white')
    i1.place(x=40, y=205)
    i2 = Label(f1, text="PRICE : 20000 ✨✨", font=("Arial", 10), fg="black", bg='white')
    i2.place(x=40, y=230)
    i3 = Label(f1, text="★★★★", font=("Arial", 10), fg="#FFAA33", bg='white')
    i3.place(x=40, y=255)
    btni = Button(f1, text="ADD to cart", width=10, height=1, activebackground="#EB984E",
                  fg="white", bg='#F4D03F', cursor='circle', font=("Arial", 10, "bold"), command=ib)
    btni.place(x=250, y=230)

    # poco
    o = Label(f1, text="POCO M2  ", font=("Arial black", 13, "bold"), fg="black", bg='white')
    o.place(x=40, y=345)
    o1 = Label(f1, text="4GB RAM 64GB 📱 ", font=("Comic Sans MS", 10), fg="black", bg='white')
    o1.place(x=40, y=370)
    o2 = Label(f1, text="PRICE : 12000 ✨✨", font=("Arial", 10), fg="black", bg='white')
    o2.place(x=40, y=395)
    o3 = Label(f1, text="★★★★ ", font=("Arial", 10), fg="#FFAA33", bg='white')
    o3.place(x=40, y=420)
    btno = Button(f1, text="ADD to cart", width=10, height=1, activebackground="#EB984E",
                  fg="white", bg='#F4D03F', cursor='circle', font=("Arial", 10, "bold"), command=ob)
    btno.place(x=250, y=395)

    # redmi
    r = Label(f1, text="REDMI C20 ", font=("Arial black", 13, "bold"), fg="black", bg='white')
    r.place(x=560, y=20)
    r1 = Label(f1, text="12GB RAM 129GB 📱 ", font=("Comic Sans MS", 10), fg="black", bg='white')
    r1.place(x=560, y=45)
    r2 = Label(f1, text="PRICE : 36000 ✨✨", font=("Arial", 10), fg="black", bg='white')
    r2.place(x=560, y=65)
    r3 = Label(f1, text="★★★★★ ", font=("Arial", 10), fg="#FFAA33", bg='white')
    r3.place(x=560, y=90)
    btnr = Button(f1, text="ADD to cart", width=10, height=1, activebackground="#EB984E",
                  fg="white", bg='#F4D03F', cursor='circle', font=("Arial", 10, "bold"), command=rb)
    btnr.place(x=770, y=45)

    # techno
    t = Label(f1, text="TECHNO C7A ", font=("Arial black", 13, "bold"), fg="black", bg='white')
    t.place(x=560, y=180)
    t1 = Label(f1, text="8GB RAM 128GB 📱 ", font=("Comic Sans MS", 10), fg="black", bg='white')
    t1.place(x=560, y=205)
    t2 = Label(f1, text="PRICE : 15000 ✨✨ ", font=("Arial", 10), fg="black", bg='white')
    t2.place(x=560, y=230)
    t3 = Label(f1, text="★★★ ", font=("Arial", 10), fg="#FFAA33", bg='white')
    t3.place(x=560, y=255)
    btnt = Button(f1, text="ADD to cart", width=10, height=1, activebackground="#EB984E",
                  fg="white", bg='#F4D03F', cursor='circle', font=("Arial", 10, "bold"), command=tb)
    btnt.place(x=770, y=230)

    # REALME
    e = Label(f1, text="REALMI M30 PRO ", font=("Arial black", 13, "bold"), fg="black", bg='white')
    e.place(x=560, y=345)
    e1 = Label(f1, text="12GB RAM 6124GB 📱 ", font=("Comic Sans MS", 10), fg="black", bg='white')
    e1.place(x=560, y=370)
    e2 = Label(f1, text="PRICE : 33000 ✨✨", font=("Arial", 10), fg="black", bg='white')
    e2.place(x=560, y=395)
    e3 = Label(f1, text="★★★★ ", font=("Arial", 10), fg="#FFAA33", bg='white')
    e3.place(x=560, y=420)
    btne = Button(f1, text="ADD to cart", width=10, height=1, activebackground="#EB984E",
                  fg="white", bg='#F4D03F', cursor='circle', font=("Arial", 10, "bold"), command=eb)
    btne.place(x=770, y=395)

    # home buttom
    butnh = Button(f1, text='Back To Home', width=40, height=2, activebackground='#2E86C1',
                   fg='white', bg='#5DADE2', cursor='mouse', font=("Arial", 15, "bold")
                   ,command=ff.destroy)
    butnh.place(x=0, y=529)
    butnc = Button(f1, text='Viwe Your Cart', width=40, height=2, activebackground='#D35400',
                   fg='white', bg='#DC7633', cursor='mouse', font=("Arial", 15, "bold"),command=cart)
    butnc.place(x=500, y=529)

#tv page
    #SAM BUTTON
def sab():
    messagebox.showinfo("Message", "SUMSUNG H03 ADDED TO CART")

#amazon button

def ab():
    messagebox.showinfo("Message", "AMAZONBASIS Z100 ADDED TO CART")

#panasonic button
def ob():
    messagebox.showinfo("Message", "PANASONIC S9 ADDED TO CART")

#redmi
def rb():
    messagebox.showinfo("Message", "REDMI z720 ADDED TO CART")

#lg
def lb():
    messagebox.showinfo("Message", "LG 900 ADDED TO CART")

#realmi
def sb():
    messagebox.showinfo("Message", "SONY 3E PRO ADDED TO CART")    

    

##
###title
def tv():
    ff = Frame(fra,bg='gray')
    ff.pack(fill=X)
    name=Label(ff,text="---ONLINE SHOP NAME---",bg="black",font=("Brush Script MT",30,'bold')
       ,fg="white",width=200)
    name.pack()
#frame
    f1 = Frame(ff, bg="white", width=1000, height=600)  
    f1.pack()
###samsung

    s=Label(f1,text="SUMSUNG H03 ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    s.place(x=40,y=20)
    s1=Label(f1,text="4K UHD 32 inchs ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    s1.place(x=40,y=45)
    sS=Label(f1,text="SMART TV ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    sS.place(x=40,y=65)    
    s2=Label(f1,text="PRICE : 25000  ✨",font=("Arial", 10),
        fg="black",bg='white')
    s2.place(x=40,y=90)
    s3=Label(f1,text="★★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    s3.place(x=40,y=115)
    btns=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=sab)
    btns.place(x=300,y=65)

#amazon

    i=Label(f1,text="AMAZONBASIS Z100 ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    i.place(x=40,y=185)
    i1=Label(f1,text="HD SCREEN 28 inches",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    i1.place(x=40,y=210)
    i1=Label(f1,text="NORMAL TV",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    i1.place(x=40,y=230)    
    i2=Label(f1,text="PRICE : 12000  ✨",font=("Arial", 10),
        fg="black",bg='white')
    i2.place(x=40,y=255)
    i3=Label(f1,text="★★★",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    i3.place(x=40,y=280)
    btni=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=ab)
    btni.place(x=300,y=230)
##
###panasonic
    o=Label(f1,text="PANASONIC S9  ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    o.place(x=40,y=355)
    o1=Label(f1,text="FULL HD 48 inches ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    o1.place(x=40,y=385)
    oc=Label(f1,text="SMART TV",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    oc.place(x=40,y=405)    
    o2=Label(f1,text="PRICE : 18000  ✨",font=("Arial", 10),
        fg="black",bg='white')
    o2.place(x=40,y=430)
    o3=Label(f1,text="★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    o3.place(x=40,y=455)
    btno=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=ob)
    btno.place(x=300,y=405)

###sony
    r=Label(f1,text="REDMI z720 ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    r.place(x=560,y=20)
    r1=Label(f1,text="4K ULTRA HD 55 inches",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    r1.place(x=560,y=45)
    r1=Label(f1,text="ANDROID TV",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    r1.place(x=560,y=65)    
    r2=Label(f1,text="PRICE : 30000 ✨✨",font=("Arial", 10),
        fg="black",bg='white')
    r2.place(x=560,y=90)
    r3=Label(f1,text="★★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    r3.place(x=560,y=115)
    btnr=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=rb)
    btnr.place(x=800,y=65)

###LG

    l=Label(f1,text="LG 900 ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    l.place(x=560,y=185)
    l1=Label(f1,text="4K UHD 32 inchs ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    l1.place(x=560,y=210)
    ll=Label(f1,text="NORMAL TV",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    ll.place(x=560,y=230)    
    l2=Label(f1,text="PRICE : 26000  ✨",font=("Arial", 10),
        fg="black",bg='white')
    l2.place(x=560,y=255)
    l3=Label(f1,text="★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    l3.place(x=560,y=280)
    btnl=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=lb)
    btnl.place(x=800,y=230)

###SONY
    o=Label(f1,text="SONY 3E PRO ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    o.place(x=560,y=355)
    o1=Label(f1,text=" HD 32 inches ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    o1.place(x=560,y=385)
    oc=Label(f1,text="ANDROID TV",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    oc.place(x=560,y=405)    
    o2=Label(f1,text="PRICE : 10000  ✨",font=("Arial", 10),
        fg="black",bg='white')
    o2.place(x=560,y=430)
    o3=Label(f1,text="★★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    o3.place(x=560,y=455)
    btno=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=sb)
    btno.place(x=800,y=405)    

    
#home buttom
    
    butnh=Button(f1,text='Back To Home',width=40,height=2,activebackground='#2E86C1',
                 fg='white',bg='#5DADE2',cursor='mouse',font=("Arial", 15, "bold")
                 ,command=ff.destroy)
    butnh.place(x=0,y=529)
    butnc=Button(f1,text='Viwe Your Cart',width=40,height=2,activebackground='#D35400',
                 fg='white',bg='#DC7633',cursor='mouse',font=("Arial", 15, "bold"),command=cart)
    butnc.place(x=500,y=529)


#accessories


#SPEAKER
def sb():
    messagebox.showinfo("Message", "SONY 0071 ADDED TO CART")

#TWS

def tb():
    messagebox.showinfo("Message", "TRUCK AIR BUTS + ADDED TO CART")

#pendrive
def pb():
    messagebox.showinfo("Message", "ZEBRONICS ZEB 2 ADDED TO CART")

#NECKBAND
def nb():
    messagebox.showinfo("Message", "BOAT ROCKERS 260 PRO ADDED TO CART")

#watch
def wb():
    messagebox.showinfo("Message", "SAMSUNG WATCH-4 ADDED TO CART")
##
#mouse
def ab():
    messagebox.showinfo("Message", "ASUS 4.0 ADDED TO CART")    

    

##
###title
def accessories():
    ff = Frame(fra,bg='gray')
    ff.pack(fill=X)
    name=Label(ff,text="---ONLINE SHOP NAME---",bg="black",font=("Brush Script MT",30,'bold')
       ,fg="white",width=200)
    name.pack()

#frame
    f1 = Frame(ff, bg="white", width=1000, height=600)  
    f1.pack()
###samsung

    s=Label(f1,text="SPEAKER ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    s.place(x=40,y=20)
    s1=Label(f1,text="SONY 0071 ",font=("Comic Sans MS", 10,'bold'),
        fg="black",bg='white')
    s1.place(x=40,y=55)
    sS=Label(f1,text="1 HOUR CHARGE = 10 Hr BACKUP",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    sS.place(x=40,y=75)    
    s2=Label(f1,text="PRICE : 2500  ✨",font=("Arial", 10),
        fg="black",bg='white')
    s2.place(x=40,y=100)
    s3=Label(f1,text="★★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    s3.place(x=40,y=125)
    btns=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=sb)
    btns.place(x=300,y=75)

#TWS

    i=Label(f1,text="--TWS-- ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    i.place(x=40,y=195)
    i1=Label(f1,text="TRUCK AIR BUTS +",font=("Comic Sans MS", 10,'bold'),
        fg="black",bg='white')
    i1.place(x=40,y=230)
    i1=Label(f1,text="10 MM DRIVER 12Hr BACKUP",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    i1.place(x=40,y=250)    
    i2=Label(f1,text="PRICE : 1200  ✨",font=("Arial", 10),
        fg="black",bg='white')
    i2.place(x=40,y=275)
    i3=Label(f1,text="★★★★",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    i3.place(x=40,y=300)
    btni=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=tb)
    btni.place(x=300,y=250)
##
###paNDRIVE
    o=Label(f1,text="-PENDRIVE- ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    o.place(x=40,y=365)
    o1=Label(f1,text="ZEBRONICS ZEB 2",font=("Comic Sans MS", 10,'bold'),
        fg="black",bg='white')
    o1.place(x=40,y=405)
    oc=Label(f1,text="256 GB ",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    oc.place(x=40,y=425)    
    o2=Label(f1,text="PRICE : 900  ✨",font=("Arial", 10),
        fg="black",bg='white')
    o2.place(x=40,y=450)
    o3=Label(f1,text="★★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    o3.place(x=40,y=475)
    btno=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=pb)
    btno.place(x=300,y=425)
##
##neckband

    s=Label(f1,text="NECKBAND",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    s.place(x=560,y=20)
    s1=Label(f1,text="BOAT ROCKERS 260 PRO",font=("Comic Sans MS", 10,'bold'),
        fg="black",bg='white')
    s1.place(x=560,y=55)
    sS=Label(f1,text="20MM DRIVER 1 DAY BACKUP",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    sS.place(x=560,y=75)    
    s2=Label(f1,text="PRICE : 1500  ✨",font=("Arial", 10),
        fg="black",bg='white')
    s2.place(x=560,y=100)
    s3=Label(f1,text="★★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    s3.place(x=560,y=125)
    btns=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=nb)
    btns.place(x=800,y=75)
##
##WATCH
    i=Label(f1,text="SMART WATCH",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    i.place(x=560,y=195)
    i1=Label(f1,text="SAMSUNG WATCH-4",font=("Comic Sans MS", 10,'bold'),
        fg="black",bg='white')
    i1.place(x=560,y=230)
    i1=Label(f1,text="BLUETOOTH SUPPORTED 5G",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    i1.place(x=560,y=250)    
    i2=Label(f1,text="PRICE : 12000  ✨",font=("Arial", 10),
        fg="black",bg='white')
    i2.place(x=560,y=275)
    i3=Label(f1,text="★★★★",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    i3.place(x=560,y=300)
    btni=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=wb)
    btni.place(x=800,y=250)
##
#####MOUSE
    o=Label(f1,text="-MOUSE- ",font=("Arial black", 13, "bold"),
        fg="black",bg='white')
    o.place(x=560,y=365)
    o1=Label(f1,text="ASUS 4.0",font=("Comic Sans MS", 10,'bold'),
        fg="black",bg='white')
    o1.place(x=560,y=405)
    oc=Label(f1,text="BLUETOOTH v5.0 STANDBY",font=("Comic Sans MS", 10),
        fg="black",bg='white')
    oc.place(x=560,y=425)    
    o2=Label(f1,text="PRICE : 800  ✨",font=("Arial", 10),
        fg="black",bg='white')
    o2.place(x=560,y=450)
    o3=Label(f1,text="★★★ ",font=("Arial", 10),
        fg="#FFAA33",bg='white')
    o3.place(x=560,y=475)
    btno=Button(f1,text="ADD to cart",width=10,height=1,activebackground="#EB984E",
                fg="white",bg='#F4D03F',cursor='circle',font=("Arial", 10, "bold"),command=ab)
    btno.place(x=800,y=425)
    
#home buttom
    butnh=Button(f1,text='Back To Home',width=40,height=2,activebackground='#2E86C1',
                 fg='white',bg='#5DADE2',cursor='mouse',font=("Arial", 15, "bold")
                 ,command=ff.destroy)
    butnh.place(x=0,y=529)
    butnc=Button(f1,text='Viwe Your Cart',width=40,height=2,activebackground='#D35400',
                 fg='white',bg='#DC7633',cursor='mouse',font=("Arial", 15, "bold"),command=cart)
    butnc.place(x=500,y=529)    


    












def regis():

##        
    f1=Frame(top,height=2000,width=2000,bg='#000033')
    f1.pack(fill=X)

    title=Label(f1,text="ミ★Imagecon online shoping★彡",font=("Times New Roman",40,"bold"),bg="#000033",fg="red")
    title.place(x=250,y=20)

    address=Label(f1,text="New Bus Stand, Salem - 636004",font=("Times New Roman",20,"bold"),bg="#000033",fg="red").place(x=430,y=90)

                        
    copyrght=Label(f1,text="@2023 imagecon online shoping - Salem",font=("Times New Roman",15,"bold"),bg="#000033",fg="red").place(x=400,y=520)

                        
                            


        

                            
    label_3 = Label(f1, text="GENDER", font=("Calibri", 20), bg="white",fg="red")
    label_3.grid(column=0, row=3, padx=50, pady=260)
    data = tk.StringVar()
    ebb_3= ttk.Combobox(f1, textvariable=data)
    ebb_3["values"] = ("MALE", "FEMALE", "TRANSGENDER")
    ebb_3.current(0)  
    ebb_3.grid(column=1, row=2, padx=1, pady=10)
    ebb_3.current()
    ebb_3["values"]=("MALE","FEMALE","TRANSGENDER")
    ebb_3.grid(column=1,row=3)


                    
    label_4=Label(f1,text="DATE_OF_BIRTH",font=("Calibri",20),bg="white",fg="red")
    label_4.place(x=690,y=270)
    ebb_4=Entry(f1)
    ebb_4.place(x=940,y=279,width=220,height=23)
                            
       
                            
        
                            
    label_7=Label(f1,text="MOBILE_NO",font=("Calibri",20),bg="white",fg="red")
    label_7.place(x=50,y=310)
    ebb_7=Entry(f1)
    ebb_7.place(x=250,y=320,width=220,height=23)
                                
    label_8=Label(f1,text="E-MAIL_ID",font=("Calibri",20),bg="white",fg="red")
    label_8.place(x=690,y=320)
    ebb_8=Entry(f1)
    ebb_8.place(x=940,y=329,width=220,height=23)

                                
    label_10=Label(f1,text="USERNAME",font=("Calibri",20),bg="white",fg="red")
    label_10.place(x=50,y=360)
    ebb_10=Entry(f1)
    ebb_10.place(x=250,y=370,width=220,height=23)
                                
    label_11=Label(f1,text="PASSWORD",font=("Calibri",20),bg="white",fg="red")
    label_11.place(x=50,y=410)
    ebb_11=Entry(f1)
    ebb_11.place(x=250,y=410,width=220,height=23)
                                
    label_12=Label(f1,text="CONFIRM_PASSWORD",font=("Calibri",20),bg="white",fg="red")
    label_12.place(x=690,y=370)
    ebb_12=Entry(f1)
    ebb_12.place(x=940,y=380,width=220,height=23)

    nxt=Button(f1,text="Back",activebackground="red",cursor="clock",
                                font=("times new roman",10,"bold"),bg="green",fg="yellow",command=f1.destroy).place(x=100,y=520)
    def save():
##        if (ebb_1.get()=="" or ebb_2.get()=="" or ebb_3.get()=="" or ebb_4.get()=="" or ebb_7.get()=="" or ebb_8.get()=="" or ebb_10.get()=="" or ebb_11.get()=="" or ebb_12.get()==""):
##            messagebox.showerror("Error", "Enter all details")
##        elif (ebb_11.get()!=ebb_12.get()):
##             messagebox.showerror("Error", "Check Both Password")
          if (ebb_2.get()):
              op = messagebox.askyesno("Save", "Do you really want to save?")
              if op > 0:
                connection=mysql.connector.connect(host='localhost',
                                   user='root',password='Kousi7023',database='new')
                print("Conncted successfully")
                cursor=connection.cursor()

                sql_statement=("INSERT INTO registration(last name) VALUES(%s)")
                values=(ebb_2.get())
                cursor.execute(sql_statement,values)
                connection.commit()
                cursor.close()
                connection.close()
                print("database is stored!")


    label_2=Label(f1,text="LAST_NAME",font=("Calibri",20),bg="white",fg="red")
    label_2.place(x=690,y=220)
    ebb_2=Entry(f1)
    ebb_2.place(x=940,y=229,width=220,height=23)
        
    reg_button=tk.Button(f1,text="REGISTER",font=("Times New Roman",15,"bold"),bg="gray",fg="black",command=save)
    reg_button.place(x=500,y=520)

    

                
                

                

 
        

#page2
title=Label(top,text="ミ★Imagecon online shoping★彡",font=("Times New Roman",40,"bold"),bg="#000033",fg="red")
title.place(x=250,y=20)

address=Label(top,text="New Bus Stand, Salem - 636004",font=("Times New Roman",20,"bold"),bg="#000033",fg="red").place(x=430,y=90)

copyrght=Label(top,text="@2023 imagecon online shoping - Salem",font=("Times New Roman",15,"bold"),bg="#000033",fg="white").place(x=50,y=500)
     

user=Label(top,text="username",font=("lucida calligraphy",10,"bold"),bg="white",fg="red").place(x=50,y=250)
n1=Entry(top,font=(20)).place(x=200,y=250)


passwd=Label(top,text="password",font=("lucida calligraphy",10,"bold"),bg="white",fg="red").place(x=50,y=300)

n1=Entry(top,font=(20)).place(x=200,y=300)
        
def func1():
    messagebox.showerror("Hello","Something Wrong")

    
b1=Button(top,text="Submit",activebackground="yellow",cursor='star',font=("Times New Roman",10,"bold"),foreground="red",background="white",command=home).place(x=90,y=400)
b3=Button(top,text="Register",activebackground="yellow",cursor='shuttle',font=("Times New Roman",10,"bold"),foreground="red",background="white",command=regis).place(x=200,y=400)
b2=Button(top,text="Cancel",activebackground="yellow",cursor='clock',font=("Times New Roman",10,"bold"),foreground="red",background="white",command=func1).place(x=310,y=400)
top.mainloop()


from Tkinter import *

root=Tk()
root.configure(background = 'lightblue1')
p=PhotoImage(file="Phonebook-512.gif")
Label(root,image=p).pack()
Label(root,text='Python Project',font='Cambria  15',bg='lightblue1').pack()
Label(root,text='       ',bg='lightblue1').pack()
Label(root,text='CONTACT BOOK',font='Cambria  15',bg='lightblue1').pack()
Label(root,text='       ',bg='lightblue1').pack()
Label(root,text=' Developed by - Nitin bora',font='Cambria  15',bg='lightblue1').pack()
Label(root,text='       ',bg='lightblue1').pack()
Label(root,text='Enrollment number = 181B136',font='Cambria  15',bg='lightblue1').pack()
def close(e=1):
    root.destroy()
root.bind('<Motion>',close)
root.mainloop()

root=Tk()
from tkMessageBox import *

import sqlite3
con=sqlite3.Connection("contact")
cur=con.cursor()

root.configure(background = 'lightblue1')

root.geometry('600x720') 
def fun1():
    x=(a.get(),m.get(),b.get(),e.get(),f.get(),g.get(),h.get(),k.get(),l.get())
    cur.execute('insert into contact(fname,mname,lname ,company ,address,city ,pin , website ,dob)values (?,?,?,?,?,?,?,?,?)',x)
    
  
    cur.execute("select max(id) from contact")
    val=cur.fetchall()
    val=int(val[0][0])
    print val
    
    cur.execute("insert into phone values(?,?,?)",(val,v1.get(),c.get()))
    cur.execute("insert into email values(?,?,?)",(val,v2.get(),d.get()))
    con.commit()
    cur.execute("select * from contact ")
    p=cur.fetchall()
    print p
    cur.execute("select * from phone ")
    p=cur.fetchall()
    print p
    cur.execute("select * from email ")
    p=cur.fetchall()
    print p
    q=showinfo('save','contact saved successfully')
    a.delete(0,END)
    m.delete(0,END)
    b.delete(0,END)
    e.delete(0,END)
    f.delete(0,END)
    g.delete(0,END)
    h.delete(0,END)
    k.delete(0,END)
    l.delete(0,END)
    d.delete(0,END)
    c.delete(0,END)
    
v=0
t=0
def fun2():
    global v
    global t
    root=Tk()
    
    root.configure(background = 'lightblue1')
    Label(root,text='    Searching in Phonebook     ',font='arial,50,Bold').grid(row = 1, column = 0,columnspan = 3,pady=15)
    Label(root,text='Enter name',font='Cambria  14',bg='lightblue1').grid(row = 2, column = 0)
    kn=Entry(root,text='search',width=40,font='Cambria  15')
    kn.grid(row=2,column=1,sticky=W)
    Label(root,text='                                ',bg='lightblue1').grid(row=2,column=2)
    lb=Listbox(root,width=40, height=20,font='Cambria  15')
    lb.grid(row=3,column=1,sticky=E,pady=1)
    def des():
        root.destroy()
    Button(root,text='Close',command=des,font='Cambria  12').grid(row=4,column=1,pady=5)
    def self(e=1):
        global v
        global t
        t=lb.curselection()
        print t
        t=t[0]
        lb.delete(0,END)
        lb.insert(END,"First Name: {}".format(v[t][1]))
        lb.insert(END,"Middle Name: {}".format(v[t][2]))
        lb.insert(END,"Last Name: {}".format(v[t][3]))
        lb.insert(END,"Commpany: {}".format(v[t][4]))
        lb.insert(END,"Address: {}".format(v[t][5]))
        lb.insert(END,"City: {}".format(v[t][6]))
        lb.insert(END,"Pincode: {}".format(v[t][7]))
        lb.insert(END,"Website: {}".format(v[t][8]))
        lb.insert(END,"Date of Birth: {}".format(v[t][9]))
        print "NO",v[t][0]
        cur.execute('select * from phone where id=?',(v[t][0],))
        ph=cur.fetchall()
        print "PH",ph
        lb.insert(END,"Phone: {}".format(ph[0][2]))
        cur.execute('select * from email p where p.id=?',(v[t][0],))
        ph2=cur.fetchall()
        print ph2
        lb.insert(END,"Email: {}".format(ph2[0][2]))
        print ph2
        def edit():
            
            root=Tk()
            def des2():
                root.destroy()
            root.configure(background = 'lightblue1')
            j=0
            i=0
            Label(root,text="First name",font='Cambria  14' ,bg='lightblue1').grid(row=i,column=j,sticky=W,pady=1)
            a1=Entry(root,width=30,font='Cambria  14')
            j+=1
            a1.grid(row=i,column=j)
            i+=1
            a1.insert(0,v[t][1])
            j=0
            Label(root,text="Middle name",font='Cambria  14' ,bg='lightblue1').grid(row=i,column=j,sticky=W,pady=1)
            m1=Entry(root,width=30,font='Cambria  14')
            j+=1
            m1.grid(row=i,column=j)
            i+=1
            m1.insert(0,v[t][2])
            j=0
            Label(root,text="Last name",font='Cambria  14' ,bg='lightblue1').grid(row=i,column=j,sticky=W,pady=1)
            b1=Entry(root,width=30,font='Cambria  14')
            j+=1
            b1.grid(row=i,column=j)
            i+=1
            b1.insert(0,v[t][3])

            j=0
            Label(root,text="Phone number",font='Cambria  14' ,bg='lightblue1').grid(row=i,column=j,sticky=W,pady=1)
            c1=Entry(root,width=30,font='Cambria  14')
            j+=1
            c1.grid(row=i,column=j)
            i+=1
            c1.insert(0,ph[0][2])
            j=0
            Label(root,text="Email ",font='Cambria  14' ,bg='lightblue1').grid(row=i,column=j,sticky=W,pady=1)
            d1=Entry(root,width=30,font='Cambria  14')
            j+=1
            d1.grid(row=i,column=j)
            i+=1
            d1.insert(0,ph2[0][2])

            j=0
            Label(root,text="Company name ",font='Cambria  14',bg='lightblue1').grid(row=i,column=j,sticky=W,pady=1)
            e1=Entry(root,width=30,font='Cambria  14')
            j+=1
            e1.grid(row=i,column=j)
            i+=1
            e1.insert(0,v[t][4])
            j=0
            Label(root,text="Address",font='Cambria  14' ,bg='lightblue1').grid(row=i,column=j,sticky=W,pady=1)
            f1=Entry(root,width=30,font='Cambria  14')
            j+=1
            f1.grid(row=i,column=j)
            i+=1
            f1.insert(0,v[t][5])
            j=0
            Label(root,text="City",font='Cambria  14' ,bg='lightblue1').grid(row=i,column=j,sticky=W,pady=1)
            g1=Entry(root,width=30,font='Cambria  14')
            j+=1
            g1.grid(row=i,column=j)
            i+=1
            g1.insert(0,v[t][6])
            j=0
            Label(root,text="Pincode" ,font='Cambria  14',bg='lightblue1').grid(row=i,column=j,sticky=W,pady=1)
            h1=Entry(root,width=30,font='Cambria  14')
            j+=1
            h1.grid(row=i,column=j)
            i+=1
            h1.insert(0,v[t][7])
            j=0
            Label(root,text="Website",font='Cambria  14',bg='lightblue1' ).grid(row=i,column=j,sticky=W,pady=1)
            k1=Entry(root,width=30,font='Cambria  14')
            j+=1
            k1.grid(row=i,column=j)
            i+=1
            k1.insert(0,v[t][8])
            j=0
            Label(root,text="Date of birth",font='Cambria  14',bg='lightblue1' ).grid(row=i,column=j,sticky=W,pady=1)
            l1=Entry(root,width=30,font='Cambria  14')
            j+=1
            l1.insert(0,v[t][9])
            l1.grid(row=i,column=j)
            i+=1
            def save():
                print "t"
                cur.execute('update contact set fname=?,mname=?,lname=?,company=?,address=?,city=?,pin=?,website=?,dob=? where id=?',(a1.get(),m1.get(),b1.get(),e1.get(),f1.get(),g1.get(),h1.get(),k1.get(),l1.get(),v[t][0]))
                cur.execute('update phone set pno=? where id=?',(c1.get(),v[t][0]))
                cur.execute('update email set email=? where id=?',(d1.get(),v[t][0]))
                con.commit()
                showinfo('update','Contact updated Successfully')
                des2()
                
            def close2():
                root.destroy()
            Button(root,text='Save',command=save,font='Cambria  12').grid(row=i,column=j,pady=8)
            Button(root,text='close',command=close2,font='Cambria  12').grid(row=i,column=j+1,pady=8)
            root.mainloop()
        def delete():
            que=askyesno('Delete','Are you sure want to delete')
            if que==True:
                cur.execute('DELETE FROM contact WHERE fname=?',(v[t][1],))
                showinfo('Delete','Contact deleted successfully')
                con.commit()
            
        Button(root,text='Edit',command=edit,font='Cambria  12').grid(row=4,column=3,pady=8)
        Button(root,text='Delete',command=delete,font='Cambria  12').grid(row=4,column=2,pady=8)
    def click(e=1):
        global v
        lb.delete(0,END)
        cur.execute("select * from contact where fname LIKE '%{}%' OR mname like '%{}%' or lname like '%{}%' ".format(kn.get(),kn.get(),kn.get()) )
        v=cur.fetchall()
        print v
        for i in range(len(v)):
            v1=v[i][1]+" "+v[i][2]+" "+v[i][3]
            lb.insert(END,v1)
            items=lb.curselection()
            print items
            lb.bind("<Double-Button-1>", self)
    kn.bind("<KeyPress>",click)
    
    root.mainloop()
    
def fun3():
    root.destroy()

def fun4():
    showinfo('edit','To edit , go to search window')
    
i=IntVar()
i=0
j=IntVar()
j=0
v1=IntVar()
v2=IntVar()

j+=1
p=PhotoImage(file="Phonebook-512.gif")
Label(root,image=p).grid(row=i,column=j)  

i+=1
Label(root,text="CONTACT BOOK",font='arial  25  bold' ,bg='lightblue1').grid(row=i,column=j,sticky=W,pady=15)
i+=1

j=0
Label(root,text="First name",font='Cambria  12' ,bg='lightblue1').grid(row=i,column=j,sticky=W)
a=Entry(root)
j+=1
a.grid(row=i,column=j)
i+=1

j=0
Label(root,text="Middle name",font='Cambria  12' ,bg='lightblue1').grid(row=i,column=j,sticky=W)
m=Entry(root)
j+=1
m.grid(row=i,column=j)
i+=1

j=0
Label(root,text="Last name",font='Cambria  12' ,bg='lightblue1').grid(row=i,column=j,sticky=W)
b=Entry(root)
j+=1
b.grid(row=i,column=j)
i+=1

j=0
Label(root,text='Select Phone Type',font='Cambria  12',bg='lightblue1').grid(row=i,column=j,sticky=W)
j=+1
Radiobutton(root,text='Home',font='Cambria  12',bg='lightblue1',variable=v1,value=1).grid(row=i,column=j)
j+=1
Radiobutton(root,text='Office',font='Cambria  12',bg='lightblue1',variable=v1,value=2).grid(row=i,column=j)
i+=1

j=0
Label(root,text="Phone number",font='Cambria  12' ,bg='lightblue1').grid(row=i,column=j,sticky=W)
c=Entry(root)
def con1():
    showinfo('stay tune for next update', 'Sorry this button is under construction')
Button(root,text="+",command=con1).grid(row=i,column=j+2)

j+=1
c.grid(row=i,column=j)
i+=1

j=0
Label(root,text='Select Email Type',font='Cambria  12',bg='lightblue1').grid(row=i,column=j,sticky=W)
j=+1
Radiobutton(root,text='Home',font='Cambria  12',bg='lightblue1',variable=v2,value=1).grid(row=i,column=j)
j+=1
Radiobutton(root,text='Office',font='Cambria  12',bg='lightblue1',variable=v2,value=2).grid(row=i,column=j)
i+=1

j=0
Label(root,text="Email ",font='Cambria  12' ,bg='lightblue1').grid(row=i,column=j,sticky=W)
d=Entry(root)
Button(root,text="+",command=con1).grid(row=i,column=j+2)
j+=1
d.grid(row=i,column=j)
i+=1

j=0
Label(root,text="Company name ",font='Cambria  12',bg='lightblue1').grid(row=i,column=j,sticky=W)
e=Entry(root)
j+=1
e.grid(row=i,column=j)
i+=1

j=0
Label(root,text="Address",font='Cambria  12' ,bg='lightblue1').grid(row=i,column=j,sticky=W)
f=Entry(root)
j+=1
f.grid(row=i,column=j)
i+=1

j=0
Label(root,text="City",font='Cambria  12' ,bg='lightblue1').grid(row=i,column=j,sticky=W)
g=Entry(root)
j+=1
g.grid(row=i,column=j)
i+=1

j=0
Label(root,text="Pincode" ,font='Cambria  12',bg='lightblue1').grid(row=i,column=j,sticky=W)
h=Entry(root)
j+=1
h.grid(row=i,column=j)
i+=1

j=0
Label(root,text="Website",font='Cambria  12',bg='lightblue1' ).grid(row=i,column=j,sticky=W)
k=Entry(root)
j+=1
k.grid(row=i,column=j)
i+=1

j=0
Label(root,text="Date of birth",font='Cambria  12',bg='lightblue1' ).grid(row=i,column=j,sticky=W)
l=Entry(root)
j+=1
l.grid(row=i,column=j)
i+=1

j=0
Button(root,text='Save',font='Cambria  12',command=fun1).grid(row=i,column=j,pady=9)
j+=1
Button(root,text='Search',font='Cambria  12',command=fun2).grid(row=i,column=j,pady=9)
j+=1
Button(root,text='Close',font='Cambria  12',command=fun3).grid(row=i,column=j,pady=9)
j+=1
Button(root,text='Edit',font='Cambria  12',command=fun4).grid(row=i,column=j,pady=9)

##sql

cur.execute('create table if not exists contact ( id integer primary key autoincrement ,fname varchar(200),mname varchar(200),lname varchar(200),company varchar(200),address varchar(200),city varchar(200),pin number(10), website varchar(200), dob date)') 
cur.execute('create table if not exists phone ( id integer, ctype varchar(2) ,pno number(11) , primary key(pno,id),foreign key(id) references contact(id))')
cur.execute('create table if not exists email ( id integer, etype varchar(2) ,email varchar(110) , primary key(email,id),foreign key(id) references contact(id))')

root.mainloop()

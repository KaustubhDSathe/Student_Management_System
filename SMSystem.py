def addstudent():
    def submitadd():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        
        try:
            strr = 'insert into studentdata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr,(id,name,mobile,email,address,gender,dob,addeddate,addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notificatrions','Id {} Name {} Added sucessfully.. and want to clean the form'.format(id,name),parent=addroot)
            if(res==True):
                idval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                dobval.set('')
        except:
            messagebox.showerror('Notifications','Id Already Exist try another id...',parent=addroot)
        strr = 'select * from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenmttable.delete(*studenmttable.get_children())
        for i in  datas:
            vv = [i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            studenmttable.insert('',END,values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('640x530+220+200')
    addroot.title('Student Management System')
    addroot.config(bg='skyblue')
    addroot.iconbitmap('mana.ico')
    addroot.resizable(False,False)
    #--------------------------------------------------- Add studenmt Labels
    idlabel = Label(addroot,text='Enter Id : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=2,width=12,anchor='w')
    idlabel.place(x=10,y=30)

    namelabel = Label(addroot,text='Enter Name : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=2,width=12,anchor='w')
    namelabel.place(x=10,y=90)

    mobilelabel = Label(addroot,text='Enter Mobile : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=2,width=12,anchor='w')
    mobilelabel.place(x=10,y=150)

    emaillabel = Label(addroot,text='Enter Email : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=2,width=12,anchor='w')
    emaillabel.place(x=10,y=210)

    addresslabel = Label(addroot,text='Enter Address : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=2,width=12,anchor='w')
    addresslabel.place(x=10,y=270)

    genderlabel = Label(addroot,text='Enter Gender : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=2,width=12,anchor='w')
    genderlabel.place(x=10,y=330)

    doblabel = Label(addroot,text='Enter D.O.B : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=2,width=12,anchor='w')
    doblabel.place(x=10,y=390)

    ##----------------------------------------------------------- Add student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()

    identry = Entry(addroot,font=('roman',20),bd=5,textvariable=idval)
    identry.place(x=300,y=30)

    nameentry = Entry(addroot,font=('roman',20),bd=5,textvariable=nameval)
    nameentry.place(x=300,y=90)

    mobileentry = Entry(addroot,font=('roman',20),bd=5,textvariable=mobileval)
    mobileentry.place(x=300,y=150)

    emailentry = Entry(addroot,font=('roman',20),bd=5,textvariable=emailval)
    emailentry.place(x=300,y=210)

    addressentry = Entry(addroot,font=('roman',20),bd=5,textvariable=addressval)
    addressentry.place(x=300,y=270)

    genderentry = Entry(addroot,font=('roman',20),bd=5,textvariable=genderval)
    genderentry.place(x=300,y=330)

    dobentry = Entry(addroot,font=('roman',20),bd=5,textvariable=dobval)
    dobentry.place(x=300,y=390)
    ############------------------------- add button
    submitbtn = Button(addroot,text='Submit',font=('roman',15),width=20,bd=5,activebackground='blue',activeforeground='white',
                      bg='ivory2',command=submitadd)
    submitbtn.place(x=150,y=460)



    addroot.mainloop()

def searchstudent():
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if(id != ''):
            strr = 'select *from studentdata1 where id=%s'
            mycursor.execute(strr,(id))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif(name != ''):
            strr = 'select *from studentdata1 where name=%s'
            mycursor.execute(strr,(name))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif(mobile != ''):
            strr = 'select *from studentdata1 where mobile=%s'
            mycursor.execute(strr,(mobile))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif(email != ''):
            strr = 'select *from studentdata1 where email=%s'
            mycursor.execute(strr,(email))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif(address != ''):
            strr = 'select *from studentdata1 where address=%s'
            mycursor.execute(strr,(address))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif(gender != ''):
            strr = 'select *from studentdata1 where gender=%s'
            mycursor.execute(strr,(gender))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)
        elif(dob != ''):
            strr = 'select *from studentdata1 where dob=%s'
            mycursor.execute(strr,(dob))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)

        elif(addeddate != ''):
            strr = 'select *from studentdata1 where addeddate=%s'
            mycursor.execute(strr,(addeddate))
            datas = mycursor.fetchall()
            studenmttable.delete(*studenmttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenmttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('640x560+220+200')
    searchroot.title('Student Management System')
    searchroot.config(bg='skyblue')
    searchroot.iconbitmap('mana.ico')
    searchroot.resizable(False,False)
    #--------------------------------------------------- Add studenmt Labels
    idlabel = Label(searchroot,text='Enter Id : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=30)

    namelabel = Label(searchroot,text='Enter Name : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=90)

    mobilelabel = Label(searchroot,text='Enter Mobile : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=150)

    emaillabel = Label(searchroot,text='Enter Email : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=210)

    addresslabel = Label(searchroot,text='Enter Address : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=270)

    genderlabel = Label(searchroot,text='Enter Gender : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=330)

    doblabel = Label(searchroot,text='Enter D.O.B : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=390)

    #datelabel = Label(searchroot,text='Enter Date : ',bg='skyblue3',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    #datelabel.place(x=10,y=450)

    ##----------------------------------------------------------- Add student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()

    identry = Entry(searchroot,font=('roman',20),bd=5,textvariable=idval)
    identry.place(x=300,y=30)

    nameentry = Entry(searchroot,font=('roman',20),bd=5,textvariable=nameval)
    nameentry.place(x=300,y=90)

    mobileentry = Entry(searchroot,font=('roman',20),bd=5,textvariable=mobileval)
    mobileentry.place(x=300,y=150)

    emailentry = Entry(searchroot,font=('roman',20),bd=5,textvariable=emailval)
    emailentry.place(x=300,y=210)

    addressentry = Entry(searchroot,font=('roman',20),bd=5,textvariable=addressval)
    addressentry.place(x=300,y=270)

    genderentry = Entry(searchroot,font=('roman',20),bd=5,textvariable=genderval)
    genderentry.place(x=300,y=330)

    dobentry = Entry(searchroot,font=('roman',20),bd=5,textvariable=dobval)
    dobentry.place(x=300,y=390)

    #dateentry = Entry(searchroot,font=('roman',20,'bold'),bd=5,textvariable=dateval)
    #dateentry.place(x=300,y=450)
    ############------------------------- add button
    submitbtn = Button(searchroot,text='Submit',font=('roman',15),width=20,bd=5,activebackground='blue',activeforeground='white',
                      bg='ivory2',command=search)
    submitbtn.place(x=150,y=490)



    searchroot.mainloop()
def deletestudent():
    cc = studenmttable.focus()
    content = studenmttable.item(cc)
    pp = content['values'][0]
    strr = 'delete from studentdata1 where id=%s'
    mycursor.execute(strr,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(pp))
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenmttable.delete(*studenmttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenmttable.insert('', END, values=vv)

def deleteall():
    #kk=studenmttable.focus()
    #content=studenmttable.item(kk)
    #ss=content['values'][0]
    strr='delete from studentdata1'
    mycursor.execute(strr)
    con.commit()
    messagebox.showinfo('Notifications','Successfully Deleted')
    #strr = 'select *from studentdata1'
    #mycursor.execute(strr)

def updatestudent():
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        strr = 'update studentdata1 set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        mycursor.execute(strr,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id),parent=updateroot)
        strr = 'select *from studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenmttable.delete(*studenmttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenmttable.insert('', END, values=vv)


    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('640x565+220+160')
    updateroot.title('Student Management System')
    updateroot.config(bg='skyblue')
    updateroot.iconbitmap('mana.ico')
    updateroot.resizable(False,False)
    #--------------------------------------------------- Add studenmt Labels
    idlabel = Label(updateroot,text='Enter Id : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=30)

    namelabel = Label(updateroot,text='Enter Name : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=90)

    mobilelabel = Label(updateroot,text='Enter Mobile : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=150)

    emaillabel = Label(updateroot,text='Enter Email : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=210)

    addresslabel = Label(updateroot,text='Enter Address : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=270)

    genderlabel = Label(updateroot,text='Enter Gender : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=330)

    doblabel = Label(updateroot,text='Enter D.O.B : ',bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=390)
    
    

    #datelabel = Label(updateroot,text='Enter Date : ',bg='skyblue3',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    #datelabel.place(x=10,y=450)

    #timelabel = Label(updateroot,text='Enter Time : ',bg='skyblue3',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    #timelabel.place(x=10,y=510)

    ##----------------------------------------------------------- Add student Entry
    idval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    dobval = StringVar()
    dateval = StringVar()
    timeval = StringVar()

    identry = Entry(updateroot,font=('roman',20),bd=5,textvariable=idval)
    identry.place(x=300,y=30)

    nameentry = Entry(updateroot,font=('roman',20),bd=5,textvariable=nameval)
    nameentry.place(x=300,y=90)

    mobileentry = Entry(updateroot,font=('roman',20),bd=5,textvariable=mobileval)
    mobileentry.place(x=300,y=150)

    emailentry = Entry(updateroot,font=('roman',20),bd=5,textvariable=emailval)
    emailentry.place(x=300,y=210)

    addressentry = Entry(updateroot,font=('roman',20),bd=5,textvariable=addressval)
    addressentry.place(x=300,y=270)

    genderentry = Entry(updateroot,font=('roman',20),bd=5,textvariable=genderval)
    genderentry.place(x=300,y=330)

    dobentry = Entry(updateroot,font=('roman',20),bd=5,textvariable=dobval)
    dobentry.place(x=300,y=390)

    #dateentry = Entry(updateroot,font=('roman',20,'bold'),bd=5,textvariable=dateval)
    #dateentry.place(x=300,y=450)

    #timeentry = Entry(updateroot,font=('roman',20,'bold'),bd=5,textvariable=dateval)
    #timeentry.place(x=300,y=510)
    ############------------------------- add button
    submitbtn = Button(updateroot,text='Submit',font=('roman',15),width=20,bd=5,activebackground='blue',activeforeground='white',
                      bg='ivory2',command=update)
    submitbtn.place(x=160,y=500)
    cc = studenmttable.focus()
    content = studenmttable.item(cc)
    pp = content['values']
    if(len(pp) != 0):
        idval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        dobval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])

    updateroot.mainloop()
def showstudent():
    strr = 'select *from studentdata1'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    studenmttable.delete(*studenmttable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenmttable.insert('', END, values=vv)




def exitstudent():
    res = messagebox.askyesnocancel('Notification','Do you want to exit?')
    if(res == True):
        root.destroy()


###################################################################################Connecttion of Database
def Connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host,user=user,password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications','Data is incorrect please try again',parent=dbroot)
            return
        try:
            strr = 'create database studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'create table studentdata1(id int,name varchar(20),mobile varchar(12),email varchar(30),address varchar(100),gender varchar(50),dob varchar(50),date varchar(50),time varchar(50))'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int not null'
            mycursor.execute(strr)
            strr = 'alter table studentdata1 modify column id int primary key'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','database created and now you are connected connected to the database ....',parent=dbroot)

        except:
            strr = 'use studentmanagementsystem1'
            mycursor.execute(strr)
            messagebox.showinfo('Notification','Now you are connected to the database ....',parent=dbroot)
        dbroot.destroy()



    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap('mana.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='skyblue')
    #-------------------------------Connectdb Labels
    hostlabel = Label(dbroot,text="Enter Host : ",bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot,text="Enter User : ",bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    userlabel.place(x=10,y=70)

    passwordlabel = Label(dbroot,text="Enter Password : ",bg='skyblue3',font=('times',20),relief=GROOVE,borderwidth=3,width=13,anchor='w')
    passwordlabel.place(x=10,y=130)

    #-------------------------Connectdb Entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry = Entry(dbroot,font=('roman',15),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot,font=('roman',15),bd=5,textvariable=userval)
    userentry.place(x=250,y=70)

    passwordentry = Entry(dbroot,font=('roman',15),bd=5,textvariable=passwordval)
    passwordentry.place(x=250,y=130)

    #-------------------------------- Connectdb button
    submitbutton = Button(dbroot,text='Submit',font=('roman',15),bg='ivory2',bd=5,width=20,activebackground='blue',
                          activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=190)

    dbroot.mainloop()
###########################################
def tick():
    time_string = time.strftime("%H:%M:%S")
    date_string = time.strftime("%d/%m/%Y")
    clock.config(text='Date :'+date_string+"\n"+"Time : "+time_string)
    clock.after(200,tick)
#######################################INTRO SLIDER
import random
colors = ['black']
def IntroLabelColorTick():
    fg = random.choice(colors)
    SliderLabel.config(fg=fg)
    SliderLabel.after(2,IntroLabelColorTick)
def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count = 0
        text = ''
        SliderLabel.config(text=text)
    else:
        text = text+ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(300,IntroLabelTick)
#########################################################################################################
def about():
    messagebox.showinfo("Info","This is the project developed by students of DYPIEMR for OYTIE PVT.LTD.")
    
##########################################################################################################
from tkinter import *
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
#import pandas
import pymysql
import time
root = Tk()
root.title('Student Management System')
root.config(bg='burlywood1')
root.geometry('1470x750+200+50')
root.iconbitmap('mana.ico')
root.resizable(False,False)
############################################################################################################  Frames
##---------------------------------------------------------------------------- dataentry frame

DataEntryFrame = Frame(root,bg='skyblue',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=100,width=450,height=630)
frontlabel = Label(DataEntryFrame,text='--------------Data Entry--------------',width=30,font=('AdonisC',22,'italic bold'),bg='skyblue')
frontlabel.pack(side=TOP,expand=True)
addbtn = Button(DataEntryFrame,text='1. Add Student',width=25,font=('AdonisC',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn = Button(DataEntryFrame,text='2. Search Student',width=25,font=('AdonisC',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn = Button(DataEntryFrame,text='3. Delete Student',width=25,font=('AdonisC',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn = Button(DataEntryFrame,text='4. Update Student',width=25,font=('AdonisC',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=updatestudent)
updatebtn.pack(side=TOP,expand=True)

showallbtn = Button(DataEntryFrame,text='5. Show All',width=25,font=('AdonisC',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=showstudent)
showallbtn.pack(side=TOP,expand=True)

resetbtn = Button(DataEntryFrame,text='5. Reset',width=25,font=('AdonisC',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=deleteall)
resetbtn.pack(side=TOP,expand=True)


exitbtn = Button(DataEntryFrame,text='7.  Exit',width=25,font=('AdonisC',20,'bold'),bd=6,bg='skyblue3',activebackground='blue',relief=RIDGE,
                activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)

##-----------------------------------------------------------Show data frame
ShowDataFrame = Frame(root,bg='gold2',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=500,y=100,width=920,height=630)

##-------------------------------------------------  Showdataframe
style = ttk.Style()
style.configure('Treeview.Heading',font=('AdonisC',20,'bold'),foreground='blue')
style.configure('Treeview',font=('times',15,'bold'),background='burlywood1',foreground='black')
scroll_x = Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame,orient=VERTICAL)
studenmttable = Treeview(ShowDataFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B'),
                         yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=studenmttable.xview)
scroll_y.config(command=studenmttable.yview)
studenmttable.heading('Id',text='Id')
studenmttable.heading('Name',text='Name')
studenmttable.heading('Mobile No',text='Mobile No')
studenmttable.heading('Email',text='Email')
studenmttable.heading('Address',text='Address')
studenmttable.heading('Gender',text='Gender')
studenmttable.heading('D.O.B',text='D.O.B')
#studenmttable.heading('Added Date',text='Added Date')
#studenmttable.heading('Added Time',text='Added Time')
studenmttable['show'] = 'headings'
studenmttable.column('Id',width=100)
studenmttable.column('Name',width=200)
studenmttable.column('Mobile No',width=200)
studenmttable.column('Email',width=300)
studenmttable.column('Address',width=200)
studenmttable.column('Gender',width=100)
studenmttable.column('D.O.B',width=150)
#studenmttable.column('Added Date',width=150)
#studenmttable.column('Added Time',width=150)
studenmttable.pack(fill=BOTH,expand=1)

################################################################################################################  Slider
ss = 'Welcome To Student Management System'
count = 0
text = ''
##################################
SliderLabel = Label(root,text=ss,font=('AdonisC',30,'italic bold'),relief='sunken',borderwidth=4,width=37,bg='slategray1')
SliderLabel.place(x=290,y=0)
IntroLabelTick()
IntroLabelColorTick()
############################################################################################################### clock
clock = Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='skyblue3')
clock.place(x=0,y=0)
tick()
################################################################################################################## ConnectDatabaseButton
connectbutton = Button(root,text='Connect To Database',width=17,font=('AdonisC',18,'italic bold'),relief=RIDGE,borderwidth=4,bg='skyblue2',
                       activebackground='blue',activeforeground='white',command=Connectdb)
connectbutton.place(x=1205,y=0)

#################################################################################################################aboutbutton
connectbutton = Button(root,text='About',width=7,font=('AdonisC',18,'italic bold'),relief=RIDGE,borderwidth=4,bg='skyblue2',
                       activebackground='blue',activeforeground='white',command=about)
connectbutton.place(x=158,y=0)
root.mainloop()

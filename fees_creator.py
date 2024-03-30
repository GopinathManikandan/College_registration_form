from tkinter import *
import tkinter.ttk as ttk
from tkinter import messagebox
def co():
    

    frame=Tk()
    frame.geometry("1920x1080")
    label=Label(frame,text="-----FEES REGISTER-----",font=("arial","20","italic","bold"))
    label.pack()

    #adding menu bar
    menubar=Menu(frame)
    file=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="File",menu=file)

    #components of menubar
    file.add_command(label="New file!",command=None)
    file.add_command(label="open",command=None)
    file.add_command(label="Save",command=None)
    file.add_separator()
    def hi3():                   #destroy the screen
        frame.destroy()

    file.add_command(label="Exit",command=hi3)

    #adding edit bar
    frame.configure(menu=menubar)
    edit=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Edit",menu=edit)
    edit.add_command(label="Cut",command=None)
    edit.add_command(label="Copy",command=None)
    edit.add_command(label="Paste",command=None)
    edit.add_separator()

    #adding options of help button

    help_=Menu(menubar,tearoff=0)
    menubar.add_cascade(label="Help",menu=help_)
    help_.add_command(label="license",command=None)
    help_.add_command(label="contact",command=None)
    help_.add_command(label="about us",command=None)
    help_.add_separator()
    help_.add_command(label="About Tk",command=None)

    #name of the student
    place1=StringVar()
    a11=Label(frame,text = "Name",font=("","18","")).place(x=80,y=80)  
    a1 = Entry(frame,font=("","18",""),textvariable=place1).place(x=250,y=80)

    #student dept
    place2=StringVar()
    combo_box=Label(frame,text="Dept",font=("","18","")).place(x=1100,y=80)
    course_selection=["--select Course--","Ai&Ds","Mech Engg", "Civil Engg", "ECE", "EEE", "CSE", "Aero Engg", "BME", "Cyber Security", "Mechatronics Engg", "Marine Engg"]
    combo=ttk.Combobox(frame,values=course_selection,width=20,height = 20,textvariable=place2)
    combo.place(x=1230,y=85)
    def comboo(*args):
        return place2.get()
    place2.trace('w',comboo)
    

    #Year of student
    place3=StringVar()
    a18=Label(frame,text = "Batch",font=("","18","")).place(x=600,y=80)  
    a8 = Entry(frame,font=("","18",""),textvariable=place3).place(x=780,y=80)
    

    #roll number of student
    place4=StringVar()
    a12=Label(frame,text = "Roll no",font=("","18","")).place(x=1100,y=160)  
    a2= Entry(frame,font=("","18",""),textvariable=place4).place(x=1250,y=160)
    
    
    # hostel or dayschlor\
    place5=StringVar()
    hd=Label(frame,text="Hostel",font=("","18","")).place(x=80,y=250)
    a13=Checkbutton(frame,text="Yes",variable=place5,onvalue="Hostel",offvalue=0,height=0,width=0,font=("","14","")).place(x=240,y=250)
    a3=Checkbutton(frame,text="No",variable=place5,onvalue="Dayscholor",offvalue=0,height=0,width=0,font=("","14","")).place(x=320,y=250)

    #hostel fees
    place6=StringVar()
    a17 = Label(frame,text = "Hostel fees",font=("","18","")).place(x=600,y=250)  
    a7 = Entry(frame,font=("","18",""),textvariable=place6).place(x=780,y=250)

    #mess fees
    place7=StringVar()
    a18 = Label(frame,text = "Mess fees",font=("","18","")).place(x=1100,y=250)  
    a8 = Entry(frame,font=("","18",""),textvariable=place7).place(x=1250,y=250)

    #exam fees creator
    place8=StringVar()
    a14=Label(frame,text = "Exam fees",font=("","18","")).place(x=80,y=320)  
    a4= Entry(frame,font=("","18",""),textvariable=place8).place(x=250,y=320)

    #Semester fees creator
    place9=StringVar()
    a19=Label(frame,text="Year",font=("","18","")).place(x=80,y=400)
    course_selection=["--select Course--","1st year","2nd year","3rd year","4th year"]
    a9=ttk.Combobox(frame,values=course_selection,width=20,textvariable=place9)
    a9.place(x=250,y=400)
    def combo1(*args):
        return place9.get()
    place9.trace('w',combo1)

    #label of fees paying
    place10=StringVar()
    a20=Label(frame,text="Paying",font=("","18","")).place(x=600,y=400)
    A2=Entry(frame,font=("","18",""),textvariable=place10).place(x=780,y=400)


    #labeliling the balance
    place11=StringVar()
    a21=Label(frame,text="balance",font=("","18","")).place(x=1100,y=400)
    A21=Entry(frame,font=("","18",""),textvariable=place11).place(x=1250,y=400)
    


    #Bus fees
    place12=StringVar()
    a16=Label(frame,text = "Bus fees",font=("","18","")).place(x=80,y=160)  
    a6= Entry(frame,font=("","18",""),textvariable=place12).place(x=250,y=160)

    #bus no
    place13=StringVar()
    A18=Label(frame,text = "Bus no",font=("","18","")).place(x=600,y=160)  
    A8= Entry(frame,font=("","18",""),textvariable=place13).place(x=780,y=160)

     #info about bus fees
    place14=StringVar()
    info=Label(frame,text=" * IF DAYSCHOLOR",font=("mangolian baiti","10","italic","bold"),textvariable=place14)
    info.place(x=250,y=197)

    #lab fee
    place15=StringVar()
    A17=Label(frame,text = "Lab fees",font=("","18","")).place(x=80,y=480)  
    A7= Entry(frame,font=("","18",""),textvariable=15).place(x=250,y=480)

    #date
    place16=StringVar()
    Date=Label(frame,text="Date",font=("","18","")).place(x=1273,y=5)
    date_label=Entry(frame,font=("","9",""),textvariable=16).place(x=1350,y=10)

    #course fees in another window
    def hi4():
        frame1=Tk()
        fr1=Frame(frame1,width=420,height=320,bg="white")
        fr1.place(x=1350,y=780)
        frame1.geometry("250x250")
        label1=Label(frame1,text="AI&DS ---- 95k \n Mech ---- 55k \n civil ---- 72k \n Ece ---- 65k \n EEE ---- 65k \n Cse ---- 85k \n Aero ---- 1,10L \n cyber ---- 98k \n Marine ---- 1L",font=("","15",""))
        label1.place(x=0,y=0)

    #button for courses
    label=Button(frame,text="Fees Details",font=("ariel","18","italic","bold"),activeforeground="red",activebackground="black",command=hi4)
    label.place(x=1070,y=710)

    #save button on screen
    print(comboo())
    def process():
        import mysql.connector as mysql
        mydb= mysql.connect(host="localhost",user="root",password="1234",database="avengers",auth_plugin="mysql_native_password")
        mycursor=mydb.cursor()
        mycursor.execute("insert into list2(date, name, Batch, Dept, Bus_fees, Bus_no, Roll_no, Student_type, Hostel_fees, Mess_fees, Exam_fees, Year, Paying, Balance, lab_fees) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[place16.get(),place1.get(), place3.get(), comboo(), place6.get(), place13.get(), place2.get(), place5.get(),place7.get(),place8.get(), place4.get(), combo1(), place10.get(), place11.get(), place15.get()]) 
        print("Details are saved sucessfully")
        mydb.commit()
        frame.destroy()

    label=Button(frame,text="Save",font=("ariel","18","italic","bold"),activeforeground="red",activebackground="black",command=process)
    label.place(x=1270,y=710)
    

    #Exit button on screen
    def hiii():                     #destroy the screen
        messagebox.showerror("Askquestion","Are you sure?")
        frame.destroy()

    exits=Button(frame,text="Cancel",font=("ariel","18","italic","bold"),activeforeground="red",activebackground="black", command=hiii)
    exits.place(x=1410,y=710)


co()



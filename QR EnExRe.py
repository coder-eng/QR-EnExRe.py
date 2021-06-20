from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
from datetime import datetime,timedelta,date
import cv2
import playsound
import speech_recognition as sr
import webbrowser as wb
from tkinter.messagebox import Message
import pandas
from tkinter import messagebox,filedialog
from tkinter.ttk import Treeview
import tkinter
import qrcode
# --------------------------------------------------------- CREATING LOGIN WINDOW ---------------------------------------------------------------------

window = Tk()
window.title('QR EnExRe')
window.geometry("1350x700+0+0")
window.resizable(0,0)
#----------------------------------------------------    backgroung image   ---------------------------
img = ImageTk.PhotoImage(Image.open("F:\\New Volume\\PycharmProjects\\imagess\\simBlurImage.jpg"))
my = Label(image=img)
my.pack()

# creating labelframe inside main window
frame = Frame(width=500, height=460)
frame.config(bg="#ffffff")
frame.place(x=450, y=140)

framelog1=Frame(window,width=100, height=460)
framelog1.config(bg="#091D34")
framelog1.place(x=400,y=140)

# adding logo of college on login frame
img1 = ImageTk.PhotoImage(Image.open('F:\\New Volume\\PycharmProjects\\imagess\\IMG-20201005-WA0004.jpg'))
my1  = Label(frame,image=img1)
my1.place(x=185,y=20)

#------------------------------------------  label and entry box for user_id  -----------------------------------
user_id = Label(frame,text='Email:',font=('times', 20, "bold"),width=10,bg="white").place(x=40,y=180)

user_var = StringVar()
user_entrybox = Entry(frame,width=45,font=("times new roman",12),textvariable=user_var,bg="#b3b3b3")
user_entrybox.place(x=80,y=220,height="35")
user_entrybox.focus()

#-----------------------------------------  label and entry box for password  -----------------------------------
password = Label(frame,text='Password:',font=('times', 20,'bold'),width=10,bg="white").place(x=60,y=270)

password_var = StringVar()
pass_entrybox = Entry(frame,width=45,font=("times new roman",12),textvariable=password_var,show="*",bg="#b3b3b3").place(x=80,y=310,height="35")

#---------------------------------------  button for forgot password  --------------------------------------------------
btn_forgot_pass = Button(frame,text="Forgot Password?",font=("times new roman",15),bd=0,fg="#B00857",bg="white",cursor="hand2").place(x=300,y=360)

#------------------------------------ function for calling automatic message ---------------------------------
def msg(str1,int1,str2):
    TIME_TO_WAIT = int1  # in milliseconds
    root = Tk()
    root.withdraw()
    root.after(TIME_TO_WAIT, root.destroy)
    Message(title=str1, message=str2, master=root).show()

# _________________________________________  code for database connectivity  ________________________________
def database():
    global cur, conn

    try:
        conn = mysql.connector.connect(user='root', host='localhost', database='in_out_activity',password='$@ffron@09')
        cur = conn.cursor()
    except:
        try:
            conn = mysql.connector.connect(user='root', host='localhost', password='$@ffron@09')
            cur = conn.cursor()
            str1 = 'create database in_out_activity '
            cur.execute(str1)
            str2 = 'use in_out_activity'
            cur.execute(str2)
            str3 = 'create table activity(ID varchar(20) not null,Name varchar(25) not null,Flag bool not null,Date varchar(12),Time varchar(255) not null,flag2 bool default -1,last_time varchar(10),primary key(ID,date),foreign key (ID) references new_table(ID) on delete cascade)'
            cur.execute(str3)
        except:
            msg("ERROR",2000,'you are not connected to server')
        else:
            print('connected succesfully')
            msg('notification',2000,"connected successfuly and the database is created successfully in your system")
    else:
        msg("notification", 2000, 'connected successfuly')
        print('connected succesfully')

database()
current_date = date.today()
def message():
    messagebox.showerror("ERROR", " password is wrong")

#------------------------------------- sign up function to open the system -----------------------------
def signup():
    global cur,conn
    registration = Toplevel()
    registration.title('QR EnExRe')
    registration.geometry("1350x700+0+0")
    registration.resizable(0, 0)
    registration.config(bg="#ffbf80")
    # ---------------------------------- cofee image  ---------------------------------------------------
    img1 = ImageTk.PhotoImage(Image.open('F:\\New Volume\\PycharmProjects\\imagess\\add_another.jpg'))
    my1 = Label(registration, image=img1)
    my1.place(x=70, y=90)

    # ---------------------------------- frame for registration -------------------------------------------------

    frame_r = Frame(registration, bg="black")
    frame_r.place(x=670, y=90, width=610, height=500)

    title = Label(registration, text="REGISTER HERE", font=("times new roman", 25, "bold"), bg="black",
                  fg="white").place(x=740, y=95)

    name_l = Label(registration, text="Name", font=("times new roman", 15), bg="black", fg="white").place(x=740, y=150)
    name_var_r = StringVar()
    name_var_r_entrybox = Entry(registration, width=45, font=("times new roman", 12), textvariable=name_var_r,
                                bg="white")
    name_var_r_entrybox.place(x=740, y=180, height="25")
    name_var_r_entrybox.focus()

    email_l = Label(registration, text="E-mail", font=("times new roman", 15), bg="black", fg="white").place(x=740,
                                                                                                             y=225)
    email_var_r = StringVar()
    email_var_r_entrybox = Entry(registration, width=45, font=("times new roman", 12), textvariable=email_var_r,
                                 bg="white")
    email_var_r_entrybox.place(x=740, y=255, height="25")

    password_l = Label(registration, text="Password", font=("times new roman", 15), bg="black", fg="white").place(x=740,
                                                                                                                  y=305)
    password_var_r = StringVar()
    password_var_r_entrybox = Entry(registration, width=45, font=("times new roman", 12), textvariable=password_var_r,
                                    bg="white")
    password_var_r_entrybox.place(x=740, y=335, height="25")

    security_l = Label(registration, text="Security Question", font=("times new roman", 15), bg="black",
                       fg="white").place(x=740, y=385)
    security_var = StringVar()
    security_combobox = ttk.Combobox(registration, width=57, textvariable=security_var, state='readonly')
    security_combobox['values'] = (
    'select', 'Your pet name', 'Your birth place', 'your nick name', 'your favourite color')
    security_combobox.current(0)
    security_combobox.place(x=740, y=415, height="25")

    answer_l = Label(registration, text="Answer", font=("times new roman", 15), bg="black", fg="white").place(x=740,
                                                                                                              y=465)
    answer_var_r = StringVar()
    answer_var_r_entrybox = Entry(registration, width=45, font=("times new roman", 12), textvariable=answer_var_r,
                                  bg="white")
    answer_var_r_entrybox.place(x=740, y=495, height="25")

    def register():

        name = name_var_r.get()
        emaail = email_var_r.get()
        password = password_var_r.get()
        question = security_var.get()
        answer = answer_var_r.get()

        if (name == '' or emaail == '' or password == '' or question == '' or answer == ''):
            messagebox.showerror('error', 'all fields are required', parent=registration)
            return
        else:
            try:
                query = "create table if not exists login(name varchar(30) not null, email varchar(40) not null primary key,password varchar(20) not null, security_question varchar(100) not null,answer varchar(20) not null)"
                cur.execute(query)
                str1 = 'insert into login values(%s,%s,%s,%s,%s)'
                data = (name, emaail, password, question, answer)
                cur.execute(str1,data)
                conn.commit()
            except mysql.connector.IntegrityError as err:
                messagebox.showerror("error", err, parent=registration)
                return
            else:
                messagebox.showinfo('notification', 'registered successfully', parent=registration)

    proceed = Button(registration, text='Proceed Here', font=("times new roman", 15, "bold"), bg="#ffbf80",
                     command=register)
    proceed.place(x=740, y=538, height=26)

    registration.mainloop()

#------------------------------------- end of sign up function to open the system -----------------------------
#-----------------------------  button for sign up function to open the system ---------------------------
btn_sign_up = Button(frame,text="Sign Up?",font=("times new roman",15),bd=0,fg="#B00857",bg="white",cursor="hand2",command=signup).place(x=80,y=360)

#__________________________________________ deshboard function  _____________________________________________
def deshboard():
    global pass1, opened2,count,text,opened_logout,opened,opened_ll

    window.withdraw()
    #-------------------------- function for log out -----------------------------------------------------
    def logout():
        global opened_logout
        login1.withdraw()
        window.deiconify()

        if opened_logout == True:
            pass

    #-------------------------  function for exit button ---------------------------------------------------
    def exit():
        window.destroy()

    #-------------------------  function for scan here button  ---------------------------------------------
    def scanner():
        global srno, conn
        cur = conn.cursor()

        # initalize the cam
        cap = cv2.VideoCapture(0)
        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()

        while True:
            list1 = ''
            _, img = cap.read()
            # detect and decode
            srno, bbox, _ = detector.detectAndDecode(img)

            # check if there is a QRCode in the image
            if bbox is not None:

                if srno:
                    now = datetime.now()
                    addout_time = now.strftime("%H:%M:%S")
                    list1 = list1 + ',' + str(addout_time)
                    # query for time string of student who hava scanned qrcode
                    query = 'SELECT EXISTS(SELECT * from activity WHERE ID=%s and Date=%s)'
                    # query = "select time from student where Serial_number=%s"
                    data = (srno, current_date)
                    cur.execute(query, data)
                    ind = cur.fetchone()

                    # checking if it is first entry of the day
                    if (ind[0] == 0):
                        query = "select Name,Type,hostel from new_table where ID=%s"
                        data = (srno,)
                        cur.execute(query, data)
                        new_name = cur.fetchone()
                        if (new_name == None):
                            #msg("error", 2000, "please scan a valid QRcode")
                            playsound.playsound('qrcode.mp3', True)
                        else:
                            # asking for entry or exit, for the first entry of the day
                            playsound.playsound('welcome1.mp3', True)
                            playsound.playsound('welcome2.mp3', True)
                            playsound.playsound('welcome3.mp3', True)


                            # taking user input from microphone
                            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

                            # obtain audio from the microphone
                            # -----------------------------------      code for speech to text   -----------------------------------
                            def user_input():
                                r = sr.Recognizer()
                                with sr.Microphone() as source:
                                    print("Please wait. Calibrating microphone...")
                                    msg("message", 2000, "Please wait. Calibrating microphone...")
                                    # listen for 5 seconds and create the ambient noise energy level
                                    r.adjust_for_ambient_noise(source, duration=5)
                                    msg("message", 2000, "Say something!")
                                    audio = r.listen(source)

                                # recognize speech
                                try:
                                    text = r.recognize_google(audio)

                                    print("I thinks you said '" + r.recognize_google(audio) + "'")

                                    f_text = 'https://www.google.co.in/search?q=' + text
                                    wb.get(chrome_path).open(f_text)
                                    return text
                                # except sr.UnknownValueError:
                                #  print("I could not understand audio")
                                except sr.RequestError as e:
                                    print("error; {0}".format(e))

                                except Exception as e:
                                    print(e)

                            # -----------------------------------------------------------------------------------------------
                            while (1):
                                textd = user_input()
                                if (textd == "exit"):
                                    flag = 'out'
                                    query = "insert into activity (ID,Name,Flag,Date,Time,flag2,last_time,Type,Hostel) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                    data = (
                                    srno, new_name[0], flag, current_date, list1, flag, addout_time, new_name[1],
                                    new_name[2])
                                    cur.execute(query, data)
                                    conn.commit()
                                    print("[+] QR Code detected, dataa:", srno)
                                    msg("message", 2000, 'your recorded  time is ' + addout_time)
                                    break
                                elif (textd == 'entry'):
                                    flag = 'in'
                                    query = "insert into activity (ID,Name,Flag,Date,Time,flag2,last_time,Type,Hostel) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                    data = (
                                    srno, new_name[0], flag, current_date, list1, flag, addout_time, new_name[1],
                                    new_name[2])
                                    cur.execute(query, data)
                                    conn.commit()
                                    print("[+] QR Code detected, dataa:", srno)
                                    msg("message", 2000, 'your recorded  time is ' + addout_time)
                                    break
                                else:
                                    playsound.playsound('welcome4.mp3', True)
                                    continue
                                # ----------------------------------------------------------------------------------
                        # cur.execute('SET SQL_SAFE_UPDATES=1')

                    else:

                        query = "select Time,flag2, Flag from activity where ID=%s and Date=%s"
                        data = (srno, current_date)
                        cur.execute(query, data)
                        row = cur.fetchone()
                        print(row)
                        time_string = row[0]
                        # print(result)
                        f = row[1]

                        F = row[2]
                        print(F)
                        # checking time elapsed between two scan
                        current_time = datetime.strptime(addout_time, '%H:%M:%S').time()
                        result1 = time_string[-8:]
                        last_time = datetime.strptime(result1, '%H:%M:%S').time()
                        time_elapsed = datetime.combine(date.today(), current_time) - datetime.combine(date.today(),
                                                                                                       last_time)
                        duration_in_s = time_elapsed.total_seconds()
                        diff = timedelta(hours=0, minutes=1, seconds=00)
                        print(duration_in_s)

                        # no one can scan same qr code with in some interval

                        if (time_elapsed > diff):
                            result = time_string + list1
                            print(f)
                            if (f == 'out'):
                                f = 'in'
                            else:
                                f = 'out'

                            query = "update activity set time =%s, flag2=%s, last_time=%s where ID=%s and Date=%s"
                            data = (result, f, addout_time, srno, current_date)
                            cur.execute(query, data)
                            # cur.execute('SET SQL_SAFE_UPDATES=1')
                            conn.commit()
                            print("[+] QR Code detected, dataa:", srno)
                            msg("message", 2000, 'your recorded  time is ' + addout_time)

                        else:
                            msg("Warning", 2000, "You can't scan QRCode within 1 minute")

            # display the result
            cv2.imshow('image', img)
            if cv2.waitKey(1) == ord("q"):
                break

    # -------------------------  end of  scan here function  ------------------------------------------

    # -------------------------  function for admin button  ------------------------------------------
    def login_for_adminn():
        global opened, opened_ll,opened_log_admin,opened_home
        login1.withdraw()

        def admin():

            login_for_admin.withdraw()
            if opened_ll == True:
                login_for_admin.deiconify()
            else:
                view = Toplevel()
                view.title("admin")
                view.config(bg="black")
                view.geometry('1350x700+0+0')
                view.resizable(0, 0)

                def manage_student():
                    global cur
                    mng = LabelFrame(view, width=1170, height=500, text="Manage Student Record", labelanchor="n",
                                     font=("arial", 20, 'bold'), bg="#F7D4EC", fg="#C21460")
                    mng.config(bg="#F7D4EC")
                    mng.place(x=165, y=180)

                    frame4 = LabelFrame(mng, bg="white")
                    table = Treeview(frame4, columns=('ID', 'Name', 'Contact_number', 'Email_id', 'Gender',
                                                      'Academic_year', 'Semester', 'Department', 'Student_type',
                                                      'Hostel_name',
                                                      'Room_number', 'Father_name', 'Mother_name', 'Home_address',
                                                      'State',
                                                      'City'))
                    table.column('ID', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('ID', text='ID', anchor=tkinter.CENTER)
                    table.column('Name', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Name', text='Name', anchor=tkinter.CENTER)
                    table.column('Contact_number', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Contact_number', text='Contact_number', anchor=tkinter.CENTER)
                    table.column('Email_id', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Email_id', text='Email_id', anchor=tkinter.CENTER)
                    table.column('Gender', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Gender', text='Gender', anchor=tkinter.CENTER)
                    table.column('Academic_year', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Academic_year', text='Academic_year', anchor=tkinter.CENTER)
                    table.column('Semester', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Semester', text='Semester', anchor=tkinter.CENTER)
                    table.column('Department', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Department', text='Department', anchor=tkinter.CENTER)
                    table.column('Student_type', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Student_type', text='Student_type', anchor=tkinter.CENTER)
                    table.column('Hostel_name', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Hostel_name', text='Hostel_name', anchor=tkinter.CENTER)
                    table.column('Room_number', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Room_number', text='Room_number', anchor=tkinter.CENTER)
                    table.column('Father_name', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Father_name', text='Father_name', anchor=tkinter.CENTER)
                    table.column('Mother_name', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Mother_name', text='Mother_name', anchor=tkinter.CENTER)
                    table.column('Home_address', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Home_address', text='Home_address', anchor=tkinter.CENTER)
                    table.column('State', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('State', text='State', anchor=tkinter.CENTER)
                    table.column('City', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('City', text='City', anchor=tkinter.CENTER)
                    table['show'] = 'headings'
                    s = ttk.Style(frame4)
                    s.theme_use('winnative')

                    # ----------------------- use it for apply on all widget ------------------------------------------
                    # s.configure('.',font=("times new roman", 12,'bold'))
                    s.configure('Treeview.Heading', font=("times new roman", 15, 'bold'), foreground='red',
                                backgound='blue')
                    s.configure('Treeview', font=("chiller", 12, 'bold'), foreground='red')
                    xs = ttk.Scrollbar(frame4, orient='horizontal')
                    xs.configure(command=table.xview)
                    ys = ttk.Scrollbar(frame4, orient='vertical')
                    ys.configure(command=table.yview)
                    table.configure(xscrollcommand=xs.set, yscrollcommand=ys.set)
                    xs.pack(side=BOTTOM, fill=X)
                    ys.pack(side=RIGHT, fill=Y)
                    frame4.place(x=390, y=16, width=750, height=433)
                    table.pack(fill=BOTH, expand=1)

                    entry_text = Label(mng, text="ID:", font=('goudy old style', 20, 'bold'), bg='#F7D4EC',
                                       fg="black")
                    entry_text.place(x=30, y=15, width=35, height=25)

                    entry_var = StringVar()
                    entry_entrybox = Entry(mng, width=32, font=("times new roman", 12), textvariable=entry_var,
                                           bg="#b3b3b3")
                    entry_entrybox.place(x=80, y=15, height=25)

                    # -------------------------------------------------  creating button  ------------------------------------

                    # ------------------------------------  add  ---------------------------------------------------------

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> function to add <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def add_student():
                        add = Toplevel()
                        add.title('Student record')
                        add.config(bg="#FFE8DC")
                        add.geometry('1350x700+0+0')

                        # cerate a frame for hedaline
                        frames = Frame(add, width=1365, height=25)
                        frames.config(bg="#341809")
                        frames.place(x=0, y=0)

                        # create lables for student data record
                        add_box = LabelFrame(add, width=682, height=675, text="ADD STUDENT INFORMATION ",
                                             font=('arial', 20, 'bold'), fg="red")
                        add_box.config(bg="#F0F7D4")
                        add_box.place(x=1, y=25)

                        student_name_lable = Label(add, text="Student Name ", font=('arial', 15, 'bold'),
                                                   fg='blue')  # pack,grid
                        student_name_lable.config(bg="#F0F7D4")
                        student_name_lable.place(x=20, y=70)

                        father_name_lable = Label(add, text="Father's Name ", font=('arial', 15, 'bold'), fg='blue')
                        father_name_lable.config(bg="#F0F7D4")
                        father_name_lable.place(x=20, y=110)

                        mother_name_lable = Label(add, text="Mother's Name ", font=('arial', 15, 'bold'), fg='blue')
                        mother_name_lable.config(bg="#F0F7D4")
                        mother_name_lable.place(x=20, y=150)

                        email_lable = Label(add, text="Email Id ", font=('arial', 15, 'bold'), fg='blue')
                        email_lable.config(bg="#F0F7D4")
                        email_lable.place(x=20, y=190)

                        contact_lable = Label(add, text="Contact ", font=('arial', 15, 'bold'), fg='blue')
                        contact_lable.config(bg="#F0F7D4")
                        contact_lable.place(x=20, y=230)

                        Sr_no_lable = Label(add, text="Sr.no. ", font=('arial', 15, 'bold'), fg='blue')
                        Sr_no_lable.config(bg="#F0F7D4")
                        Sr_no_lable.place(x=20, y=270)

                        # radio button for dayscholar or hosteler
                        usertype = StringVar()
                        radiobtn1 = Radiobutton(add, text='Day-Scholar', font=('arial', 15, 'bold'), bg="#F0F7D4",
                                                fg='blue',
                                                value='Day-Scholar', variable=usertype)
                        radiobtn1.place(x=20, y=310)

                        radiobtn1 = Radiobutton(add, text='Hosteler', font=('arial', 15, 'bold'), bg="#F0F7D4",
                                                fg='blue',
                                                value='Hosteler', variable=usertype)
                        radiobtn1.place(x=300, y=310)

                        gender_lable = Label(add, text="Gender ", font=('arial', 15, 'bold'), fg='blue')
                        gender_lable.config(bg="#F0F7D4")
                        gender_lable.place(x=20, y=350)

                        Hostel_lable = Label(add, text="Hostel Name ", font=('arial', 15, 'bold'), fg='blue')
                        Hostel_lable.config(bg="#F0F7D4")
                        Hostel_lable.place(x=20, y=390)

                        accademic_year = Label(add, text="Accedamic Year ", font=('arial', 15, 'bold'), fg='blue')
                        accademic_year.config(bg="#F0F7D4")
                        accademic_year.place(x=20, y=430)

                        semester_lable = Label(add, text="Semester ", font=('arial', 15, 'bold'), fg='blue',
                                               bg="#F0F7D4")
                        semester_lable.place(x=20, y=470)

                        department_lable = Label(add, text="Department ", font=('arial', 15, 'bold'), fg='blue',
                                                 bg="#F0F7D4")
                        department_lable.place(x=20, y=510)

                        Room_lable = Label(add, text="Room Number ", font=('arial', 15, 'bold'), fg='blue',
                                           bg="#F0F7D4").place(
                            x=20,
                            y=550)

                        address_lable = Label(add, text="Home Address", font=('arial', 15, 'bold'), fg='blue')
                        address_lable.config(bg="#F0F7D4")
                        address_lable.place(x=20, y=590)

                        state_lable = Label(add, text="State ", font=('arial', 15, 'bold'), fg='blue')
                        state_lable.config(bg="#F0F7D4")
                        state_lable.place(x=20, y=630)

                        City_lable = Label(add, text="City", font=('arial', 15, 'bold'), fg='blue')
                        City_lable.config(bg="#F0F7D4")
                        City_lable.place(x=20, y=670)
                        print('priya')

                        # create entrybox
                        student_name_var = StringVar()
                        student_name_entrybox = Entry(add, width=50, textvariable=student_name_var)
                        student_name_entrybox.place(x=250, y=70)
                        student_name_entrybox.focus()
                        name = student_name_var.get()
                        print(name)

                        father_name_var = StringVar()
                        father_name_entrybox = Entry(add, width=50, textvariable=father_name_var)
                        father_name_entrybox.place(x=250, y=110)

                        mothers_name_var = StringVar()
                        mothers_name_entrybox = Entry(add, width=50, textvariable=mothers_name_var)
                        mothers_name_entrybox.place(x=250, y=150)

                        email_var = StringVar()
                        email_entrybox = Entry(add, width=50, textvariable=email_var)
                        email_entrybox.place(x=250, y=190)

                        contact_var = StringVar()
                        contact_entrybox = Entry(add, width=50, textvariable=contact_var)
                        contact_entrybox.place(x=250, y=230)

                        sr_no_var = StringVar()
                        sr_no_entrybox = Entry(add, width=50, textvariable=sr_no_var)
                        sr_no_entrybox.place(x=250, y=270)

                        gender_var = StringVar()
                        gender_combobox = ttk.Combobox(add, width=47, textvariable=gender_var, state='readonly')
                        gender_combobox['values'] = ('select', 'Male', 'Female', 'Other')
                        gender_combobox.current(0)
                        gender_combobox.place(x=250, y=350)

                        Hostel_var = StringVar()
                        Hostel_entrybox = Entry(add, width=50, textvariable=Hostel_var)
                        Hostel_entrybox.place(x=250, y=390)

                        Accademic_year_var = StringVar()
                        Accademic_year_entrybox = Entry(add, width=50, textvariable=Accademic_year_var)
                        Accademic_year_entrybox.place(x=250, y=430)

                        Semester_var = StringVar()
                        Semester_entrybox = Entry(add, width=50, textvariable=Semester_var)
                        Semester_entrybox.place(x=250, y=470)

                        Department_var = StringVar()
                        Department_entrybox = Entry(add, width=50, textvariable=Department_var)
                        Department_entrybox.place(x=250, y=510)

                        room_var = StringVar()
                        room_entrybox = Entry(add, width=50, textvariable=room_var)
                        room_entrybox.place(x=250, y=550)

                        address_var = StringVar()
                        address_entrybox = Entry(add, width=50, textvariable=address_var)
                        address_entrybox.place(x=250, y=590)

                        state_var = StringVar()
                        state_entrybox = Entry(add, width=50, textvariable=state_var)
                        state_entrybox.place(x=250, y=630)

                        City_var = StringVar()
                        City_entrybox = Entry(add, width=50, textvariable=City_var)
                        City_entrybox.place(x=250, y=670)

                        # QR CODE
                        def QRCode():
                            sr = sr_no_var.get()
                            fileName = sr + '.jpg'
                            # ============Now generate and save qr code================
                            img = qrcode.make(sr)
                            img.save(fileName)
                            add.photo = PhotoImage(file=fileName)
                            QR.config(image=add.photo, text='QR Code Generated Successfully!',
                                      fg='green', compound=TOP, width=300, height=300)
                            messagebox.showinfo('Saved',
                                                'QR code saved as " ' + fileName + ' " successfully!\n\tin current location',
                                                parent=add)

                        # ---------------------------  function to add student --------------------------------------------
                        def add_stu():
                            global conn, cur
                            radio = usertype.get()
                            name = student_name_var.get()
                            fname = father_name_var.get()
                            mname = mothers_name_var.get()
                            email = email_var.get()
                            contact = contact_var.get()
                            sr = sr_no_var.get()
                            gender = gender_var.get()
                            hostel = Hostel_var.get()
                            accademic = Accademic_year_var.get()
                            semester = Semester_var.get()
                            department = Department_var.get()
                            room = room_var.get()
                            address = address_var.get()
                            state = state_var.get()
                            city = City_var.get()
                            if (radio == 'Day-Scholar'):
                                hostel = None
                                room = None

                            if (
                                    name == '' or accademic == '' or semester == '' or department == '' or sr == '' or email == '' or contact == '' or radio == '' or gender == '' or fname == '' or mname == '' or address == '' or state == '' or city == ''):
                                messagebox.showerror('error', 'Except hostel and room number, all fields are required',
                                                     parent=add)
                                return
                            else:
                                try:
                                    query = 'create table if not exists student(Serial_number varchar(20) not null primary key,Name varchar(25) not null,Contact varchar(10) not null,Email varchar(30) not null unique,Gender varchar(10) not null,Academic_year varchar(5) not null,Semester varchar(5) not null,Department varchar(40) not null,Student_Type varchar(15) not null,Hostel_name varchar(25),Room_number varchar(5),Father_name varchar(30) not null,Mother_name varchar(30) not null,Address varchar(50) not null,State varchar(10) not null,City varchar(10) not null)'
                                    cur.execute(query)
                                    query = "create table if not exists new_table(ID varchar(20) not null primary key,Name varchar(25) not null,Type varchar(15) not null,hostel varchar(25),foreign key (ID) references staff(ID) on delete cascade,foreign key (ID) references student(Serial_number) on delete cascade)"
                                    cur.execute(query)
                                    cur.execute('SET foreign_key_checks = 0')
                                    str1 = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                    cur.execute(str1, (
                                        sr, name, contact, email, gender, accademic, semester, department, radio,
                                        hostel, room,
                                        fname,
                                        mname, address, state, city))
                                    cur.execute('SET foreign_key_checks = 1')
                                    conn.commit()
                                except mysql.connector.IntegrityError as err:
                                    messagebox.showerror("error", err, parent=add)
                                    return
                                else:
                                    QRCode()
                                    messagebox.showinfo('notification',
                                                        'QR Code generated and student added successfully',
                                                        parent=add)

                        # Add student button for student record page
                        Add_student = Button(add, text="ADD STUDENT & GENERATE QR CODE", fg="white", bg="red",
                                             font=('arial', 15, 'bold'),
                                             command=add_stu)
                        Add_student.place(x=825, y=475)

                        # function for adding another student
                        def add_another():
                            student_name_entrybox.delete(0, END)
                            father_name_entrybox.delete(0, END)
                            mothers_name_entrybox.delete(0, END)
                            email_entrybox.delete(0, END)
                            contact_entrybox.delete(0, END)
                            sr_no_entrybox.delete(0, END)
                            radiobtn1.deselect()
                            gender_combobox.set('')
                            Hostel_entrybox.delete(0, END)
                            Accademic_year_entrybox.delete(0, END)
                            Semester_entrybox.delete(0, END)
                            Department_entrybox.delete(0, END)
                            room_entrybox.delete(0, END)
                            address_entrybox.delete(0, END)
                            state_entrybox.delete(0, END)
                            City_entrybox.delete(0, END)

                        # function for resetting qr code
                        def reset():
                            sr_no_entrybox.delete(0, END)
                            sr_no_entrybox.config(bg='white')
                            QR.config(image='', text='', width=0, height=0)

                        # button for adding another student
                        add_student2 = Button(add, text="ADD ANOTHER STUDENT", fg="white", bg="red",
                                              font=('arial', 15, 'bold'),
                                              command=lambda: [add_another(), reset()])
                        add_student2.place(x=890, y=550)

                        """""
                        # button for reset
                        reset1 = Button(add, text="RESET", fg="white", bg="red", font=('arial', 15, 'bold'), command=reset)
                        reset1.place(x=965, y=625)
                        """
                        QR = Label(add, text='No QR\nAvailable', font=('times new roman', 15), image='', bg='plum1')
                        QR.place(x=870, y=75, width='300', height='350')
                        add.mainloop()

                    Add = Button(mng, text="Add Record", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                 fg="white", bg="#94B814", activebackground='#C21460', command=add_student)
                    Add.place(x=30, y=50)

                    # --------------------------------------   search   -----------------------------------------------------
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  function to search  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def searchst():
                        entry = entry_var.get()
                        print(entry)
                        query = "select * from student where Serial_number=%s"
                        data = (entry,)
                        cur.execute(query, data)
                        final = cur.fetchall()
                        table.delete(*table.get_children())
                        if not final:
                            messagebox.showinfo('message', "No record found")
                        else:
                            i = 0
                            for ro in final:
                                table.insert('', i, text='', values=(
                                    ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10],
                                    ro[11],
                                    ro[12],
                                    ro[13],
                                    ro[14], ro[15]))
                                i = i + 1

                    search = Button(mng, text="Search Record", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                    fg="white", bg="#94B814", activebackground='#C21460', command=searchst)
                    search.place(x=30, y=110)

                    # -------------------------------------   delete  -------------------------------------------------------
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   function to delete  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def del1():
                        global conn, cur
                        entry = entry_var.get()

                        if (entry == ''):
                            cc = table.focus()
                            content = table.item(cc)
                            pp = content['values'][0]
                            strr = 'delete from student where Serial_number=%s'
                            data = (pp,)
                            cur.execute(strr, data)
                            conn.commit()
                            messagebox.showinfo('notification', 'ID {} deleted succesfully...'.format(pp))
                        else:
                            query = 'select * from student  where Serial_number=%s'
                            data = (entry,)
                            cur.execute(query, data)
                            result = cur.fetchone()
                            if (result == None):
                                messagebox.showerror('error', 'record is not present')
                            else:
                                strr = 'delete from student where Serial_number=%s'
                                data = (entry,)
                                cur.execute(strr, data)
                                conn.commit()
                                messagebox.showinfo('notification', 'ID {} deleted succesfully...'.format(entry))

                        query = "select * from student"
                        cur.execute(query)
                        final = cur.fetchall()
                        table.delete(*table.get_children())
                        if not final:
                            messagebox.showinfo('message', "No record found")
                        else:
                            i = 0
                            for ro in final:
                                table.insert('', i, text='', values=(
                                    ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10],
                                    ro[11],
                                    ro[12],
                                    ro[13],
                                    ro[14], ro[15]))
                                i = i + 1

                    delete = Button(mng, text="Delete Record", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                    fg="white", bg="#94B814", activebackground='#C21460', command=del1)
                    delete.place(x=30, y=170)

                    # ------------------------------------   update  -----------------------------------------------------------
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   function for update  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def up():
                        global conn, cur
                        entry = entry_var.get()
                        query = 'select * from student  where Serial_number=%s'
                        data = (entry,)
                        cur.execute(query, data)
                        result = cur.fetchall()
                        if (result == None):
                            messagebox.showerror('error', 'record is not present')
                        else:
                            i = 0
                            for ro in result:
                                table.insert('', i, text='', values=(
                                    ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10],
                                    ro[11],
                                    ro[12],
                                    ro[13],
                                    ro[14], ro[15]))
                                i = i + 1
                            cc = table.focus()
                            content = table.item(cc)
                            pp = content['values']
                            # ------------------------ defining update window --------------------------------------------------
                            update = Toplevel()
                            update.title('Student record')
                            update.config(bg="#FFE8DC")
                            update.geometry('650x700+0+0')

                            # cerate a frame for hedaline
                            frames = Frame(update, width=1365, height=25)
                            frames.config(bg="#341809")
                            frames.place(x=0, y=0)

                            # create lables for student data record
                            update_box = LabelFrame(update, width=682, height=675, text="UPDATE STUDENT INFORMATION ",
                                                    font=('arial', 20, 'bold'), fg="red")
                            update_box.config(bg="#F0F7D4")
                            update_box.place(x=1, y=25)

                            student_name_lable = Label(update, text="Student Name ", font=('arial', 15, 'bold'),
                                                       fg='blue')  # pack,grid
                            student_name_lable.config(bg="#F0F7D4")
                            student_name_lable.place(x=20, y=70)

                            father_name_lable = Label(update, text="Father's Name ", font=('arial', 15, 'bold'),
                                                      fg='blue')
                            father_name_lable.config(bg="#F0F7D4")
                            father_name_lable.place(x=20, y=110)

                            mother_name_lable = Label(update, text="Mother's Name ", font=('arial', 15, 'bold'),
                                                      fg='blue')
                            mother_name_lable.config(bg="#F0F7D4")
                            mother_name_lable.place(x=20, y=150)

                            email_lable = Label(update, text="Email Id ", font=('arial', 15, 'bold'), fg='blue')
                            email_lable.config(bg="#F0F7D4")
                            email_lable.place(x=20, y=190)

                            contact_lable = Label(update, text="Contact ", font=('arial', 15, 'bold'), fg='blue')
                            contact_lable.config(bg="#F0F7D4")
                            contact_lable.place(x=20, y=230)

                            city_lable = Label(update, text="City ", font=('arial', 15, 'bold'), fg='blue')
                            city_lable.config(bg="#F0F7D4")
                            city_lable.place(x=20, y=270)

                            # radio button for dayscholar or hosteler
                            usertype = StringVar()
                            radiobtn1 = Radiobutton(update, text='Day-Scholar', font=('arial', 15, 'bold'),
                                                    bg="#F0F7D4",
                                                    fg='blue',
                                                    value='Day-Scholar', variable=usertype)
                            radiobtn1.place(x=20, y=310)

                            radiobtn1 = Radiobutton(update, text='Hosteler', font=('arial', 15, 'bold'), bg="#F0F7D4",
                                                    fg='blue',
                                                    value='Hosteler', variable=usertype)
                            radiobtn1.place(x=300, y=310)

                            gender_lable = Label(update, text="Gender ", font=('arial', 15, 'bold'), fg='blue')
                            gender_lable.config(bg="#F0F7D4")
                            gender_lable.place(x=20, y=350)

                            Hostel_lable = Label(update, text="Hostel Name ", font=('arial', 15, 'bold'), fg='blue')
                            Hostel_lable.config(bg="#F0F7D4")
                            Hostel_lable.place(x=20, y=390)

                            accademic_year = Label(update, text="Accedamic Year ", font=('arial', 15, 'bold'),
                                                   fg='blue')
                            accademic_year.config(bg="#F0F7D4")
                            accademic_year.place(x=20, y=430)

                            semester_lable = Label(update, text="Semester ", font=('arial', 15, 'bold'), fg='blue',
                                                   bg="#F0F7D4")
                            semester_lable.place(x=20, y=470)

                            department_lable = Label(update, text="Department ", font=('arial', 15, 'bold'), fg='blue',
                                                     bg="#F0F7D4")
                            department_lable.place(x=20, y=510)

                            Room_lable = Label(update, text="Room Number ", font=('arial', 15, 'bold'), fg='blue',
                                               bg="#F0F7D4").place(
                                x=20,
                                y=550)

                            updateress_lable = Label(update, text="Home updateress", font=('arial', 15, 'bold'),
                                                     fg='blue')
                            updateress_lable.config(bg="#F0F7D4")
                            updateress_lable.place(x=20, y=590)

                            state_lable = Label(update, text="State ", font=('arial', 15, 'bold'), fg='blue')
                            state_lable.config(bg="#F0F7D4")
                            state_lable.place(x=20, y=630)
                            print('priya')

                            # create entrybox
                            student_name_var = StringVar()
                            student_name_entrybox = Entry(update, width=50, textvariable=student_name_var)
                            student_name_entrybox.place(x=250, y=70)
                            student_name_entrybox.focus()
                            name = student_name_var.get()
                            print(name)

                            father_name_var = StringVar()
                            father_name_entrybox = Entry(update, width=50, textvariable=father_name_var)
                            father_name_entrybox.place(x=250, y=110)

                            mothers_name_var = StringVar()
                            mothers_name_entrybox = Entry(update, width=50, textvariable=mothers_name_var)
                            mothers_name_entrybox.place(x=250, y=150)

                            email_var = StringVar()
                            email_entrybox = Entry(update, width=50, textvariable=email_var)
                            email_entrybox.place(x=250, y=190)

                            contact_var = StringVar()
                            contact_entrybox = Entry(update, width=50, textvariable=contact_var)
                            contact_entrybox.place(x=250, y=230)

                            City_var = StringVar()
                            City_entrybox = Entry(update, width=50, textvariable=City_var)
                            City_entrybox.place(x=250, y=270)

                            gender_var = StringVar()
                            gender_combobox = ttk.Combobox(update, width=47, textvariable=gender_var, state='readonly')
                            gender_combobox['values'] = ('select', 'Male', 'Female', 'Other')
                            gender_combobox.current(0)
                            gender_combobox.place(x=250, y=350)

                            Hostel_var = StringVar()
                            Hostel_entrybox = Entry(update, width=50, textvariable=Hostel_var)
                            Hostel_entrybox.place(x=250, y=390)

                            Accademic_year_var = StringVar()
                            Accademic_year_entrybox = Entry(update, width=50, textvariable=Accademic_year_var)
                            Accademic_year_entrybox.place(x=250, y=430)

                            Semester_var = StringVar()
                            Semester_entrybox = Entry(update, width=50, textvariable=Semester_var)
                            Semester_entrybox.place(x=250, y=470)

                            Department_var = StringVar()
                            Department_entrybox = Entry(update, width=50, textvariable=Department_var)
                            Department_entrybox.place(x=250, y=510)

                            room_var = StringVar()
                            room_entrybox = Entry(update, width=50, textvariable=room_var)
                            room_entrybox.place(x=250, y=550)

                            updateress_var = StringVar()
                            updateress_entrybox = Entry(update, width=50, textvariable=updateress_var)
                            updateress_entrybox.place(x=250, y=590)

                            state_var = StringVar()
                            state_entrybox = Entry(update, width=50, textvariable=state_var)
                            state_entrybox.place(x=250, y=630)

                            # --------------------------- setting older values -----------------------------------------
                            # sr_no_var.set(pp[0])
                            student_name_var.set(pp[1])
                            contact_var.set(pp[2])
                            email_var.set(pp[3])
                            gender_var.set(pp[4])
                            Accademic_year_var.set(pp[5])
                            Semester_var.set(pp[6])
                            Department_var.set(pp[7])
                            radiobtn1.select()
                            Hostel_var.set(pp[9])
                            room_var.set(pp[10])
                            father_name_var.set(pp[11])
                            mothers_name_var.set(pp[12])
                            updateress_var.set(pp[13])
                            state_var.set(pp[14])
                            City_var.set(pp[15])

                            def update_func():

                                # ------------------- getting updated data ----------------------------------------------
                                radio = usertype.get()
                                name = student_name_var.get()
                                fname = father_name_var.get()
                                mname = mothers_name_var.get()
                                email = email_var.get()
                                contact = contact_var.get()
                                # sr = sr_no_var.get()
                                gender = gender_var.get()
                                hostel = Hostel_var.get()
                                accademic = Accademic_year_var.get()
                                semester = Semester_var.get()
                                department = Department_var.get()
                                room = room_var.get()
                                address = updateress_var.get()
                                state = state_var.get()
                                city = City_var.get()
                                if (radio == 'Day-Scholar'):
                                    hostel = None
                                    room = None

                                # -------------------------- query for update ------------------------------------------
                                query = "update student set Name=%s,Contact=%s,Email=%s,Gender=%s,Academic_year=%s,Semester=%s," \
                                        "Department=%s,Student_Type=%s,Hostel_name=%s,Room_number=%s,Father_name=%s,Mother_name=%s," \
                                        "Address=%s,State=%s,City=%s where Serial_number=%s"
                                data = (
                                    name, contact, email, gender, accademic, semester, department, radio, hostel, room,
                                    fname,
                                    mname,
                                    address, state, city, pp[0])
                                cur.execute(query, data)
                                conn.commit()
                                messagebox.showinfo('notification', 'ID {} Updated succesfully...'.format(pp[0]),
                                                    parent=update)

                                query = "select * from student"
                                cur.execute(query)
                                final = cur.fetchall()
                                table.delete(*table.get_children())
                                if not final:
                                    messagebox.showinfo('message', "No record found")
                                else:
                                    i = 0
                                    for ro in final:
                                        table.insert('', i, text='', values=(
                                            ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9],
                                            ro[10],
                                            ro[11],
                                            ro[12], ro[13],
                                            ro[14], ro[15]))
                                        i = i + 1

                                update.mainloop()

                            # -------------------- update button -------------------------------------------------------
                            update_b = Button(update, text="UPDATE STUDENT ", fg="white", bg="red",
                                              font=('arial', 10, 'bold'),
                                              command=update_func)
                            update_b.place(x=250, y=655)

                    update = Button(mng, text="Update Record", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                    fg="white", bg="#94B814", activebackground='#C21460', command=up)
                    update.place(x=30, y=230)

                    # ------------------------------------  export  -----------------------------------------------------------
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   function for export  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def exp():
                        ff = filedialog.asksaveasfilename()
                        gg = table.get_children()
                        ID, Name, Contact_number, Email_id, Gender, Academic_year, Semester, Department, Student_type, Hostel_name, Room_number, Father_name, Mother_name, Home_address, State, City = [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
                        for i in gg:
                            content = table.item(i)
                            pp = content['values']
                            ID.append(pp[0]), Name.append(pp[1]), Contact_number.append(pp[2]), Email_id.append(
                                pp[3]), Gender.append(
                                pp[4]), Academic_year.append(pp[5]), Semester.append(pp[6]), Department.append(
                                pp[7]), Student_type.append(pp[8]), Hostel_name.append(pp[9]), Room_number.append(
                                pp[10]), Father_name.append(pp[11]), Mother_name.append(pp[12]), Home_address.append(
                                pp[13]), State.append(pp[14]), City.append(pp[15])
                        dd = ['ID', 'Name', 'Contact_number', 'Email_id', 'Gender',
                              'Academic_year', 'Semester', 'Department', 'Student_type', 'Hostel_name',
                              'Room_number', 'Father_name', 'Mother_name', 'Home_address', 'State', 'City']
                        df = pandas.DataFrame(
                            list(zip(ID, Name, Contact_number, Email_id, Gender, Academic_year, Semester, Department,
                                     Student_type,
                                     Hostel_name, Room_number, Father_name, Mother_name, Home_address, State, City)),
                            columns=dd)
                        paths = r'{}.csv'.format(ff)
                        df.to_csv(paths, index=False)
                        messagebox.showinfo('notification', 'Student data is saved {}'.format(paths))

                    export = Button(mng, text="Export Record", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                    fg="white", bg="#94B814", activebackground='#C21460', command=exp)
                    export.place(x=30, y=290)

                    # ------------------------------------ view all -------------------------------------------------------------
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   function to view all  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def view_all():

                        query = "select * from student"
                        cur.execute(query, )
                        final = cur.fetchall()
                        table.delete(*table.get_children())
                        if not final:
                            messagebox.showinfo('message', "No record found")
                        else:
                            i = 0
                            for ro in final:
                                table.insert('', i, text='', values=(
                                    ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10],
                                    ro[11],
                                    ro[12],
                                    ro[13],
                                    ro[14], ro[15]))
                                i = i + 1

                    viewS = Button(mng, text="View All", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                   fg="white", bg="#94B814", activebackground='#C21460', command=view_all)
                    viewS.place(x=30, y=350)

                    # ------------------------------------  exit  -------------------------------------------------------------
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   function to exit  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def ex():
                        res = messagebox.askyesnocancel('notification', 'Do you want to exit')
                        if (res == True):
                            mng.destroy()

                    exit = Button(mng, text="Exit", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                  fg="white", bg="#94B814", activebackground='#C21460', command=ex)
                    exit.place(x=30, y=410)

                def manage_academic_management():
                    global cur
                    mng = LabelFrame(view, width=1170, height=500, text="Manage Academic/Management Record",
                                     labelanchor="n",
                                     font=("arial", 20, 'bold'), bg="#F7D4EC", fg="#C21460")
                    mng.config(bg="#F7D4EC")
                    mng.place(x=165, y=180)

                    frame4 = LabelFrame(mng, bg="white")
                    table = Treeview(frame4,
                                     columns=(
                                     'ID', 'Name', 'Email_id', 'Contact_number', 'Gender', 'Type', 'Home_address',
                                     'State', 'City', 'Department', 'Residence', 'Designation'))
                    table.column('ID', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('ID', text='ID', anchor=tkinter.CENTER)
                    table.column('Name', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Name', text='Name', anchor=tkinter.CENTER)
                    table.column('Contact_number', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Contact_number', text='Contact_number', anchor=tkinter.CENTER)
                    table.column('Email_id', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Email_id', text='Email_id', anchor=tkinter.CENTER)
                    table.column('Gender', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Gender', text='Gender', anchor=tkinter.CENTER)
                    table.column('Department', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Department', text='Department', anchor=tkinter.CENTER)
                    table.column('Type', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Type', text='Type', anchor=tkinter.CENTER)
                    table.column('Residence', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Residence', text='Residence', anchor=tkinter.CENTER)
                    table.column('Designation', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Designation', text='Designation', anchor=tkinter.CENTER)
                    table.column('Home_address', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('Home_address', text='Home_address', anchor=tkinter.CENTER)
                    table.column('State', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('State', text='State', anchor=tkinter.CENTER)
                    table.column('City', width=220, minwidth=220, anchor=tkinter.CENTER)
                    table.heading('City', text='City', anchor=tkinter.CENTER)
                    table['show'] = 'headings'
                    s = ttk.Style(frame4)
                    s.theme_use('winnative')

                    # ----------------------- use it for apply on all widget ------------------------------------------
                    # s.configure('.',font=("times new roman", 12,'bold'))
                    s.configure('Treeview.Heading', font=("times new roman", 15, 'bold'), foreground='red',
                                backgound='blue')
                    s.configure('Treeview', font=("chiller", 12, 'bold'), foreground='red')
                    xs = ttk.Scrollbar(frame4, orient='horizontal')
                    xs.configure(command=table.xview)
                    ys = ttk.Scrollbar(frame4, orient='vertical')
                    ys.configure(command=table.yview)
                    table.configure(xscrollcommand=xs.set, yscrollcommand=ys.set)
                    xs.pack(side=BOTTOM, fill=X)
                    ys.pack(side=RIGHT, fill=Y)
                    frame4.place(x=390, y=16, width=750, height=433)
                    table.pack(fill=BOTH, expand=1)

                    entry_text = Label(mng, text="ID:", font=('goudy old style', 20, 'bold'), bg='#F7D4EC',
                                       fg="black")
                    entry_text.place(x=30, y=15, width=35, height=25)

                    entry_var = StringVar()
                    entry_entrybox = Entry(mng, width=32, font=("times new roman", 12), textvariable=entry_var,
                                           bg="#b3b3b3")
                    entry_entrybox.place(x=80, y=15, height=25)

                    # -------------------------------------------------  creating button  ------------------------------------

                    # ------------------------------------  add  ---------------------------------------------------------

                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> function to add <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def add_():
                        add = Toplevel()
                        add.title('Academic/management record')
                        add.config(bg="#FFE8DC")
                        add.geometry('1350x700+0+0')
                        # cerate a frame for hedaline
                        frames = Frame(add, width=1365, height=25)
                        frames.config(bg="#341809")
                        frames.place(x=0, y=0)

                        # create lables for academic/management data record
                        add_box = LabelFrame(add, width=682, height=630, text="ADD ACADEMIC/MANAGEMENT INFORMATION ",
                                             font=('arial', 20, 'bold'), fg="red")
                        add_box.config(bg="#F0F7D4")
                        add_box.place(x=1, y=25)

                        # creating faculty name lable and entry box--------------------------------------------------------------------------------------------
                        name_lable = Label(add_box, text="Name ", font=('arial', 15, 'bold'), fg='blue')
                        name_lable.config(bg="#F0F7D4")
                        name_lable.place(x=20, y=30)

                        name_var = StringVar()
                        name_entrybox = Entry(add_box, width=50, textvariable=name_var)
                        name_entrybox.place(x=250, y=30)
                        name_entrybox.focus()
                        # --------------------------------------------------------------------------------------------------------------------------------------

                        # creating email lable and entry box---------------------------------------------------------------------------------------------------
                        email_lable = Label(add_box, text="Email Id ", font=('arial', 15, 'bold'), fg='blue')
                        email_lable.config(bg="#F0F7D4")
                        email_lable.place(x=20, y=70)

                        email_var = StringVar()
                        email_entrybox = Entry(add_box, width=50, textvariable=email_var)
                        email_entrybox.place(x=250, y=70)
                        # ---------------------------------------------------------------------------------------------------------------------------------------

                        # creating contact lable and entry box---------------------------------------------------------------------------------------------------
                        contact_lable = Label(add_box, text="Contact ", font=('arial', 15, 'bold'), fg='blue')
                        contact_lable.config(bg="#F0F7D4")
                        contact_lable.place(x=20, y=110)

                        contact_var = StringVar()
                        contact_entrybox = Entry(add_box, width=50, textvariable=contact_var)
                        contact_entrybox.place(x=250, y=110)
                        # ------------------------------------------------------------------------------------------------------------------------------------------

                        # creating gender lable and combo box------------------------------------------------------------------------------------------------------
                        gender_lable = Label(add_box, text="Gender ", font=('arial', 15, 'bold'), fg='blue')
                        gender_lable.config(bg="#F0F7D4")
                        gender_lable.place(x=20, y=150)

                        gender_var = StringVar()
                        gender_combobox = ttk.Combobox(add_box, width=47, textvariable=gender_var, state='readonly')
                        gender_combobox['values'] = ('select', 'Male', 'Female', 'Other')
                        gender_combobox.current(0)
                        gender_combobox.place(x=250, y=150)
                        # -------------------------------------------------------------------------------------------------------------------------------------------

                        # creating radio button  ----------------------------------------------------------------------------------------------------------
                        usertype = StringVar()
                        radiobtn1 = Radiobutton(add_box, text='Academic', font=('arial', 15, 'bold'), bg="#F0F7D4",
                                                fg='blue',
                                                value='Academic', variable=usertype)
                        radiobtn1.place(x=20, y=190)

                        radiobtn1 = Radiobutton(add_box, text='Management', font=('arial', 15, 'bold'), bg="#F0F7D4",
                                                fg='blue',
                                                value='Management', variable=usertype)
                        radiobtn1.place(x=300, y=190)

                        # ---------------------------------------------------------------------------------------------------------------------------------------------

                        # creating ID lable and entry box------------------------------------------------------------------------------------------------------------
                        id_no_lable = Label(add_box, text="ID Number ", font=('arial', 15, 'bold'), fg='blue')
                        id_no_lable.config(bg="#F0F7D4")
                        id_no_lable.place(x=20, y=230)

                        id_var = StringVar()
                        id_entrybox = Entry(add_box, width=50, textvariable=id_var)
                        id_entrybox.place(x=250, y=230)
                        # ---------------------------------------------------------------------------------------------------------------------------------------------

                        # creating address lable and entry box------------------------------------------------------------------------------------------------------------
                        address_lable = Label(add_box, text="Home Address", font=('arial', 15, 'bold'), fg='blue')
                        address_lable.config(bg="#F0F7D4")
                        address_lable.place(x=20, y=270)

                        address_var = StringVar()
                        address_entrybox = Entry(add_box, width=50, textvariable=address_var)
                        address_entrybox.place(x=250, y=270)
                        # ---------------------------------------------------------------------------------------------------------------------------------------------

                        # creating state lable and entry box------------------------------------------------------------------------------------------------------------
                        state_lable = Label(add_box, text="State ", font=('arial', 15, 'bold'), fg='blue')
                        state_lable.config(bg="#F0F7D4")
                        state_lable.place(x=20, y=310)

                        state_var = StringVar()
                        state_entrybox = Entry(add_box, width=50, textvariable=state_var)
                        state_entrybox.place(x=250, y=310)
                        # ---------------------------------------------------------------------------------------------------------------------------------------------

                        # creating city lable and entry box------------------------------------------------------------------------------------------------------------
                        City_lable = Label(add_box, text="City", font=('arial', 15, 'bold'), fg='blue')
                        City_lable.config(bg="#F0F7D4")
                        City_lable.place(x=20, y=350)

                        City_var = StringVar()
                        City_entrybox = Entry(add_box, width=50, textvariable=City_var)
                        City_entrybox.place(x=250, y=350)
                        # ---------------------------------------------------------------------------------------------------------------------------------------------

                        # creating department lable and entry box------------------------------------------------------------------------------------------------------------
                        department_lable = Label(add_box, text="Department ", font=('arial', 15, 'bold'), fg='blue')
                        department_lable.config(bg="#F0F7D4")
                        department_lable.place(x=20, y=390)

                        Department_var = StringVar()
                        Department_entrybox = Entry(add_box, width=50, textvariable=Department_var)
                        Department_entrybox.place(x=250, y=390)
                        # ---------------------------------------------------------------------------------------------------------------------------------------------

                        # creating resident lable and combo box------------------------------------------------------------------------------------------------------
                        resident_lable = Label(add_box, text="Resident ", font=('arial', 15, 'bold'), fg='blue')
                        resident_lable.config(bg="#F0F7D4")
                        resident_lable.place(x=20, y=430)

                        resident_var = StringVar()
                        resident_combobox = ttk.Combobox(add_box, width=47, textvariable=resident_var, state='readonly')
                        resident_combobox['values'] = ('select', 'yes', 'no')
                        resident_combobox.current(0)
                        resident_combobox.place(x=250, y=430)
                        # -------------------------------------------------------------------------------------------------------------------------------------------

                        # creating designation lable and combo box------------------------------------------------------------------------------------------------------
                        designation_lable = Label(add_box, text="Designation ", font=('arial', 15, 'bold'), fg='blue')
                        designation_lable.config(bg="#F0F7D4")
                        designation_lable.place(x=20, y=470)

                        designation_var = StringVar()
                        designation_combobox = ttk.Combobox(add_box, width=47, textvariable=designation_var,
                                                            state='readonly')
                        designation_combobox['values'] = (
                            'select', 'Director', 'Registrar', 'Dean', 'H.O.D', 'Professor', 'Assistant Professor',
                            'Lab Assistant',
                            'Clerk', 'Accountant', 'Librarian', 'other')
                        designation_combobox.current(0)
                        designation_combobox.place(x=250, y=470)
                        # ----------------------------------------------------------------------------------------------------------------

                        # create a check box
                        checkbtn_var = IntVar()
                        checkbtn = Checkbutton(add, text=" Please ensure that the details filled in are correct",
                                               onvalue='1',
                                               offvalue='0', font=('arial', 12), bg="#FFE8DC", fg='Black',
                                               variable=checkbtn_var)
                        checkbtn.place(x=1, y=660)

                        # QR CODE
                        def QRCode():
                            id = id_entrybox.get()
                            fileName = id + '.jpg'
                            # ============Now generate and save qr code================
                            if len(id) < 1:
                                messagebox.showwarning('Warning!', 'Enter your id first in entry box', parent=add)
                                # sr_no_var.config(bg='red2')
                                QR.config(text='There is an error occured in Generating QR Code', image='',
                                          width=40, height=15, fg='red')
                            else:
                                img = qrcode.make(id)
                                img.save(fileName)
                                add.photo = PhotoImage(file=fileName)
                                QR.config(image=add.photo, text='QR Code Generated Successfully!',
                                          fg='green', compound=TOP, width=300, height=300)
                                messagebox.showinfo('Saved',
                                                    'QR code saved as " ' + fileName + ' " successfully!\n\tin current location',
                                                    parent=add)

                        # ---------------------------------------------------  function to add record  -----------------------------------------------------
                        def add_record():
                            id = id_var.get()
                            name = name_var.get()
                            email = email_var.get()
                            contact = contact_var.get()
                            gender = gender_var.get()
                            type = usertype.get()
                            address = address_var.get()
                            state = state_var.get()
                            city = City_var.get()
                            department = Department_var.get()
                            resident = resident_var.get()
                            designation = designation_var.get()
                            if (
                                    id == '' or name == '' or email == '' or contact == '' or gender == '' or type == '' or address == '' or state == '' or city == '' or department == '' or resident == '' or designation == ''):
                                messagebox.showerror('error', 'All fields are required', parent=add)
                                return
                            else:
                                try:
                                    query = 'create table if not exists staff( ID varchar(20) not null primary key,Name varchar(30) not null,Email varchar(30) not null unique,Contact varchar(10) not null,Gender varchar(10) not null,Type varchar(10) not null,Address varchar(50) not null,State varchar(10) not null,City varchar(10) not null,Department varchar(40) not null,Resident varchar(3) not null,Designation varchar(30) not null)'
                                    cur.execute(query)
                                    query = "create table if not exists new_table(ID varchar(20) not null primary key,Name varchar(25) not null,Type varchar(15) not null,hostel varchar(25),foreign key (ID) references staff(ID) on delete cascade,foreign key (ID) references student(Serial_number) on delete cascade)"
                                    cur.execute(query)
                                    cur.execute('SET foreign_key_checks = 0')
                                    str1 = 'insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                                    cur.execute(str1, (
                                        id, name, email, contact, gender, type, address, state, city, department,
                                        resident,
                                        designation))
                                    cur.execute('SET foreign_key_checks = 1')
                                    conn.commit()
                                except mysql.connector.IntegrityError as err:
                                    messagebox.showerror("error", err, parent=add)
                                    return
                                else:
                                    QRCode()
                                    messagebox.showinfo('notification',
                                                        'QR Code generated and record added successfully',
                                                        parent=add)

                        # Add student button for student record page
                        Add_details = Button(add, text="ADD RECORD & GENERATE QR CODE", fg="white", bg="red",
                                             font=('arial', 15, 'bold'), command=add_record)
                        Add_details.place(x=825, y=460)

                        # function for adding another student
                        def add_another():
                            name_entrybox.delete(0, END)
                            email_entrybox.delete(0, END)
                            contact_entrybox.delete(0, END)
                            id_entrybox.delete(0, END)
                            gender_combobox.set('')
                            Department_entrybox.delete(0, END)
                            address_entrybox.delete(0, END)
                            state_entrybox.delete(0, END)
                            City_entrybox.delete(0, END)
                            resident_combobox.set('')
                            designation_combobox.set('')
                            radiobtn1.deselect()

                        # function for resetting qr code
                        def reset():
                            id_entrybox.delete(0, END)
                            id_entrybox.config(bg='white')
                            QR.config(image='', text='', width=0, height=0)

                        # button for adding another student
                        add_details2 = Button(add, text="ADD ANOTHER RECORD", fg="white", bg="red",
                                              font=('arial', 15, 'bold'),
                                              command=lambda: [add_another(), reset()])
                        add_details2.place(x=890, y=535)

                        """""
                        #button for reset
                        reset = Button(add, text = "RESET", fg="white", bg="red", font = ('arial', 15, 'bold'), command = reset)
                        reset.place(x=965,y= 610)
                        """
                        QR = Label(add, text='No QR\nAvailable', font=('times new roman', 15), image='', bg='plum1')
                        QR.place(x=870, y=75, width='300', height='350')
                        add.mainloop()

                    Add = Button(mng, text="Add Record", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                 fg="white", bg="#94B814", activebackground='#C21460', command=add_)
                    Add.place(x=30, y=50)

                    # --------------------------------------   search   -----------------------------------------------------
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  function to search  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def searchst():
                        entry = entry_var.get()
                        print(entry)
                        query = "select * from staff where ID=%s"
                        data = (entry,)
                        cur.execute(query, data)
                        final = cur.fetchall()
                        table.delete(*table.get_children())
                        if not final:
                            messagebox.showinfo('message', "No record found")
                        else:
                            i = 0
                            for ro in final:
                                table.insert('', i, text='', values=(
                                    ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10],
                                    ro[11]))
                                i = i + 1

                    search = Button(mng, text="Search Record", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                    fg="white", bg="#94B814", activebackground='#C21460', command=searchst)
                    search.place(x=30, y=110)

                    # -------------------------------------   delete  -------------------------------------------------------
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   function to delete  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def del1():
                        global conn, cur
                        entry = entry_var.get()

                        if (entry == ''):
                            cc = table.focus()
                            content = table.item(cc)
                            pp = content['values'][0]
                            strr = 'delete from staff where ID=%s'
                            data = (pp,)
                            cur.execute(strr, data)
                            conn.commit()
                            messagebox.showinfo('notification', 'ID {} deleted succesfully...'.format(pp))
                        else:
                            query = 'select * from staff  where ID=%s'
                            data = (entry,)
                            cur.execute(query, data)
                            result = cur.fetchone()
                            if (result == None):
                                messagebox.showerror('error', 'record is not present')
                            else:
                                strr = 'delete from staff where ID=%s'
                                data = (entry,)
                                cur.execute(strr, data)
                                conn.commit()
                                messagebox.showinfo('notification', 'ID {} deleted succesfully...'.format(entry))

                        query = "select * from staff"
                        cur.execute(query)
                        final = cur.fetchall()
                        table.delete(*table.get_children())
                        if not final:
                            messagebox.showinfo('message', "No record found")
                        else:
                            i = 0
                            for ro in final:
                                table.insert('', i, text='', values=(
                                    ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10],
                                    ro[11]))
                                i = i + 1

                    delete = Button(mng, text="Delete Record", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                    fg="white", bg="#94B814", activebackground='#C21460', command=del1)
                    delete.place(x=30, y=170)

                    # ------------------------------------   update  -----------------------------------------------------------
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   function for update  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def up():
                        global conn, cur
                        entry = entry_var.get()
                        # -------------------------------------- checking ID for update is present or not -----------
                        query = 'select * from staff  where ID=%s'
                        data = (entry,)
                        cur.execute(query, data)
                        result = cur.fetchall()
                        if (result == None):
                            messagebox.showerror('error', 'record is not present')
                        else:
                            i = 0
                            for ro in result:
                                table.insert('', i, text='', values=(
                                    ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10],
                                    ro[11]))
                                i = i + 1
                            cc = table.focus()
                            content = table.item(cc)
                            pp = content['values']
                            # ------------------------ defining update window --------------------------------------------------
                            update = Toplevel()
                            update.title('Academic/management record')
                            update.config(bg="#FFE8DC")
                            update.geometry('700x700+0+0')
                            # cerate a frame for hedaline
                            frames = Frame(update, width=1365, height=25)
                            frames.config(bg="#341809")
                            frames.place(x=0, y=0)

                            # create lables for academic/management data record
                            update_box = LabelFrame(update, width=690, height=600,
                                                    text="Update Academic/Management Information ",
                                                    font=('arial', 20, 'bold'), fg="red")
                            update_box.config(bg="#F0F7D4")
                            update_box.place(x=1, y=25)

                            # creating faculty name lable and entry box--------------------------------------------------------------------------------------------
                            name_lable = Label(update_box, text="Name ", font=('arial', 15, 'bold'), fg='blue')
                            name_lable.config(bg="#F0F7D4")
                            name_lable.place(x=20, y=30)

                            name_var = StringVar()
                            name_entrybox = Entry(update_box, width=50, textvariable=name_var)
                            name_entrybox.place(x=250, y=30)
                            name_entrybox.focus()
                            # --------------------------------------------------------------------------------------------------------------------------------------

                            # creating email lable and entry box---------------------------------------------------------------------------------------------------
                            email_lable = Label(update_box, text="Email Id ", font=('arial', 15, 'bold'), fg='blue')
                            email_lable.config(bg="#F0F7D4")
                            email_lable.place(x=20, y=70)

                            email_var = StringVar()
                            email_entrybox = Entry(update_box, width=50, textvariable=email_var)
                            email_entrybox.place(x=250, y=70)
                            # ---------------------------------------------------------------------------------------------------------------------------------------

                            # creating contact lable and entry box---------------------------------------------------------------------------------------------------
                            contact_lable = Label(update_box, text="Contact ", font=('arial', 15, 'bold'), fg='blue')
                            contact_lable.config(bg="#F0F7D4")
                            contact_lable.place(x=20, y=110)

                            contact_var = StringVar()
                            contact_entrybox = Entry(update_box, width=50, textvariable=contact_var)
                            contact_entrybox.place(x=250, y=110)
                            # ------------------------------------------------------------------------------------------------------------------------------------------

                            # creating gender lable and combo box------------------------------------------------------------------------------------------------------
                            gender_lable = Label(update_box, text="Gender ", font=('arial', 15, 'bold'), fg='blue')
                            gender_lable.config(bg="#F0F7D4")
                            gender_lable.place(x=20, y=150)

                            gender_var = StringVar()
                            gender_combobox = ttk.Combobox(update_box, width=47, textvariable=gender_var,
                                                           state='readonly')
                            gender_combobox['values'] = ('select', 'Male', 'Female', 'Other')
                            gender_combobox.current(0)
                            gender_combobox.place(x=250, y=150)
                            # -------------------------------------------------------------------------------------------------------------------------------------------

                            # creating radio button  ----------------------------------------------------------------------------------------------------------
                            usertype = StringVar()
                            radiobtn1 = Radiobutton(update_box, text='Academic', font=('arial', 15, 'bold'),
                                                    bg="#F0F7D4",
                                                    fg='blue',
                                                    value='Academic', variable=usertype)
                            radiobtn1.place(x=20, y=190)

                            radiobtn1 = Radiobutton(update_box, text='Management', font=('arial', 15, 'bold'),
                                                    bg="#F0F7D4",
                                                    fg='blue',
                                                    value='Management', variable=usertype)
                            radiobtn1.place(x=300, y=190)

                            # ---------------------------------------------------------------------------------------------------------------------------------------------

                            # creating ID lable and entry box------------------------------------------------------------------------------------------------------------
                            id_no_lable = Label(update_box, text="ID Number ", font=('arial', 15, 'bold'), fg='blue')
                            id_no_lable.config(bg="#F0F7D4")
                            id_no_lable.place(x=20, y=230)

                            id_var = StringVar()
                            id_entrybox = Entry(update_box, width=50, textvariable=id_var)
                            id_entrybox.place(x=250, y=230)
                            # ---------------------------------------------------------------------------------------------------------------------------------------------

                            # creating updateress lable and entry box------------------------------------------------------------------------------------------------------------
                            updateress_lable = Label(update_box, text="Home updateress", font=('arial', 15, 'bold'),
                                                     fg='blue')
                            updateress_lable.config(bg="#F0F7D4")
                            updateress_lable.place(x=20, y=270)

                            updateress_var = StringVar()
                            updateress_entrybox = Entry(update_box, width=50, textvariable=updateress_var)
                            updateress_entrybox.place(x=250, y=270)
                            # ---------------------------------------------------------------------------------------------------------------------------------------------

                            # creating state lable and entry box------------------------------------------------------------------------------------------------------------
                            state_lable = Label(update_box, text="State ", font=('arial', 15, 'bold'), fg='blue')
                            state_lable.config(bg="#F0F7D4")
                            state_lable.place(x=20, y=310)

                            state_var = StringVar()
                            state_entrybox = Entry(update_box, width=50, textvariable=state_var)
                            state_entrybox.place(x=250, y=310)
                            # ---------------------------------------------------------------------------------------------------------------------------------------------

                            # creating city lable and entry box------------------------------------------------------------------------------------------------------------
                            City_lable = Label(update_box, text="City", font=('arial', 15, 'bold'), fg='blue')
                            City_lable.config(bg="#F0F7D4")
                            City_lable.place(x=20, y=350)

                            City_var = StringVar()
                            City_entrybox = Entry(update_box, width=50, textvariable=City_var)
                            City_entrybox.place(x=250, y=350)
                            # ---------------------------------------------------------------------------------------------------------------------------------------------

                            # creating department lable and entry box------------------------------------------------------------------------------------------------------------
                            department_lable = Label(update_box, text="Department ", font=('arial', 15, 'bold'),
                                                     fg='blue')
                            department_lable.config(bg="#F0F7D4")
                            department_lable.place(x=20, y=390)

                            Department_var = StringVar()
                            Department_entrybox = Entry(update_box, width=50, textvariable=Department_var)
                            Department_entrybox.place(x=250, y=390)
                            # ---------------------------------------------------------------------------------------------------------------------------------------------

                            # creating resident lable and combo box------------------------------------------------------------------------------------------------------
                            resident_lable = Label(update_box, text="Resident ", font=('arial', 15, 'bold'), fg='blue')
                            resident_lable.config(bg="#F0F7D4")
                            resident_lable.place(x=20, y=430)

                            resident_var = StringVar()
                            resident_combobox = ttk.Combobox(update_box, width=47, textvariable=resident_var,
                                                             state='readonly')
                            resident_combobox['values'] = ('select', 'yes', 'no')
                            resident_combobox.current(0)
                            resident_combobox.place(x=250, y=430)
                            # -------------------------------------------------------------------------------------------------------------------------------------------

                            # creating designation lable and combo box------------------------------------------------------------------------------------------------------
                            designation_lable = Label(update_box, text="Designation ", font=('arial', 15, 'bold'),
                                                      fg='blue')
                            designation_lable.config(bg="#F0F7D4")
                            designation_lable.place(x=20, y=470)

                            designation_var = StringVar()
                            designation_combobox = ttk.Combobox(update_box, width=47, textvariable=designation_var,
                                                                state='readonly')
                            designation_combobox['values'] = (
                                'select', 'Director', 'Registrar', 'Dean', 'H.O.D', 'Professor', 'Assistant Professor',
                                'Lab Assistant',
                                'Clerk', 'Accountant', 'Librarian', 'other')
                            designation_combobox.current(0)
                            designation_combobox.place(x=250, y=470)
                            # ----------------------------------------------------------------------------------------------------------------

                            # create a check box
                            checkbtn_var = IntVar()
                            checkbtn = Checkbutton(update, text=" Please ensure that the details filled in are correct",
                                                   onvalue='1',
                                                   offvalue='0', font=('arial', 12), bg="#FFE8DC", fg='Black',
                                                   variable=checkbtn_var)
                            checkbtn.place(x=1, y=590)

                            # --------------------------- setting older values -----------------------------------------
                            id_var.set(pp[0])
                            name_var.set(pp[1])
                            email_var.set(pp[2])
                            contact_var.set(pp[3])
                            gender_var.set(pp[4])
                            radiobtn1.select()
                            updateress_var.set(pp[6])
                            state_var.set(pp[7])
                            City_var.set(pp[8])
                            Department_var.set(pp[9])
                            resident_var.set(pp[10])
                            designation_var.set(pp[11])

                            def update_func():

                                # ------------------- getting updated data ----------------------------------------------
                                radio = usertype.get()
                                name = name_var.get()
                                email = email_var.get()
                                contact = contact_var.get()
                                # sr = sr_no_var.get()
                                gender = gender_var.get()
                                department = Department_var.get()
                                updateress = updateress_var.get()
                                state = state_var.get()
                                city = City_var.get()
                                resident = resident_var.get()
                                designation = designation_var.get()

                                # -------------------------- query for update ------------------------------------------
                                query = "update staff set Name=%s,Contact=%s,Email=%s,Gender=%s,Department=%s," \
                                        "Type=%s,Resident=%s,Designation=%s," \
                                        "Address=%s,State=%s,City=%s where ID=%s"
                                data = (
                                    name, contact, email, gender, department, radio, resident, designation, updateress,
                                    state,
                                    city,
                                    pp[0])
                                cur.execute(query, data)
                                conn.commit()
                                messagebox.showinfo('notification', 'ID {} Updated succesfully...'.format(pp[0]),
                                                    parent=update)

                                query = "select * from staff"
                                cur.execute(query)
                                final = cur.fetchall()
                                table.delete(*table.get_children())
                                if not final:
                                    messagebox.showinfo('message', "No record found")
                                else:
                                    i = 0
                                    for ro in final:
                                        table.insert('', i, text='', values=(
                                            ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9],
                                            ro[10],
                                            ro[11],))
                                        i = i + 1

                                update.mainloop()

                            # -------------------- update button -------------------------------------------------------
                            update_b = Button(update, text="Update", fg="white", bg="red",
                                              font=('arial', 10, 'bold'),
                                              command=update_func)
                            update_b.place(x=250, y=655)

                    update = Button(mng, text="Update Record", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                    fg="white", bg="#94B814", activebackground='#C21460', command=up)
                    update.place(x=30, y=230)

                    # ------------------------------------  export  -----------------------------------------------------------
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   function for export  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def exp():
                        ff = filedialog.asksaveasfilename()
                        gg = table.get_children()
                        ID, Name, Email_id, Contact_number, Gender, Type, Home_address, State, City, Department, Residence, Designation = [], [], [], [], [], [], [], [], [], [], [], []
                        for i in gg:
                            content = table.item(i)
                            pp = content['values']
                            ID.append(pp[0]), Name.append(pp[1]), Email_id.append(pp[2]), Contact_number.append(
                                pp[3]), Gender.append(pp[4]), Type.append(pp[5]), Home_address.append(
                                pp[6]), State.append(
                                pp[7]), City.append(pp[8]), Department.append(pp[9]), Residence.append(
                                pp[10]), Designation.append(
                                pp[11])
                        dd = ['ID', 'Name', 'Email_id', 'Contact_number', 'Gender', 'Type', 'Home_address',
                              'State', 'City', 'Department', 'Residence', 'Designation']
                        df = pandas.DataFrame(list(
                            zip(ID, Name, Email_id, Contact_number, Gender, Type, Home_address, State, City, Department,
                                Residence,
                                Designation)), columns=dd)
                        paths = r'{}.csv'.format(ff)
                        df.to_csv(paths, index=False)
                        messagebox.showinfo('notification', ' Data is saved {}'.format(paths))

                    export = Button(mng, text="Export Record", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                    fg="white", bg="#94B814", activebackground='#C21460', command=exp)
                    export.place(x=30, y=290)

                    # ------------------------------------ view all -------------------------------------------------------------
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   function to view all  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def view_all():

                        query = "select * from staff"
                        cur.execute(query, )
                        final = cur.fetchall()
                        table.delete(*table.get_children())
                        if not final:
                            messagebox.showinfo('message', "No record found")
                        else:
                            i = 0
                            for ro in final:
                                table.insert('', i, text='', values=(
                                    ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7], ro[8], ro[9], ro[10],
                                    ro[11]))
                                i = i + 1

                    viewS = Button(mng, text="View All", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                   fg="white", bg="#94B814", activebackground='#C21460', command=view_all)
                    viewS.place(x=30, y=350)

                    # ------------------------------------  exit  -------------------------------------------------------------
                    # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>   function to exit  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                    def ex():
                        res = messagebox.askyesnocancel('notification', 'Do you want to exit')
                        if (res == True):
                            mng.destroy()

                    exit = Button(mng, text="Exit", width=25, font=('arial', 15, 'bold'), relief=RIDGE,
                                  fg="white", bg="#94B814", activebackground='#C21460', command=ex)
                    exit.place(x=30, y=410)

                frame_text = Label(view, text="QR EnExRe", font=('goudy old style', 20, 'bold'),
                                   bg='#e1dd72',
                                   fg="#1b6535", padx=10)
                frame_text.place(x=0, y=0, relwidth=1, height=50)

                frame_menu = Label(view, width=50, bg="#1b6535").place(x=0, y=95, relwidth=1, height=80)

                # ------------------------------------  label for query  ------------------------------------------------------
                frame_query = Label(view, text="Query", font=('goudy old style', 20, 'bold'), bg='#a8c66c',
                                    fg="#1b6535",
                                    padx=5,
                                    anchor='w')
                frame_query.place(x=0, y=50, relwidth=1, height=50)

                query_var = StringVar()
                query_combobox = ttk.Combobox(view, width=80, textvariable=query_var, state='readonly',
                                              font=("times new roman", 12))
                query_combobox['values'] = (
                    'All hosteler who are outside from given time', 'Hostelers who are still outside the campus',
                    'Day-Scholar who are still in the campus',
                    'Hostelers of a particular hostel who are/were outside from the given time',
                    "view record of a person of a particular date",
                    'view all records of a particular date', "view record of a person of a particular month")
                # search_combobox.current(0)
                query_combobox.place(x=100, y=60, height="25")

                # --------------------------------------------  searchby label and combobox  -------------------------------
                search_lable = Label(view, text="Search By", font=('arial', 15, 'bold'), bg='#1b6535', fg="#ffe066")
                search_lable.place(x=65, y=105)

                search_var = StringVar()
                search_combobox = ttk.Combobox(view, width=20, textvariable=search_var, state='readonly',
                                               font=("times new roman", 12))
                search_combobox['values'] = ('Hostel Name', 'Id')
                # search_combobox.current(0)
                search_combobox.place(x=20, y=140, height="25")

                # --------------------------------- hostel/id label and entry box  ---------------------------------------------
                search_lable1 = Label(view, text="Enter Hostel Name/ID", font=('arial', 15, 'bold'), bg='#1b6535',
                                      fg="#ffe066")
                search_lable1.place(x=250, y=105)

                search_var1 = StringVar()
                search_entrybox = Entry(view, width=25, font=("times new roman", 12), textvariable=search_var1,
                                        bg="#b3b3b3")
                search_entrybox.place(x=250, y=140, height="25")
                # ---------------------------------  day label and combobox  ------------------------------------------------------

                day_lable = Label(view, text="Day", font=('arial', 15, 'bold'), bg='#1b6535', fg="#ffe066")
                day_lable.place(x=506, y=105)

                day_var = StringVar()
                day_combobox = ttk.Combobox(view, width=5, textvariable=day_var, state='readonly',
                                            font=("times new roman", 12))
                day_combobox['values'] = (
                    '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16',
                    '17', '18',
                    '19',
                    '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
                # day_combobox.current(0)
                day_combobox.place(x=500, y=140, height="25")

                # ---------------------------------  month label and combobox  ------------------------------------------------------

                month_lable = Label(view, text="Month", font=('arial', 15, 'bold'), bg='#1b6535', fg="#ffe066")
                month_lable.place(x=609, y=105)

                month_var = StringVar()
                month_combobox = ttk.Combobox(view, width=10, textvariable=month_var, state='readonly',
                                              font=("times new roman", 12))
                month_combobox['values'] = (
                    'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                    'November',
                    'December')
                # month_combobox.current(0)
                month_combobox.place(x=600, y=140, height="25")

                # ---------------------------------  year label and combobox  ------------------------------------------------------

                year_lable = Label(view, text="Year", font=('arial', 15, 'bold'), bg='#1b6535', fg="#ffe066")
                year_lable.place(x=738, y=105)

                year_var = StringVar()
                year_combobox = ttk.Combobox(view, width=7, textvariable=year_var, state='readonly',
                                             font=("times new roman", 12))
                year_combobox['values'] = ('2021', '2022', '2023', '2024', '2025', '2026', '2027')
                # year_combobox.current(0)
                year_combobox.place(x=730, y=140, height="25")

                # ---------------------------------  time label and combobox  -------------------------------------------------

                time_lable = Label(view, text="Time", font=('arial', 15, 'bold'), bg='#1b6535', fg="#ffe066")
                time_lable.place(x=850, y=105)

                time_var = StringVar()
                time_entrybox = Entry(view, width=10, font=("times new roman", 12), textvariable=time_var, bg="#b3b3b3")
                time_entrybox.place(x=835, y=140)
                # ---------------------------------  type label and combobox  -------------------------------------------------

                type_lable = Label(view, text="Type", font=('arial', 15, 'bold'), bg='#1b6535', fg="#ffe066")
                type_lable.place(x=985, y=105)

                type_var = StringVar()
                type_combobox = ttk.Combobox(view, width=7, textvariable=type_var, state='readonly',
                                             font=("times new roman", 12))
                type_combobox['values'] = ('Hosteler', 'Day-Scholar', 'Academic', 'management')
                type_combobox.place(x=978, y=140)

                def clear():
                    query_combobox.set('')
                    day_combobox.set('')
                    type_combobox.set('')
                    month_combobox.set('')
                    year_combobox.set('')
                    search_combobox.set('')
                    time_entrybox.delete(0, END)
                    search_entrybox.delete(0, END)

                def display():
                    global conn, cur, table
                    # cur= conn.cursor()
                    if (month_var.get() == 'January'):
                        month = '01'
                    elif (month_var.get() == 'February'):
                        month = '02'
                    elif (month_var.get() == 'March'):
                        month = '03'
                    elif (month_var.get() == 'April'):
                        month = '04'
                    elif (month_var.get() == 'May'):
                        month = '05'
                    elif (month_var.get() == 'June'):
                        month = '06'
                    elif (month_var.get() == 'July'):
                        month = '07'
                    elif (month_var.get() == 'August'):
                        month = '08'
                    elif (month_var.get() == 'September'):
                        month = '09'
                    elif (month_var.get() == 'October'):
                        month = '10'
                    elif (month_var.get() == 'November'):
                        month = '11'
                    else:
                        month = '12'

                    year = year_var.get()
                    day = day_var.get()
                    search_by = search_var.get()
                    search_entry = search_var1.get()
                    time = time_var.get()
                    type = type_var.get()
                    query = query_var.get()
                    current_date_display = year + '-' + month + '-' + day

                    def tree_query1_2_5():

                        frame4 = LabelFrame(view, bg="white")
                        table = Treeview(frame4, columns=('ID', 'Name', 'Hostel'))
                        table.column('ID', width=50, minwidth=50, anchor=tkinter.CENTER)
                        table.column('Name', width=50, minwidth=50, anchor=tkinter.CENTER)
                        table.column('Hostel', width=50, minwidth=50, anchor=tkinter.CENTER)
                        table.heading('ID', text='ID', anchor=tkinter.CENTER)
                        table.heading('Name', text='Name', anchor=tkinter.CENTER)
                        table.heading('Hostel', text='Hostel', anchor=tkinter.CENTER)
                        table['show'] = 'headings'
                        s = ttk.Style(frame4)
                        s.theme_use('winnative')
                        s.configure('Treeview.Heading', font=("times new roman", 15, 'bold'), foreground='red',
                                    backgound='blue')
                        s.configure('Treeview', font=("chiller", 12, 'bold'), foreground='red')
                        xs = ttk.Scrollbar(frame4, orient='horizontal')
                        xs.configure(command=table.xview)
                        ys = ttk.Scrollbar(frame4, orient='vertical')
                        ys.configure(command=table.yview)
                        table.configure(xscrollcommand=xs.set, yscrollcommand=ys.set)
                        xs.pack(side=BOTTOM, fill=X)
                        ys.pack(side=RIGHT, fill=Y)
                        frame4.place(x=200, y=200, width=1100, height=450)
                        table.pack(fill=BOTH, expand=1)
                        if not final:
                            messagebox.showinfo('message', "No record found")
                        else:
                            i = 0
                            for ro in final:
                                table.insert('', i, text='', values=(ro[0], ro[1], ro[2]))
                                i = i + 1

                    def tree_query6_7():
                        frame4 = LabelFrame(view, bg="white")
                        table = Treeview(frame4,
                                         columns=(
                                             'ID', 'Name', 'Ist-Activity', 'Date', 'Time', 'last-Activity', 'Type',
                                             'Hostel'))
                        table.column('ID', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('Name', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('Ist-Activity', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('Date', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('Time', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('last-Activity', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('Type', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('Hostel', width=220, minwidth=220, anchor=tkinter.CENTER)

                        table.heading('Type', text='Type', anchor=tkinter.CENTER)
                        table.heading('Name', text='Name', anchor=tkinter.CENTER)
                        table.heading('ID', text='ID', anchor=tkinter.CENTER)
                        table.heading('Date', text='Date', anchor=tkinter.CENTER)
                        table.heading('Hostel', text='Hostel', anchor=tkinter.CENTER)
                        table.heading('Ist-Activity', text='Ist-Activity', anchor=tkinter.CENTER)
                        table.heading('last-Activity', text='Last-Activity', anchor=tkinter.CENTER)
                        table.heading('Time', text='Time', anchor=tkinter.CENTER)
                        table['show'] = 'headings'
                        s = ttk.Style(frame4)
                        s.theme_use('clam')
                        s.configure('Treeview.Heading', font=("times new roman", 15, 'bold'), foreground='red',
                                    backgound='blue')
                        s.configure('Treeview', font=("chiller", 12, 'bold'), foreground='red')
                        xs = ttk.Scrollbar(frame4, orient='horizontal')
                        xs.configure(command=table.xview)
                        ys = ttk.Scrollbar(frame4, orient='vertical')
                        ys.configure(command=table.yview)
                        table.configure(xscrollcommand=xs.set, yscrollcommand=ys.set)
                        xs.pack(side=BOTTOM, fill=X)
                        ys.pack(side=RIGHT, fill=Y)
                        frame4.place(x=200, y=200, width=1100, height=450)
                        table.pack(fill=BOTH, expand=1)
                        if not final:
                            messagebox.showinfo('message', "No record found")
                        else:
                            i = 0
                            for ro in final:
                                table.insert('', i, text='',
                                             values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7]))
                                i = i + 1

                    # ----------------------------------  1--------------------------------------------------------------
                    if (query == 'All hosteler who are outside from given time'):
                        query = "select ID,Name,hostel from activity where Date=%s and Type=%s and last_time>%s"
                        data = (current_date_display, 'Hosteler', time)
                        cur.execute(query, data)
                        final = cur.fetchall()
                        tree_query1_2_5()

                    # -------------------------------------------------------------- 2 -------------------------------------
                    elif (query == 'Hostelers who are still outside the campus'):
                        query = "select ID,Name,hostel from activity where Date=%s and Type=%s and flag2=%s"
                        data = (current_date_display, 'hosteler', 'out')
                        cur.execute(query, data)
                        final = cur.fetchall()
                        tree_query1_2_5()
                    # -------------------------------------------------------------- 3 ---------------------------------------
                    elif (query == 'Day-Scholar who are still in the campus'):
                        query = "select ID,Name from activity where Date=%s and Type=%s and flag2=%s"
                        data = (current_date_display, type, 'in')
                        cur.execute(query, data)
                        final = cur.fetchall()
                        frame4 = LabelFrame(view, bg="white")
                        table = Treeview(frame4, columns=('ID', 'Name'))
                        table.column('ID', width=50, minwidth=50, anchor=tkinter.CENTER)
                        table.column('Name', width=50, minwidth=50, anchor=tkinter.CENTER)
                        table.heading('ID', text='ID', anchor=tkinter.CENTER)
                        table.heading('Name', text='Name', anchor=tkinter.CENTER)
                        table['show'] = 'headings'
                        s = ttk.Style(frame4)
                        s.theme_use('clam')
                        s.configure('Treeview.Heading', font=("times new roman", 15, 'bold'), foreground='red',
                                    backgound='blue')
                        s.configure('Treeview', font=("chiller", 12, 'bold'), foreground='red')
                        xs = ttk.Scrollbar(frame4, orient='horizontal')
                        xs.configure(command=table.xview)
                        ys = ttk.Scrollbar(frame4, orient='vertical')
                        ys.configure(command=table.yview)
                        table.configure(xscrollcommand=xs.set, yscrollcommand=ys.set)
                        xs.pack(side=BOTTOM, fill=X)
                        ys.pack(side=RIGHT, fill=Y)
                        frame4.place(x=200, y=200, width=1100, height=450)
                        table.pack(fill=BOTH, expand=1)
                        if not final:
                            messagebox.showinfo('message', "No record found")
                        else:
                            i = 0
                            for ro in final:
                                table.insert('', i, text='', values=(ro[0], ro[1], ro[2]))
                                i = i + 1

                    # -------------------------------------------------------------  4 ----------------------------------------
                    elif (query == 'Hostelers of a particular hostel who are/were outside from the given time'):
                        query = "select ID,Name,hostel from activity where Date=%s and Type=%s and hostel=%s "
                        data = (current_date_display, 'hosteler', search_entry)
                        cur.execute(query, data)
                        final = cur.fetchall()
                        tree_query1_2_5()

                    # -------------------------------------------------------------  5  ---------------------------------------
                    elif (query == 'view record of a person of a particular date'):
                        query = "select Name, Type,hostel from activity where Date=%s and ID=%s"
                        data = (current_date_display, search_entry)
                        cur.execute(query, data)
                        final = cur.fetchall()
                        # -------------------------- left treeview ---------------------------------------------------
                        frame4 = LabelFrame(view, bg="white")
                        table = Treeview(frame4, columns=('Name', 'Type', 'Hostel'))
                        table.column('Name', width=50, minwidth=50, anchor=tkinter.CENTER)
                        table.column('Type', width=50, minwidth=50, anchor=tkinter.CENTER)
                        table.column('Hostel', width=50, minwidth=50, anchor=tkinter.CENTER)
                        table.heading('Type', text='Type', anchor=tkinter.CENTER)
                        table.heading('Name', text='Name', anchor=tkinter.CENTER)
                        table.heading('Hostel', text='Hostel', anchor=tkinter.CENTER)
                        table['show'] = 'headings'
                        s = ttk.Style(frame4)
                        s.theme_use('clam')
                        s.configure('Treeview.Heading', font=("times new roman", 15, 'bold'), foreground='red',
                                    backgound='blue')
                        s.configure('Treeview', font=("chiller", 12, 'bold'), foreground='red')
                        xs = ttk.Scrollbar(frame4, orient='horizontal')
                        xs.configure(command=table.xview)
                        ys = ttk.Scrollbar(frame4, orient='vertical')
                        ys.configure(command=table.yview)
                        table.configure(xscrollcommand=xs.set, yscrollcommand=ys.set)
                        xs.pack(side=BOTTOM, fill=X)
                        ys.pack(side=RIGHT, fill=Y)
                        frame4.place(x=200, y=200, width=700, height=450)
                        table.pack(fill=BOTH, expand=1)
                        # -------------------------------------- right treeview ------------------------------------------
                        frame5 = LabelFrame(view, bg="white")
                        table2 = Treeview(frame5, columns=('Entry-Time', 'Exit-Time'))
                        table2.column('Entry-Time', width=10, minwidth=10, anchor=tkinter.CENTER)
                        table2.column('Exit-Time', width=10, minwidth=10, anchor=tkinter.CENTER)
                        table2.heading('Entry-Time', text='Entry-Time', anchor=tkinter.CENTER)
                        table2.heading('Exit-Time', text='Exit-Time', anchor=tkinter.CENTER)
                        table2['show'] = 'headings'
                        s = ttk.Style(frame5)
                        s.theme_use('clam')
                        s.configure('Treeview.Heading', font=("times new roman", 15, 'bold'), foreground='red',
                                    backgound='blue')
                        s.configure('Treeview', font=("chiller", 12, 'bold'), foreground='red')
                        xs = ttk.Scrollbar(frame5, orient='horizontal')
                        xs.configure(command=table2.xview)
                        ys = ttk.Scrollbar(frame5, orient='vertical')
                        ys.configure(command=table2.yview)
                        table2.configure(xscrollcommand=xs.set, yscrollcommand=ys.set)
                        xs.pack(side=BOTTOM, fill=X)
                        ys.pack(side=RIGHT, fill=Y)
                        frame5.place(x=900, y=200, width=400, height=450)
                        table2.pack(fill=BOTH, expand=1)
                        # ----------------------------------- inserting data into left treeview --------------------------
                        if not final:
                            messagebox.showinfo('message', "No record found")
                        else:
                            i = 0
                            for ro in final:
                                table.insert('', i, text='', values=(ro[0], ro[1], ro[2]))
                                i = i + 1

                        # -----------------------------------------------------------------------------------------------

                        query = 'select Time,Flag from activity where Date=%s and ID=%s'
                        data = (current_date_display, search_entry)
                        cur.execute(query, data)
                        result = cur.fetchall()
                        result = result[0]
                        flag = result[1]
                        result1 = result[-8:]

                        if (result != None):
                            result = result[0]
                            result = result[1:len(result)]
                            result = result.split(',')
                            list2 = []
                            for i in range(len(result)):
                                list2.append(result[i])

                        if not result:
                            messagebox.showinfo('message', "No record found")
                        else:
                            listt = []
                            if len(list2) % 2 == 0:
                                listt = list2
                            else:
                                listt = list2
                                listt.append(None)

                            i = 0
                            for x in range(0, len(listt) - 1, 2):
                                if (flag == 'out'):
                                    table2.insert('', i, text='', values=(list2[x + 1], list2[x]))

                                else:
                                    table2.insert('', i, text='', values=(list2[x], list2[x + 1]))
                                i = i + 1

                        # -------------------------------------------------------------------------------------------------

                    # ------------------------------------------------------------   6  ---------------------------------------
                    elif (query == 'view all records of a particular date'):
                        query = "select ID,Name,Flag ,Date,Time,Flag2,Type, hostel from activity where Date=%s"
                        data = (current_date_display,)
                        cur.execute(query, data)
                        final = cur.fetchall()
                        frame4 = LabelFrame(view, bg="white")
                        table = Treeview(frame4,
                                         columns=(
                                             'ID', 'Name', 'Ist-Activity', 'Date', 'Time', 'last-Activity', 'Type',
                                             'Hostel'))
                        table.column('ID', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('Name', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('Ist-Activity', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('Date', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('Time', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('last-Activity', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('Type', width=220, minwidth=220, anchor=tkinter.CENTER)
                        table.column('Hostel', width=220, minwidth=220, anchor=tkinter.CENTER)

                        table.heading('Type', text='Type', anchor=tkinter.CENTER)
                        table.heading('Name', text='Name', anchor=tkinter.CENTER)
                        table.heading('ID', text='ID', anchor=tkinter.CENTER)
                        table.heading('Date', text='Date', anchor=tkinter.CENTER)
                        table.heading('Hostel', text='Hostel', anchor=tkinter.CENTER)
                        table.heading('Ist-Activity', text='Ist-Activity', anchor=tkinter.CENTER)
                        table.heading('last-Activity', text='Last-Activity', anchor=tkinter.CENTER)
                        table.heading('Time', text='Time', anchor=tkinter.CENTER)
                        table['show'] = 'headings'
                        s = ttk.Style(frame4)
                        s.theme_use('clam')
                        s.configure('Treeview.Heading', font=("times new roman", 15, 'bold'), foreground='red',
                                    backgound='blue')
                        s.configure('Treeview', font=("chiller", 12, 'bold'), foreground='red')
                        xs = ttk.Scrollbar(frame4, orient='horizontal')
                        xs.configure(command=table.xview)
                        ys = ttk.Scrollbar(frame4, orient='vertical')
                        ys.configure(command=table.yview)
                        table.configure(xscrollcommand=xs.set, yscrollcommand=ys.set)
                        xs.pack(side=BOTTOM, fill=X)
                        ys.pack(side=RIGHT, fill=Y)
                        frame4.place(x=200, y=200, width=1100, height=450)
                        table.pack(fill=BOTH, expand=1)
                        if not final:
                            messagebox.showinfo('message', "No record found")
                        else:
                            i = 0
                            for ro in final:
                                table.insert('', i, text='',
                                             values=(ro[0], ro[1], ro[2], ro[3], ro[4], ro[5], ro[6], ro[7]))
                                i = i + 1
                    # ------------------------------------------------------------   7  ---------------------------------------
                    elif (query == 'view record of a person of a particular month'):
                        query = "select ID,Name,Flag ,Date,Time,Flag2,Type, hostel from activity where month(Date)=%s and year(date)=%s and ID=%s"
                        data = (month, year, search_entry)
                        cur.execute(query, data)
                        final = cur.fetchall()
                        tree_query6_7()

                # --------------------------------------------- search button --------------------------------------------------
                search = Button(view, text="Search", fg="WHITE", bg="blue", font=("times new roman", 12, 'bold'),
                                command=display)
                search.config(width=10, height=5, highlightbackground="#cccccc", highlightthickness=2)
                search.place(x=1100, y=140, height="25")

                # --------------------------------------------- clear button --------------------------------------------------
                clear = Button(view, text="Clear", fg="WHITE", bg="blue", font=("times new roman", 12, 'bold'),
                               command=clear)
                clear.config(width=10, height=5, highlightbackground="#cccccc", highlightthickness=2)
                clear.place(x=1240, y=140, height="25")

                #--------------------------------------- function for home button --------------------------------------

                def home():
                    view.withdraw()
                    login1.deiconify()

                    if opened_home == True:
                        pass


                # --------------------------------------------- home button --------------------------------------------------
                Home_button = Button(view, text="Home", command=home,font=("times new roman", 10, 'bold'), fg="WHITE", bg="gray")
                Home_button.config(width=20, height=4, highlightbackground="#cccccc", highlightthickness=2)
                Home_button.place(x=0, y=180)
                opened_home =False

                # --------------------------------------------- manage student button --------------------------------------------------
                manages_button = Button(view, text="Manage\nStudent Record", font=("times new roman", 10, 'bold'),
                                        fg="WHITE",
                                        bg="gray", command=manage_student)
                manages_button.config(width=20, height=4, highlightbackground="#cccccc", highlightthickness=2)
                manages_button.place(x=0, y=253)

                # --------------------------------------------- manage academic/management button --------------------------------------------------
                managem_button = Button(view, text="Manage\nAcademic/Management\nRecord",
                                        font=("times new roman", 10, 'bold'),
                                        fg="WHITE", bg="gray", command=manage_academic_management)
                managem_button.config(width=20, height=4, highlightbackground="#cccccc", highlightthickness=2)
                managem_button.place(x=0, y=326)

                def another_admin():
                    registration = Toplevel()
                    registration.title('QR EnExRe')
                    registration.geometry("1350x700+0+0")
                    registration.resizable(0, 0)
                    registration.config(bg="#ffbf80")
                    # ---------------------------------- cofee image  ---------------------------------------------------
                    img1 = ImageTk.PhotoImage(Image.open('F:\\New Volume\\PycharmProjects\\imagess\\add_another.jpg'))
                    my1 = Label(registration, image=img1)
                    my1.place(x=110, y=90)

                    # ---------------------------------- frame for registration -------------------------------------------------

                    frame_r = Frame(registration, bg="black")
                    frame_r.place(x=710, y=90, width=530, height=500)

                    title = Label(registration, text="REGISTER HERE", font=("times new roman", 25, "bold"), bg="black",
                                  fg="white").place(x=740, y=95)

                    name_l = Label(registration, text="Name", font=("times new roman", 15), bg="black",
                                   fg="white").place(x=740,
                                                     y=150)
                    name_var_r = StringVar()
                    name_var_r_entrybox = Entry(registration, width=45, font=("times new roman", 12),
                                                textvariable=name_var_r,
                                                bg="white")
                    name_var_r_entrybox.place(x=740, y=180, height="25")
                    name_var_r_entrybox.focus()

                    email_l = Label(registration, text="E-mail", font=("times new roman", 15), bg="black",
                                    fg="white").place(
                        x=740,
                        y=225)
                    email_var_r = StringVar()
                    email_var_r_entrybox = Entry(registration, width=45, font=("times new roman", 12),
                                                 textvariable=email_var_r,
                                                 bg="white")
                    email_var_r_entrybox.place(x=740, y=255, height="25")

                    password_l = Label(registration, text="Password", font=("times new roman", 15), bg="black",
                                       fg="white").place(
                        x=740,
                        y=305)
                    password_var_r = StringVar()
                    password_var_r_entrybox = Entry(registration, width=45, font=("times new roman", 12),
                                                    textvariable=password_var_r,
                                                    bg="white")
                    password_var_r_entrybox.place(x=740, y=335, height="25")

                    security_l = Label(registration, text="Security Question", font=("times new roman", 15), bg="black",
                                       fg="white").place(x=740, y=385)
                    security_var = StringVar()
                    security_combobox = ttk.Combobox(registration, width=57, textvariable=security_var,
                                                     state='readonly')
                    security_combobox['values'] = (
                        'select', 'Your pet name', 'Your birth place', 'your nick name', 'your favourite color')
                    security_combobox.current(0)
                    security_combobox.place(x=740, y=415, height="25")

                    answer_l = Label(registration, text="Answer", font=("times new roman", 15), bg="black",
                                     fg="white").place(
                        x=740,
                        y=465)
                    answer_var_r = StringVar()
                    answer_var_r_entrybox = Entry(registration, width=45, font=("times new roman", 12),
                                                  textvariable=answer_var_r,
                                                  bg="white")
                    answer_var_r_entrybox.place(x=740, y=495, height="25")

                    def register():
                        global cur, conn
                        name = name_var_r.get()
                        emaail = email_var_r.get()
                        password = password_var_r.get()
                        question = security_var.get()
                        answer = answer_var_r.get()

                        if (name == '' or emaail == '' or password == '' or question == '' or answer == ''):
                            messagebox.showerror('error', 'all fields are required', parent=registration)
                            return
                        else:
                            try:
                                query = "create table if not exists admin(name varchar(30) not null, email varchar(40) not null primary key,password varchar(20) not null, security_question varchar(100) not null,answer varchar(20) not null)"
                                cur.execute(query)
                                str1 = 'insert into admin values(%s,%s,%s,%s,%s)'
                                data = (name, emaail, password, question, answer)
                                cur.execute(str1, data)
                                conn.commit()
                            except mysql.connector.IntegrityError as err:
                                messagebox.showerror("error", err, parent=registration)
                                return
                            else:
                                messagebox.showinfo('notification', 'registered successfully', parent=registration)

                    proceed = Button(registration, text='Proceed Here', font=("times new roman", 15, "bold"),
                                     bg="#ffbf80",
                                     command=register)
                    proceed.place(x=740, y=538, height=26)

                    registration.mainloop()

                # -------------------------------------------- add another admin button -----------------------------------------
                addm_button = Button(view, text="Add Another\nAdmin", font=("times new roman", 10, 'bold'), fg="WHITE",
                                     bg="gray",
                                     command=another_admin)
                addm_button.config(width=20, height=4, highlightbackground="#cccccc", highlightthickness=2)
                addm_button.place(x=0, y=399)

                # ------------------------------------------- function for change password -----------------------------------
                def change():
                    global cur, conn
                    frame4 = LabelFrame(view, bg="white")
                    frame4.place(x=200, y=200, width=1100, height=480)

                    changep = Label(frame4, bg='#ff6600', text='Change Password', font=("times new roman", 25, 'bold'),
                                    fg='white')
                    changep.place(x=0, y=0, relwidth=1, height=50)
                    # -------------------------------------------- name label and entry box ------------------------------------
                    name_l = Label(frame4, text="Name", font=("times new roman", 20, 'bold'), bg="white",
                                   fg="black").place(
                        x=50, y=70)
                    name_var_r = StringVar()
                    name_var_r_entrybox = Entry(frame4, width=40, font=("times new roman", 15), textvariable=name_var_r,
                                                bg="white")
                    name_var_r_entrybox.place(x=50, y=120, height="35")
                    name_var_r_entrybox.focus()

                    # ----------------------------------- old password label and entry box --------------------------------------
                    password_o = Label(frame4, text="Old Password", font=("times new roman", 20, 'bold'), bg="white",
                                       fg="black").place(
                        x=50, y=190)
                    password_var_o = StringVar()
                    password_var_o_entrybox = Entry(frame4, width=40, font=("times new roman", 15),
                                                    textvariable=password_var_o,
                                                    bg="white")
                    password_var_o_entrybox.place(x=50, y=240, height="35")

                    # ------------------------------- security question label -------------------------------------------
                    security_l = Label(frame4, text="Security Question", font=("times new roman", 20, 'bold'),
                                       bg="white",
                                       fg="black").place(x=50, y=310)
                    security_var = StringVar()
                    security_combobox = ttk.Combobox(frame4, width=65, textvariable=security_var, state='readonly')
                    security_combobox['values'] = (
                        'select', 'Your pet name', 'Your birth place', 'your nick name', 'your favourite color')
                    security_combobox.current(0)
                    security_combobox.place(x=50, y=360, height="35")

                    # -------------------------------------- email label and entry box --------------------------------------
                    email_l = Label(frame4, text="E-mail", font=("times new roman", 20, 'bold'), bg="white",
                                    fg="black").place(
                        x=640, y=70)
                    email_var_r = StringVar()
                    email_var_r_entrybox = Entry(frame4, width=40, font=("times new roman", 15),
                                                 textvariable=email_var_r,
                                                 bg="white")
                    email_var_r_entrybox.place(x=640, y=120, height="35")

                    # ------------------------------ new password label and entry box -----------------------------------------
                    password_n = Label(frame4, text="New Password", font=("times new roman", 20, 'bold'), bg="white",
                                       fg="black").place(
                        x=640, y=190)
                    password_var_n = StringVar()
                    password_var_n_entrybox = Entry(frame4, width=40, font=("times new roman", 15),
                                                    textvariable=password_var_n,
                                                    bg="white")
                    password_var_n_entrybox.place(x=640, y=240, height="35")

                    # -------------------------- answer label -----------------------------------------------------------
                    answer_l = Label(frame4, text="Answer", font=("times new roman", 20, 'bold'), bg="white",
                                     fg="black").place(
                        x=640, y=310)
                    answer_var_r = StringVar()
                    answer_var_r_entrybox = Entry(frame4, width=40, font=("times new roman", 15),
                                                  textvariable=answer_var_r,
                                                  bg="white")
                    answer_var_r_entrybox.place(x=640, y=360, height="35")

                    def submit_f():
                        name = name_var_r.get()
                        password_o = password_var_o.get()
                        security = security_var.get()
                        email = email_var_r.get()
                        password_n = password_var_n.get()
                        answer = answer_var_r.get()

                        query = "select password,security_question, answer from admin where email=%s"
                        data = (email,)
                        cur.execute(query, data)
                        result = cur.fetchone()
                        print(result[0])
                        if (result[0] == password_o and result[1] == security and result[2] == answer):
                            try:
                                query = 'update admin set password=%s where email=%s'
                                data = (password_n, email)
                                cur.execute(query, data)
                                conn.commit()
                            except:
                                messagebox.showerror('error', 'your password is not updated, please try again')
                            else:
                                messagebox.showinfo('notification', 'your password is updated successfully')
                                name_var_r_entrybox.delete(0, END)
                                password_var_o_entrybox.delete(0, END)
                                security_combobox.set('')
                                email_var_r_entrybox.delete(0, END)
                                password_var_n_entrybox.delete(0, END)
                                answer_var_r_entrybox.delete(0, END)

                        elif (password_o != result[0]):
                            messagebox.showerror('error', 'your old password does not match')
                        elif (result[1] != security):
                            messagebox.showerror('error', 'your security question does not match')
                        else:
                            messagebox.showerror('error', 'your answer does not match')

                    # ----------------------------- submit button --------------------------------------------------------
                    submit = Button(frame4, text="Submit", font=('times new roman', 20, 'bold'), width=10,
                                    bg="#ff6600", fg="white", command=submit_f).place(x=300, y=420, height="40")

                    # ----------------------------- exit button --------------------------------------------------------
                    exit = Button(frame4, text="Exit", font=('times new roman', 20, 'bold'), width=10,
                                  bg="#ff6600", fg="white", command=frame4.destroy).place(x=600, y=420, height="40")

                # ------------------------------------------ change password -------------------------------------------------
                changeb_button = Button(view, text="Change\nPassword", font=("times new roman", 10, 'bold'), fg="WHITE",
                                        bg="gray",
                                        command=change)
                changeb_button.config(width=20, height=4, highlightbackground="#cccccc", highlightthickness=2)
                changeb_button.place(x=0, y=472)

                # ----------------------------------------- export button ------------------------------------------------------
                export_button = Button(view, text="Export\nRecord", font=("times new roman", 10, 'bold'), fg="WHITE",
                                       bg="gray")
                export_button.config(width=20, height=4, highlightbackground="#cccccc", highlightthickness=2)
                export_button.place(x=0, y=545)


                #-------------------------------------- function for logout ---------------------------

                def logout_admin():
                    global opened_log_admin
                    view.withdraw()
                    login_for_admin.deiconify()

                    if opened_log_admin == True:
                        pass


                # --------------------------------------------- logout button --------------------------------------------------
                logout_button = Button(view, text="Log Out",command=logout_admin, font=("times new roman", 10, 'bold'), fg="WHITE",
                                       bg="gray")
                logout_button.config(width=20, height=4, highlightbackground="#cccccc", highlightthickness=2)
                logout_button.place(x=0, y=618)
                opened_log_admin = False
                view.mainloop()


        if(opened==True):
            login1.deiconify()
        else:

            login_for_admin = Toplevel()
            login_for_admin.title('Login For Admin')
            login_for_admin.geometry('1350x700+0+0')
            login_for_admin.resizable(0, 0)
            # login_for_admin.config(bg="#346AFE")

            img_la = ImageTk.PhotoImage(Image.open("F:\\New Volume\\PycharmProjects\\imagess\\backgound.jpg"))
            my = Label(login_for_admin,image=img_la)
            my.pack()

            # ---------------------------------------  login frame  -----------------------------------------------
            login_frame = Frame(login_for_admin, bd=0, bg="white").place(x=325, y=100, width=700, height=450)

            img_a = ImageTk.PhotoImage(Image.open('F:\\New Volume\\PycharmProjects\\imagess\\resizeimag1.jpg'))
            my_a = Label(login_for_admin, image=img_a)
            my_a.place(x=330, y=120)

            title = Label(login_for_admin, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white",
                          fg="#031F3C").place(x=620, y=120)

            Email = Label(login_for_admin, text="EMAIL ADDRESS", font=("times new roman", 18, "bold"), bg="white",
                          fg="gray").place(x=620, y=190)
            txt_email = Entry(login_for_admin, font=("times new roman", 20), bg="lightgray", width='25')
            txt_email.place(x=625, y=230, height="40")

            pas = Label(login_for_admin, text="PASSWORD", font=("times new roman", 18, "bold"), bg="white",
                        fg="gray").place(
                x=620, y=300)
            txt_pas = Entry(login_for_admin, font=("times new roman", 20), show='*', bg="lightgray", width='25')
            txt_pas.place(x=625, y=340, height="40")

            # ---------------------------------------  button for forgot password  --------------------------------------------------
            btn_forgot_pass = Button(login_for_admin, text="Forgot Password?", font=("times new roman", 20), bd=0,
                                     fg="#B00857",
                                     bg="white", cursor="hand2").place(x=615, y=410)

            # ---------------------------------------  button for forgot password  --------------------------------------------------
            btn_sign_up = Button(login_for_admin, text="Sign Up?", font=("times new roman", 20), bd=0, fg="#B00857",
                                 bg="white",
                                 cursor="hand2").place(x=870, y=410)

            def login():
                global cur, conn
                email = txt_email.get()
                passw = txt_pas.get()
                query = 'select email,password from admin where email=%s'
                data = (email,)
                cur.execute(query, data)
                result = cur.fetchall()
                if not result:
                    messagebox.showerror('error', "No record found!!\nplease signup")
                else:
                    for (username, passwords) in result:
                        if passw == passwords and email == username:
                            txt_email.delete(0, END)
                            admin()
                        else:
                            messagebox.showerror('error', 'password is wrong')

            login = Button(login_for_admin, text="Login", command=login, font=('times new roman', 20, 'bold'), width=10,
                           bg="#C21460", fg="white").place(x=625, y=480, height="40")
            opened_ll = False
            login_for_admin.mainloop()

    # -------------------------  end of admin function  ------------------------------------------


    #--------------------------------  remaining part of dashboard function  --------------------------------------
    if opened2 == True:
        window.deiconify()

    else:
        login1 = Toplevel()
        login1.title('QR EnExRe')
        login1.geometry('1350x700+0+0')
        login1.resizable(0, 0)
        login1.config(bg="white")

        img = ImageTk.PhotoImage(Image.open("F:\\New Volume\\PycharmProjects\\imagess\\image_12100.jpg"))
        my = Label(login1,image=img)
        my.place(x=0,y=130)

        # -------------------------------------------------------------------------function for slider-----------
        def sliders():
            global count, text
            if (count >= len(string)):
                count = 0
                text = ''
                sliderlabel.config(text=text)

            else:
                text = text + string[count]
                count = count + 1
                sliderlabel.config(text=text)
            sliderlabel.after(200, sliders)

        # -----------------------------------------------------  slider  ------------------------------------
        count = 0
        text = ''
        string = "WELCOME TO QR EnExRe"
        sliderlabel = Label(login1, text=string, relief=GROOVE, borderwidth=5,
                            font=("goudy old style", 20, 'bold'), bg="#02231C", fg="white", bd=0)
        sliderlabel.place(x=0, y=5, relwidth=1, height=50)
        sliders()

        # --------------------------------------- lable frame  ------------------------------------------------------
        desh_label = Label(login1, text='DASHBOARD', relief=GROOVE, borderwidth=5,
                           font=("goudy old style", 20, 'bold'), bg="#55D9C0", fg="#02231C", bd=0)
        desh_label.place(x=0, y=55, relwidth=1, height=50)


        # ---------------------------------------  button for qrcode scanner -------------------------------------------
        imgq = ImageTk.PhotoImage(Image.open("F:\\New Volume\\PycharmProjects\\imagess\\qrc1.jpg"))
        my = Label(login1,image=imgq)
        my.place(x=775, y=130)
        qr = Button(login1, text="scan here", command=scanner,font=('times new roman', 20, 'bold'), width=11, bg="#C21460",
                    fg="white").place(x=780, y=312, height="40")

        # ---------------------------------------   BUTTON FOR ADMIN   ---------------------------------------
        imga = ImageTk.PhotoImage(Image.open("F:\\New Volume\\PycharmProjects\\imagess\\adminc.jpg"))
        my3 = Label(login1,image=imga)
        my3.place(x=1050, y=130)

        admin = Button(login1, text="Admin", font=('times new roman', 20, 'bold'), width=11, bg="#C21460",
                       fg="white",command=login_for_adminn).place(x=1050, y=312, height="40")
        opened = False

        # ---------------------------------------  BUTTON FOR exit  -------------------------------------

        img3 = ImageTk.PhotoImage(Image.open("F:\\New Volume\\PycharmProjects\\imagess\\exitc.png"))
        my3 = Label(login1,image=img3)
        my3.place(x=1050, y=420)

        exitb = Button(login1, text="Exit",command=exit ,font=('times new roman', 20, 'bold'), width=11, bg="#C21460",
                      fg="white").place(x=1050, y=600, height="40")

        # ---------------------------------------  button for log out  ----------------------------------------------

        img2 = ImageTk.PhotoImage(Image.open("F:\\New Volume\\PycharmProjects\\imagess\\logc.jpg"))
        my2 = Label(login1,image=img2)
        my2.place(x=775, y=420)

        logoutb = Button(login1, text="log out", command=logout,font=('times new roman', 20, 'bold'), width=11, bg="#C21460",fg="white").place(x=775, y=600, height="40")
        opened_logout=False
        login1.mainloop()
#__________________________________________ end of deshboard function  _________________________________________
#_________________________________  function for login  user __________________________________________________________
def login():
        user = user_var.get()
        pass1 = password_var.get()
        cur = conn.cursor()
        query = "select email,password from login where email=%s"
        data=(user,)
        cur.execute(query,data)
        result=cur.fetchall()
        if not result:
            messagebox.showerror('error', "No record found!!\nplease signup")
        else:
            for (username, passwords) in result:
                if pass1 == passwords and user == username:
                    user_entrybox.delete(0, END)
                    # pass_entrybox.delete(0,END)
                    deshboard()
                else:
                    message()

login = Button(frame,text="Login",command=login,font=('times', 20, 'bold'),width=10,bg="#B00857",fg="white",cursor="hand2").place(x=80,y=400,height="40")
opened2=False

window.mainloop()
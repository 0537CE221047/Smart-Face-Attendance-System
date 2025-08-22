
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector 
from tkinter import messagebox
import cv2




class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACEATTENDANCEPROJECT")


          # *****************left label frame*********************
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        self.var_photo_sample = StringVar()




        self.photoimg0 = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Working.jpeg").resize((500, 130), Image.LANCZOS))
        self.photoimg1 = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Student Class.jpeg").resize((500, 130), Image.LANCZOS))
        self.photoimg2 = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Student Photo.jpeg").resize((500, 130), Image.LANCZOS))


        Label(self.root, image=self.photoimg0).place(x=0, y=0, width=500, height=130)
        Label(self.root, image=self.photoimg1).place(x=500, y=0, width=500, height=130)
        Label(self.root, image=self.photoimg2).place(x=1000, y=0, width=500, height=130)

        self.photoimg3 = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\BG Photo.avif").resize((1530, 660), Image.LANCZOS))
        self.bg_img = Label(self.root, image=self.photoimg3)
        self.bg_img.place(x=0, y=130, width=1530, height=660)


        title_lbl = Label(self.bg_img, text="STUDENT MANAGEMENT SYSTEM", 
                          font=("times new roman", 35, "bold"), bg="darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame=Frame(self.bg_img,bd=2)
        main_frame.place(x=10 , y=55 , width=1505 , height=585)


          # left label frame

        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)


        self.photoimg_left = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Classroom.jpg").resize((720, 130), Image.LANCZOS))

        Label(Left_frame, image=self.photoimg_left).place(x=10, y=0, width=745, height=130)


         # current course
        Current_Course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        Current_Course_frame.place(x=5,y=135,width=750,height=100)

          # Department (row=0, col=0)
        dep_label = Label(Current_Course_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        dep_combo = ttk.Combobox(Current_Course_frame, textvariable=self.var_dep,font=("times new roman", 12, "bold"), width=18, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science", "AIML", "Electronics & Comm", "Civil", "Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)

          # Course (row=0, col=2)
        course_label = Label(Current_Course_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        course_combo = ttk.Combobox(Current_Course_frame,textvariable=self.var_course, font=("times new roman", 12, "bold"), width=18, state="readonly")
        course_combo["values"] = ("Select Course", "B.Tech", "M.Tech", "B.Sc", "M.Sc", "PhD")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx=10, pady=5, sticky=W)

          # Year (row=1, col=0)
        year_label = Label(Current_Course_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        year_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        year_combo = ttk.Combobox(Current_Course_frame,textvariable=self.var_year, font=("times new roman", 12, "bold"), width=18, state="readonly")
        year_combo["values"] = ("2025-26", "2026-27", "2027-28", "2028-29", "2029-30")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)

         # Semester (row=1, col=2)
        sem_label = Label(Current_Course_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        sem_combo = ttk.Combobox(Current_Course_frame,textvariable=self.var_semester, font=("times new roman", 12, "bold"), width=18, state="readonly")
        sem_combo["values"] = ("Select Semester", "Semester 1", "Semester 2", "Semester 3", "Semester 4","Semester 5", "Semester 6", "Semester 7", "Semester 8")
        sem_combo.current(0)
        sem_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)


          # Class Student Information
        Class_Student_frame = LabelFrame(Left_frame, bd=2, bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        Class_Student_frame.place(x=5, y=250, width=720, height=300)

          # Student ID
        student_id_label = Label(Class_Student_frame, text="Student ID", font=("times new roman", 12, "bold"), bg="white")
        student_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        student_id_entry = Entry(Class_Student_frame,textvariable=self.var_std_id ,font=("times new roman", 12, "bold"), width=20, bg="lightyellow")
        student_id_entry.grid(row=0, column=1, padx=10, pady=5, sticky=W)


          # Student Name
        student_name_label = Label(Class_Student_frame, text="Student Name", font=("times new roman", 12, "bold"), bg="white")
        student_name_label.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        student_name_entry = Entry(Class_Student_frame,textvariable=self.var_std_name, font=("times new roman", 12, "bold"), width=20, bg="lightyellow")
        student_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)


         # Class Division 
        class_div_label = Label(Class_Student_frame, text="Class Division", font=("times new roman", 12, "bold"), bg="white")
        class_div_label.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        class_div_combo = ttk.Combobox(Class_Student_frame,textvariable=self.var_div, values=("Select Division", "A", "B", "C", "D"), font=("times new roman", 12, "bold"), width=18, state="readonly")
        class_div_combo.current(0)
        class_div_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)


          # Roll Number 
        roll_no_label = Label(Class_Student_frame, text="Roll Number", font=("times new roman", 12, "bold"), bg="white")
        roll_no_label.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        roll_no_entry = Entry(Class_Student_frame,textvariable=self.var_roll, font=("times new roman", 12, "bold"), width=20, bg="lightyellow")
        roll_no_entry.grid(row=3, column=1, padx=10, pady=5, sticky=W)


         # Email 
        email_label = Label(Class_Student_frame, text="Email", font=("times new roman", 12, "bold"), bg="white")
        email_label.grid(row=4, column=0, padx=10, pady=5, sticky=W)

        email_entry = Entry(Class_Student_frame,textvariable=self.var_email, font=("times new roman", 12, "bold"), width=20, bg="lightyellow")
        email_entry.grid(row=4, column=1, padx=10, pady=5, sticky=W)


       
          # Address
        address_label = Label(Class_Student_frame, text="Address", font=("times new roman", 12, "bold"), bg="white")
        address_label.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        address_entry = Entry(Class_Student_frame,textvariable=self.var_address, font=("times new roman", 12, "bold"), width=20, bg="lightyellow")
        address_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Gender
        gender_label = Label(Class_Student_frame, text="Gender", font=("times new roman", 12, "bold"), bg="white")
        gender_label.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        gender_combo = ttk.Combobox(Class_Student_frame,textvariable=self.var_gender, font=("times new roman", 12, "bold"), width=18, state="readonly")
        gender_combo["values"] = ("Select Gender", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # DOB
        dob_label = Label(Class_Student_frame, text="DOB", font=("times new roman", 12, "bold"), bg="white")
        dob_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        dob_entry = Entry(Class_Student_frame,textvariable=self.var_dob, font=("times new roman", 12, "bold"), width=20, bg="lightyellow")
        dob_entry.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Phone Number
        phone_label = Label(Class_Student_frame, text="Phone Number", font=("times new roman", 12, "bold"), bg="white")
        phone_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        phone_entry = Entry(Class_Student_frame,textvariable=self.var_phone, font=("times new roman", 12, "bold"), width=20, bg="lightyellow")
        phone_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

         # Teacher Name
        teacher_label = Label(Class_Student_frame, text="Teacher Name", font=("times new roman", 12, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)
        teacher_entry = Entry(Class_Student_frame,textvariable=self.var_teacher, font=("times new roman", 12, "bold"), width=20, bg="lightyellow")
        teacher_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)


         # Radio buttons
        self.var_radio1=StringVar()
        Radiobutton1=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        Radiobutton1.grid(row=6,column=0)

        
        Radiobutton2=ttk.Radiobutton(Class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        Radiobutton2.grid(row=6,column=1)

         #  buttons frame 
        btn_frame=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=716,height=70)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="Darkgreen",fg="white")
        save_btn.grid(row=0,column=0)


        update_btn=Button(btn_frame,text="update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="Darkgreen",fg="white")
        update_btn.grid(row=0,column=1)


        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="Darkgreen",fg="white")
        Delete_btn.grid(row=0,column=2)


        reset_btn=Button(btn_frame,text="reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="Darkgreen",fg="white")
        reset_btn.grid(row=0,column=3)

        btn_frame1=Frame(Class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="Darkgreen",fg="white")
        take_photo_btn.grid(row=0,column=1)

        update_photo_btn=Button(btn_frame1,text="update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="Darkgreen",fg="white")
        update_photo_btn.grid(row=0,column=2)


        
         #  Right label frame 
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=800,y=10,width=690,height=580)


        self.photoimg_Right = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\students in classroom.jpg").resize((720, 130), Image.LANCZOS))

        Label(Right_frame, image=self.photoimg_Right).place(x=10, y=0, width=745, height=130)


        Search_frame = LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        Search_frame.place(x=5, y=135, width=680, height=70)


        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="white", fg="white")

        search_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        search_entry = Entry(Search_frame, font=("times new roman", 12, "bold"), width=20, bg="lightyellow")
        search_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)


         # Label for "Search By:"
        search_label = Label(Search_frame, text="Search By:", font=("times new roman", 12, "bold"), bg="Darkgreen",fg="white")
        search_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

         # Combobox for selecting search option
        search_combo = ttk.Combobox(Search_frame, font=("times new roman", 12, "bold"), width=15, state="readonly")
        search_combo["values"] = ("Select", "Roll no.", "Phone number")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=10, sticky=W)


       
        search_entry = ttk.Entry(Search_frame,width=15, font=("times new roman",13,"bold"))  # width=2 for spacing
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky="w")


        search_btn=Button(Search_frame,text="Search",width=13,font=("times new roman",13, "bold"),
                    bg="darkgreen", fg="white")
        search_btn.grid(row=0, column=3,padx=(5,0),pady=10,sticky="w")


        showAll_btn = Button(Search_frame, text="Show All", width=8, font=("times new roman", 13, "bold"),
                     bg="darkgreen", fg="white")
        showAll_btn.grid(row=0, column=4,padx=4,pady=5,sticky="w")


           # ==== Table Frame ====
        table_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5, y=210, width=700, height=340)

          # ==== Scrollbars ====
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

         # ==== Treeview ====
        self.student_table = ttk.Treeview(
        table_frame,
        columns=("dep", "course", "year", "sem", "id", "name","div","roll","gender","dob","email","phone","teacher","photo","address"),
        xscrollcommand=scroll_x.set,
        yscrollcommand=scroll_y.set
         )

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.student_table.pack(fill=BOTH, expand=1)

        # ==== Headings ====
        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("roll", text="Roll No.")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")       
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table.heading("address", text="Address")
       
        self.student_table["show"] = "headings"


        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("teacher", width=150)
        self.student_table.column("photo", width=150)
        self.student_table.column("address", width=100)
        
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


         # ================ function declaration ===================
    def add_data(self):
         if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "":
           messagebox.showerror("Error", "All fields are required", parent=self.root)
         else : 
           try:
              conn = mysql.connector.connect(
                             host="localhost",
                               user="root",
                                 password="root",
                                   database="face_recognizer")
                       
                                                                     
              self.my_cursor = conn.cursor()
              self.my_cursor.execute("""
                   INSERT INTO student(
                       `Dep`,`Course`,`Year`,`semester`,`Std_Id`,`Std_name`,`Div`,`Roll No.`,`Gender`,`DOB`,`Email`,`phone`,`Teacher`,`PhotoSample`,`Address`
                    ) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)""", (
            self.var_dep.get(),
            self.var_course.get(),
            self.var_year.get(),
            self.var_semester.get(),
            self.var_std_id.get(),
            self.var_std_name.get(),
            self.var_div.get(),
            self.var_roll.get(),
            self.var_gender.get(),
            self.var_dob.get(),
            self.var_email.get(),
            self.var_phone.get(),
            self.var_teacher.get(),
            self.var_photo_sample.get(),
            self.var_address.get()
            

             
        ))

              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("Success", "Student data has been added successfully", parent=self.root)

           except Exception as e:
            messagebox.showerror("Database Error", f"Due to: {str(e)}", parent=self.root)


            # ================ fetch data  ===================
    def fetch_data(self):
     conn = mysql.connector.connect( host="localhost", user="root",password="root", database="face_recognizer")
     self.my_cursor = conn.cursor()
     self.my_cursor.execute("select * from student")
     data=self.my_cursor.fetchall()

     if len(data)!=0:
        self.student_table.delete(*self.student_table.get_children())
        for i in data:
            self.student_table.insert("",END,values=i)
        conn.commit()
     conn.close() 



    
    
                      
     # ================ update data get cursor ===================   
    
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]


        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_teacher.set(data[12]),
        self.var_address.set(data[13]),
        self.var_radio1.set(data[14]),


# ================ update function ===================

    def update_data(self):
     if self.var_dep.get() == "Select Department" or self.var_std_id.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
     else:
        try:
            update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent=self.root)
            if update > 0:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="root", database="face_recognizer"
                )
                self.my_cursor = conn.cursor()

                self.my_cursor.execute("""
                    UPDATE student SET 
                       `Dep`=%s, 
                        `Course`=%s, 
                        `Year`=%s, 
                        `semester`=%s, 
                        `Std_name`=%s, 
                        `Div`=%s, 
                        `Roll No.`=%s, 
                        `Gender`=%s, 
                        `DOB`=%s, 
                        `Email`=%s, 
                        `phone`=%s, 
                        `Teacher`=%s, 
                        `PhotoSample`=%s, 
                        `Address`=%s 
                    WHERE `Std_Id`=%s
                """, (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),           # 'Roll No.' column ka actual value
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_address.get(),
                    self.var_std_id.get()
                ))

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
            else:
                  return
        except Exception as e:
            messagebox.showerror("Error",f"Due to:{str(e)}",parent=self.root)


# Delete Function==================

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student ID must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delete this student?", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                         host="localhost",
                         user="root",
                         password="root",
                         database="face_recognizer"
                )
                    my_cursor = conn.cursor()
                    query = "DELETE FROM student WHERE Std_Id=%s"
                    value = (self.var_std_id.get(),)
                    my_cursor.execute(query, value)
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Delete", "Successfully deleted student record", parent=self.root)
                    self.fetch_data()  # refresh the table after deletion
                else:
                    return
            except Exception as es:
                  messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)



 # reset Button===================

    def reset_data(self):
      self.var_dep.set("Select Department")
      self.var_course.set("Select Course")
      self.var_year.set("Select Year")
      self.var_semester.set("Select Semester")
      self.var_std_id.set("")
      self.var_std_name.set("")
      self.var_div.set("Select Division")
      self.var_roll.set("")
      self.var_gender.set("Select Gender")
      self.var_dob.set("")
      self.var_email.set("")
      self.var_phone.set("")
      self.var_address.set("")
      self.var_teacher.set("")
      self.var_photo_sample.set("No")    # based on yes or no


      # Generating Data Set and Take photo samples=================
    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        try:
           conn = mysql.connector.connect(
               host="localhost", 
               user="root", 
               password="root", 
               database="face_recognizer"
            )
           my_cursor = conn.cursor()

        # Directly update this student's data
           query = """
           UPDATE student SET
               `Dep`=%s, `course`=%s, `Year`=%s, `Semester`=%s, `Std_Id`=%s, `Std_name`=%s, 
               `Div`=%s, `Roll No.`=%s, `Gender`=%s, `DOB`=%s, `Email`=%s, `Phone`=%s,
               `Address`=%s, `Teacher`=%s, `PhotoSample`=%s
           WHERE Std_Id=%s
           """

           values = (
               self.var_dep.get(),
               self.var_course.get(),
               self.var_year.get(),
               self.var_semester.get(),
               self.var_std_id.get(),
               self.var_std_name.get(),
               self.var_div.get(),
               self.var_roll.get(),
               self.var_gender.get(),
               self.var_dob.get(),
               self.var_email.get(),
               self.var_phone.get(),
               self.var_address.get(),
               self.var_teacher.get(),
               self.var_photo_sample.get(),
               self.var_std_id.get()
           )

           my_cursor.execute(query, values)
           conn.commit()
           self.fetch_data()
           conn.close()

        # ================== Load predefined data on frontalface from OpenCV ==================
           face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

           def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    return img[y:y+h, x:x+w]
                return None

           cap = cv2.VideoCapture(0)
           img_id = 0
           while True:
               ret, my_frame = cap.read()
               if face_cropped(my_frame) is not None:
                   img_id += 1
                   face = cv2.resize(face_cropped(my_frame), (450, 450))
                   face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                   file_name_path = f"Data/user.{self.var_std_id.get()}.{img_id}.jpg"
                   cv2.imwrite(file_name_path, face)

                   cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                   cv2.imshow("Cropped Face", face)

               if cv2.waitKey(1) == 13 or img_id == 100:  # 13 is Enter key
                    break

           cap.release()
           cv2.destroyAllWindows()

           messagebox.showinfo("Result", "Generating dataset completed!", parent=self.root)

        except Exception as e:
            messagebox.showerror("Error", f"Due to: {str(e)}", parent=self.root)

if __name__ == "__main__":
         root = Tk()
         obj = Student(root)
         root.mainloop()












     





























           

    
        

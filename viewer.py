

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from time import strftime
from datetime import datetime
from tkinter import messagebox as mbox
from train import Train
from Face_Recognition import Face_Recognition
from Attendance import Attendance
from Developer import Developer
from Help import Help



class FACEATTENDANCEPROJECT:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACEATTENDANCEPROJECT")


        # Top 3 header images
        self.photoimg0 = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Best System.jpg").resize((500, 130), Image.LANCZOS))
        self.photoimg1 = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\MenL Photo.webp").resize((500, 130), Image.LANCZOS))
        self.photoimg2 = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Side Photo.webp").resize((500, 130), Image.LANCZOS))

        # Background image
        self.photoimg3 = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\BG Photo.avif").resize((1530, 660), Image.LANCZOS))

        Label(self.root, image=self.photoimg0).place(x=0, y=0, width=500, height=130)
        Label(self.root, image=self.photoimg1).place(x=500, y=0, width=500, height=130)
        Label(self.root, image=self.photoimg2).place(x=1000, y=0, width=500, height=130)

        # Background label
        self.bg_img = Label(self.root, image=self.photoimg3)
        self.bg_img.place(x=0, y=130, width=1530, height=660)

        # Title
        title_lbl = Label(self.bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE", 
                          font=("times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        #===============Time====================
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font=('times new roman', 14, 'bold'),
            background='white', foreground='blue')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

    
       # Student Image Button
        self.student_img = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\STUDENTS DETAIL.jpeg").resize((220, 220), Image.LANCZOS))


        b1 = Button(self.root,image=self.student_img,command=self.student_details, cursor="hand2")
        b1.place(x=200, y=200, width=220, height=220)


        # Student Text Button
        b1 = Button(self.root, text="Student Details", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white",command=self.student_details)
        b1.place(x=200, y=420, width=220, height=40)


        # Detect Face Button

        self.face_detector_img = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Face Recognition.jpg").resize((220, 220), Image.LANCZOS))
        b2 = Button(self.root, image=self.face_detector_img, cursor="hand2",command=self.face_data)
        b2.place(x=500, y=200, width=220, height=220)

        # Face Detector Text Button
        b2 = Button(self.root, text="Face Detector", cursor="hand2",command=self.face_data,
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b2.place(x=500, y=420, width=220, height=40)


        # Attendance Image Button                                          
        self.attendance_img = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Face Attendance.webp").resize((220, 220), Image.LANCZOS))
        b3 = Button(self.root, image=self.attendance_img, cursor="hand2",command=self.Attendance_data)
        b3.place(x=800, y=200, width=220, height=220)  # spacing adjusted from previous one

        # Attendance Text Button
        b3 = Button(self.root, text="Attendance", cursor="hand2",command=self.Attendance_data,
              font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b3.place(x=800, y=420, width=220, height=40)

        # ---------- Help Desk Button ----------
        self.helpdesk_img = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Help Desk.webp").resize((220, 220), Image.LANCZOS))
        b4 = Button(self.root, image=self.helpdesk_img, cursor="hand2",command=self.Help_data)
        b4.place(x=1100, y=200, width=220, height=220)

        b4 = Button(self.root, text="Help Desk", cursor="hand2",command=self.Help_data,
              font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b4.place(x=1100, y=420, width=220, height=40)


        # ---------- Train Data Button ----------
        self.traindata_img = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Train Dta.jpg").resize((220, 220), Image.LANCZOS))
        b5 = Button(self.root, image=self.traindata_img, cursor="hand2",command=self.train_data)
        b5.place(x=200, y=500, width=220, height=220)

        b5 = Button(self.root, text="Train Data", cursor="hand2",command=self.train_data,
              font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b5.place(x=200, y=720, width=220, height=40)


        # Photos image button
        self.Photos_img = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Photos.jpg").resize((220, 220), Image.LANCZOS))
        b6 = Button(self.root, image=self.Photos_img, cursor="hand2",command=self.open_img)
        b6.place(x=500, y=500, width=220, height=220)  # same y as Train Data

        # Photos text label
        b6 = Button(self.root, text="Photos", cursor="hand2",command=self.open_img,
              font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b6.place(x=500, y=720, width=220, height=40)  # same y as Train Data text


        # Developer image button
        self.Developer_img = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Developer.avif").resize((220, 220), Image.LANCZOS))
        b7 = Button(self.root, image=self.Developer_img, cursor="hand2",command=self.Developer_data)
        b7.place(x=800, y=500, width=220, height=220)  # same y as Train Data & Photos

        # Developer text label
        b7 = Button(self.root, text="Developer", cursor="hand2",command=self.Developer_data,
              font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b7.place(x=800, y=720, width=220, height=40)  # same y as others


        # Exit image button
        self.Exit_img = ImageTk.PhotoImage(Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\EXIT.jpeg").resize((220, 220), Image.LANCZOS))
        b8 = Button(self.root, image=self.Exit_img, cursor="hand2", command=self.iExit)  # optional exit command
        b8.place(x=1100, y=500, width=220, height=220)  # same y as others

        # Exit text label
        b8 = Button(self.root, text="Exit", cursor="hand2",command=self.iExit,
              font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b8.place(x=1100, y=720, width=220, height=40)



    def open_img(self):
          os.startfile("Data")

    

    def iExit(self):
        i_exit = mbox.askyesno("Face Recognition", "Are you sure exit this project", parent=self.root)
        if i_exit:
         self.root.destroy()


# =============Function Button=====================
    def  student_details(self):
           self.new_window=Toplevel(self.root)
           self.app=Student(self.new_window)




    def  train_data(self):
           self.new_window=Toplevel(self.root)
           self.app=Train(self.new_window)



    def  face_data(self):
           self.new_window=Toplevel(self.root)
           self.app=Face_Recognition(self.new_window)


    def  Attendance_data(self):
           self.new_window=Toplevel(self.root)
           self.app=Attendance(self.new_window)


    def  Developer_data(self):
           self.new_window=Toplevel(self.root)
           self.app=Developer(self.new_window)



    def  Help_data(self):
           self.new_window=Toplevel(self.root)
           self.app=Help(self.new_window)







    
    

if __name__ == "__main__":
      root = Tk()
      obj = FACEATTENDANCEPROJECT(root)
      root.mainloop()

    

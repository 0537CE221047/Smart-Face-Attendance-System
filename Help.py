       
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector 
from tkinter import messagebox
import cv2




class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACEATTENDANCEPROJECT")


        title_lbl = Label(self.root, text="How can I help you?", 
                          font=("times new roman", 35, "bold"), bg="navyblue", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        img_top = Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Help.jpg")
        img_top = img_top.resize((1530, 710), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=710)


        skill_label = Label(self.root, text="Email: sheetaldamah22@gmail.com", font=("Arial", 17), fg="white", bg="navyblue")
        skill_label.place(x=630, y=718)



if __name__ == "__main__":
    root = Tk()
    obj =Help (root)
    root.mainloop()

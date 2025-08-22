from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector 
from tkinter import messagebox
import cv2




class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACEATTENDANCEPROJECT")




        title_lbl = Label(self.root, text="DEVELOPER", 
                          font=("times new roman", 35, "bold"), bg="purple", fg="white")
        title_lbl.place(x=0, y=0, width=1530, height=45)


        img_top = Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Girl Dev.jpg")
        img_top = img_top.resize((1530, 710), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=45, width=1530, height=710)


        main_frame=Frame(self.root,bd=2,bg="white")
        main_frame.place(x=480 , y=160, width=500 , height=200)

        img_top1 = Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Girl Dev.jpg")
        img_top1 = img_top1.resize((500, 200), Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)



        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=0, y=0, width=500, height=200)

         

        # Photo load karna (corner me lagane ke liye)
        my_photo = Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\MyPhoto.jpg")
        my_photo = my_photo.resize((90, 90), Image.LANCZOS)  # corner ke liye small size
        self.my_photo_img = ImageTk.PhotoImage(my_photo)

        # Corner me lagana (right-bottom)
        photo_lbl = Label(main_frame, image=self.my_photo_img, bg="white")
        photo_lbl.place(x=0, y=0)

        name_label = Label(main_frame, text="Hello! my name is Sheetal .", font=("Arial", 14, "bold"), fg="white", bg="purple")
        name_label.place(x=100, y=5)

        skill_label = Label(main_frame, text="I am full stack Developer", font=("Arial", 12), fg="white", bg="purple")
        skill_label.place(x=100, y=38)

        skill_label = Label(main_frame, text="Email- sheetaldamah22@gmail.com", font=("Arial", 12), fg="white", bg="purple")
        skill_label.place(x=100, y=69)

        
        


        





if __name__ == "__main__":
    root = Tk()
    obj =Developer (root)
    root.mainloop()

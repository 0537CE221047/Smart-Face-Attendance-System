from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector 
from tkinter import messagebox
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
from utils import draw_boundray


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACEATTENDANCEPROJECT")



        title_lbl = Label(self.root, text="FACE RECOGNITION", 
                          font=("times new roman", 35, "bold"), bg="white", fg="Darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)



        # Left image
        img_left = Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Face Recognition.jpg")
        img_left = img_left.resize((650, 700), Image.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl_left = Label(self.root, image=self.photoimg_left)
        f_lbl_left.place(x=0, y=55, width=650, height=700)

        # Right image
        img_bottom = Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Scanning Face.jpg")
        img_bottom = img_bottom.resize((950, 700), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl_right = Label(self.root, image=self.photoimg_bottom)
        f_lbl_right.place(x=650, y=55, width=918, height=700)




        b1 = Button(f_lbl_right, text="Face Recognition",cursor="hand2",command=self.face_recog,
                      font=("times new roman", 18, "bold"), bg="darkblue", fg="white")
        b1.place(x=200, y=655, width=200, height=40)




        #=============Attendance============== 
    def mark_attendance(self,i,r,n,d):
        with open("Sheetal.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list)and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Preset")
                










         #=============Face Recognition============== 

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minimumneighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minimumneighbors)

            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                # Database connection
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="root",
                    database="face_recognizer"
                )
                my_cursor = conn.cursor()

                # Student Name
                my_cursor.execute("SELECT Std_name FROM student WHERE Std_Id=%s", (id,))
                row = my_cursor.fetchone()
                n = "+".join(map(str, row)) if row else "Unknown"

                # Roll No. (space wale column ke liye backticks)
                my_cursor.execute("SELECT `Roll No.` FROM student WHERE Std_Id=%s", (id,))
                row = my_cursor.fetchone()
                r = "+".join(map(str, row)) if row else "Unknown"

                # Department
                my_cursor.execute("SELECT Dep FROM student WHERE Std_Id=%s", (id,))
                row = my_cursor.fetchone()
                d = "+".join(map(str, row)) if row else "Unknown"


                # Department
                my_cursor.execute("SELECT Std_Id FROM student WHERE Std_Id=%s", (id,))
                row = my_cursor.fetchone()
                i = "+".join(map(str, row)) if row else "Unknown"

                conn.close()

                if confidence > 77:
                    cv2.putText(img, f"Id: {r}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Roll No.: {r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Std_name: {n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Dep: {d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i,r,n,d)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            draw_boundray(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

              # Load classifier and face recognizer
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

              # Start video capture
        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key to exit
               break

        video_cap.release()
        cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()

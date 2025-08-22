from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import os
import datetime
import time
import random
from viewer import FACEATTENDANCEPROJECT




def main():
    win = Tk()
    app = Login_Window(win)
    win.mainloop()


class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background Image
        self.photoimg0 = ImageTk.PhotoImage(
            Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Login BG.jpg").resize((1530, 780), Image.LANCZOS)
        )
        Label(self.root, image=self.photoimg0).place(x=0, y=0, width=1530, height=780)

        # Frame
        frame = Frame(self.root, bg="darkblue")
        frame.place(x=230, y=350, width=340, height=420)

        # Login Logo
        img1 = Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\login.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="darkblue", borderwidth=0)
        lblimg1.place(x=300, y=350, width=190, height=100)

        # Title
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"),
                        fg="white", bg="navyblue")
        get_str.place(x=95, y=100)

        # Username
        username_label = Label(frame, text="Username", font=("times new roman", 15, "bold"),
                               fg="white", bg="navyblue")
        username_label.place(x=95, y=150)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=95, y=185, width=200)

        # Password
        password_label = Label(frame, text="Password", font=("times new roman", 15, "bold"),
                               fg="white", bg="navyblue")
        password_label.place(x=95, y=220)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=95, y=250, width=200)

        # Login Button
        login_btn = Button(frame, text="Login", font=("times new roman", 15, "bold"),
                           bd=3, relief=RIDGE, bg="blue", fg="white",
                           activeforeground="white", activebackground="blue",
                           width=12, command=self.login)
        login_btn.place(x=95, y=305)

        # Register Button
        register_btn = Button(frame, text="Register", command=self.register_window,
                              font=("times new roman", 12, "underline"),
                              fg="white", bg="navyblue", bd=0, cursor="hand2")
        register_btn.place(x=95, y=365)

        # Forgot Password Button
        forgot_btn = Button(frame, text="Forgot Password?", 
                            font=("times new roman", 12, "underline"),
                            fg="white", bg="navyblue", bd=0, cursor="hand2",command=self.forgot_password_window)
        forgot_btn.place(x=180, y=365)



    # ---------------- LOGIN ----------------
    
    def login(self):
        username = self.txtuser.get()
        password = self.txtpass.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        # Hardcoded admin login
        if username == "sheetal" and password == "bittu":
            messagebox.showinfo("Success", "Welcome to the Face Attendance System Software")
            self.root.destroy()
            new_win = Tk()
            app = FACEATTENDANCEPROJECT(new_win)
            new_win.mainloop()
            return

        # MySQL login check
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",  # apna DB password
                database="my_data"
            )
            cur = conn.cursor()
            cur.execute("SELECT * FROM register WHERE Email=%s AND password=%s", (username, password))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Username & Password")
            else:
                access = messagebox.askyesno("YesNo", "Access only admin?")
                if access:
                    self.root.destroy()
                    new_win = Tk()
                    app = FACEATTENDANCEPROJECT(new_win)
                    new_win.mainloop()

            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}")

    # ---------------- REGISTER WINDOW ----------------
    def register_window(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    # ---------------- FORGOT PASSWORD WINDOW ----------------
    def forgot_password_window(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Forgot Password")
        self.root2.geometry("400x300+500+200")
        self.root2.config(bg="white")

        lbl = Label(self.root2, text="Enter Registered Email", 
                font=("times new roman", 14, "bold"), bg="white")
        lbl.pack(pady=20)

        self.var_email = StringVar()
        txt_email = Entry(self.root2, textvariable=self.var_email, 
                      font=("times new roman", 12), bd=2, relief=GROOVE)
        txt_email.pack(pady=10)

        lbl_pass = Label(self.root2, text="Enter New Password", 
                     font=("times new roman", 14, "bold"), bg="white")
        lbl_pass.pack(pady=10)

        self.var_newpass = StringVar()
        txt_pass = Entry(self.root2, textvariable=self.var_newpass, show="*", 
                     font=("times new roman", 12), bd=2, relief=GROOVE)
        txt_pass.pack(pady=10)

        btn_reset = Button(self.root2, text="Reset Password", 
                       font=("times new roman", 12, "bold"),
                       bg="blue", fg="white", command=self.reset_password)
        btn_reset.pack(pady=20)

    # ---------------- RESET PASSWORD FUNCTION ----------------
    def reset_password(self):
        email = self.var_email.get()
        new_pass = self.var_newpass.get()

        if email == "" or new_pass == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
            return

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="root",
                database="my_data"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s", (email,))
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Email, not registered!", parent=self.root2)
            else:
                my_cursor.execute("UPDATE register SET password=%s WHERE email=%s", (new_pass, email))
                conn.commit()
                if my_cursor.rowcount > 0:
                    messagebox.showinfo("Success", "Password reset successful!", parent=self.root2)
                    self.root2.destroy()
                else:
                    messagebox.showerror("Error", "Password update failed!", parent=self.root2)

            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {str(e)}", parent=self.root2)

    
      
            
    
                
                

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ============== Variable Declaration ==========
        self.var_fname = StringVar()
        self.var_Lname = StringVar()
        self.var_contact = StringVar()
        self.var_Email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()
        self.var_check = IntVar()

        # =============== BG Image ==============
        self.photoimg = ImageTk.PhotoImage(
            Image.open(r"C:\FACE ATTENDANCE PROJECT\PHOTOS FROM COLLEGE\Purple.png").resize((1530, 780), Image.LANCZOS)
        )
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=1530, height=780)

        # =============== Main Frame ==============
        center_frame = Frame(root, bg="white", bd=2, relief=RIDGE, height=450, width=500)
        center_frame.pack(expand=True, pady=100)

        register_lbl = Label(root, text="REGISTER HERE..", font=("times new roman", 20, "bold"),
                             fg="purple", bg="white")
        register_lbl.place(x=630, y=200)

        # =============== Labels and Entries ==============
        Label(root, text="First Name:", font=("times new roman", 15, "bold"), bg="white").place(x=540, y=242)
        ttk.Entry(root, textvariable=self.var_fname, font=("times new roman", 13, "bold")).place(x=540, y=266, width=170)

        Label(root, text="Last Name:", font=("times new roman", 15, "bold"), bg="white").place(x=540, y=325)
        ttk.Entry(root, textvariable=self.var_Lname, font=("times new roman", 13, "bold")).place(x=540, y=350, width=170)

        Label(root, text="Contact:", font=("times new roman", 15, "bold"), bg="white").place(x=540, y=400)
        ttk.Entry(root, textvariable=self.var_contact, font=("times new roman", 13, "bold")).place(x=540, y=425, width=170)

        Label(root, text="Email:", font=("times new roman", 15, "bold"), bg="white").place(x=540, y=470)
        ttk.Entry(root, textvariable=self.var_Email, font=("times new roman", 13, "bold")).place(x=540, y=495, width=170)

        Label(root, text="Password:", font=("times new roman", 15, "bold"), bg="white").place(x=800, y=240)
        ttk.Entry(root, textvariable=self.var_pass, font=("times new roman", 13, "bold"), show="*").place(x=800, y=266, width=170)

        Label(root, text="Confirm Password:", font=("times new roman", 15, "bold"), bg="white").place(x=800, y=325)
        ttk.Entry(root, textvariable=self.var_confpass, font=("times new roman", 13, "bold"), show="*").place(x=800, y=350, width=170)

        Label(root, text="Security Question:", font=("times new roman", 15, "bold"), bg="white").place(x=800, y=400)
        security_q_combo = ttk.Combobox(root, textvariable=self.var_securityQ, font=("times new roman", 13, "bold"),
                                        state="readonly", width=18)
        security_q_combo["values"] = ("Select", "Your Birth Place", "Your Best Friend's Name",
                                      "Your Pet Name", "Your Favourite Teacher")
        security_q_combo.current(0)
        security_q_combo.place(x=800, y=425)

        Label(root, text="Security Answer:", font=("times new roman", 15, "bold"), bg="white").place(x=800, y=470)
        ttk.Entry(root, textvariable=self.var_securityA, font=("times new roman", 13, "bold")).place(x=800, y=495, width=170)

        # ============ Check Button ===========
        Checkbutton(root, variable=self.var_check, text="I Agree to Terms & Conditions",
                    font=("times new roman", 12), bg="white", onvalue=1, offvalue=0).place(x=540, y=550)

        # =============== Register Button ===============
        Button(root, text="Register", font=("times new roman", 15, "bold"),
               bg="darkgreen", fg="white", cursor="hand2").place(x=570, y=590, width=120, height=35)

        # Login Now Button
        Button(root, text="Login Now", command=self.login,
               font=("times new roman", 15, "bold"), bg="purple",
               fg="white", cursor="hand2").place(x=710, y=590, width=120, height=35)

    # ================= Function Declarations ==================
    def login(self):
        self.root.destroy()
        main()








if __name__ == "__main__":
    main()

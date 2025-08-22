from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector


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

        register_lbl = Label(root, text="REGISTER HERE..", font=("times new roman", 20, "bold"), fg="purple", bg="white")
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
        security_q_combo = ttk.Combobox(root, textvariable=self.var_securityQ, font=("times new roman", 13, "bold"), state="readonly", width=18)
        security_q_combo["values"] = ("Select", "Your Birth Place", "Your Best Friend's Name", "Your Pet Name", "Your Favourite Teacher")
        security_q_combo.current(0)
        security_q_combo.place(x=800, y=425)

        Label(root, text="Security Answer:", font=("times new roman", 15, "bold"), bg="white").place(x=800, y=470)
        ttk.Entry(root, textvariable=self.var_securityA, font=("times new roman", 13, "bold")).place(x=800, y=495, width=170)

        # ============ Check Button ===========
        Checkbutton(root, variable=self.var_check, text="I Agree to Terms & Conditions",
                    font=("times new roman", 12), bg="white", onvalue=1, offvalue=0).place(x=540, y=550)

        # =============== Register Button ===============
        Button(root, text="Register", command=self.register_data, font=("times new roman", 15, "bold"),
               bg="darkgreen", fg="white", cursor="hand2").place(x=570, y=590, width=120, height=35)

        # Login Now Button (Text Based)
        Button(root, text="Login Now", command=self.login, font=("times new roman", 15, "bold"),
               bg="purple", fg="white", cursor="hand2").place(x=710, y=590, width=120, height=35)

    # ================= Function Declarations ==================
    def register_data(self):
        try:
            # Validations
            if self.var_fname.get() == "" or self.var_Email.get() == "" or self.var_securityQ.get() == "Select":
                messagebox.showerror("Error", "All fields are required")
                return
            elif self.var_pass.get() != self.var_confpass.get():
                messagebox.showerror("Error", "Password and confirm password must be same")
                return
            elif self.var_check.get() == 0:
                messagebox.showerror("Error", "Please agree to our terms and conditions")
                return

            # Database Connection
            conn = mysql.connector.connect(host="localhost", user="root", password="root", database="my_data")
            cur = conn.cursor()

            # Check if user exists
            cur.execute("SELECT * FROM register WHERE email=%s", (self.var_Email.get(),))
            row = cur.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exists, please try another email")
            else:
                cur.execute("INSERT INTO register (fname, lname, contact, Email, securityQ, securityA, password) VALUES (%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_fname.get(),
                    self.var_Lname.get(),
                    self.var_contact.get(),
                    self.var_Email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_pass.get()
                ))
                conn.commit()
                messagebox.showinfo("Success", "Registration successful")
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}")

    def login(self):
        messagebox.showinfo("Login", "This will open login window (functionality to be added)")



if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()

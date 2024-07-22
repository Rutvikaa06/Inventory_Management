from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import sqlite3
import email_pass
import os
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        #===bg image==
        self.bg=ImageTk.PhotoImage(file="images/imagebg.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)
      
        #===left image===
        self.left=ImageTk.PhotoImage(file="images/back.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=700)

        #register frame==
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=600)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)
    
        #----row1
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_lname.place(x=370,y=130,width=250)

        #-----------------#row2
        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_email.place(x=370,y=200,width=250)

        #----row3
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=240)
      
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)
        
        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_answer.place(x=370,y=270,width=250)

        #=====
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_password.place(x=50,y=340,width=250)

        cpassword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="lightgray")
        self.txt_cpassword.place(x=370,y=340,width=250)

        #==terms==
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg="white",font=("times new roman",12)).place(x=50,y=380)
     
        lbl_utype=Label(frame1,text="User Type",font=("times new roman",15,"bold"),bg="white",fg="gray").place(x=370,y=380)
        self.cmb_utype=ttk.Combobox(frame1,values=("Select","Admin","Customer","Supplier"),state='readonly',justify=CENTER,font=("times new roman",15))
        self.cmb_utype.place(x=370,y=410,width=250)
        self.cmb_utype.current(0)


        self.btn_img=ImageTk.PhotoImage(file="images/sol1.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
       
        btn_login=Button(self.root,text="Sign In",command=self.login_window,font=("times new roman",20),bd=0,cursor="hand2").place(x=175,y=540,width=180)
    
    def login_window(self):
        self.root.destroy()
        os.system("python login.py")


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_utype.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_cpassword.delete(0,END)
        self.cmb_quest.current(0)

    def register_data(self):
        if self.txt_fname.get()==""  or self.txt_contact.get()=="" or self.txt_email.get()=="" or self.cmb_utype.get()=="Select" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)
        elif self.txt_password.get()!=self.txt_cpassword.get():
            messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree our terms & condition",parent=self.root)
        else:
            try:
                con=sqlite3.connect(database=r'ims.db')
                cur=con.cursor()
                cur.execute("select * from register where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                #print(row)
                if row!=None:
                    messagebox.showerror("Error","User Alreadty Exist,Please try with another email",parent=self.root)
                else:
                    cur.execute("insert into register (f_name,l_name,contact,email,utype,question,answer,password) values(?,?,?,?,?,?,?,?)",(
                           self.txt_fname.get(),
                           self.txt_lname.get(),
                           self.txt_contact.get(),
                           self.txt_email.get(),
                           self.cmb_utype.get(),
                           self.cmb_quest.get(),
                           self.txt_answer.get(),
                           self.txt_password.get(),
                          ))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","Register Successfully",parent=self.root)
                    self.clear()
                    self.login_window()
            except Exception as es:
                    messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
            
           


root=Tk()
obj=Register(root)
root.mainloop()
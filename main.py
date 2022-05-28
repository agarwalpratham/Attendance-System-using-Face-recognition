from cProfile import label
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendence
from authority import Authority
import os


class face_recognition_system:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1530x790+0+0")
            self.root.title("Attendance System")
            

             # background insertion

            img=Image.open(r"images\back.jpg")
            img=img.resize((1530,790),Image.ANTIALIAS)
            self.photoimg=ImageTk.PhotoImage(img)

            bg_img=Label(self.root,image=self.photoimg)
            bg_img.place(x=0,y=0,width=1530,height=790)

            # title bar

            title_lbl=Label(bg_img,text="Attendance System using Face Recognition",font=("times new roman",35,"bold"),bg="brown",fg="black")
            title_lbl.place(x=0,y=0,width=1530,height=55)

            #student record button

            img1=Image.open(r"images\student_record.jpg")
            img1=img1.resize((220,220),Image.ANTIALIAS)
            self.photoimg1=ImageTk.PhotoImage(img1)

            b1=Button(bg_img,image=self.photoimg1,command=self.student_records,cursor="hand2")
            b1.place(x=280,y=125,width=220,height=220)

            b1_1=Button(bg_img,text="Student Record",command=self.student_records,cursor="hand2",font=("times new roman",15,"bold"),bg="red",fg="black")
            b1_1.place(x=280,y=325,width=220,height=35)

            #attendance mark button

            img2=Image.open(r"images\mark_atten.jpg")
            img2=img2.resize((220,220),Image.ANTIALIAS)
            self.photoimg2=ImageTk.PhotoImage(img2)

            b2=Button(bg_img,image=self.photoimg2,command=self.face_data,cursor="hand2")
            b2.place(x=650,y=250,width=220,height=220)

            b2_2=Button(bg_img,text="Mark Attendance",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="red",fg="black")
            b2_2.place(x=650,y=450,width=220,height=35)

            #face detect button

            img3=Image.open(r"images\mark1.jpg")
            img3=img3.resize((220,220),Image.ANTIALIAS)
            self.photoimg3=ImageTk.PhotoImage(img3)

            b3=Button(bg_img,image=self.photoimg3,cursor="hand2",command=self.authority_data)
            b3.place(x=1020,y=125,width=220,height=220)

            b3_3=Button(bg_img,text="Authentication",cursor="hand2",command=self.authority_data,font=("times new roman",15,"bold"),bg="red",fg="black")
            b3_3.place(x=1020,y=325,width=220,height=35)

            #Train Face button

            img5=Image.open(r"images\train.jpg")
            img5=img5.resize((220,220),Image.ANTIALIAS)
            self.photoimg5=ImageTk.PhotoImage(img5)

            b5=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.train_data)
            b5.place(x=280,y=400,width=220,height=220)

            b5_5=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="red",fg="black")
            b5_5.place(x=280,y=600,width=220,height=35)

            #Attendance record button

            img6=Image.open(r"images\attend.jpg")
            img6=img6.resize((220,220),Image.ANTIALIAS)
            self.photoimg6=ImageTk.PhotoImage(img6)

            b6=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
            b6.place(x=1020,y=400,width=220,height=220)

            b6_6=Button(bg_img,text="Attendance Record",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="red",fg="black")
            b6_6.place(x=1020,y=600,width=220,height=40)
            

        # =====================Functions Button================
        
        def open_img(self):
            os.startfile("data")

        def student_records(self):
            self.new_window=Toplevel(self.root)
            self.app=student(self.new_window)   

        def train_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Train(self.new_window)   
        def face_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Face_Recognition(self.new_window)   
        def attendance_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Attendence(self.new_window)   
        def authority_data(self):
            self.new_window=Toplevel(self.root)
            self.app=Authority(self.new_window)   

if __name__=="__main__":
    root=Tk()
    obj=face_recognition_system(root)
    root.mainloop()
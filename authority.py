from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2
import os
import numpy as np


class Authority:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1530x790+0+0")
            self.root.title("Exam Authority")
     

            title_lbl=Label(self.root,text="Exam Centre Authentication",font=("times new roman",35,"bold"),bg="black",fg="green")
            title_lbl.place(x=0,y=0,width=1530,height=55)

            # image 1

            img_top=Image.open(r"images\security.jpg")
            img_top=img_top.resize((1530,735),Image.ANTIALIAS)
            self.photoimg_top=ImageTk.PhotoImage(img_top)

            f_lbl=Label(self.root,image=self.photoimg_top)
            f_lbl.place(x=0,y=55,width=1530,height=735)

            # image 2

            # img_bottom=Image.open(r"images\mark_atten_2.jpg")
            # img_bottom=img_bottom.resize((950,735),Image.ANTIALIAS)
            # self.photoimg_bottom=ImageTk.PhotoImage(img_bottom)

            # f_lbl=Label(self.root,image=self.photoimg_bottom)
            # f_lbl.place(x=650,y=55,width=950,height=735)
            # button 
            b4_4=Button(f_lbl,text="Scan Face to authenticate your access",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="blue",fg="white")
            b4_4.place(x=100,y=225,width=400,height=40)

            # ============face recognition==========

        def face_recog(self):
            def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
                gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

                coord=[]

                for(x,y,w,h) in features:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                    confidence=int((100*(1-predict/300)))

                    conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="sys")
                    my_cursor=conn.cursor()

                    my_cursor.execute("select name from sys.student where student_id="+str(id))
                    n=my_cursor.fetchone()
                    n="+".join(n)

                    my_cursor.execute("select roll from sys.student where student_id="+str(id))
                    r=my_cursor.fetchone()
                    r="+".join(r)
                    
                    my_cursor.execute("select dep from sys.student where student_id="+str(id))
                    d=my_cursor.fetchone()
                    d="+".join(d)
                    
                    my_cursor.execute("select student_id from sys.student where student_id="+str(id))
                    i=my_cursor.fetchone()
                    i="+".join(i)
                    
                    if confidence>77:
                       cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                       cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                       cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                       cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                       messagebox.showinfo("Examination Authority",f"Good Morning, {n}\nAll the best for the exam.")
                    else:
                        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                        cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                    coord=[x,y,w,h]
                return coord    

            def recognize(img,clf,faceCascade):    
                coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
                return img

            faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")    
            clf=cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap=cv2.VideoCapture(0)

            while True:
                ret,img=video_cap.read()
                img=recognize(img,clf,faceCascade)
                cv2.imshow("Welcome to face recognition",img)

                if cv2.waitKey(1)==13:
                    break
            video_cap.release()
            cv2.destroyAllWindows()













if __name__ == "__main__":
        root=Tk()
        obj=Authority(root)
        root.mainloop()
from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector
import cv2 


# from jmespath import search


class student:
        def __init__(self,root):
            self.root=root
            self.root.geometry("1530x790+0+0")
            self.root.title("Attendence System")
            
            # ==========variables=============
            self.var_dep=StringVar()
            self.var_course=StringVar()
            self.var_year=StringVar()
            self.var_semester=StringVar()
            self.var_std_id=StringVar()
            self.var_std_name=StringVar()
            self.var_div=StringVar()
            self.var_roll=StringVar()
            self.var_gender=StringVar()
            self.var_dob=StringVar()
            self.var_email=StringVar()
            self.var_phone=StringVar()
            self.var_address=StringVar()
            self.var_teacher=StringVar()
            
  # image1

            img1=Image.open(r"images\sr_1.jpg")
            img1=img1.resize((510,130),Image.ANTIALIAS)
            self.photoimg1=ImageTk.PhotoImage(img1)

            bg_img1=Label(self.root,image=self.photoimg1)
            bg_img1.place(x=0,y=0,width=510,height=130)
  # image2

            img2=Image.open(r"images\sr_2.jpg")
            img2=img2.resize((510,130),Image.ANTIALIAS)
            self.photoimg2=ImageTk.PhotoImage(img2)

            bg_img2=Label(self.root,image=self.photoimg2)
            bg_img2.place(x=500,y=0,width=510,height=130)
  # image3

            img3=Image.open(r"images\sr_3.jpg")
            img3=img3.resize((510,130),Image.ANTIALIAS)
            self.photoimg3=ImageTk.PhotoImage(img3)

            bg_img3=Label(self.root,image=self.photoimg3)
            bg_img3.place(x=1000,y=0,width=510,height=130)

  # background insertion

            img=Image.open(r"images\ise_dept.jpg")
            img=img.resize((1530,850),Image.ANTIALIAS)
            self.photoimg=ImageTk.PhotoImage(img)

            bg_img=Label(self.root,image=self.photoimg)
            bg_img.place(x=0,y=130,width=1530,height=850)


    # title bar

            title_lbl=Label(bg_img,text="Students Record",font=("times new roman",35,"bold"),bg="black",fg="red")
            title_lbl.place(x=0,y=0,width=1530,height=50)

    # main frames

            main_frame=Frame(bg_img,bd=2,bg="white")
            main_frame.place(x=20,y=50,width=1480,height=600)

    # left label frame

            left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="white")
            left_frame.place(x=10,y=10,width=730,height=580)
    
            img_left=Image.open(r"images\sr_4.jpg")
            img_left=img_left.resize((710,130),Image.ANTIALIAS)
            self.photoimg_left=ImageTk.PhotoImage(img_left)

            bg_img_left=Label(left_frame,image=self.photoimg_left)
            bg_img_left.place(x=5,y=0,width=710,height=130)
      
            # current course

            current_course_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Current Course Info",font=("times new roman",12,"bold"),bg="white")
            current_course_frame.place(x=5,y=135,width=720,height=150)

            # department 
            
            dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
            dep_label.grid(row=0,column=0,padx=10,sticky=W)

            dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
            dep_combo["values"]=("Select Department","Computer","Civil","ECE","IT","Mechanical")
            dep_combo.current(0)
            dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
       
            # Course 

            course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
            course_label.grid(row=0,column=2,padx=10,sticky=W)

            course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),width=17,state="readonly")
            course_combo["values"]=("Select Course","BE","ME")
            course_combo.current(0)
            course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)
            
            # Year 

            year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
            year_label.grid(row=1,column=0,padx=10,sticky=W)

            year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),width=17,state="readonly")
            year_combo["values"]=("Select year","1st","2nd","3rd","4th","5th")
            year_combo.current(0)
            year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

            # Semester 

            semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
            semester_label.grid(row=1,column=2,padx=10,sticky=W)

            semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),width=17,state="readonly")
            semester_combo["values"]=("Select semester","1st","2nd")
            semester_combo.current(0)
            semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

            # Class Student Information

            class_student_frame=LabelFrame(left_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"),bg="white")
            class_student_frame.place(x=5,y=250,width=720,height=300)

             #student id
        
            student_id_label=Label(class_student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
            student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

            student_id_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
            student_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

             #student name
        
            student_name_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
            student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

            student_name_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
            student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

             #class division
        
            class_div_label=Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
            class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

            div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),width=17,state="readonly")
            div_combo["values"]=("Select division","A","B","C")
            div_combo.current(0)
            div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)
    

             #Roll No
        
            roll_no_label=Label(class_student_frame,text="Roll NO.:",font=("times new roman",13,"bold"),bg="white")
            roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

            roll_no_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
            roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
            
             #Gender
        
            Gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
            Gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

            gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=17,state="readonly")
            gender_combo["values"]=("Select gender","MALE","FEMALE")
            gender_combo.current(0)
            gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)
    
             #DOB
        
            dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
            dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

            dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
            dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
    
             #Email
        
            email_label=Label(class_student_frame,text="email:",font=("times new roman",13,"bold"),bg="white")
            email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

            email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
            email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
    
             #Phone Number
        
            phone_label=Label(class_student_frame,text="Phone No. :",font=("times new roman",13,"bold"),bg="white")
            phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

            phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
            phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
    
             # Address
        
            address_label=Label(class_student_frame,text="Classroom:",font=("times new roman",13,"bold"),bg="white")
            address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

            address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
            address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
    
             #Faculty Name
        
            faculty_label=Label(class_student_frame,text="Faculty Name:",font=("times new roman",13,"bold"),bg="white")
            faculty_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

            faculty_entry=ttk.Entry(class_student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))
            faculty_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

            #radio button
            self.var_radio1=StringVar()
            radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
            radiobtn1.grid(row=6,column=0)

            radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
            radiobtn2.grid(row=6,column=1)

            #button frame

            btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
            btn_frame.place(x=0,y=200,width=715,height=70)

            save_btn=Button(btn_frame,text="Save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
            save_btn.grid(row=0,column=0)

            update_btn=Button(btn_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
            update_btn.grid(row=0,column=1)
            
            delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
            delete_btn.grid(row=0,column=2)

            reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
            reset_btn.grid(row=0,column=3)

            btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
            btn_frame1.place(x=0,y=235,width=715,height=35)
            
            take_photo_btn=Button(btn_frame1,command=self.generate_dataset,text="Take Photo Sample",width=70,font=("times new roman",13,"bold"),bg="blue",fg="white")
            take_photo_btn.grid(row=0,column=0)
            

    # right label frame
            right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",13,"bold"),bg="white")
            right_frame.place(x=750,y=10,width=720,height=580)

            img_right=Image.open(r"images\ise_dept.jpg")
            img_right=img_right.resize((720,130),Image.ANTIALIAS)
            self.photoimg_right=ImageTk.PhotoImage(img_right)

            bg_img_right=Label(right_frame,image=self.photoimg_right)
            bg_img_right.place(x=5,y=0,width=720,height=130)

         # ===========table frame=======

            table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
            table_frame.place(x=5,y=140,width=710,height=420)

            scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

            self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","faculty","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_x.config(command=self.student_table.xview)
            scroll_y.config(command=self.student_table.yview)

            self.student_table.heading("dep",text="Department")
            self.student_table.heading("course",text="Course")
            self.student_table.heading("year",text="Year")
            self.student_table.heading("sem",text="Semester")
            self.student_table.heading("id",text="StudentId")
            self.student_table.heading("name",text="Name")
            self.student_table.heading("div",text="Division")
            self.student_table.heading("roll",text="Roll No.")
            self.student_table.heading("gender",text="Gender")
            self.student_table.heading("dob",text="DOB")
            self.student_table.heading("email",text="Email")
            self.student_table.heading("phone",text="Phone")
            self.student_table.heading("address",text="Address")
            self.student_table.heading("faculty",text="Faculty")
            self.student_table.heading("photo",text="PhotoSampleStatus")
            self.student_table["show"]="headings"

            self.student_table.column("dep",width=100)
            self.student_table.column("course",width=100)
            self.student_table.column("year",width=100)
            self.student_table.column("sem",width=100)
            self.student_table.column("id",width=100)
            self.student_table.column("name",width=100)
            self.student_table.column("div",width=100)
            self.student_table.column("roll",width=100)
            self.student_table.column("gender",width=100)
            self.student_table.column("dob",width=100)
            self.student_table.column("email",width=100)
            self.student_table.column("phone",width=100)
            self.student_table.column("address",width=100)
            self.student_table.column("faculty",width=100)
            self.student_table.column("photo",width=150)

            self.student_table.pack(fill=BOTH,expand=1)
            self.student_table.bind("<ButtonRelease>",self.get_cursor)
            self.fetch_data()

        #     ==============function declaration============

        #     StringVar()
        def add_data(self):
               if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                       messagebox.showerror("Error","All Fields are required",parent=self.root)
               else:
                   try:
                        conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="sys")
                        my_cursor=conn.cursor()
                        my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

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
                                                                                                        self.var_radio1.get()
                                                                                                ))
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Success","student details has been added successfully",parent=self.root)                                               
                   except Exception as es:
                           messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   

                # ===========fetch data===========
        def fetch_data(self):
                conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="sys")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                data=my_cursor.fetchall()

                if len(data)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in data:
                            self.student_table.insert("",END,values=i)
                        conn.commit()
                conn.close()   
                # ===============get cursor=======
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
                self.var_address.set(data[12]),
                self.var_teacher.set(data[13]),
                self.var_radio1.set(data[14])

        # update function
        def update_data(self):
                if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                        messagebox.showerror("Error","All Fields are required",parent=self.root)
                else:
                    try:    
                        Update=messagebox.askyesno("Update","Do You want to update details",parent=self.root)
                        if Update>0:
                           conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="sys")
                           my_cursor=conn.cursor()
                           my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                           
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get(),
                                                                                                        self.var_std_id.get()
                                                                                                        ))
                        else:
                             if not Update:
                                  return
                        messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                    except Exception as es:
                         messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
        # delete function
        def delete_data(self):
                if self.var_std_id.get()=="":
                        messagebox.showerror("Error","student id must be required",parent=self.root)
                else:
                        try:
                                delete=messagebox.askyesno("Student Delete page","Do you want to delete the record?",parent=self.root)
                                if delete>0:
                                        conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="sys")
                                        my_cursor=conn.cursor()
                                        sql="delete from student where student_id=%s"
                                        val=(self.var_std_id.get(),)
                                        my_cursor.execute(sql,val)
                                else:
                                        if not delete:
                                                return    
                                conn.commit()
                                self.fetch_data()
                                conn.close()
                                messagebox.showinfo("Delete","Deletion Successful",parent=self.root)
                        except Exception as es:
                          messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
        #reset function
        def reset_data(self):
                self.var_dep.set("Select Department")
                self.var_course.set("Select Course")
                self.var_year.set("Select year")
                self.var_semester.set("Select semester")
                self.var_std_id.set("")
                self.var_std_name.set("")
                self.var_div.set("Select division")
                self.var_roll.set("")
                self.var_gender.set("Select gender")
                self.var_dob.set("")
                self.var_email.set("")
                self.var_phone.set("")
                self.var_address.set("")
                self.var_teacher.set("")
                self.var_radio1.set("")

        #    ==========generate dataset==========

        def generate_dataset(self):
                if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                        messagebox.showerror("Error","All Fields are required",parent=self.root)
                else:
                    try:    
                        conn=mysql.connector.connect(host="localhost",username="root",password="0000",database="sys")
                        my_cursor=conn.cursor()
                        my_cursor.execute("select * from student")
                        myresult=my_cursor.fetchall()
                        id=0
                        for x in myresult:
                                id+=1
                        my_cursor.execute("update student set dep=%s,course=%s,year=%s,semester=%s,name=%s,division=%s,roll=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,teacher=%s,photosample=%s where student_id=%s",(
                           
                                                                                                        self.var_dep.get(),
                                                                                                        self.var_course.get(),
                                                                                                        self.var_year.get(),
                                                                                                        self.var_semester.get(),
                                                                                                        self.var_std_name.get(),
                                                                                                        self.var_div.get(),
                                                                                                        self.var_roll.get(),
                                                                                                        self.var_gender.get(),
                                                                                                        self.var_dob.get(),
                                                                                                        self.var_email.get(),
                                                                                                        self.var_phone.get(),
                                                                                                        self.var_address.get(),
                                                                                                        self.var_teacher.get(),
                                                                                                        self.var_radio1.get(),
                                                                                                        self.var_std_id.get()==id+1
                                                                                                ))
                        conn.commit()
                        self.fetch_data()
                        self.reset_data()
                        conn.close()

                        # =======Load predefined data on face frontals from OPENCV=====

                        face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                        def face_cropped(img):
                                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                                faces=face_classifier.detectMultiScale(gray,1.3,5)
                                # scaling factor=1.3
                                # minimum neighbor= 5
                                

                                for (x,y,w,h) in faces:
                                        face_cropped=img[y:y+h,x:x+w]
                                        return face_cropped

                        cap=cv2.VideoCapture(0)
                        img_id=0
                        while True:
                                ret,my_frame=cap.read()
                                if face_cropped(my_frame) is not None:
                                        img_id+=1
                                        face=cv2.resize(face_cropped(my_frame),(450,450))
                                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                                        cv2.imwrite(file_name_path,face)
                                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                                        cv2.imshow("cropped face",face)

                                if cv2.waitKey(1)==13 or int(img_id)==100:
                                        break
                        cap.release()
                        cv2.destroyAllWindows()
                        messagebox.showinfo("Result","Generating data sets complted!!!")
                    except Exception as es:
                        messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root) 




if __name__=="__main__":
        root=Tk()
        obj=student(root)
        root.mainloop()
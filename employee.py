from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox

class Employee:
    def __init__(self,root):
       self.root=root  
       self.root.geometry("1530x790+0+0")
       self.root.title("Employee Management System")

       #variables
       self.var_dep=StringVar()
       self.var_name=StringVar()
       self.var_designation=StringVar()
       self.var_email=StringVar()
       self.var_address=StringVar()
       self.var_married=StringVar()
       self.var_dob=StringVar()
       self.var_doj=StringVar()
       self.var_idproofcomb=StringVar()
       self.var_idproof=StringVar()
       self.var_gender=StringVar()
       self.var_Phone=StringVar()
       self.var_country=StringVar()
       self.var_salary=StringVar()



       lbl_title=Label(self.root,text="VENAY'S EMPLOYEE MANGEMENT SYSTEM",font=("times new roman",37,"bold"),fg="black",bg="white")
       lbl_title.place(x=0,y=0,width=1530,height=50)

       #logo
       img_logo=Image.open("project_image/myimage.JPG")
       img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
       self.photo_logo=ImageTk.PhotoImage(img_logo)

       self.logo=Label(self.root,image=self.photo_logo)
       self.logo.place(x=270,y=0,width=50,height=50)

       #frame
       img_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
       img_frame.place(x=0,y=50,width=1530,height=160)

       #1 image

       img1=Image.open("project_image/img1.jpg")
       img1=img1.resize((540,160),Image.ANTIALIAS)
       self.photo1=ImageTk.PhotoImage(img1)

       self.img_1=Label(img_frame,image=self.photo1)
       self.img_1.place(x=0,y=0,width=540,height=160)

       #2 image 
       img_2=Image.open("project_image/img2.jpg")
       img_2=img_2.resize((540,160),Image.ANTIALIAS)
       self.photo2=ImageTk.PhotoImage(img_2)

       self.img_2=Label(img_frame,image=self.photo2)
       self.img_2.place(x=540,y=0,width=540,height=160)

       #3 image 
       img_3=Image.open("project_image/img3.jpg")
       img_3=img_3.resize((540,160),Image.ANTIALIAS)
       self.photo3=ImageTk.PhotoImage(img_3)

       self.img_3=Label(img_frame,image=self.photo3)
       self.img_3.place(x=1000,y=0,width=540,height=160)

       #main frame
       main_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
       main_frame.place(x=10,y=220,width=1500,height=560)
        #upper frame 
       upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Employee Information",font=('times new roman',17,'bold'),fg='red')
       upper_frame.place(x=10,y=10,width=1480,height=270)

       #labels and entry fields
       lbl_dep=Label(upper_frame,text="Department:",font=('arial',17,'bold'),bg='white')
       lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

       combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',17,'bold'),width=19,state="readonly")
       combo_dep['value']=("select Department",'HR','software Engineer','manager')
       combo_dep.current(0)
       combo_dep.grid(row=0,column=1,padx=2,pady=7,sticky=W)
        # Name
       lbl_Name=Label(upper_frame,text="Name:",font=('arial',17,'bold'),bg='white')
       lbl_Name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

       txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',16,'bold'))
       txt_Name.grid(row=0,column=3,padx=2,pady=7)

       #lbl_designation
       lbl_Designation=Label(upper_frame,font=('arial',17,'bold'),text="Designation:",bg='white')
       lbl_Designation.grid(row=1,column=0,padx=2,pady=7,sticky=W)

       txt_Designation=ttk.Entry(upper_frame,textvariable=self.var_designation,width=22,font=('arial',16,'bold'))
       txt_Designation.grid(row=1,column=1,padx=2,pady=7)

       # email
       lbl_email=Label(upper_frame,text="E-mail:",font=('arial',17,'bold'),bg='white')
       lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

       txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('arial',16,'bold'))
       txt_email.grid(row=1,column=3,padx=2,pady=7)

       #Address
       lbl_Address=Label(upper_frame,text="Address:",font=('arial',17,'bold'),bg='white')
       lbl_Address.grid(row=2,column=0,padx=2,pady=7,sticky=W)

       txt_Address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',16,'bold'))
       txt_Address.grid(row=2,column=1,padx=2,pady=7)

       #Married
       lbl_Married=Label(upper_frame,text="Married status:",font=('arial',17,'bold'),bg='white')
       lbl_Married.grid(row=2,column=2,padx=2,pady=7,sticky=W)

       com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('arial',17,'bold'),width=19,state="readonly")
       com_txt_married['value']=("",'Married','Unmarried')
       com_txt_married.current(0)
       com_txt_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)

       #Dob
       lbl_Dob=Label(upper_frame,text="DOB:",font=('arial',17,'bold'),bg='white')
       lbl_Dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

       txt_Dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('arial',16,'bold'))
       txt_Dob.grid(row=3,column=1,padx=2,pady=7)

       #Doj
       lbl_Doj=Label(upper_frame,text="DOJ:",font=('arial',17,'bold'),bg='white')
       lbl_Doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

       txt_Doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('arial',16,'bold'))
       txt_Doj.grid(row=3,column=3,padx=2,pady=7)

       #Id proof
       com_txt_Proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font=('arial',17,'bold'),width=18,state="readonly")
       com_txt_Proof['value']=("select ID proof",'PANCARD','AADHAR CARD','DRIVING LICENCE','PASSPORT')
       com_txt_Proof.current(0)
       com_txt_Proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)
       
       txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("arial",16,"bold"))
       txt_proof.grid(row=4,column=1,padx=2,pady=7)

       #Gender
       lbl_gender=Label(upper_frame,text="Gender:",font=('arial',17,'bold'),bg='white')
       lbl_gender.grid(row=4,column=2,padx=2,sticky=W)

       com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',17,'bold'),width=19,state="readonly")
       com_txt_gender['value']=("","Male",'Female','Other')
       com_txt_gender.current(0)
       com_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W)



       #phone
       lbl_phone=Label(upper_frame,text="Phone:",font=('arial',17,'bold'),bg='white')
       lbl_phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)

       txt_phone=ttk.Entry(upper_frame,textvariable=self.var_Phone,width=22,font=('arial',16,'bold'))
       txt_phone.grid(row=0,column=5,padx=2,pady=7,sticky=W)

       

       #Country
       lbl_country=Label(upper_frame,text="country:",font=('arial',17,'bold'),bg='white')
       lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)

       txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial',16,'bold'))
       txt_country.grid(row=1,column=5,padx=2,pady=7,sticky=W)

       

       #ctc
       lbl_salary=Label(upper_frame,text="salary(CTC):",font=('arial',17,'bold'),bg='white')
       lbl_salary.grid(row=2,column=4,padx=2,pady=7,sticky=W)

       txt_salary=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',16,'bold'))
       txt_salary.grid(row=2,column=5,padx=2,pady=7,sticky=W)

      

       #Button frame 
       button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='black')
       button_frame.place(x=1190,y=10,width=160,height=180)

       btn_add=Button(button_frame,text="Save",command=self.add_data,font=('arial',18,'bold'),width=11,fg="black")
       btn_add.grid(row=0,column=0,padx=0,pady=5)

       btn_update=Button(button_frame,text="Update",command=self.update_data,font=('arial',18,'bold'),width=11,bg="blue",fg="black")
       btn_update.grid(row=1,column=0,padx=0,pady=5)

       btn_delete=Button(button_frame,text="Delete",command=self.delete_data,font=('arial',18,'bold'),width=11,bg="blue",fg="black")
       btn_delete.grid(row=2,column=0,padx=0,pady=5)

       btn_clear=Button(button_frame,text="Clear",command=self.reset_data,font=('arial',18,'bold'),width=11,bg="blue",fg="black")
       btn_clear.grid(row=3,column=0,padx=0,pady=5)

        #down frame
       down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text="Employee Information table",font=('times new roman',17,'bold'),fg='red')
       down_frame.place(x=10,y=280,width=1480,height=270)

        #search frame 
       Search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg="white",text="Search employee information",font=('times new roman',17,'bold'),fg='red')
       Search_frame.place(x=0,y=0,width=1470,height=60)

       search_by=Label(Search_frame,font=('arial',17,'bold'),text="Search by:",bg="red",fg="white")
       search_by.grid(row=0,column=0,sticky=W,padx=5)
       #search

       self.var_com_search=StringVar()
       com_txt_search=ttk.Combobox(Search_frame,textvariable=self.var_com_search,font=('arial',17,'bold'),width=19,state="readonly")
       com_txt_search['value']=("Select option",'Phone','Id-proof')
       com_txt_search.current(0)
       com_txt_search.grid(row=0,column=1,padx=5,sticky=W)

       self.var_com_search=StringVar()
       txt_search=ttk.Entry(Search_frame,width=22,font=('arial',16,'bold'))
       txt_search.grid(row=0,column=2,padx=5) 

       btn_search=Button(Search_frame,text="Search",command=self.search_data,font=('arial',18,'bold'),width=11,bg="blue",fg="black")
       btn_search.grid(row=0,column=3,padx=5)

       btn_ShowAll=Button(Search_frame,text="Show All",command=self.fetch_data,font=('arial',18,'bold'),width=11,bg="blue",fg="black")
       btn_ShowAll.grid(row=0,column=4,padx=5)

   # ______________________ Employee table___________________
       #table frame
       table_frame=Frame(down_frame,bd=3,relief=RIDGE,bg="white")
       table_frame.place(x=0,y=60,width=1470,height=170)

       scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

       self.employee_table=ttk.Treeview(table_frame,column=("dep","name","degi","email","address","married","dob","doj","idproofcomb","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)

       scroll_x.config(command=self.employee_table.xview)
       scroll_y.config(command=self.employee_table.yview)

       self.employee_table.heading("dep",text="Department")
       self.employee_table.heading("name",text="Name")
       self.employee_table.heading("degi",text="Designation")
       self.employee_table.heading("email",text="E-mail")
       self.employee_table.heading("address",text="Address")
       self.employee_table.heading("married",text="Marial status")
       self.employee_table.heading("dob",text="DOB")
       self.employee_table.heading("doj",text="DOJ")
       self.employee_table.heading("idproofcomb",text="ID Type")
       self.employee_table.heading("idproof",text="id Proof")
       self.employee_table.heading("gender",text="Gender")
       self.employee_table.heading("phone",text="phone")
       self.employee_table.heading("country",text="Country")
       self.employee_table.heading("salary",text="Salary")

       self.employee_table["show"]="headings"

       self.employee_table.column("dep",width=100)
       self.employee_table.column("name",width=100)
       self.employee_table.column("degi",width=100)
       self.employee_table.column("email",width=100)
       self.employee_table.column("address",width=100)
       self.employee_table.column("married",width=100)
       self.employee_table.column("dob",width=100)
       self.employee_table.column("doj",width=100)
       self.employee_table.column("idproofcomb",width=100)
       self.employee_table.column("idproof",width=100)
       self.employee_table.column("gender",width=100)
       self.employee_table.column("phone",width=100)
       self.employee_table.column("country",width=100)
       self.employee_table.column("salary",width=120)
       

       self.employee_table.pack(fill=BOTH,expand=1)
       self.employee_table.bind("<ButtonRelease>",self.get_cursor)
       self.fetch_data()

       # ______________________________function declations_______________________________

    def add_data(self):  
        if self.var_dep.get()=="" or self.var_email.get()=="":
           messagebox.showerror("error","All fields are required")
        else:
             try:
              conn=mysql.connector.connect(host="localhost",user="root",password="ilove@!c.s",database="mydata")
              my_cursor=conn.cursor()
              my_cursor.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_designation.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_married.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_doj.get(),
                                                                                                            self.var_idproofcomb.get(),
                                                                                                            self.var_idproof.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_Phone.get(),
                                                                                                            self.var_country.get(),
                                                                                                            self.var_salary.get()
                 


                                                                                                             ))
              conn.commit()
              self.fetch_data()
              conn.close()
              messagebox.showinfo("yeah!! success","Employee has been added!",parent=self.root)
             except Exception as es:
                messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root)

      #fetch data
    def fetch_data(self):
         conn=mysql.connector.connect(host="localhost",user="root",password="ilove@!c.s",database="mydata")
         my_cursor=conn.cursor()
         my_cursor.execute("select * from Employee")
         data=my_cursor.fetchall()
         if len(data)!=0:
              self.employee_table.delete(*self.employee_table.get_children())
              for i in data:
                  self.employee_table.insert("",END,values=i)
         conn.commit()
         conn.close()       

         # get cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content["values"]


        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_Phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
           messagebox.showerror("error","All fields are required")
        else:
            try:
              
                update=messagebox.askyesno("update","are you sure to add employee data")
                if update>0:
                 conn=mysql.connector.connect(host="localhost",user="root",password="ilove@!c.s",database="mydata")
                 my_cursor=conn.cursor()
                 my_cursor.execute("update Employee set Department=%s, Name=%s, Designation=%s, Email=%s, Address=%s, Married_status=%s, DOB=%s, DOJ=%s, id_proof_type=%s, Gender=%s, Phone=%s, Country=%s, Salary=%s where id_proof=%s",(

                                                                                                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                                                                                                        self.var_name.get(),
                                                                                                                                                                                                                                        self.var_designation.get(),
                                                                                                                                                                                                                                        self.var_email.get(),
                                                                                                                                                                                                                                        self.var_address.get(),
                                                                                                                                                                                                                                        self.var_married.get(),
                                                                                                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                                                                                                        self.var_doj.get(),
                                                                                                                                                                                                                                        self.var_idproofcomb.get(),
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                                                                                                        self.var_Phone.get(),
                                                                                                                                                                                                                                        self.var_country.get(),
                                                                                                                                                                                                                                        self.var_salary.get(),
                                                                                                                                                                                                                                        self.var_idproof.get()
                
                                                                                                                                                                                                                                        ))
                else:
                  if not update:
                    return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","employee sucessfully added",parent=self.root)
            except Exception as es:
                messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root)

    # delete button
    def delete_data(self):
       if self.var_idproof.get()=="":
          messagebox.showerror("error","All the fields are required")
       else:
          try:
            Delete=messagebox.askyesno("update","are you sure to delete employee data")
            if Delete>0:
               conn=mysql.connector.connect(host="localhost",user="root",password="ilove@!c.s",database="mydata")
               my_cursor=conn.cursor() 
               sql="delete from employee where id_proof=%s"
               value=(self.var_idproof.get(),)
               my_cursor.execute(sql,value)
            else:
               if not Delete:
                  return
            conn.commit()
            self.fetch_data()
            conn.close() 
            messagebox.showinfo("Delete","employee sucessfully Deleted",parent=self.root)
          except Exception as es:
            messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root)   

    #reset      
    def reset_data(self):
       self.var_dep.set("Select Department")
       self.var_name.set("")
       self.var_designation.set("")
       self.var_email.set("")
       self.var_address.set("")
       self.var_married.set("Married")
       self.var_dob.set("")
       self.var_doj.set("")
       self.var_idproofcomb.set("Select ID proof")
       self.var_idproof.set("")
       self.var_gender.set("")
       self.var_Phone.set("")
       self.var_country.set("")
       self.var_salary.set("")
    #search 
    def search_data(self):
       if self.var_com_search.get()=="" or self.var_search.get()=="":
          
          messagebox.showerror("error","Please select option")
       else:
         try:
           
               conn=mysql.connector.connect(host="localhost",user="root",password="ilove@!c.s",database="mydata")
               my_cursor=conn.cursor()  
               my_cursor.execute("select * from employee where " +str(self.var_com_search.get())+"LIKE '%"+str(self.var_com_search.get()+"%'"))
               rows=my_cursor.fetchall()
               if len(rows)!=0:
                  self.employee_table.delete(*self.employee_table.get_children())
                  for i in rows:
                     self.employee_table.insert("",END,values=i)
               conn.commit
               conn.close()           
         except Exception as es:
            messagebox.showerror("error",f"Due To:{str(es)}",parent=self.root) 

                

            


              

                 



       
       
        

                   
              
             
           
           
if __name__=="__main__":
  
  root=Tk()
  obj=Employee(root)
  root.mainloop()
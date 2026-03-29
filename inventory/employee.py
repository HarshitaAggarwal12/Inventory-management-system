from tkinter import *
from tkinter import ttk,messagebox
import sqlite3


class employeeclass:
    def __init__(self, window):  # Accepting the Toplevel window from the main GUI
        self.window = window  # Using the passed Toplevel window
        self.window.geometry('1080x530+100+110')  # Set the geometry of the Toplevel window
        self.window.title("Employee Management System")
        self.window.config(padx=10, pady=10, bg="light grey")

        # Example content for Employee window (add more widgets as needed)
        lbl_employee_title = Label(self.window, text="Employee Details",
                                   font=("times new roman", 20, "bold"), bg="blue", fg="white")
        lbl_employee_title.place(x=0, y=80, relwidth=1)

        # ALL  VARIABLES
        self.var_Searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_emp_id = StringVar()
        self.var_genders = StringVar()
        self.var_contact = StringVar()
        self.var_name = StringVar()
        self.var_DOB = StringVar()
        self.var_doj = StringVar()
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_user_type = StringVar()
        self.var_address = StringVar()
        self.var_salary = StringVar()

        # Add more widgets for employee management here if needed

        # Creating the search bar section
        Search_Frame = LabelFrame(self.window, text="Search Employee", font=("arial", 9, "bold"),
                                  bg="white", fg="black", relief=RIDGE)
        Search_Frame.place(x=280, y=5, height=65, width=600)

        cmb_search = ttk.Combobox(Search_Frame, textvariable=self.var_Searchby,
                                  values=("Search","Empid", "Email", "Name", "Contact"), state="readonly", justify=CENTER)
        cmb_search.place(x=10, y=10, width=100, height=30)
        cmb_search.current(0)

        self.search_entry = Entry(Search_Frame, textvariable=self.var_searchtxt, font=("arial", 15),
                                  bg="lightyellow", fg="black", relief=SUNKEN)
        self.search_entry.place(x=150, y=10, width=250, height=30)

        # Search button
        self.search_button = Button(Search_Frame, text="Search", font=("arial", 12, "bold"),
                                    bg="green", fg="black", cursor="hand2", command=self.search)
        self.search_button.place(x=420, y=10, width=150, height=25)

        # inventory labels
        #emp id
        lbl_Empid = Label(self.window, text="Emp ID:", font=("arial", 15), bg="light grey", fg="black")
        lbl_Empid.place(x=100, y=150)
        self.Empid_entry = Entry(self.window, textvariable=self.var_emp_id, font=("arial", 15),
                                 bg="lightyellow", fg="black", relief=SUNKEN)
        self.Empid_entry.place(x=180, y=155, width=200, height=20)

        #gender
        lbl_gender = Label(self.window, text="Gender", font=("arial", 15), bg="light grey", fg="black")
        lbl_gender.place(x=400, y=150)
        cmb_gender = ttk.Combobox(self.window, textvariable=self.var_genders, values=("Search", "Male", "Female", "Other"),
                                  state="readonly", justify=CENTER, font=("arial", 15))
        cmb_gender.place(x=480, y=155, width=200, height=20)

        #contact
        lbl_contact = Label(self.window, text="Contact No.", font=("arial", 15), bg="light grey", fg="black")
        lbl_contact.place(x=700, y=150)
        self.contact_entry = Entry(self.window, textvariable=self.var_contact, font=("arial", 15),
                                 bg="lightyellow", fg="black", relief=SUNKEN)
        self.contact_entry.place(x=820, y=155, width=200, height=20)

        #name
        lbl_name = Label(self.window, text="Name:", font=("arial", 15), bg="light grey", fg="black")
        lbl_name.place(x=100, y=200)
        self.name_entry = Entry(self.window, textvariable=self.var_name, font=("arial", 15),
                                 bg="lightyellow", fg="black", relief=SUNKEN)
        self.name_entry.place(x=180, y=205, width=200, height=20)

        #DOB
        lbl_DOB = Label(self.window, text="D.O.B:", font=("arial", 15), bg="light grey", fg="black")
        lbl_DOB.place(x=400, y=200)
        self.DOB_entry = Entry(self.window, textvariable=self.var_DOB, font=("arial", 15),
                                 bg="lightyellow", fg="black", relief=SUNKEN)
        self.DOB_entry.place(x=480, y=205, width=200, height=20)

        #DOJ
        lbl_doj = Label(self.window, text="D.O.J:", font=("arial", 15), bg="light grey", fg="black")
        lbl_doj.place(x=700, y=200)
        self.doj_entry = Entry(self.window, textvariable=self.var_doj, font=("arial", 15),
                                   bg="lightyellow", fg="black", relief=SUNKEN)
        self.doj_entry.place(x=820, y=205, width=200, height=20)

        # Email
        lbl_email = Label(self.window, text="Email:", font=("arial", 15), bg="light grey", fg="black")
        lbl_email.place(x=100, y=250)
        self.email_entry = Entry(self.window, textvariable=self.var_email, font=("arial", 15),
                                bg="lightyellow", fg="black", relief=SUNKEN)
        self.email_entry.place(x=180, y=255, width=200, height=20)

        # password
        lbl_password = Label(self.window, text="Password:", font=("arial", 13), bg="light grey", fg="black")
        lbl_password.place(x=400, y=250)
        self.password_entry = Entry(self.window, textvariable=self.var_password, font=("arial", 15),
                               bg="lightyellow", fg="black", relief=SUNKEN)
        self.password_entry.place(x=480, y=255, width=200, height=20)

        # user type
        lbl_user = Label(self.window, text="User Type", font=("arial", 15), bg="light grey", fg="black")
        lbl_user.place(x=700, y=250)
        cmb_user = ttk.Combobox(self.window, textvariable=self.var_user_type,
                                  values=("Admin", "Employee"),
                                  state="readonly", justify=CENTER, font=("arial", 15))
        cmb_user.place(x=820, y=255, width=200, height=20)

        # address
        lbl_address = Label(self.window, text="Address:", font=("arial", 12), bg="light grey", fg="black")
        lbl_address.place(x=100, y=300)
        self.address_entry = Entry(self.window, textvariable=self.var_address, font=("arial", 15),
                                bg="lightyellow", fg="black", relief=SUNKEN)
        self.address_entry.place(x=180, y=305, width=300, height=50)

        # salary
        lbl_salary = Label(self.window, text="Salary:", font=("arial", 12), bg="light grey", fg="black")
        lbl_salary.place(x=550, y=305)
        self.salary_entry = Entry(self.window, textvariable=self.var_salary, font=("arial", 15),
                                    bg="lightyellow", fg="black", relief=SUNKEN)
        self.salary_entry.place(x=620, y=305, width=200, height=20)

        #save button
        self.save_button = (Button(self.window,command=self.add, text="SAVE", bg="light blue", font=("arial", 13, "bold"), cursor="hand2")
            .place(x=550, y=335, height=20, width=90))

        #update button
        self.update_button = (Button(self.window,command=self.update, text="UPDATE", bg="light pink", font=("arial", 13, "bold"), cursor="hand2")
            .place(x=650, y=335, height=20, width=90))

        #delete button
        self.delete_button = (Button(self.window,command=self.delete, text="DELETE", bg="beige", font=("arial", 13, "bold"), cursor="hand2")
            .place(x=750, y=335, height=20, width=90))

        #clear button
        self.save_button = (Button(self.window,command=self.clear, text="CLEAR", bg="lavender", font=("arial", 13, "bold"), cursor="hand2")
            .place(x=850, y=335, height=20, width=100))

        #create a frame
        bottom_menu=Frame(self.window,bd=2,relief=RIDGE, bg="white")
        bottom_menu.place(x=30, y=380, height=130, width=1000)

        #scroll bar
        scroll_x=Scrollbar(bottom_menu, orient=HORIZONTAL)
        scroll_y=Scrollbar(bottom_menu, orient=VERTICAL)



        #scroll_x menu
        self.EmployeeTree = ttk.Treeview(bottom_menu, columns=("empid", "name", "email", "gender", "contact", "dob", "doj", "password", "utype", "address", "salary"),
                                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.EmployeeTree.heading("empid", text="EMP ID")
        self.EmployeeTree.heading("name", text="NAME")
        self.EmployeeTree.heading("email", text="EMAIL")
        self.EmployeeTree.heading("gender", text="Gender")
        self.EmployeeTree.heading("contact", text="Contact")
        self.EmployeeTree.heading("dob", text="DOB")
        self.EmployeeTree.heading("doj", text="DOJ")
        self.EmployeeTree.heading("password", text="Password")
        self.EmployeeTree.heading("utype", text="User Type")
        self.EmployeeTree.heading("address", text="Address")
        self.EmployeeTree.heading("salary", text="Salary")

        # scroll bar calling
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.EmployeeTree.xview)
        scroll_y.config(command=self.EmployeeTree.yview)

        self.EmployeeTree["show"] = "headings"

        self.EmployeeTree.column("empid", width=80)
        self.EmployeeTree.column("name", width=100)
        self.EmployeeTree.column("email", width=110)
        self.EmployeeTree.column("gender", width=80)
        self.EmployeeTree.column("contact", width=90)
        self.EmployeeTree.column("dob", width=90)
        self.EmployeeTree.column("doj", width=90)
        self.EmployeeTree.column("password", width=90)
        self.EmployeeTree.column("utype", width=100)
        self.EmployeeTree.column("address", width=120)
        self.EmployeeTree.column("salary", width=100)

        self.EmployeeTree.pack(fill=BOTH, expand=True)
        self.EmployeeTree.bind("<ButtonRelease-1>",self.get_data)


        self.show()

#************************************************************************
#save button input
    def add(self):
        con=sqlite3.connect(database=r'ed.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.window)
            else:
                cur.execute("Select * from employee where empid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error","Employee ID Already Exists",parent=self.window)
                else:
                    cur.execute("Insert into employee(empid, name, email, gender, contact, dob, doj, password, utype, address, salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_genders.get(),
                        self.var_contact.get(),
                        self.var_DOB.get(),
                        self.var_doj.get(),
                        self.var_password.get(),
                        self.var_user_type.get(),
                        self.var_address.get(),
                        self.var_salary.get(),
                    ))

                    con.commit()
                    messagebox.showinfo("Success","Employee successfully added",parent=self.window)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")

    def show(self):
        con = sqlite3.connect(database=r'ed.db')
        cur = con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmployeeTree.delete(*self.EmployeeTree.get_children())
            for row in rows:
                self.EmployeeTree.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")

    def get_data(self,ev):
        f=self.EmployeeTree.focus()
        content=(self.EmployeeTree.item(f))
        row=content['values']
        #print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_genders.set(row[3])
        self.var_contact.set(row[4])
        self.var_DOB.set(row[5])
        self.var_doj.set(row[6])
        self.var_password.set(row[7])
        self.var_user_type.set(row[8])
        self.var_address.set(row[9])
        self.var_salary.set(row[10])


        #update button input
    def update(self):
        con=sqlite3.connect(database=r'ed.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.window)
            else:
                cur.execute("Select * from employee where empid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid employee id",parent=self.window)
                else:
                    cur.execute("Update employee set name=?, email=?, gender=?, contact=?, dob=?, doj=?, password=?, utype=?, address=?, salary=? where empid=?",(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_genders.get(),
                        self.var_contact.get(),
                        self.var_DOB.get(),
                        self.var_doj.get(),
                        self.var_password.get(),
                        self.var_user_type.get(),
                        self.var_address.get(),
                        self.var_salary.get(),
                        self.var_emp_id.get(),
                    ))

                    con.commit()
                    messagebox.showinfo("Success","Employee successfully updated",parent=self.window)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")

            #delete button input

    def delete(self):
        con = sqlite3.connect(database=r'ed.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get() == "":
                messagebox.showerror("Error","Employee ID Must be required",parent=self.window)
            else:
                cur.execute("Select * from employee where empid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid employee id",parent=self.window)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.window)
                    if op==True:
                        cur.execute("Delete from employee where empid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Employee successfully deleted",parent=self.window)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")

    #clear button input
    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_genders.set("Select")
        self.var_contact.set("")
        self.var_DOB.set("")
        self.var_doj.set("")
        self.var_password.set("")
        self.var_user_type.set("")
        self.var_address.set("")
        self.var_salary.set("")
        self.show()


    def search(self):
        con = sqlite3.connect(database=r'ed.db')
        cur = con.cursor()
        try:
            if self.var_Searchby.get()=="Select":
                messagebox.showerror("Error","Please select an option",parent=self.window)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Please enter a search term",parent=self.window)
            else:
                query = f"SELECT * FROM employee WHERE {self.var_Searchby.get()} LIKE ?"
                cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))

                rows = cur.fetchall()
                if len(rows)!=0:
                    self.EmployeeTree.delete(*self.EmployeeTree.get_children())
                    for row in rows:
                        self.EmployeeTree.insert("", END, values=row)
                else:
                    messagebox.showerror("Error","No records found!!",parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")



# No need for Tk() here as this will be called from the main GUI
if __name__ == "__main__":
    window = Tk()
    obj = employeeclass(window)
    window.mainloop()
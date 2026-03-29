from tkinter import *
from tkinter import ttk,messagebox
import sqlite3


class supplyclass:
    def __init__(self, window):  # Accepting the Toplevel window from the main GUI
        self.window = window  # Using the passed Toplevel window
        self.window.geometry('1080x530+100+110')  # Set the geometry of the Toplevel window
        self.window.title("Supply Details")
        self.window.config(padx=10, pady=10, bg="light grey")

        # Example content for Employee window (add more widgets as needed)
        lbl_supply_title = Label(self.window, text="Manage Supply Details",
                                   font=("times new roman", 20, "bold"), bg="blue", fg="white")
        lbl_supply_title.place(x=0, y=0, relwidth=1)

        # ALL  VARIABLES
        self.var_Searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.var_sup_id =StringVar()
        self.var_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_des = StringVar()


        # Add more widgets for employee management here if needed

        #Creating the search bar section
        Search_Frame = LabelFrame(self.window, font=("arial", 5, "bold"),
                                  bg="white", fg="black", relief=RIDGE)
        Search_Frame.place(x=580, y=50, height=50, width=480)

        lbl_search = Label(self.window, text="Invoice No.", font=("arial", 13), fg="black")
        lbl_search.place(x=600, y=65, width=90, height=20)
        #lbl_search.current(0)

        self.search_entry = Entry(Search_Frame, textvariable=self.var_searchtxt, font=("arial", 15),
                                  bg="lightyellow", fg="black", relief=SUNKEN)
        self.search_entry.place(x=110, y=10, width=250, height=30)

        #Search button
        self.search_button = Button(Search_Frame, text="Search", font=("arial", 12, "bold"),
                                    bg="green", fg="black", cursor="hand2",command=self.search)
        self.search_button.place(x=370, y=12, width=100, height=25)

        # supplies labels
        #sup id
        lbl_sup = Label(self.window, text="Supplier id :", font=("arial", 15), bg="light grey", fg="black")
        lbl_sup.place(x=40, y=50)
        self.sup_entry = Entry(self.window, textvariable=self.var_sup_id, font=("arial", 15),
                                   bg="lightyellow", fg="black", relief=SUNKEN)
        self.sup_entry.place(x=205, y=55, width=200, height=20)

        #invoice
        lbl_invoice = Label(self.window, text="Invoice No. :", font=("arial", 15), bg="light grey", fg="black")
        lbl_invoice.place(x=40, y=100)
        self.invoice_entry = Entry(self.window, textvariable=self.var_invoice, font=("arial", 15),
                                 bg="lightyellow", fg="black", relief=SUNKEN)
        self.invoice_entry.place(x=205, y=105, width=200, height=20)


        #name
        lbl_name = Label(self.window, text="Supplier Name:", font=("arial", 15), bg="light grey", fg="black")
        lbl_name.place(x=40, y=150)
        self.name_entry = Entry(self.window, textvariable=self.var_name, font=("arial", 15),
                                 bg="lightyellow", fg="black", relief=SUNKEN)
        self.name_entry.place(x=205, y=155, width=200, height=20)


#        #contact
        lbl_contact = Label(self.window, text="Contact:", font=("arial", 15), bg="light grey", fg="black")
        lbl_contact.place(x=40, y=200)
        self.contact_entry = Entry(self.window, textvariable=self.var_contact, font=("arial", 15),
                                   bg="lightyellow", fg="black", relief=SUNKEN)
        self.contact_entry.place(x=205, y=205, width=200, height=20)


        # address
        lbl_address = Label(self.window, text="Description:", font=("arial", 15), bg="light grey", fg="black")
        lbl_address.place(x=40, y=250)
        self.address_entry = Entry(self.window, textvariable=self.var_des, font=("arial", 15),
                                bg="lightyellow", fg="black", relief=SUNKEN)
        self.address_entry.place(x=205, y=255, width=350, height=150)

        #save button
        self.save_button = (Button(self.window,command=self.add, text="SAVE", bg="light blue", font=("arial", 13, "bold"), cursor="hand2")
            .place(x=155, y=455, height=20, width=90))

        #update button
        self.update_button = (Button(self.window,command=self.update, text="UPDATE", bg="light pink", font=("arial", 13, "bold"), cursor="hand2")
            .place(x=255, y=455, height=20, width=90))

        #delete button
        self.delete_button = (Button(self.window,command=self.delete, text="DELETE", bg="beige", font=("arial", 13, "bold"), cursor="hand2")
            .place(x=355, y=455, height=20, width=90))

        #clear button
        self.clear_button = (Button(self.window,command=self.clear, text="CLEAR", bg="lavender", font=("arial", 13, "bold"), cursor="hand2")
            .place(x=455, y=455, height=20, width=100))

        #create a frame
        side_menu=Frame(self.window,bd=2,relief=RIDGE, bg="white")
        side_menu.place(x=580, y=120, height=390, width=480)

        #scroll bar
        scroll_x=Scrollbar(side_menu, orient=HORIZONTAL)
        scroll_y=Scrollbar(side_menu, orient=VERTICAL)

#
#
        #scroll_x menu
        self.SupplyTree = ttk.Treeview(side_menu, columns=("sup_id","InvoiceNo","Name","Contact","Description"),
                                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.SupplyTree.heading("sup_id", text="Sup ID")
        self.SupplyTree.heading("InvoiceNo", text="Invoice_ID")
        self.SupplyTree.heading("Name", text="Name")
        self.SupplyTree.heading("Contact", text="Contact")
        self.SupplyTree.heading("Description", text="Description")

        # scroll bar calling
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.SupplyTree.xview)
        scroll_y.config(command=self.SupplyTree.yview)

        self.SupplyTree["show"] = "headings"

        self.SupplyTree.column("sup_id", width=80)
        self.SupplyTree.column("InvoiceNo", width=100)
        self.SupplyTree.column("Name", width=110)
        self.SupplyTree.column("Contact", width=80)
        self.SupplyTree.column("Description", width=90)

        self.SupplyTree.pack(fill=BOTH, expand=True)
        self.SupplyTree.bind("<ButtonRelease-1>",self.get_data)


        self.show()
#************************************************************************
#save button input
    def add(self):
        con=sqlite3.connect(database=r'supplier.db')
        cur=con.cursor()
        try:
            if self.var_sup_id.get() == "":
                messagebox.showerror("Error","Supplier ID Must be required",parent=self.window)
            else:
                cur.execute("Select * from supply where sup_id=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","Supplier ID Already Exists",parent=self.window)
                else:
                    # Get the maximum Invoice_no and increment it
                    cur.execute("SELECT MAX(InvoiceNo) FROM supply")
                    max_invoice = cur.fetchone()[0]

                    # If no invoice exists yet, start from 1
                    if max_invoice is None:
                        new_invoice_no = 1
                    else:
                        new_invoice_no = int(max_invoice) + 1

                    self.var_invoice.set(new_invoice_no)  # Set the incremented invoice number to the variable
                    cur.execute("Insert into supply(sup_id,InvoiceNo,Name,Contact,Description) values(?,?,?,?,?)",(
                    self.var_sup_id.get(),
                    self.var_invoice.get(),
                    self.var_name.get(),
                    self.var_contact.get(),
                    self.var_des.get(),
                    ))

                    con.commit()
                    messagebox.showinfo("Success","Supplier successfully added",parent=self.window)
                    self.show()
                    
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")

    def show(self):
        con = sqlite3.connect(database=r'supplier.db')
        cur = con.cursor()
        try:
            cur.execute("select * from supply")
            rows=cur.fetchall()
            self.SupplyTree.delete(*self.SupplyTree.get_children())
            for row in rows:
                self.SupplyTree.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")

    def get_data(self,ev):
        f=self.SupplyTree.focus()
        content=(self.SupplyTree.item(f))
        row=content['values']
        #print(row)
        self.var_sup_id.set(row[0])
        self.var_invoice.set(row[1])
        self.var_name.set(row[2])
        self.var_contact.set(row[3])
        self.var_des.set(row[4])



        #update button input
    def update(self):
        con=sqlite3.connect(database=r'supplier.db')
        cur=con.cursor()
        try:
            if self.var_sup_id.get() == "":
                messagebox.showerror("Error","Supplier ID Must be required",parent=self.window)
            else:
                cur.execute("Select * from supply where sup_id=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid supplier id",parent=self.window)
                else:
                    cur.execute("Update supply set InvoiceNo=?,Name=?,Contact=?,Description=? where sup_id=?",(
                        self.var_sup_id.get(),
                        self.var_invoice.get(),
                        self.var_name.get(),
                        self.var_contact.get(),
                        self.var_des.get(),
                    ))

                    con.commit()
                    messagebox.showinfo("Success","Supplies successfully updated",parent=self.window)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")

            #delete button input

    def delete(self):
        con = sqlite3.connect(database=r'supplier.db')
        cur = con.cursor()
        try:
            if self.var_sup_id.get() == "":
                messagebox.showerror("Error","Supplier ID Must be required",parent=self.window)
            else:
                cur.execute("Select * from supply where sup_id=?",(self.var_sup_id.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid supplier id",parent=self.window)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.window)
                    if op==True:
                        cur.execute("Delete from supply where sup_id=?",(self.var_sup_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","supplier successfully deleted",parent=self.window)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")

    #clear button input
    def clear(self):
        self.var_sup_id.set("")
        self.var_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.var_des.set("")
        self.show()

    #search button commands
    def search(self):
        con = sqlite3.connect(database=r'supplier.db')
        cur = con.cursor()
        try:
            if self.var_Searchby.get()=="Select":
                messagebox.showerror("Error","Please select an option",parent=self.window)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Please enter a search term",parent=self.window)
            else:
                query = f"SELECT * FROM supply WHERE sup_id LIKE ?"
                cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))

                rows = cur.fetchall()
                if len(rows)!=0:
                    self.SupplyTree.delete(*self.SupplyTree.get_children())
                    for row in rows:
                        self.SupplyTree.insert("", END, values=row)
                else:
                    messagebox.showerror("Error","No records found!!",parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")



# No need for Tk() here as this will be called from the main GUI
if __name__ == "__main__":
    window = Tk()
    obj = supplyclass(window)
    window.mainloop()
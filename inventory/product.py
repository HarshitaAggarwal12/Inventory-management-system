from itertools import product
from tkinter import *
from tkinter import ttk,messagebox
import sqlite3



class productclass:
    def __init__(self, window):  # Accepting the Toplevel window from the main GUI
        self.window = window  # Using the passed Toplevel window
        self.window.geometry('1080x530+100+110')  # Set the geometry of the Toplevel window
        self.window.title("Employee Management System")
        self.window.config(padx=10, pady=10, bg="white")

        # Example content for Employee window (add more widgets as needed)


        # ALL  VARIABLES
        self.var_Searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_product_id = StringVar()
        self.var_category = StringVar()
        self.var_supplier = StringVar()
        self.var_name = StringVar()
        self.var_price = StringVar()
        self.var_qty = StringVar()
        self.var_status = StringVar()




        # Creating the search bar section
        Search_Frame = LabelFrame(self.window, text="Search Product", font=("arial", 12, "bold"),
                                  bg="lightgrey", fg="black", relief=RIDGE)
        Search_Frame.place(x=510, y=5, height=70, width=550)

        cmb_search = ttk.Combobox(Search_Frame, textvariable=self.var_Searchby,
                                  values=("Search","product_id","Category", "Supplier", "Name"), state="readonly", justify=CENTER)
        cmb_search.place(x=20, y=5, width=100, height=30)
        cmb_search.current(0)

        self.search_entry = Entry(Search_Frame, textvariable=self.var_searchtxt, font=("arial", 20),
                                  bg="lightyellow", fg="black", relief=SUNKEN)
        self.search_entry.place(x=130, y=5, width=250, height=30)

        # Search button
        self.search_button = Button(Search_Frame,command=self.search, text="Search", font=("arial", 15, "bold"),
                                    bg="green", fg="black", cursor="hand2")
        self.search_button.place(x=400, y=5, width=130, height=30)


        #right menu
        # create a frame
        right_menu = Frame(self.window, bd=2, relief=RIDGE, bg="light grey")
        right_menu.place(x=5, y=5, height=495, width=485)

        #product title
        lbl_product_title = Label(right_menu, text="Manage Product Details",
                                   font=("times new roman", 20, "bold"), bg="blue", fg="white")
        lbl_product_title.pack(side=TOP,fill=X)




        # inventory labels
        #category
        lbl_category = Label(right_menu, text="Category ", font=("arial", 15), bg="light grey", fg="black")
        lbl_category.place(x=25, y=75)
        self.cmb_category = ttk.Combobox(right_menu, textvariable=self.var_category,values=( "Other"),
                                        state="readonly", justify=CENTER, font=("arial", 15))
        self.cmb_category.place(x=155, y=82, width=200, height=30)

        #supplier
        lbl_supplier = Label(right_menu, text="Supplier ", font=("arial", 15), bg="light grey", fg="black")
        lbl_supplier.place(x=25, y=135)
        self.cmb_supplier = ttk.Combobox(right_menu, textvariable=self.var_supplier, values=( "Other"),
                                  state="readonly", justify=CENTER, font=("arial", 15))
        self.cmb_supplier.place(x=155, y=135, width=200, height=30)

#
        #name
        lbl_name = Label(right_menu, text="Name", font=("arial", 15), bg="light grey", fg="black")
        lbl_name.place(x=25, y=185)
        self.name_entry = Entry(right_menu, textvariable=self.var_name, font=("arial", 15),
                                 bg="lightyellow", fg="black", relief=SUNKEN)
        self.name_entry.place(x=155, y=190, width=200, height=30)

        #price
        lbl_price = Label(right_menu, text="Price", font=("arial", 15), bg="light grey", fg="black")
        lbl_price.place(x=25, y=240)
        self.price_entry = Entry(right_menu, textvariable=self.var_price, font=("arial", 15),
                                 bg="lightyellow", fg="black", relief=SUNKEN)
        self.price_entry.place(x=155, y=240, width=200, height=30)

        #quantity
        lbl_qty = Label(right_menu, text="Quantity", font=("arial", 15), bg="light grey", fg="black")
        lbl_qty.place(x=25, y=295)
        self.qty_entry = Entry(right_menu, textvariable=self.var_qty, font=("arial", 15),
                                   bg="lightyellow", fg="black", relief=SUNKEN)
        self.qty_entry.place(x=155, y=295, width=200, height=30)

        # status
        lbl_status = Label(right_menu, text="Status", font=("arial", 15), bg="light grey", fg="black")
        lbl_status.place(x=25, y=355)
        cmb_status = ttk.Combobox(right_menu, textvariable=self.var_status,values=("Active", "Inactive"),
                                  state="readonly", justify=CENTER, font=("arial", 15))
        cmb_status.place(x=155, y=355, width=200, height=30)


        #save button
        self.save_button = (Button(right_menu,command=self.add, text="SAVE", bg="light blue", font=("arial", 15, "bold"), cursor="hand2")
            .place(x=30, y=430, height=30, width=90))

        #update button
        self.update_button = (Button(right_menu,command=self.update, text="UPDATE", bg="light pink", font=("arial", 15, "bold"), cursor="hand2")
            .place(x=130, y=430, height=30, width=90))

        #delete button
        self.delete_button = (Button(right_menu,command=self.delete, text="DELETE", bg="beige", font=("arial", 15, "bold"), cursor="hand2")
            .place(x=230, y=430, height=30, width=90))

        #clear button
        self.save_button = (Button(right_menu,command=self.clear, text="CLEAR", bg="lavender", font=("arial", 15, "bold"), cursor="hand2")
            .place(x=330, y=430, height=30, width=100))

        #create a frame
        bottom_menu=Frame(self.window,bd=2,relief=RIDGE, bg="light grey")
        bottom_menu.place(x=510, y=80, height=420, width=550)

        #scroll bar
        scroll_x=Scrollbar(bottom_menu, orient=HORIZONTAL)
        scroll_y=Scrollbar(bottom_menu, orient=VERTICAL)



        #scroll_x menu
        self.ProductTree = ttk.Treeview(bottom_menu, columns=("Product_id", "Category", "Supplier", "Name", "Price", "Quantity", "Status"),
                                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.ProductTree.heading("Product_id", text="Product_id")
        self.ProductTree.heading("Category", text="Category")
        self.ProductTree.heading("Supplier", text="Supplier")
        self.ProductTree.heading("Name", text="Name")
        self.ProductTree.heading("Price", text="Price")
        self.ProductTree.heading("Quantity", text="Quantity")
        self.ProductTree.heading("Status", text="Status")

        # scroll bar calling
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.ProductTree.xview)
        scroll_y.config(command=self.ProductTree.yview)

        self.ProductTree["show"] = "headings"

        self.ProductTree.column("Product_id", width=80)
        self.ProductTree.column("Category", width=100)
        self.ProductTree.column("Supplier", width=110)
        self.ProductTree.column("Name", width=80)
        self.ProductTree.column("Price", width=90)
        self.ProductTree.column("Quantity", width=90)
        self.ProductTree.column("Status", width=90)


        self.ProductTree.pack(fill=BOTH, expand=True)
        self.ProductTree.bind("<ButtonRelease-1>",self.get_data)
        self.fetchall_cat()
        self.fetchall_sup()
#
        self.show()
#
# #************************************************************************
    #fetching data from supplier and category
    def fetchall_cat(self):
        con = sqlite3.connect(database=r'category.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM category")
            cat=cur.fetchall()
            self.cmb_category['values'] = [row[0] for row in cat]
            #print(cat)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.window)

    
    def fetchall_sup(self):
        con = sqlite3.connect(database=r'supplier.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM supply")
            sup=cur.fetchall()
            self.cmb_supplier['values'] = [row[0] for row in sup]
            #print(sup)

            

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.window)



#save button input
    def add(self):
        con = sqlite3.connect(database=r'product.db')
        cur = con.cursor()
        try:
            # Check if Name is empty
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Name must be required", parent=self.window)
            else:
                # Check if the name already exists
                cur.execute("SELECT * FROM product WHERE Name = ?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Name already exists", parent=self.window)
                else:
                    # Get the maximum productID and increment it
                    cur.execute("SELECT MAX(Product_id) FROM product")
                    max_product = cur.fetchone()[0]
                    
                    # If no product exists yet, start from 1
                    if max_product is None:
                        new_product_no = 1
                    else:
                        new_product_no = int(max_product) + 1
                    
                    self.var_product_id.set(new_product_no)
                    # Insert the new category, Category_id will auto-increment
                    cur.execute("INSERT INTO product (Product_id,Category, Supplier,Name, Price, Quantity, Status) VALUES (?,?,?,?,?,?,?)", (
                        # new_product_id,
                        self.var_product_id.get(),
                        self.var_category.get(),
                        self.var_supplier.get(),
                        self.var_name.get(),
                        self.var_price.get(),
                        self.var_qty.get(),
                        self.var_status.get(),
                    ))

                    # Commit the changes
                    con.commit()
                    messagebox.showinfo("Success", "Entry successfully added", parent=self.window)

                    # # Refresh the view (optional)
                    self.show()

                    


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.window)

    def show(self):
        con = sqlite3.connect(database=r'product.db')
        cur = con.cursor()
        try:
            cur.execute("select * from product")
            rows=cur.fetchall()
            self.ProductTree.delete(*self.ProductTree.get_children())
            for row in rows:
                self.ProductTree.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")

    def get_data(self,ev):
        f=self.ProductTree.focus()
        content=(self.ProductTree.item(f))
        row=content['values']
        if row :
            self.var_product_id.set(row[0])
            self.var_category.set(row[1])
            self.var_supplier.set(row[2])
            self.var_name.set(row[3])
            self.var_price.set(row[4])
            self.var_qty.set(row[5])
            self.var_status.set(row[6])



        #update button input
    def update(self):
        con=sqlite3.connect(database=r'product.db')
        cur=con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error","Name Must be required",parent=self.window)
            else:
                cur.execute("Select * from product where Name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Name",parent=self.window)
                else:
                    cur.execute("Update product set Product_id=?,Category=?, Supplier=?, Price=?, Quantity=?, Status=? where Name=?",(
                    self.var_product_id.get(),
                    self.var_category.get(),
                    self.var_supplier.get(),

                    self.var_price.get(),
                    self.var_qty.get(),
                    self.var_status.get(),
                    self.var_name.get(),
                    ))

                    con.commit()
                    messagebox.showinfo("Success","Entry successfully updated",parent=self.window)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to:{str(ex)}")

            #delete button input

    def delete(self):
        con = sqlite3.connect(database=r'product.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error","Name Must be required",parent=self.window)
            else:
                cur.execute("Select * from product where Name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Name",parent=self.window)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.window)
                    if op==True:
                        cur.execute("Delete from product where name=?",(self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Entry successfully deleted",parent=self.window)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")

    #clear button input
    def clear(self):
        self.var_product_id.set(""),
        self.var_category.set("Select"),
        self.var_supplier.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Select"),
        self.show()


    def search(self):
        con = sqlite3.connect(database=r'product.db')
        cur = con.cursor()
        try:
            if self.var_Searchby.get()=="Select":
                messagebox.showerror("Error","Please select an option",parent=self.window)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Please enter a search term",parent=self.window)
            else:
                query = f"SELECT * FROM product WHERE {self.var_Searchby.get()} LIKE ?"
                cur.execute(query, ('%' + self.var_searchtxt.get() + '%',))

                rows = cur.fetchall()
                if len(rows)!=0:
                    self.ProductTree.delete(*self.ProductTree.get_children())
                    for row in rows:
                        self.ProductTree.insert("", END, values=row)
                else:
                    messagebox.showerror("Error","No records found!!",parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")


# No need for Tk() here as this will be called from the main GUI
if __name__ == "__main__":
    window = Tk()
    obj = productclass(window)
    window.mainloop()
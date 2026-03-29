from tkinter  import *
import datetime
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import sqlite3
import time

class Billclass:
    def __init__(self,window):
        self.window = window
        self.window.geometry('1480x650+0+0')
        self.window.title("Inventory Management System")
        self.shop_icon = PhotoImage(file= "images/logo1.png")
        #title
        self.label = (Label(self.window, text="Inventory Management System",font=("time new roman",30,"bold"),
                           bg="navy blue",fg="white",padx=40,anchor="w",image=self.shop_icon,compound=LEFT)
                      .place(x=0, y=0,height=80,relwidth=1))

        self.logout_button = (Button(self.window, text="Logout",command= self.logout,bg="light grey",font=("time new roman",20,"bold"),cursor="hand2")
                              .place(x=1050,y=15,height=30,width=100))

    
        self.current_time_date = datetime.datetime.now()
        current_date_str = self.current_time_date.strftime("%d:%m:%Y")
        current_time_str = self.current_time_date.strftime("%H:%M:%S")
        self.time_label = Label(self.window, text=f"Welcome to Inventory Management System \t\t Date: {current_date_str}\t\t Time: {current_time_str} ",
                                font=("arial", 12), bg="grey", fg="white")
        self.time_label.place(x=0, y=80, relwidth=1)
        self.update_time()

        self.total_products=0

        # ALL  VARIABLES
        # self.var_Searchby = StringVar()
        # self.var_product_entry = StringVar()
        self.var_product_id=StringVar()
        self.var_input=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        self.var_product_name=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_qty_sold=StringVar()
        self.var_in_stock_entry=StringVar()
        self.var_cal_input=StringVar()
        self.cart_list=[]
        

        #left_frame
        leftmenumain=Frame(self.window,bd=2,relief=RIDGE)
        leftmenumain.place(x=10, y=120, height=470, width=370)

        lbl_footer =Label(leftmenumain, text="NOTE/:'Enter 0 QTY to Remove the Product From Cart.'",
                            font=("time new roman", 10,"bold"), fg="black",).pack(side=BOTTOM,fill=X)

        #inner frames
        upr_frame=Frame(leftmenumain,bd=2,relief=RIDGE)
        upr_frame.place(x=8, y=8, height=100, width=350)

        

        #product title
        lbl_product_title = Label(upr_frame, text="All Products",
                                   font=("times new roman", 20, "bold"), bg="black", fg="white")
        lbl_product_title.place(x=0, y=0, height=25, width=350)

        #haedings
        lbl_heading_title = Label(upr_frame, text="Search Product | By Name",
                                   font=("times new roman", 12, "bold"), fg="green")
        lbl_heading_title.place(x=0, y=40, height=15,width=200)

         #haedings
        lbl_heading_title2 = Label(upr_frame, text="Product Name",
                                   font=("times new roman", 12, "italic"), fg="Black")
        lbl_heading_title2.place(x=5, y=70, height=15,width=100)

        self.name_entry = Entry(upr_frame, textvariable=self.var_product_name, font=("arial", 15),
                                 bg="lightyellow", fg="black", relief=SUNKEN)
        self.name_entry.place(x=110, y=70, width=132, height=20)

         #show all button
        self.show_all_button = (Button(upr_frame, text="SHOW ALL",command=self.fetchall_product, bg="light blue", font=("times new roman", 10,"italic","bold"), cursor="hand2")
            .place(x=248, y=35, height=20, width=90))

        #search button
        self.search_button = (Button(upr_frame, text="SEARCH",command=self.search, bg="light pink", font=("times new roman", 10,"italic","bold"), cursor="hand2")
            .place(x=248, y=68, height=20, width=90))

        self.lower_frame=Frame(leftmenumain,bd=2,relief=RIDGE)
        self.lower_frame.place(x=8, y=115, height=320, width=350)

         #scroll bar
        scroll_x=Scrollbar(self.lower_frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(self.lower_frame, orient=VERTICAL)

         #scroll_x menu
        self.LeftTree = ttk.Treeview(self.lower_frame, columns=("Product_id", "Name", "Price", "Quantity", "Status"),
                                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.LeftTree.heading("Product_id", text="Product_id")
        self.LeftTree.heading("Name", text="Name")
        self.LeftTree.heading("Price", text="Price")
        self.LeftTree.heading("Quantity", text="Quantity")
        self.LeftTree.heading("Status", text="Status")

        # scroll bar calling
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.LeftTree.xview)
        scroll_y.config(command=self.LeftTree.yview)

        self.LeftTree["show"] = "headings"

        self.LeftTree.column("Product_id", width=80)
        self.LeftTree.column("Name", width=80)
        self.LeftTree.column("Price", width=90)
        self.LeftTree.column("Quantity", width=90)
        self.LeftTree.column("Status", width=90)


        self.LeftTree.pack(fill=BOTH, expand=True)
        self.fetchall_product()


        #centre_frame
        centremenumain=Frame(self.window,bd=2,relief=RIDGE)
        centremenumain.place(x=385, y=120, height=470, width=505)

        #inner frames
        upr_frame=Frame(centremenumain,bd=2,relief=RIDGE)
        upr_frame.place(x=8, y=8, height=60, width=485)

        lbl_product_title = Label(upr_frame, text="Customer Details",
                                   font=("times new roman", 22, "bold"), bg="grey", fg="white")
        lbl_product_title.place(x=0, y=0, height=27, width=485)

         #haedings
        lbl_heading_title = Label(upr_frame, text="Name",
                                   font=("times new roman", 12, "italic"), fg="Black")
        lbl_heading_title.place(x=5, y=35, height=15,width=100)

        self.name_entry = Entry(upr_frame, textvariable=self.var_name, font=("arial", 15),
                                 bg="white", fg="black", relief=SUNKEN)
        self.name_entry.place(x=90, y=32, width=132, height=20)

        lbl_heading_title2 = Label(upr_frame, text="Contact No.",
                                   font=("times new roman", 12, "italic"), fg="Black")
        lbl_heading_title2.place(x=235, y=35, height=15,width=100)

        self.name_entry = Entry(upr_frame, textvariable=self.var_contact, font=("arial", 15),
                                 bg="white", fg="black", relief=SUNKEN)
        self.name_entry.place(x=330, y=32, width=132, height=20)

        left_frame=Frame(centremenumain,bd=2,relief=RIDGE)
        left_frame.place(x=8, y=75, height=300, width=270)

        ########################### Calculator #######################
        # self.var_cal_input=StringVar()

        self.cal_entry = Entry(left_frame, textvariable=self.var_cal_input, font=("arial", 15),width=23,state="readonly",justify=RIGHT,
                                 bg="lightgrey", fg="black",bd=5, relief=SUNKEN)
        self.cal_entry.grid(row=0,columnspan=4)

        btn_7=Button(left_frame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=2,width=4,pady=10,cursor='hand2').grid(row=1,column=0)
        btn_8=Button(left_frame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=2,width=4,pady=10,cursor='hand2').grid(row=1,column=1)
        btn_9=Button(left_frame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=2,width=4,pady=10,cursor='hand2').grid(row=1,column=2)
        btn_sum=Button(left_frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=2,width=4,pady=10,cursor='hand2').grid(row=1,column=3)

        btn_4=Button(left_frame,text='4',font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=2,width=4,pady=10,cursor='hand2').grid(row=2,column=0)
        btn_5=Button(left_frame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=2,width=4,pady=10,cursor='hand2').grid(row=2,column=1)
        btn_6=Button(left_frame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=2,width=4,pady=10,cursor='hand2').grid(row=2,column=2)
        btn_minus=Button(left_frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),bd=2,width=4,pady=10,cursor='hand2').grid(row=2,column=3)

        btn_1=Button(left_frame,text='1',font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=2,width=4,pady=10,cursor='hand2').grid(row=3,column=0)
        btn_2=Button(left_frame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=2,width=4,pady=10,cursor='hand2').grid(row=3,column=1)
        btn_3=Button(left_frame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=2,width=4,pady=10,cursor='hand2').grid(row=3,column=2)
        btn_mul=Button(left_frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=2,width=4,pady=10,cursor='hand2').grid(row=3,column=3)

        btn_C=Button(left_frame,text='C',font=('arial',15,'bold'),command=lambda:self.var_cal_input.set(""),bd=2,width=4,pady=10,cursor='hand2').grid(row=4,column=0)
        btn_0=Button(left_frame,text='0',font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=2,width=4,pady=10,cursor='hand2').grid(row=4,column=1)
        btn_equal=Button(left_frame,text='=',font=('arial',15,'bold'),command=self.calculate,bd=2,width=4,pady=10,cursor='hand2').grid(row=4,column=2)
        btn_div=Button(left_frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=2,width=4,pady=10,cursor='hand2').grid(row=4,column=3)

        #########################################################################
        right_frame=Frame(centremenumain,bd=2,relief=RIDGE)
        right_frame.place(x=282, y=75, height=300, width=210)

         #scroll bar
        scroll_x=Scrollbar(right_frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(right_frame, orient=VERTICAL)

        #label
        self.lbl_title = Label(right_frame, text=(f"Cart\t\t Total Product:{self.total_products}"),
                                   font=("times new roman", 9, "bold"), bg="grey", fg="white")
        self.lbl_title.pack(side=TOP, fill=X)

         #scroll_x menu
        self.RightTree = ttk.Treeview(right_frame, columns=("Product_id","Customer Name", "Product Name","Contact","Price per qty", "Quantity"),
                                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.RightTree.heading("Product_id", text="Product_id")
        self.RightTree.heading("Customer Name", text="Customer Name")
        self.RightTree.heading("Product Name", text="Product Name")
        self.RightTree.heading("Contact", text="Contact")
        self.RightTree.heading("Price per qty", text="Price per qty")
        self.RightTree.heading("Quantity", text="Quantity Sold")
 

        # scroll bar calling
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.RightTree.xview)
        scroll_y.config(command=self.RightTree.yview)

        self.RightTree["show"] = "headings"

        self.RightTree.column("Product_id", width=40)
        self.RightTree.column("Customer Name", width=80)
        self.RightTree.column("Product Name", width=90)
        self.RightTree.column("Contact", width=80)
        self.RightTree.column("Price per qty", width=100)
        self.RightTree.column("Quantity", width=90)



        self.RightTree.pack(fill=BOTH, expand=True)

        down_frame=Frame(centremenumain,bd=2,relief=RIDGE)
        down_frame.place(x=8, y=380, height=85, width=485)
        self.RightTree.bind("<ButtonRelease-1>",self.get_data1)

         #haedings
        lbl_heading_title = Label(down_frame, text="Product Name",
                                   font=("times new roman", 12, "italic"), fg="Black")
        lbl_heading_title.place(x=5, y=10, height=15,width=100)

        self.name_entry = Entry(down_frame, textvariable=self.var_pname, font=("arial", 15),
                                 bg="white", fg="black", relief=SUNKEN)
        self.name_entry.place(x=5, y=30, width=132, height=20)

        lbl_heading_title2 = Label(down_frame, text="Price Per Quantity",
                                   font=("times new roman", 12, "italic"), fg="Black")
        lbl_heading_title2.place(x=160, y=10, height=15,width=150)

        self.name_entry = Entry(down_frame, textvariable=self.var_price, font=("arial", 15),
                                 bg="white", fg="black", relief=SUNKEN)
        self.name_entry.place(x=175, y=30, width=132, height=20)

        lbl_heading_title3 = Label(down_frame, text="Quantity Sold",
                                   font=("times new roman", 12, "italic"), fg="Black")
        lbl_heading_title3.place(x=320, y=10, height=15,width=100)

        self.qty_entry = Entry(down_frame, textvariable=self.var_qty_sold, font=("arial", 15),
                                 bg="beige", fg="black", relief=SUNKEN)
        self.qty_entry.place(x=335, y=30, width=132, height=20)

        lbl_heading_title4 = Label(down_frame, text="In-Stock",
                                   font=("times new roman", 12, "italic","bold"), fg="Black")
        lbl_heading_title4.place(x=5, y=60, height=15,width=100)
        self.in_stock_entry = Entry(down_frame, textvariable=self.var_in_stock_entry, font=("arial", 15),
                                 bg="white", fg="black", relief=SUNKEN)
        self.in_stock_entry.place(x=85, y=55, width=80, height=20)
        self.LeftTree.bind("<ButtonRelease-1>",self.get_data)


         #clear button
        self.show_all_button = (Button(down_frame, text="CLEAR",command=self.clear, bg="light blue", font=("times new roman", 10,"italic","bold"), cursor="hand2")
            .place(x=170, y=55, height=20, width=80))

        #add cart button
        self.add_update_button = (Button(down_frame, text="ADD CART",command=self.add_customer, bg="light pink", font=("times new roman", 10,"italic","bold"), cursor="hand2")
            .place(x=260, y=55, height=20, width=100))
        
         #delete cart button
        self.delete_button = (Button(down_frame, text="DELETE CART",command=self.delete_all, bg="light pink", font=("times new roman", 10,"italic","bold"), cursor="hand2")
            .place(x=367, y=55, height=20, width=100))


        #right_frame
        rightmenumain=Frame(self.window,bd=2,relief=RIDGE)
        rightmenumain.place(x=895, y=120, height=470, width=370)

        #inner frame
        self.upr_frame1=Text(rightmenumain,bd=2,relief=RIDGE)
        self.upr_frame1.place(x=8, y=8, height=330, width=350)

        down_frame=Frame(rightmenumain,bd=2,relief=RIDGE)
        down_frame.place(x=8, y=345, height=115, width=350)

        #buttons

        #bill amount button
        self.bill_amnt_button = (Button(down_frame, text="Bill Amount\n[0]", bg="light blue", font=("times new roman", 10,"italic","bold"), cursor="hand2"))
        self.bill_amnt_button.place(x=5, y=5, height=50, width=110)

        #discount button
        self.discount_button = (Button(down_frame, text="Discount 5%", bg="light pink", font=("times new roman", 10,"italic","bold"), cursor="hand2")
            .place(x=121, y=5, height=50, width=110))
        
        #net_pay button
        self.net_pay_button = (Button(down_frame, text="Net Pay\n[0]", bg="light blue", font=("times new roman", 10,"italic","bold"), cursor="hand2"))
        self.net_pay_button.place(x=235, y=5, height=50, width=108)

        #print button
        self.print_button = (Button(down_frame, text="Print", bg="light pink", font=("times new roman", 10,"italic","bold"), cursor="hand2")
            .place(x=5, y=55, height=50, width=110))
        
        #clear all button
        self.clear_all_button = (Button(down_frame, text="Clear all",command=self.clear1, bg="light blue", font=("times new roman", 10,"italic","bold"), cursor="hand2")
            .place(x=121, y=55, height=50, width=110))

        #generate save bill button
        self.savebill_button = (Button(down_frame, text="Generate Save Bill",command=self.generate_bill, bg="light pink", font=("times new roman", 10,"italic","bold"), cursor="hand2"))
        self.savebill_button.place(x=235, y=55, height=50, width=108)

         #product title
        lbl_product_title = Label(self.upr_frame1, text="Customer Billing Area",
                                   font=("times new roman", 20, "bold"), bg="yellow", fg="black")
        lbl_product_title.place(x=0, y=0, height=25, width=350)


        lbl_footer =Label(self.window, text="IMS-Inventory Management | Developed by Samarpit, Ram Ratan, Harshita, Sakshi and Shraddha\nFor any Technical Issue Contact-7217742842",
                            font=("time new roman", 15,"bold"),bg="grey", fg="white",).pack(side=BOTTOM,fill=X)
        
        self.show()
        # self.update_qty()
        self.window.mainloop()
    def update_total_products(self):
        self.total_products = len(self.RightTree.get_children())
        self.lbl_title.config(text=(f"Cart\t\t Total Product:{self.total_products}"))

    def get_input(self,num):
        xnum=self.var_cal_input.get()+str(num)
        self.var_cal_input.set(xnum)


    def update_time(self):
        self.current_time_date = datetime.datetime.now()
        self.time_label.config(text=f"Welcome to Inventory Management System \t\t Date: {self.current_time_date.strftime('%d:%m:%Y')} \t\t Time: {self.current_time_date.strftime('%H:%M:%S')}")
        self.window.after(1000, self.update_time)

    def calculate(self):
        try:
            result=eval(self.var_cal_input.get())
            self.var_cal_input.set(result)
        except Exception as e:
            self.var_cal_input.set("Error")
            print(e)

    def fetchall_product(self):
        con = sqlite3.connect(database=r'product.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT Product_id,Name,Price,Quantity,Status FROM product")
            product=cur.fetchall()
            self.LeftTree.delete(*self.LeftTree.get_children())  # Clear existing rows
            for row in product:
                self.LeftTree.insert('', END, values=row)  # Insert each row into the Treeview
            

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.window)

    

    def search(self):
        con = sqlite3.connect(database=r'product.db')
        cur = con.cursor()
        try:
            if self.var_product_name.get()=="":
                messagebox.showerror("Error","Please enter a search term",parent=self.window)
            else:
                query = "SELECT Product_id,Name,Price,Quantity,Status FROM product WHERE Name LIKE ?"
                cur.execute(query, ('%' + self.var_product_name.get() + '%',))

                rows = cur.fetchall()
                if len(rows)!=0:
                    self.LeftTree.delete(*self.LeftTree.get_children())
                    for row in rows:
                        self.LeftTree.insert("", END, values=row)
                else:
                    messagebox.showerror("Error","No records found!!",parent=self.window)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")

    def get_data(self,ev):
        f=self.LeftTree.focus()
        content=(self.LeftTree.item(f))
        row=content['values']
        if row :
            # self.var_product_id.set(row[0])
            # self.var_category.set(row[1])
            # self.var_supplier.set(row[2])
            self.var_pname.set(row[1])
            self.var_price.set(row[2])
            self.var_in_stock_entry.set(row[3])
            # self.var_status.set(row[6])

    def clear(self):
        self.var_name.set("")
        self.var_contact.set("")
        self.var_pname.set("")
        self.var_price.set("")
        self.var_qty_sold.set("")
        self.var_in_stock_entry.set("")
        # self.bill_amnt.set("")
        # self.net_pay.set("")
        



    
                

                        
    def add_customer(self):
        con = sqlite3.connect(database=r'bill.db')
        cur = con.cursor()
        try:
            # Step 1: Check if the customer name is empty
            if self.var_pname.get() == "":
                messagebox.showerror("Error", "Name must be required", parent=self.window)
            else:
                # Step 2: Check if the customer name already exists
                cur.execute("SELECT * FROM bill WHERE Customer_Name = ?", (self.var_pname.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Name already exists", parent=self.window)
                else:
                    # Step 3: Get the maximum Product_id and increment it for the new entry
                    cur.execute("SELECT MAX(Product_id) FROM bill")
                    max_product = cur.fetchone()[0]
                    if max_product is None:
                        new_product_no = 1
                    else:
                        new_product_no = int(max_product) + 1

                    self.var_product_id.set(new_product_no)
                    
                    # Step 4: Insert the new entry into the `bill` table
                    cur.execute("""
                        INSERT INTO bill(Product_id, Customer_Name, Product_Name, Contact, Price_per_qty, Quantity) 
                        VALUES (?, ?, ?, ?, ?, ?)
                    """, (
                        self.var_product_id.get(),
                        self.var_name.get(),
                        self.var_pname.get(),
                        self.var_contact.get(),
                        self.var_price.get(),
                        self.var_qty_sold.get(),
                    ))

                    # Step 5: Commit the new entry
                    con.commit()

                    # Step 6: Update product quantity in the `product` table
                    # Connect to product database to update quantity
                    con_product = sqlite3.connect(database=r'product.db')
                    cur_product = con_product.cursor()

                    # Fetch current quantity from product table
                    cur_product.execute("SELECT Quantity FROM product WHERE Name = ?", (self.var_pname.get(),))
                    product_data = cur_product.fetchone()

                    if product_data is None:
                        messagebox.showerror("Error", "Product not found in inventory", parent=self.window)
                    else:
                        available_qty = int(product_data[0])
                        qty_to_deduct = int(self.var_qty_sold.get())
                        print(available_qty)
                        print(qty_to_deduct)

                        # Check if there's enough stock
                        if qty_to_deduct > available_qty:
                            messagebox.showerror("Error", "Insufficient stock available", parent=self.window)
                        else:
                            # Deduct quantity
                            new_qty = available_qty - qty_to_deduct
                            cur_product.execute("UPDATE product SET Quantity = ? WHERE Name = ?", (new_qty, self.var_pname.get()))
                            con_product.commit()
                            messagebox.showinfo("Success", "Quantity updated in product database", parent=self.window)

                        # Close product database connection
                        con_product.close()

                    # Step 7: Notify the user and update the GUI
                    messagebox.showinfo("Success", "Entry successfully added", parent=self.window)

                    # Add to cart list
                    cart_data = [self.var_product_id.get(), self.var_name.get(), self.var_pname.get(), self.var_contact.get(), self.var_price.get(), self.var_qty_sold.get()]
                    self.cart_list.append(cart_data)

                    # Refresh the view, update total products, and calculate bill amount
                    self.show()
                    self.update_total_products()
                    self.bill_amount()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.window)

        finally:
            con.close()


   
    #THE CODE  WRITTEN BY CHATGPT!!!!!!!!!
    def show(self):
        con = sqlite3.connect(database=r'bill.db')
        cur = con.cursor()
        try:
            # Fetch only the items that belong to the current Bill ID
            cur.execute("SELECT * FROM bill WHERE Product_id=?", (self.var_product_id.get(),))
            self.cart_list = cur.fetchall()

            # Clear the Treeview before inserting new data
            self.RightTree.delete(*self.RightTree.get_children())

            # Insert the fetched rows into the Treeview (cart)
            for row in self.cart_list:
                self.RightTree.insert("", END, values=row)

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}", parent=self.window)
        finally:
            con.close()

        self.bill_amount()  # Call the function to calculate the bill amount
        self.update_total_products()

        

    def delete_all(self):
        con = sqlite3.connect(database=r'bill.db')
        cur = con.cursor()
        try:
            if self.var_product_id.get() == "":
                messagebox.showerror("Error","Product id Must be required",parent=self.window)
            else:
                cur.execute("Select * from bill where Customer_Name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Customer Name",parent=self.window)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.window)
                    if op==True:
                        cur.execute("Delete from bill where Product_id=?",(self.var_product_id.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Entry successfully deleted",parent=self.window)
                        self.clear()

            self.RightTree.set("")
            self.clear()


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")




  

  


    def get_data1(self,ev):
        f=self.RightTree.focus()
        content=(self.RightTree.item(f))
        row=content['values']
        if row :
            self.var_product_id.set(row[0])
            self.var_name.set(row[1])
            self.var_contact.set(row[3])
            self.var_pname.set(row[2])
            self.var_price.set(row[4])
            self.var_qty_sold.set(row[5])
            self.bill_amount()
            

     #right frame bill buttons function
    def bill_amount(self):
        self.bill_amnt=0
        self.net_pay=0
        self.discount=0
        self.calculate_total=0
        for row_id in self.RightTree.get_children():
            row=self.RightTree.item(row_id)['values']
            if len(row) >= 2:  # Ensure row has at least 2 values
                self.bill_amnt += float(row[4]) * int(row[5])

        self.discount=(self.bill_amnt*5)/100
        self.net_pay=self.bill_amnt-self.discount
        self.bill_amnt_button.config(text=f'Bill Amount(Rs.)\n[{str(self.bill_amnt)}]')
        self.net_pay_button.config(text=f'Net Pay(Rs.)\n[{str(self.net_pay)}]')
        self.calculate_total=self.net_pay
        # self.clear1()

    def generate_bill(self):
        if self.var_name.get()=='' or self.var_contact.get()=='':
            messagebox.showerror("Error","Customer Name and Contact Number must be required",parent=self.window)

        else:
            #==========Bill Top==========
            self.bill_top()
             #==========Bill middle==========
            self.bill_middle()
              #==========Bill last==========
            self.bill_bottom()


            fp=open(f'bills/{str(self.invoice)}.txt','w')
            fp.write(self.upr_frame1.get('1.0',END))
            fp.close()
            messagebox.showinfo("Success","Bill Generated Successfully",parent=self.window)
    
            # self.save_bill()
            
            
           
            
    def bill_top(self):
        self.invoice = int(time.strftime("%H%M%S")) + int(time.strftime("%d%m%Y"))
        bill_top_temp = f'''\n
\t\tXYZ-Inventory
Phone No. 9891965435 , Delhi-110032
{str("="*43)}
Customer Name: {self.var_name.get()}
Contact No. : {self.var_contact.get()}
Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*43)}
Product Name\t\t\tQTY\tPrice
{str("="*43)}
    '''
        
        self.upr_frame1.delete('1.0', END)  # Clear the text widget before inserting
        self.upr_frame1.insert('1.0', bill_top_temp)  # Insert the formatted string at the top



    def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*43)}
Bill Amount:\t\tRs.{self.bill_amnt}
Discount:  \t\tRs.{self.discount}
Net Pay:   \t\tRs.{self.net_pay}
{str("="*43)}
Total Bill: \t\tRs{self.calculate_total}
{str("="*43)}

        '''
        self.upr_frame1.insert(END, bill_bottom_temp)

    
    def bill_middle(self):
        
        for row_id in self.RightTree.get_children():
            row = self.RightTree.item(row_id)['values']
            name = row[2]
            qty = row[5]
            price = self.var_price.get()
            price = str(price)
            self.upr_frame1.insert(END, "\n "+ name+"\t\t\t"+str(qty)+"\tRs."+price)
        # print(row_id)

    def clear1(self):
        self.upr_frame1.delete('1.0', END)

    def logout(self):
        self.window.destroy()


if __name__ == '__main__':
    window = Tk()
    root = Billclass(window)

    
    
   
   
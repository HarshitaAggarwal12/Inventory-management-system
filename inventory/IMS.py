from tkinter  import *
import datetime
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox

from employee import employeeclass
from supply import supplyclass
from category import categoryclass
from product import productclass
from sales import salesclass
from billing_area import Billclass

import os

class GUI:
    def __init__(self):
        self.window = Tk()
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
        current_date_str = self.current_time_date.strftime("%D:%M:%Y")
        current_time_str = self.current_time_date.strftime("%H:%M:%S")
        self.time_label = Label(self.window, text=f"Welcome to Inventory Management System \t\t Date: {current_date_str}\t\t Time: {current_time_str} ",
                                font=("arial", 12), bg="grey", fg="white")
        self.time_label.place(x=0, y=80, relwidth=1)

        self.update_time()

        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200))
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        #left_frame
        leftmenu=Frame(self.window,bd=2,relief=RIDGE)
        leftmenu.place(x=0, y=100, height=550, width=200)

        #logo
        lbl_menulogo=Label(leftmenu,image=self.MenuLogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        self.side_icon = PhotoImage(file= "images/side.png")

        #menu button
        lbl_menu=Label(leftmenu, text="Menu", bg="orange", font=("time new roman", 20)).pack(side=TOP,fill=X)
        btn_employee=Button(leftmenu, text="Employee",command=self.employee,image=self.side_icon,compound=LEFT,padx=3,anchor="w",
                            bg="light grey", font=("time new roman", 18), cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier = Button(leftmenu, text="Supplier",command=self.supply, image=self.side_icon, compound=LEFT, padx=3, anchor="w",
                              bg="light grey", font=("time new roman", 18), cursor="hand2").pack(side=TOP, fill=X)
        btn_category = Button(leftmenu, text="Category",command=self.category, image=self.side_icon, compound=LEFT, padx=3, anchor="w",
                              bg="light grey", font=("time new roman", 18), cursor="hand2").pack(side=TOP, fill=X)
        btn_product = Button(leftmenu, text="Product",command=self.product, image=self.side_icon, compound=LEFT, padx=3, anchor="w",
                              bg="light grey", font=("time new roman", 18), cursor="hand2").pack(side=TOP, fill=X)
        btn_sales = Button(leftmenu, text="Sales",command=self.sales, image=self.side_icon, compound=LEFT, padx=3, anchor="w",
                              bg="light grey", font=("time new roman", 18), cursor="hand2").pack(side=TOP, fill=X)
        btn_bill = Button(leftmenu, text="Bills",command=self.bill, image=self.side_icon, compound=LEFT, padx=3, anchor="w",
                              bg="light grey", font=("time new roman", 18), cursor="hand2").pack(side=TOP, fill=X)


        #main labels
        self.lbl_employee=Label(self.window,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="lavender",fg="black",font=("arial",15,"bold"))
        self.lbl_employee.place(x=350,y=120,height=180,width=250)
        self.lbl_supplier = Label(self.window, text="Total Supplier\n[0]", bd=5, relief=RIDGE, bg="pink", fg="black",font=("arial", 15, "bold"))
        self.lbl_supplier.place(x=650, y=120, height=180, width=250)
        self.lbl_category = Label(self.window, text="Total Category\n[0]", bd=5, relief=RIDGE, bg="beige", fg="black",font=("arial", 15, "bold"))
        self.lbl_category.place(x=950, y=120, height=180, width=250)
        self.lbl_product = Label(self.window, text="Total Product\n[0]", bd=5, relief=RIDGE, bg="sky blue", fg="black",font=("arial", 15, "bold"))
        self.lbl_product.place(x=500, y=350, height=180, width=250)
        self.lbl_sales = Label(self.window, text="Total Sales\n[0]", bd=5, relief=RIDGE, bg="yellow", fg="black",font=("arial", 15, "bold"))
        self.lbl_sales.place(x=800, y=350, height=180, width=250)




        lbl_footer =Label(self.window, text="IMS-Inventory Management | Developed by Samarpit, Ram ratan, Harshita, Shraddha and Sakshi\nFor any Technical Issue Contact-7212242842",
                            font=("time new roman", 10),bg="grey", fg="white",).pack(side=BOTTOM,fill=X)
        

        self.update_data()
        self.update_category()
        self.update_product()
        self.update_sales()
        self.update_supply()
        self.window.mainloop()

    def employee(self):
        # Creating a new Toplevel window when the button is clicked
        self.new_window = Toplevel(self.window)  # Create a new Toplevel window
        self.new_obj = employeeclass(self.new_window)

    def supply(self):
        self.new_window = Toplevel(self.window)  # Create a new Toplevel window
        self.new_obj = supplyclass(self.new_window)

    def category(self):
        self.new_window = Toplevel(self.window)  # Create a new Toplevel window
        self.new_obj = categoryclass(self.new_window)

    def product(self):
        self.new_window = Toplevel(self.window)  # Create a new Toplevel window
        self.new_obj = productclass(self.new_window)

    def product(self):
        self.new_window = Toplevel(self.window)  # Create a new Toplevel window
        self.new_obj = productclass(self.new_window)


    def product(self):
        self.new_window = Toplevel(self.window)  # Create a new Toplevel window
        self.new_obj = productclass(self.new_window)


    def sales(self):
        self.new_window = Toplevel(self.window)  # Create a new Toplevel window
        self.new_obj = salesclass(self.new_window)

    def bill(self):
        self.new_window = Toplevel(self.window)  # Create a new Toplevel window
        self.new_obj = Billclass(self.new_window)


    def update_time(self):
        self.current_time_date = datetime.datetime.now()
        self.time_label.config(text=f"Welcome to Inventory Management System \t\t Date: {self.current_time_date.strftime('%d:%m:%Y')} \t\t Time: {self.current_time_date.strftime('%H:%M:%S')}")
        self.window.after(1000, self.update_time)

    def update_data(self):
        con = sqlite3.connect(database=r'ed.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Employee\n[{str(len(employee))}]')
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.window)
    def update_supply(self):
        con = sqlite3.connect(database=r'supplier.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM supply")
            supply=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Supplier\n[{str(len(supply))}]')
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.window)
    def update_category(self):
        con = sqlite3.connect(database=r'category.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[{str(len(category))}]')
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.window)



    def update_product(self):
        con = sqlite3.connect(database=r'Product.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Product\n[{str(len(product))}]')

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.window)

    def update_sales(self):
        con = sqlite3.connect(database=r'bill.db')
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM bill")
            bill=len(os.listdir('bills'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.window)
    
    def logout(self):
        self.window.destroy()

if __name__ == '__main__':
    root = GUI()


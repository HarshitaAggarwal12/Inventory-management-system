from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import sqlite3


class categoryclass:
    def __init__(self, window):  # Accepting the Toplevel window from the main GUI
        self.window = window  # Using the passed Toplevel window
        self.window.geometry('1080x530+100+110')  # Set the geometry of the Toplevel window
        self.window.title("Product Details")
        self.window.config(padx=10, pady=10, bg="light grey")

        # Example content for Employee window (add more widgets as needed)
        lbl_supply_title = Label(self.window, text="Manage Product Category",
                                   font=("times new roman", 20, "bold"), bg="blue", fg="white")
        lbl_supply_title.place(x=0, y=0, relwidth=1)

        # VARIABLES
        self.var_name = StringVar()
        self.var_category_id =StringVar()

        #imagesss
        #image 1
        self.first_img = Image.open("images/category.jpg")
        self.first_img = self.first_img.resize((500,300))
        self.first_img = ImageTk.PhotoImage(self.first_img)

        lbl_first_img = Label(self.window,image=self.first_img)
        lbl_first_img.place(x=40,y=200)
        #image 2
        self.sec_img = Image.open("images/cat.jpg")
        self.sec_img = self.sec_img.resize((500, 300))
        self.sec_img = ImageTk.PhotoImage(self.sec_img)

        lbl_sec_img = Label(self.window,image=self.sec_img)
        lbl_sec_img.place(x=550, y=200)



        #name
        lbl_name = Label(self.window, text="Enter Category Name:", font=("arial", 20), bg="light grey", fg="black")
        lbl_name.place(x=40, y=80)
        self.name_entry = Entry(self.window, textvariable=self.var_name, font=("arial", 15),
                                 bg="lightyellow", fg="black", relief=SUNKEN)
        self.name_entry.place(x=40, y=145, width=400, height=30)


        #add button
        self.add_button = (Button(self.window,command=self.add, text="ADD", bg="light blue", font=("arial", 13, "bold"), cursor="hand2")
            .place(x=450, y=145, height=30, width=90))

        #delete button
        self.delete_button = (Button(self.window,command=self.delete, text="DELETE", bg="beige", font=("arial", 13, "bold"), cursor="hand2")
            .place(x=550, y=145, height=30, width=90))

        #create a frame
        side_menu=Frame(self.window,bd=2,relief=RIDGE, bg="white")
        side_menu.place(x=650, y=50, height=130, width=400)

        #scroll bar
        scroll_x=Scrollbar(side_menu, orient=HORIZONTAL)
        scroll_y=Scrollbar(side_menu, orient=VERTICAL)



        #scroll_x menu
        self.CategoryTree = ttk.Treeview(side_menu, columns=("Category_id","Name"),
                                         yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        self.CategoryTree.heading("Category_id", text="Category_ID")
        self.CategoryTree.heading("Name", text="Name")


        # scroll bar calling
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.CategoryTree.xview)
        scroll_y.config(command=self.CategoryTree.yview)

        self.CategoryTree["show"] = "headings"

        self.CategoryTree.column("Category_id", width=80)
        self.CategoryTree.column("Name", width=100)


        self.CategoryTree.pack(fill=BOTH, expand=True)
        self.CategoryTree.bind("<ButtonRelease-1>",self.get_data)


        self.show()
#************************************************************************
#add button input
    def add(self):
        con = sqlite3.connect(database=r'category.db')
        cur = con.cursor()
        try:
            # Check if Name is empty
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Name must be required", parent=self.window)
            else:
                # Check if the category name already exists
                cur.execute("SELECT * FROM category WHERE Name = ?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "Category name already exists", parent=self.window)
                else:
                    cur.execute("SELECT Category_id FROM category ORDER BY Category_id")
                    existing_ids = [r[0] for r in cur.fetchall()]

                    if existing_ids:
                        # Find the smallest missing ID
                        new_category_id = 1
                        for i in range(1, max(existing_ids) + 2):  # Loop to check missing ID
                            if i not in existing_ids:
                                new_category_id = i
                                break
                    else:
                        # If no records exist, start with 1
                        new_category_id = 1
                    # Insert the new category, Category_id will auto-increment
                    cur.execute("INSERT INTO category (Category_id,Name) VALUES (?,?)", (
                        new_category_id,
                        self.var_name.get(),
                    ))

                    # Commit the changes
                    con.commit()
                    messagebox.showinfo("Success", "Category successfully added", parent=self.window)

                    # # Refresh the view (optional)
                    self.show()

                    


        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.window)





    def show(self):
        con = sqlite3.connect(database=r'category.db')
        cur = con.cursor()
        try:
            cur.execute("select * from category")
            rows=cur.fetchall()
            self.CategoryTree.delete(*self.CategoryTree.get_children())
            for row in rows:
                self.CategoryTree.insert("", END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")

    def get_data(self,ev):
        f=self.CategoryTree.focus()
        content=(self.CategoryTree.item(f))
        row=content['values']
        #print(row)
        self.var_category_id.set(row[0])
        self.var_name.set(row[1])




    def delete(self):
        con = sqlite3.connect(database=r'category.db')
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error","Category name Must be required",parent=self.window)
            else:
                cur.execute("Select * from category where Name=?",(self.var_name.get(),))
                row=cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Category name",parent=self.window)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete",parent=self.window)
                    if op==True:
                        cur.execute("Delete from category where Name=?",(self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Success","Category name successfully deleted",parent=self.window)

                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to:{str(ex)}")

    #clear button input
    def clear(self):
        self.var_category_id.set("")
        self.var_name.set("")

        self.show()

# No need for Tk() here as this will be called from the main GUI
if __name__ == "__main__":
    window = Tk()
    obj = categoryclass(window)
    window.mainloop()
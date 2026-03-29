from tkinter import *
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import os


class salesclass:
    def __init__(self, window):  # Accepting the Toplevel window from the main GUI
        self.window = window  # Using the passed Toplevel window
        
        self.window.geometry('1080x530+100+110')  # Set the geometry of the Toplevel window
        self.window.title("Sales Details")
        self.window.config(padx=10, pady=10, bg="white")

        # Example content for Employee window (add more widgets as needed)
        lbl_sales_title = Label(self.window, text="Customer Bill Report",
                                   font=("times new roman", 20, "bold"), bg="blue", fg="white")
        lbl_sales_title.place(x=0, y=0, relwidth=1)
        
        self.bill_list=[]
        # VARIABLES
        self.var_invoice = StringVar()
        # self.var_Sales_id =StringVar()

        #imagesss
        #image 1
        self.img = Image.open("images/cat2.jpg")
        self.img = self.img.resize((400,250))
        self.img = ImageTk.PhotoImage(self.img)

        lbl_img = Label(self.window,image=self.img)
        lbl_img.place(x=650,y=130)
       



        #name
        lbl_name = Label(self.window, text="Invoice No :", font=("arial", 12,"bold"), bg="light grey", fg="black")
        lbl_name.place(x=40, y=90)
        self.name_entry = Entry(self.window, textvariable=self.var_invoice, font=("arial", 10),
                                 bg="lightyellow", fg="black", relief=SUNKEN)
        self.name_entry.place(x=140, y=90, width=240, height=25)


        #search button
        self.search_button = Button(self.window, text="SEARCH",command=self.search, font=("arial", 12, "bold"),
                                    bg="lightpink", fg="black", cursor="hand2")
        self.search_button.place(x=400, y=90, width=100, height=25)

        #clear button
        self.save_button = (Button(self.window, text="CLEAR",command=self.clear, bg="lavender", font=("arial", 12, "bold"), cursor="hand2")
            .place(x=520, y=90, height=25, width=100))

        #create a frame
        side_menu=Frame(self.window,bd=2,relief=RIDGE, bg="white")
        side_menu.place(x=40, y=135, height=370, width=180)

        #scroll bar
        
        scroll_y=Scrollbar(side_menu, orient=VERTICAL)



        #scroll_x menu
        self.Sales_list = Listbox(side_menu,yscrollcommand=scroll_y.set)
        
        # scroll bar calling
        
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_y.config(command=self.Sales_list.yview)

        self.Sales_list.pack(fill=BOTH, expand=True)

        #create a frame
        right_menu=Frame(self.window,bd=2,relief=RIDGE, bg="white")
        right_menu.place(x=230, y=135, height=370, width=400)

        #sales title
        lbl_sales_title = Label(right_menu, text="Customer Billing Area",font=("arial", 18), bg="lightgreen", fg="black")
        lbl_sales_title.pack(side=TOP,fill=X)

        #scroll bar
        scroll_y=Scrollbar(right_menu, orient=VERTICAL)
        #scroll_x menu
        self.Sales_list1 = Text(right_menu,yscrollcommand=scroll_y.set)
        
        # scroll bar calling
        
        scroll_y.pack(side=RIGHT, fill=Y)
        
        scroll_y.config(command=self.Sales_list1.yview)

        self.Sales_list1.pack(fill=BOTH, expand=True)
        self.Sales_list.bind("<ButtonRelease-1>",self.get_data)
        self.show()

#**************************************************************************************
    
        


    


    def show(self):
        del self.bill_list[:]
        self.Sales_list.delete(0,END)
        
        for i in os.listdir("bills"):
            if i.split('.')[-1]=="txt":
                self.Sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
                # print("Success")


    def get_data(self,ev):
        index_=self.Sales_list.curselection()
        file_name=self.Sales_list.get(index_)
        self.Sales_list1.delete('1.0',END)
        fp=open(f"bills/{file_name}",'r')
        for i in fp:
            self.Sales_list1.insert(END,i)
        fp.close()
        # print(file_name)

    def search(self):
        #print(self.var_invoice,self.bill_list)
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no. should be required",parent=self.window)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bills/{self.var_invoice.get()}.txt','r')
                self.Sales_list1.delete('1.0',END)
                for i in fp:
                    self.Sales_list1.insert(END,i)
                fp.close()

    def clear(self):
        self.var_invoice.set("")
        self.Sales_list1.delete('1.0',END)





# No need for Tk() here as this will be called from the main GUI
if __name__ == "__main__":
    window = Tk()
    obj = salesclass(window)
    window.mainloop()
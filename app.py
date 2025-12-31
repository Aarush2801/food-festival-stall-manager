import tkinter as tk
from tkinter import END, messagebox
import sqlite3


conn = sqlite3.connect('project.db')
c = conn.cursor()


c.execute("""
         CREATE TABLE IF NOT EXISTS stall_master_info
         (Stall_ID int PRIMARY KEY,
          Group_Leader varchar(40),
          Food_Item varchar(40),
          ward1_name varchar(20),
          ward2_name varchar(20),
          ward1_class varchar(5),
          ward2_class varchar(5))""")


conn.commit()
c.close()
conn.close()
def add():
   add_page = tk.Tk()
   add_page.title("Add")
   conn = sqlite3.connect('project.db')
   c = conn.cursor()


   def submit():
       Group_Leader_Entry.delete(0, END)
       Food_Item_Entry.delete(0, END)
       ward1_name_Entry.delete(0,END)
       ward2_class_Entry.delete(0,END)
       ward2_name_Entry.delete(0, END)
       ward1_class_Entry.delete(0,END)
       Stall_ID_Entry.delete(0,END)


       conn = sqlite3.connect('project.db')
       c = conn.cursor()
      
       c.execute ("INSERT INTO stall_master_info VALUES (:Stall_ID, :Group_Leader, :Food_Item, :ward1_name, :ward2_name, :ward1_class, :ward2_class)",
                   {
                       'Stall_ID' : Stall_ID_Entry.get(),
                       'Group_Leader' : Group_Leader_Entry.get(),
                       'Food_Item' : Food_Item_Entry.get(),
                       'ward1_name' : ward1_name_Entry.get(),
                       'ward2_name' : ward2_name_Entry.get(),
                       'ward1_class' : ward1_class_Entry.get(),
                       'ward2_class' : ward2_class_Entry.get()
                   })
       conn.commit()
       conn.close()
      
   def delete():


       conn = sqlite3.connect('project.db')
       c = conn.cursor()
       c.execute('DELETE from stall_master_info WHERE stall_id =' + delete_box.get())
       conn.commit()
       conn.close()


   Group_Leader_Entry = tk.Entry(add_page, width = 30)
   Group_Leader_Entry.grid(row=0,column=1,padx=30)
   Food_Item_Entry = tk.Entry(add_page,width = 30)
   Food_Item_Entry.grid(row=1,column=1,padx=30)
   ward1_name_Entry = tk.Entry(add_page,width = 30)
   ward1_name_Entry.grid(row=2,column=1,padx=30)
   ward2_name_Entry = tk.Entry(add_page,width = 30)
   ward2_name_Entry.grid(row=3,column=1,padx=30)
   ward1_class_Entry= tk.Entry(add_page,width = 30)
   ward1_class_Entry.grid(row=4,column=1,padx=30)
   ward2_class_Entry = tk.Entry(add_page,width = 30)
   ward2_class_Entry.grid(row=5,column=1,padx=30)
   Stall_ID_Entry = tk.Entry(add_page,width = 30)
   Stall_ID_Entry.grid(row =6,column =1,padx = 30)


   Group_Leader_Label = tk.Label(add_page, text = "Group Leader")
   Group_Leader_Label.grid(row = 0, column=0)


   Food_Item_Label = tk.Label(add_page, text = "Food Item")
   Food_Item_Label.grid(row = 1, column=0)


   ward1_name_Label = tk.Label(add_page, text = "ward1")
   ward1_name_Label.grid(row = 2, column=0)


   ward2_name_Label = tk.Label(add_page, text = "ward2")
   ward2_name_Label.grid(row = 3, column=0)


   ward1_class_Label = tk.Label(add_page, text = "ward1 class")
   ward1_class_Label.grid(row = 4, column=0)


   ward2_class_Label = tk.Label(add_page, text = "Ward2 class")
   ward2_class_Label.grid(row = 5, column=0)


   Stall_ID_Label = tk.Label(add_page, text = "Stall ID")
   Stall_ID_Label.grid(row = 6,column = 0)


   submit_button = tk.Button(add_page,text = "Add to database",command = submit)
   submit_button.grid(row = 7,column=0,columnspan=2,pady=10,padx = 10,ipadx=100)


   delete_button = tk.Button(add_page,text="Delete",command = delete)
   delete_button.grid(row = 10,columnspan = 2, column = 0,pady = 10,padx= 10,ipadx = 137)
   delete_box = tk.Entry(add_page,width = 30)
   delete_box.grid(row = 9, column = 1)


   delete_box_label = tk.Label(add_page, text = 'Delete Stall Number')
   delete_box_label.grid(row=9,column = 0)


   def query():
       conn = sqlite3.connect('project.db')
       c = conn.cursor()




       c.execute("select*,oid from stall_master_info")
       records = c.fetchall()
       print(records)
       print_records = ''
       for record in records:
           print_records += str(record) + ' '
           print(print_records)
       query_label= tk.Label(add_page, text= print_records)
       query_label.grid(row = 9, column = 0, columnspan = 2)


       conn.commit()
       conn.close()


   query_btn = tk.Button(add_page,text = "Show",command = query)
   query_btn.grid(row = 8,columnspan = 2, column = 0,pady = 10,padx= 10,ipadx = 137)


 
def search():
   search_page = tk.Tk()
   search_page.title("Modify/Searcb")


   conn = sqlite3.connect('project.db')
   c = conn.cursor()




   c.execute("select*,oid from stall_master_info")
   records = c.fetchall()
   print(records)
   print_records = ''
   for record in records:
       print_records += str(record) + ' '
       print(print_records)
       query_label= tk.Label(search_page, text= print_records)
       query_label.grid(row = 9, column = 0, columnspan = 2)


   Group_Leader_Entry = tk.Entry(search_page, width = 30)
   Group_Leader_Entry.grid(row=6,column=1,padx=30)
   Food_Item_Entry = tk.Entry(search_page,width = 30)
   Food_Item_Entry.grid(row=1,column=1,padx=30)
   ward1_name_Entry = tk.Entry(search_page,width = 30)
   ward1_name_Entry.grid(row=2,column=1,padx=30)
   ward2_name_Entry = tk.Entry(search_page,width = 30)
   ward2_name_Entry.grid(row=3,column=1,padx=30)
   ward1_class_Entry= tk.Entry(search_page,width = 30)
   ward1_class_Entry.grid(row=4,column=1,padx=30)
   ward2_class_Entry = tk.Entry(search_page,width = 30)
   ward2_class_Entry.grid(row=5,column=1,padx=30)
   Stall_ID_Entry = tk.Entry(search_page,width = 30)
   Stall_ID_Entry.grid(row =0,column =1,padx = 30)


   Group_Leader_Label = tk.Label(search_page, text = "Group Leader")
   Group_Leader_Label.grid(row = 0, column=0)


   Food_Item_Label = tk.Label(search_page, text = "Food Item")
   Food_Item_Label.grid(row = 1, column=0)


   ward1_name_Label = tk.Label(search_page, text = "ward1")
   ward1_name_Label.grid(row = 2, column=0)


   ward2_name_Label = tk.Label(search_page, text = "ward2")
   ward2_name_Label.grid(row = 3, column=0)


   ward1_class_Label = tk.Label(search_page, text = "ward1 class")
   ward1_class_Label.grid(row = 4, column=0)


   ward2_class_Label = tk.Label(search_page, text = "Ward2 class")
   ward2_class_Label.grid(row = 5, column=0)


   Stall_ID_Label = tk.Label(search_page, text = "Stall ID")
   Stall_ID_Label.grid(row = 6,column = 0)


   save_btn = tk.Button(search_page, text = 'save')
   save_btn.grid(row = 7,columnspan = 2, column = 0,pady = 10,padx= 10,ipadx = 137)


def stalls_page():
   stalls_page = tk.Tk()
   stalls_page.title("Stalls")
   search_button = tk.Button(stalls_page,text = "Modify/Search",command = search)
   search_button.pack()
   add_button = tk.Button(stalls_page,text = "Add/Delete",command = add)
   add_button.pack()
  


def home():
   home_window = tk.Tk()
   home_window.title("Home")
   Stalls_button = tk.Button(home_window,text = "Stalls",command = stalls_page)
   Stalls_button.pack()




  




# Function to check login credentials
def login():
   username = username_entry.get()
   password = password_entry.get()
  
   # Replace with your actual username and password check
   if username == "admin" and password == "password":
       messagebox.showinfo("Login Success", "Welcome!")
       home()
       root.destroy()
   else:
       messagebox.showerror("Login Failed", "Invalid username or password")


# Function to exit the login window
def cancel():
   root.destroy()


# Setting up the window
root = tk.Tk()
root.title("Login")
root.geometry("300x150")


# Username Label and Entry
username_label = tk.Label(root, text="Username")
username_label.pack(pady=5)
username_entry = tk.Entry(root)
username_entry.pack(pady=5)


# Password Label and Entry
password_label = tk.Label(root, text="Password")
password_label.pack(pady=5)
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)


# Login and Cancel Buttons
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(side=tk.LEFT, padx=20, pady=10)


cancel_button = tk.Button(root, text="Cancel", command=cancel)
cancel_button.pack(side=tk.RIGHT, padx=20, pady=10)


# Run the Tkinter event loop
root.mainloop()

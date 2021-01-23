import os
from subprocess import call

import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import sqlite3
from tkinter import *
from tkcalendar import *

global c
from tkinter import ttk
import datetime

from PIL import ImageTk, Image



rootmain = Tk()
rootmain.title('Designed by Ian')

rootmain.geometry("1000x600")

def click_openStudent():
    call(["python", "SCHOOLGUISYT2.py"])


def click_Accomodation():
    call(["python", "HOTEL SYSTEM GUI .py"])


# Define image
bg = PhotoImage(file="Images/iane (2).png")

# mylabel=Label(rootmain,text="Hello world").grid(row=0, column=0)

intr_message = '''A Python tkinter project with sqlite.
This Dtabase System helps to store details of  candidates 
and view the poll results You can create polls,
vote in them and view their results. We have used
tkinter,sqlite & matplotlib library. You can also
project the results in a pie-chart format. Sqlite is
 used to create databases and manage the data.

When you create a new poll, a new database is
 created to store the casted votes. 
 I have created a sample poll: 'myelection' 
 which incudes 3 candidates'''


def myClickentry():
    instruction_label = Label(rootmain, text=intr_message, bg="grey", fg="blue")
    instruction_label.grid(row=1, column=0)


# Create a label
my_label = Label(rootmain, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
# Add something to the top of our image
my_text = Label(rootmain, text="Kenyans in Debrecen!", font=("Old English Text MT", 25), fg="red", )

my_text.grid(row=2, column=2, ipadx=8)


# function to open a new window
# on a button click
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    root = Toplevel(rootmain)

    # sets the title of the
    # Toplevel widget
    root.title('Student Database - Kenyans in Debrecen!')

    # sets the geometry of toplevel
    root.geometry("430x570")

    # Databases

    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')

    # Create cursor
    c = conn.cursor()

    # Create table
    '''
    c.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
   )""")

'''
    # mylabel=Label(window,text="Hello world").grid(row=0, column=0)
    intr_message = '''A Python tkinter project with sqlite.
    This Dtabase System helps to store details of  candidates 
    and view the poll results You can create polls,
    vote in them and view their results. We have used
    tkinter,sqlite & matplotlib library. You can also
    project the results in a pie-chart format. Sqlite is
     used to create databases and manage the data.
    
    When you create a new poll, a new database is
     created to store the casted votes. 
     I have created a sample poll: 'myelection' 
     which incudes 3 candidates'''

    def myClickentry():
        instruction_label = Label(root, text=intr_message, bg="grey", fg="blue")
        instruction_label.grid(row=13, column=1)

    # Create Update function to update a record
    # Create Update function to update a record
    def update():
        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        # Create cursor
        c = conn.cursor()

        record_id = delete_box.get()

        c.execute("""UPDATE addresses SET
    first_name = :first,
    last_name = :last,
    address = :address,
    city = :city,
    state = :state,
    zipcode = :zipcode 
    WHERE oid = :oid""",
                  {
                      'first': f_name_editor.get(),
                      'last': l_name_editor.get(),
                      'address': address_editor.get(),
                      'city': city_editor.get(),
                      'state': state_editor.get(),
                      'zipcode': zipcode_editor.get(),
                      'oid': record_id
                  })

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        editor.destroy()
        root.deiconify()

    # Create Edit function to update a record
    def edit():
        root.withdraw()
        global editor
        editor = Tk()
        editor.title('Update A Record')

        editor.geometry("400x450")
        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        # Create cursor
        c = conn.cursor()
        record_id = clicked.get()
        # record_id = delete_box.get()
        # Query the database
        c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
        records = c.fetchall()

        # Create Global Variables for text box names
        global f_name_editor
        global l_name_editor
        global address_editor
        global city_editor
        global state_editor
        global zipcode_editor

        # Create Text Boxes
        f_name_editor = Entry(editor, width=30)
        f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
        l_name_editor = Entry(editor, width=30)
        l_name_editor.grid(row=1, column=1)
        address_editor = Entry(editor, width=30)
        address_editor.grid(row=2, column=1)
        city_editor = Entry(editor, width=30)
        city_editor.grid(row=3, column=1)
        state_editor = Entry(editor, width=30)
        state_editor.grid(row=4, column=1)
        zipcode_editor = Entry(editor, width=30)
        zipcode_editor.grid(row=5, column=1)

        # Create Text Box Labels
        f_name_label = Label(editor, text="First Name")
        f_name_label.grid(row=0, column=0, pady=(10, 0))
        l_name_label = Label(editor, text="Last Name")
        l_name_label.grid(row=1, column=0)
        address_label = Label(editor, text="Address")
        address_label.grid(row=2, column=0)
        city_label = Label(editor, text="City")
        city_label.grid(row=3, column=0)
        state_label = Label(editor, text="State")
        state_label.grid(row=4, column=0)
        zipcode_label = Label(editor, text="Zipcode")
        zipcode_label.grid(row=5, column=0)

        # Loop thru results
        for record in records:
            f_name_editor.insert(0, record[0])
            l_name_editor.insert(0, record[1])
            address_editor.insert(0, record[2])
            city_editor.insert(0, record[3])
            state_editor.insert(0, record[4])
            zipcode_editor.insert(0, record[5])

        # Create a Save Button To Save edited record
        edit_btn = Button(editor, text="Save Record", command=update, bg="green")
        edit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=145)

    # Create Function to Delete A Record
    def delete():
        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        # Create cursor
        c = conn.cursor()

        # Delete a record
        c.execute("DELETE from addresses WHERE oid = " + delete_box.get())

        delete_box.delete(0, END)

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

    # Create Submit Function For database
    def submit():
        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        # Create cursor
        c = conn.cursor()

        # Insert Into Table
        c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
                  {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'address': address.get(),
                      'city': city.get(),
                      'state': state.get(),
                      'zipcode': zipcode.get()
                  })

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        # Clear The Text Boxes
        f_name.delete(0, END)
        l_name.delete(0, END)
        address.delete(0, END)
        city.delete(0, END)
        state.delete(0, END)
        zipcode.delete(0, END)

    def show_id():
        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        # Create cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT oid FROM addresses")
        records = c.fetchall()
        # print(records)

        options = []
        global clicked
        clicked = StringVar()

        # Loop Thru Results
        print_records = ''
        for record in records:
            options.append(str(record[0]))

        clicked.set(options[0])
        drop = OptionMenu(root, clicked, *options)
        drop.grid(row=20, column=0, columnspan=2)

    # Create Query Function
    def query():
        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')
        # Create cursor
        c = conn.cursor()

        # Query the database
        c.execute("SELECT *, oid FROM addresses")
        records = c.fetchall()
        # print(records)

        # Loop Thru Results
        print_records = ''
        for record in records:
            print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

        query_label = Label(root, text=print_records)
        query_label.grid(row=12, column=0, columnspan=2)

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

    # Create Text Boxes
    f_name = Entry(root, width=30)
    f_name.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name = Entry(root, width=30)
    l_name.grid(row=1, column=1)
    address = Entry(root, width=30)
    address.grid(row=2, column=1)
    city = Entry(root, width=30)
    city.grid(row=3, column=1)
    state = Entry(root, width=30)
    state.grid(row=4, column=1)
    zipcode = Entry(root, width=30)
    zipcode.grid(row=5, column=1)
    delete_box = Entry(root, width=30)
    delete_box.grid(row=9, column=1, pady=5)

    # Create Text Box Labels
    f_name_label = Label(root, text="First Name")
    f_name_label.grid(row=0, column=0, pady=(10, 0))
    l_name_label = Label(root, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(root, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(root, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(root, text="State")
    state_label.grid(row=4, column=0)
    zipcode_label = Label(root, text="Zipcode")
    zipcode_label.grid(row=5, column=0)
    delete_box_label = Label(root, text="Select ID")
    delete_box_label.grid(row=9, column=0, pady=5)

    # Create Submit Button
    submit_btn = Button(root, text="Add Record To Database", command=submit, bg="magenta")
    submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

    # Create a Query Button
    query_btn = Button(root, text="Show Records", command=query, bg="cyan")
    query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

    # Create A Delete Button
    delete_btn = Button(root, text="Delete Record", command=delete, bg="red")
    delete_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

    # Create an Update Button
    edit_btn = Button(root, text="Edit Record//Update", command=edit, bg="blue")
    edit_btn.grid(row=11, column=0, columnspan=2, pady=10, padx=10, ipadx=143)

    bt_entry = Button(root, text="README", command=myClickentry, fg="white", bg="red")
    bt_entry.grid(row=12, column=1, pady=10, padx=10, )

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    show_id()


# on a button click
def openMedical():
    # Mini Project
    import tkinter
    import tkinter.ttk
    import tkinter.messagebox
    import sqlite3

    '''
    # Toplevel object which will
    # be treated as a new window
    window = Toplevel(rootmain)

    # sets the title of the
    # Toplevel widget
    window.title('Student Database - Kenyans in Debrecen!')

    # sets the geometry of toplevel
    window.geometry("430x570")
            # application
        rootreminder = tkinter.Tk()
        rootreminder.geometry("460x480")
        rootreminder.title("IAN To do List Reminder")
        rootreminder.rowconfigure(0, weight=1)
        rootreminder.config(bg="grey")
    '''

    class Database:
        def __init__(self):
            self.dbConnection = sqlite3.connect("dbFile.db")
            self.dbCursor = self.dbConnection.cursor()
            self.dbCursor.execute(
                "CREATE TABLE IF NOT EXISTS patient_info (id PRIMARYKEY text, fName text, lName text, dob text, "
                "mob text, yob text, gender text, address text, phone text, email text, bloodGroup text, "
                "history text, doctor text)")

        def __del__(self):
            self.dbCursor.close()
            self.dbConnection.close()

        def Insert(self, id, fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, history, doctor):
            self.dbCursor.execute("INSERT INTO patient_info VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
                id, fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, history, doctor))
            self.dbConnection.commit()

        def Update(self, fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, history, doctor, id):
            self.dbCursor.execute(
                "UPDATE patient_info SET fName = ?, lName = ?, dob = ?, mob = ?, yob = ?, gender = ?, address = ?, "
                "phone = ?, email = ?, bloodGroup = ?, history = ?, doctor = ? WHERE id = ?",
                (fName, lName, dob, mob, yob, gender, address, phone, email, bloodGroup, history, doctor, id))
            self.dbConnection.commit()

        def Search(self, id):
            self.dbCursor.execute("SELECT * FROM patient_info WHERE id = ?", (id,))
            searchResults = self.dbCursor.fetchall()
            return searchResults

        def Delete(self, id):
            self.dbCursor.execute("DELETE FROM patient_info WHERE id = ?", (id,))
            self.dbConnection.commit()

        def Display(self):
            self.dbCursor.execute("SELECT * FROM patient_info")
            records = self.dbCursor.fetchall()
            return records

    class Values:
        def Validate(self, id, fName, lName, phone, email, history, doctor):
            if not (id.isdigit() and (len(id) == 3)):
                return "id"
            elif not (fName.isalpha()):
                return "fName"
            elif not (lName.isalpha()):
                return "lName"
            elif not (phone.isdigit() and (len(phone) == 10)):
                return "phone"
            elif not (email.count("@") == 1 and email.count(".") > 0):
                return "email"
            elif not (history.isalpha()):
                return "history"
            elif not (doctor.isalpha()):
                return "doctor"
            else:
                return "SUCCESS"

    class InsertWindow:
        def __init__(self):
            self.window = Toplevel(rootmain)
            self.window.wm_title("Insert data")

            # Initializing all the variables
            self.id = tkinter.StringVar()
            self.fName = tkinter.StringVar()
            self.lName = tkinter.StringVar()
            self.address = tkinter.StringVar()
            self.phone = tkinter.StringVar()
            self.email = tkinter.StringVar()
            self.history = tkinter.StringVar()
            self.doctor = tkinter.StringVar()

            self.genderList = ["Male", "Female", "Transgender", "Other"]
            self.dateList = list(range(1, 32))
            self.monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                              "October", "November", "December"]
            self.yearList = list(range(1900, 2020))
            self.bloodGroupList = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

            # Labels
            tkinter.Label(self.window, text="Patient ID", width=25).grid(pady=5, column=1, row=1)
            tkinter.Label(self.window, text="First Name", width=25).grid(pady=5, column=1, row=2)
            tkinter.Label(self.window, text="Last Name", width=25).grid(pady=5, column=1, row=3)
            tkinter.Label(self.window, text="D.O.B", width=25).grid(pady=5, column=1, row=4)
            tkinter.Label(self.window, text="M.O.B", width=25).grid(pady=5, column=1, row=5)
            tkinter.Label(self.window, text="Y.O.B", width=25).grid(pady=5, column=1, row=6)
            tkinter.Label(self.window, text="Gender", width=25).grid(pady=5, column=1, row=7)
            tkinter.Label(self.window, text="Home Address", width=25).grid(pady=5, column=1, row=8)
            tkinter.Label(self.window, text="Phone Number", width=25).grid(pady=5, column=1, row=9)
            tkinter.Label(self.window, text="Email ID", width=25).grid(pady=5, column=1, row=10)
            tkinter.Label(self.window, text="Blood Group", width=25).grid(pady=5, column=1, row=11)
            tkinter.Label(self.window, text="Patient History", width=25).grid(pady=5, column=1, row=12)
            tkinter.Label(self.window, text="Doctor", width=25).grid(pady=5, column=1, row=13)

            # Fields
            # Entry widgets
            self.idEntry = tkinter.Entry(self.window, width=25, textvariable=self.id)
            self.fNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.fName)
            self.lNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lName)
            self.addressEntry = tkinter.Entry(self.window, width=25, textvariable=self.address)
            self.phoneEntry = tkinter.Entry(self.window, width=25, textvariable=self.phone)
            self.emailEntry = tkinter.Entry(self.window, width=25, textvariable=self.email)
            self.historyEntry = tkinter.Entry(self.window, width=25, textvariable=self.history)
            self.doctorEntry = tkinter.Entry(self.window, width=25, textvariable=self.doctor)

            self.idEntry.grid(pady=5, column=3, row=1)
            self.fNameEntry.grid(pady=5, column=3, row=2)
            self.lNameEntry.grid(pady=5, column=3, row=3)
            self.addressEntry.grid(pady=5, column=3, row=8)
            self.phoneEntry.grid(pady=5, column=3, row=9)
            self.emailEntry.grid(pady=5, column=3, row=10)
            self.historyEntry.grid(pady=5, column=3, row=12)
            self.doctorEntry.grid(pady=5, column=3, row=13)

            # Combobox widgets
            self.dobBox = tkinter.ttk.Combobox(self.window, values=self.dateList, width=20)
            self.mobBox = tkinter.ttk.Combobox(self.window, values=self.monthList, width=20)
            self.yobBox = tkinter.ttk.Combobox(self.window, values=self.yearList, width=20)
            self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderList, width=20)
            self.bloodGroupBox = tkinter.ttk.Combobox(self.window, values=self.bloodGroupList, width=20)

            self.dobBox.grid(pady=5, column=3, row=4)
            self.mobBox.grid(pady=5, column=3, row=5)
            self.yobBox.grid(pady=5, column=3, row=6)
            self.genderBox.grid(pady=5, column=3, row=7)
            self.bloodGroupBox.grid(pady=5, column=3, row=11)

            # Button widgets
            tkinter.Button(self.window, width=20, text="Insert", command=self.Insert).grid(pady=15, padx=5, column=1,
                                                                                           row=14)
            tkinter.Button(self.window, width=20, text="Reset", command=self.Reset).grid(pady=15, padx=5, column=2,
                                                                                         row=14)
            tkinter.Button(self.window, width=20, text="Close", command=self.window.destroy).grid(pady=15, padx=5,
                                                                                                  column=3,
                                                                                                  row=14)

            self.window.mainloop()

        def Insert(self):
            self.values = Values()
            self.database = Database()
            self.test = self.values.Validate(self.idEntry.get(), self.fNameEntry.get(), self.lNameEntry.get(),
                                             self.phoneEntry.get(), self.emailEntry.get(), self.historyEntry.get(),
                                             self.doctorEntry.get())
            if self.test == "SUCCESS":
                self.database.Insert(self.idEntry.get(), self.fNameEntry.get(), self.lNameEntry.get(),
                                     self.dobBox.get(),
                                     self.mobBox.get(), self.yobBox.get(), self.genderBox.get(),
                                     self.addressEntry.get(),
                                     self.phoneEntry.get(), self.emailEntry.get(), self.bloodGroupBox.get(),
                                     self.historyEntry.get(), self.doctorEntry.get())
                tkinter.messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")
            else:
                self.valueErrorMessage = "Invalid input in field " + self.test
                tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)

        def Reset(self):
            self.idEntry.delete(0, tkinter.END)
            self.fNameEntry.delete(0, tkinter.END)
            self.lNameEntry.delete(0, tkinter.END)
            self.dobBox.set("")
            self.mobBox.set("")
            self.yobBox.set("")
            self.genderBox.set("")
            self.addressEntry.delete(0, tkinter.END)
            self.phoneEntry.delete(0, tkinter.END)
            self.emailEntry.delete(0, tkinter.END)
            self.bloodGroupBox.set("")
            self.historyEntry.delete(0, tkinter.END)
            self.doctorEntry.delete(0, tkinter.END)

    class UpdateWindow:
        def __init__(self, id):
            self.window = tkinter.Tk()
            self.window.wm_title("Update data")

            # Initializing all the variables
            self.id = id

            self.fName = tkinter.StringVar()
            self.lName = tkinter.StringVar()
            self.address = tkinter.StringVar()
            self.phone = tkinter.StringVar()
            self.email = tkinter.StringVar()
            self.history = tkinter.StringVar()
            self.doctor = tkinter.StringVar()

            self.genderList = ["Male", "Female", "Transgender", "Other"]
            self.dateList = list(range(1, 32))
            self.monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                              "October", "November", "December"]
            self.yearList = list(range(1900, 2020))
            self.bloodGroupList = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

            # Labels
            tkinter.Label(self.window, text="Patient ID", width=25).grid(pady=5, column=1, row=1)
            tkinter.Label(self.window, text=id, width=25).grid(pady=5, column=3, row=1)
            tkinter.Label(self.window, text="First Name", width=25).grid(pady=5, column=1, row=2)
            tkinter.Label(self.window, text="Last Name", width=25).grid(pady=5, column=1, row=3)
            tkinter.Label(self.window, text="D.O.B", width=25).grid(pady=5, column=1, row=4)
            tkinter.Label(self.window, text="M.O.B", width=25).grid(pady=5, column=1, row=5)
            tkinter.Label(self.window, text="Y.O.B", width=25).grid(pady=5, column=1, row=6)
            tkinter.Label(self.window, text="Gender", width=25).grid(pady=5, column=1, row=7)
            tkinter.Label(self.window, text="Home Address", width=25).grid(pady=5, column=1, row=8)
            tkinter.Label(self.window, text="Phone Number", width=25).grid(pady=5, column=1, row=9)
            tkinter.Label(self.window, text="Email ID", width=25).grid(pady=5, column=1, row=10)
            tkinter.Label(self.window, text="Blood Group", width=25).grid(pady=5, column=1, row=11)
            tkinter.Label(self.window, text="Patient History", width=25).grid(pady=5, column=1, row=12)
            tkinter.Label(self.window, text="Doctor", width=25).grid(pady=5, column=1, row=13)

            # Set previous values
            self.database = Database()
            self.searchResults = self.database.Search(id)

            tkinter.Label(self.window, text=self.searchResults[0][1], width=25).grid(pady=5, column=2, row=2)
            tkinter.Label(self.window, text=self.searchResults[0][2], width=25).grid(pady=5, column=2, row=3)
            tkinter.Label(self.window, text=self.searchResults[0][3], width=25).grid(pady=5, column=2, row=4)
            tkinter.Label(self.window, text=self.searchResults[0][4], width=25).grid(pady=5, column=2, row=5)
            tkinter.Label(self.window, text=self.searchResults[0][5], width=25).grid(pady=5, column=2, row=6)
            tkinter.Label(self.window, text=self.searchResults[0][6], width=25).grid(pady=5, column=2, row=7)
            tkinter.Label(self.window, text=self.searchResults[0][7], width=25).grid(pady=5, column=2, row=8)
            tkinter.Label(self.window, text=self.searchResults[0][8], width=25).grid(pady=5, column=2, row=9)
            tkinter.Label(self.window, text=self.searchResults[0][9], width=25).grid(pady=5, column=2, row=10)
            tkinter.Label(self.window, text=self.searchResults[0][10], width=25).grid(pady=5, column=2, row=11)
            tkinter.Label(self.window, text=self.searchResults[0][11], width=25).grid(pady=5, column=2, row=12)
            tkinter.Label(self.window, text=self.searchResults[0][12], width=25).grid(pady=5, column=2, row=13)

            # Fields
            # Entry widgets
            self.fNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.fName)
            self.lNameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lName)
            self.addressEntry = tkinter.Entry(self.window, width=25, textvariable=self.address)
            self.phoneEntry = tkinter.Entry(self.window, width=25, textvariable=self.phone)
            self.emailEntry = tkinter.Entry(self.window, width=25, textvariable=self.email)
            self.historyEntry = tkinter.Entry(self.window, width=25, textvariable=self.history)
            self.doctorEntry = tkinter.Entry(self.window, width=25, textvariable=self.doctor)

            self.fNameEntry.grid(pady=5, column=3, row=2)
            self.lNameEntry.grid(pady=5, column=3, row=3)
            self.addressEntry.grid(pady=5, column=3, row=8)
            self.phoneEntry.grid(pady=5, column=3, row=9)
            self.emailEntry.grid(pady=5, column=3, row=10)
            self.historyEntry.grid(pady=5, column=3, row=12)
            self.doctorEntry.grid(pady=5, column=3, row=13)

            # Combobox widgets
            self.dobBox = tkinter.ttk.Combobox(self.window, values=self.dateList, width=20)
            self.mobBox = tkinter.ttk.Combobox(self.window, values=self.monthList, width=20)
            self.yobBox = tkinter.ttk.Combobox(self.window, values=self.yearList, width=20)
            self.genderBox = tkinter.ttk.Combobox(self.window, values=self.genderList, width=20)
            self.bloodGroupBox = tkinter.ttk.Combobox(self.window, values=self.bloodGroupList, width=20)

            self.dobBox.grid(pady=5, column=3, row=4)
            self.mobBox.grid(pady=5, column=3, row=5)
            self.yobBox.grid(pady=5, column=3, row=6)
            self.genderBox.grid(pady=5, column=3, row=7)
            self.bloodGroupBox.grid(pady=5, column=3, row=11)

            # Button widgets
            tkinter.Button(self.window, width=20, text="Update", command=self.Update).grid(pady=15, padx=5, column=1,
                                                                                           row=14)
            tkinter.Button(self.window, width=20, text="Reset", command=self.Reset).grid(pady=15, padx=5, column=2,
                                                                                         row=14)
            tkinter.Button(self.window, width=20, text="Close", command=self.window.destroy).grid(pady=15, padx=5,
                                                                                                  column=3,
                                                                                                  row=14)

            self.window.mainloop()

        def Update(self):
            self.database = Database()
            self.database.Update(self.fNameEntry.get(), self.lNameEntry.get(), self.dobBox.get(), self.mobBox.get(),
                                 self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(),
                                 self.phoneEntry.get(),
                                 self.emailEntry.get(), self.bloodGroupBox.get(), self.historyEntry.get(),
                                 self.doctorEntry.get(), self.id)
            tkinter.messagebox.showinfo("Updated data", "Successfully updated the above data in the database")

        def Reset(self):
            self.fNameEntry.delete(0, tkinter.END)
            self.lNameEntry.delete(0, tkinter.END)
            self.dobBox.set("")
            self.mobBox.set("")
            self.yobBox.set("")
            self.genderBox.set("")
            self.addressEntry.delete(0, tkinter.END)
            self.phoneEntry.delete(0, tkinter.END)
            self.emailEntry.delete(0, tkinter.END)
            self.bloodGroupBox.set("")
            self.historyEntry.delete(0, tkinter.END)
            self.doctorEntry.delete(0, tkinter.END)

    class DatabaseView:
        def __init__(self, data):
            self.databaseViewWindow = tkinter.Tk()
            self.databaseViewWindow.wm_title("Database View")

            # Label widgets
            tkinter.Label(self.databaseViewWindow, text="Database View Window", width=25).grid(pady=5, column=1, row=1)

            self.databaseView = tkinter.ttk.Treeview(self.databaseViewWindow)
            self.databaseView.grid(pady=5, column=1, row=2)
            self.databaseView["show"] = "headings"
            self.databaseView["columns"] = (
                "id", "fName", "lName", "dob", "mob", "yob", "gender", "address", "phone", "email", "bloodGroup",
                "history",
                "doctor")

            # Treeview column headings
            self.databaseView.heading("id", text="ID")
            self.databaseView.heading("fName", text="First Name")
            self.databaseView.heading("lName", text="Last Name")
            self.databaseView.heading("dob", text="D.O.B")
            self.databaseView.heading("mob", text="M.O.B")
            self.databaseView.heading("yob", text="Y.O.B")
            self.databaseView.heading("gender", text="Gender")
            self.databaseView.heading("address", text="Home Address")
            self.databaseView.heading("phone", text="Phone Number")
            self.databaseView.heading("email", text="Email ID")
            self.databaseView.heading("bloodGroup", text="Blood Group")
            self.databaseView.heading("history", text="History")
            self.databaseView.heading("doctor", text="Doctor")

            # Treeview columns
            self.databaseView.column("id", width=40)
            self.databaseView.column("fName", width=100)
            self.databaseView.column("lName", width=100)
            self.databaseView.column("dob", width=60)
            self.databaseView.column("mob", width=60)
            self.databaseView.column("yob", width=60)
            self.databaseView.column("gender", width=60)
            self.databaseView.column("address", width=200)
            self.databaseView.column("phone", width=100)
            self.databaseView.column("email", width=200)
            self.databaseView.column("bloodGroup", width=100)
            self.databaseView.column("history", width=100)
            self.databaseView.column("doctor", width=100)

            for record in data:
                self.databaseView.insert('', 'end', values=record)

            self.databaseViewWindow.mainloop()

    class SearchDeleteWindow:
        def __init__(self, task):
            window = Toplevel()
            window.wm_title(task + " data")

            # Initializing all the variables
            self.id = tkinter.StringVar()
            self.fName = tkinter.StringVar()
            self.lName = tkinter.StringVar()
            self.heading = "Please enter Patient ID to " + task

            # Labels
            tkinter.Label(window, text=self.heading, width=50).grid(pady=20, row=1)
            tkinter.Label(window, text="Patient ID", width=10).grid(pady=5, row=2)

            # Entry widgets
            self.idEntry = tkinter.Entry(window, width=5, textvariable=self.id)

            self.idEntry.grid(pady=5, row=3)

            # Button widgets
            if task == "Search":
                tkinter.Button(window, width=20, text=task, command=self.Search).grid(pady=15, padx=5, column=1, row=14)
            elif task == "Delete":
                tkinter.Button(window, width=20, text=task, command=self.Delete).grid(pady=15, padx=5, column=1, row=14)

        def Search(self):
            self.database = Database()
            self.data = self.database.Search(self.idEntry.get())
            self.databaseView = DatabaseView(self.data)

        def Delete(self):
            self.database = Database()
            self.database.Delete(self.idEntry.get())

    class HomePage:
        def __init__(self):
            self.homePageWindow = tkinter.Tk()
            self.homePageWindow.wm_title("Patient Information System")

            tkinter.Label(self.homePageWindow, text="Home Page", width=100).grid(pady=20, column=1, row=1)

            tkinter.Button(self.homePageWindow, width=20, text="Insert", command=self.Insert).grid(pady=15, column=1,
                                                                                                   row=2)
            tkinter.Button(self.homePageWindow, width=20, text="Update", command=self.Update).grid(pady=15, column=1,
                                                                                                   row=3)
            tkinter.Button(self.homePageWindow, width=20, text="Search", command=self.Search).grid(pady=15, column=1,
                                                                                                   row=4)
            tkinter.Button(self.homePageWindow, width=20, text="Delete", command=self.Delete).grid(pady=15, column=1,
                                                                                                   row=5)
            tkinter.Button(self.homePageWindow, width=20, text="Display", command=self.Display).grid(pady=15, column=1,
                                                                                                     row=6)
            tkinter.Button(self.homePageWindow, width=20, text="Exit", command=self.homePageWindow.destroy).grid(
                pady=15,
                column=1,
                row=7)

            self.homePageWindow.mainloop()

        def Insert(self):
            self.insertWindow = InsertWindow()

        def Update(self):
            self.updateIDWindow = tkinter.Tk()
            self.updateIDWindow.wm_title("Update data")

            # Initializing all the variables
            self.id = tkinter.StringVar()

            # Label
            tkinter.Label(self.updateIDWindow, text="Enter the ID to update", width=50).grid(pady=20, row=1)

            # Entry widgets
            self.idEntry = tkinter.Entry(self.updateIDWindow, width=5, textvariable=self.id)

            self.idEntry.grid(pady=10, row=2)

            # Button widgets
            tkinter.Button(self.updateIDWindow, width=20, text="Update", command=self.updateID).grid(pady=10, row=3)

            self.updateIDWindow.mainloop()

        def updateID(self):
            self.updateWindow = UpdateWindow(self.idEntry.get())
            self.updateIDWindow.destroy()

        def Search(self):
            self.searchWindow = SearchDeleteWindow("Search")

        def Delete(self):
            self.deleteWindow = SearchDeleteWindow("Delete")

        def Display(self):
            self.database = Database()
            self.data = self.database.Display()
            self.displayWindow = DatabaseView(self.data)

    window = HomePage()


def openReminders():
    import tkinter
    import threading
    from tkinter import messagebox
    import sys
    global WorkingList
    global rootreminder
    tasks = []
    timer = threading
    real_timer = threading
    ok_thread = True

    def getting_tasks(event=""):
        work = todo.get()
        hour = int(time.get())
        todo.delete(0, tkinter.END)
        time.delete(0, tkinter.END)
        todo.focus_set()
        adding_record(work, hour)

        if hour < 999:
            updating_record()

    def adding_record(work, hrs):
        tasks.append([work, hrs])
        clock = threading.Timer(hrs, proceed_time, [work])
        clock.start()

    def updating_record():
        if WorkingList.size() >= 999:
            WorkingList.delete(0, "end")

    for task in tasks:
        WorkingList.insert("end", "" + task[0] + "=======&gt;&gt;&gt; Time left: " + str(task[1]) + " Seconds")

    def proceed_time(task):
        tkinter.messagebox.showinfo("Notification", "Its Now the Time for : " + task)

    def actual_time():
        if ok_thread:
            real_timer = threading.Timer(1.0, actual_time)
            real_timer.start()

    for task in tasks:

        if task[1] == 0:
            tasks.remove(task)
            task[1] -= 1
            updating_record()

    if __name__ == '__main__':
        # application
        rootreminder = tkinter.Tk()
        rootreminder.geometry("460x480")
        rootreminder.title("IAN To do List Reminder")
        rootreminder.rowconfigure(0, weight=1)
        rootreminder.config(bg="grey")

        frame = tkinter.Frame(rootreminder)
        frame.pack()

    lbl = tkinter.Label(rootreminder, text="Enter Tasks To Do:", fg="white", bg="blue",
                        font=('Arial', 14), wraplength=200)
    lbl_hrs = tkinter.Label(rootreminder, text="Enter time (Seconds)", fg="white",
                            bg="blue", font=('Arial', 14), wraplength=200)
    todo = tkinter.Entry(rootreminder, width=30, font=('Arial', 14))
    time = tkinter.Entry(rootreminder, width=15, font=('Arial', 14))
    post = tkinter.Button(rootreminder, text='Add task', fg="white", bg='green',
                          font=('Arial', 16), relief="ridge", bd=5, height=3, width=30, command=getting_tasks)
    Exit = tkinter.Button(rootreminder, text='Exit', fg="white", bg='red', height=3,
                          font=('Arial Bold', 14), relief="ridge", bd=5, width=30, command=rootreminder.destroy)
    WorkingList = tkinter.Listbox(rootreminder, font=('Arial', 12

                                                      ))
    if tasks != "":
        actual_time()

    rootreminder.bind('&lt;Return&gt;', getting_tasks)

    lbl.place(x=0, y=10, width=200, height=25)
    lbl_hrs.place(x=235, y=10, width=200, height=25)
    todo.place(x=20, y=40, width=160, height=25)
    time.place(x=245, y=40, width=170, height=25)
    post.place(x=62, y=80, width=100, height=25)
    Exit.place(x=302, y=80, width=50, height=25)
    WorkingList.place(x=20, y=120, width=395, height=300)

    rootreminder.mainloop()
    ok_thread = False
    sys.exit("FINISHED")


def openAlarm():
    # import library

    import time
    from playsound import playsound

    # display window
    root = Tk()
    root.geometry('400x300')
    root.resizable(0, 0)
    root.config(bg='blanched almond')
    root.title('TechVidvan - Countdown Clock And Timer')
    Label(root, text='Countdown Clock and Timer', font='arial 20 bold', bg='papaya whip').pack()

    # display current time#######################

    Label(root, font='arial 15 bold', text='current time :', bg='papaya whip').place(x=40, y=70)

    # fun to display current time
    def clock():
        clock_time = time.strftime('%H:%M:%S %p')
        curr_time.config(text=clock_time)
        curr_time.after(1000, clock)

    curr_time = Label(root, font='arial 15 bold', text='', fg='gray25', bg='papaya whip')
    curr_time.place(x=190, y=70)
    clock()

    # timer countdown

    # storing seconds
    sec = StringVar()
    Entry(root, textvariable=sec, width=2, font='arial 12').place(x=250, y=155)
    sec.set('00')

    # storing minutes
    mins = StringVar()
    Entry(root, textvariable=mins, width=2, font='arial 12').place(x=225, y=155)
    mins.set('00')

    # storing hours
    hrs = StringVar()
    Entry(root, textvariable=hrs, width=2, font='arial 12').place(x=200, y=155)
    hrs.set('00')

    # fun to start countdown

    def countdown():
        times = int(hrs.get()) * 3600 + int(mins.get()) * 60 + int(sec.get())
        while times > -1:
            minute, second = (times // 60, times % 60)

            hour = 0
            if minute > 60:
                hour, minute = (minute // 60, minute % 60)

            sec.set(second)
            mins.set(minute)
            hrs.set(hour)

            root.update()
            time.sleep(1)

            if times == 0:
                playsound('Loud_Alarm_Clock_Buzzer.mp3')
                sec.set('00')
                mins.set('00')
                hrs.set('00')
            times -= 1

    Label(root, font='arial 15 bold', text='set the time', bg='papaya whip').place(x=40, y=150)

    Button(root, text='START', bd='5', command=countdown, bg='antique white', font='arial 10 bold').place(x=150, y=210)

    root.mainloop()


def openGallery():
    from PIL import ImageTk, Image
    from tkinter import messagebox
    window_gallery = Toplevel(rootmain)
    window_gallery.title("Ian gallerry")
    window_gallery.geometry('200x100')

    intr_message = '''A Python tkinter project with sqlite.
    This Voting System helps to cast votes to candidates 
    and view the poll results You can create polls,
    vote in them and view their results. We have used
    tkinter,sqlite & matplotlib library. You can also
    project the results in a pie-chart format. Sqlite is
     used to create databases and manage the data.

    When you create a new poll, a new database is
     created to store the casted votes. 
     I have created a sample poll: 'myelection' 
     which incudes 3 candidates'''

    # mingi
    my_img1 = ImageTk.PhotoImage(Image.open("Images/iane (6).jpg"), width=50, height=20)  # locatiomof folder
    my_img2 = ImageTk.PhotoImage(Image.open("Images/iane (2).png"), width=50, height=20)  # locatiomof folder
    my_img3 = ImageTk.PhotoImage(Image.open("Images/iane (4).png"), width=50, height=20)  # locatiomof folder
    my_img4 = ImageTk.PhotoImage(Image.open("Images/iane (7).jpg"), width=50, height=20)  # locatiomof folder
    my_img5 = ImageTk.PhotoImage(Image.open("Images/iane (9).jpg"), width=50, height=20)  # locatiomof folder
    my_img6 = ImageTk.PhotoImage(Image.open("Images/iane (8).jpg"), width=50, height=20)  # locatiomof folder

    image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6]

    status = Label(window_gallery)

    my_label = Label(image=my_img1)
    my_label.grid(column=0, columnspan=3, row=0)

    def forward(image_number):
        global my_label
        global button_forward
        global button_back

        my_label.grid_forget()
        my_label = Label(image=image_list[image_number - 1])
        my_label.grid(column=0, columnspan=3, row=0)

        button_forward = Button(window_gallery, text=">>", command=lambda: forward(image_number + 1))
        button_back = Button(window_gallery, text="<<", command=lambda: back(image_number - 1))

        if image_number == int(len(image_list)):
            button_forward = Button(window_gallery, text=">>", state=DISABLED)

        button_forward.grid(row=1, column=2)
        button_back.grid(row=1, column=0)

        status = Label(window_gallery, text="image" + str(image_number) + "OF" + str(len(image_list)), bd=1,
                       relief=SUNKEN,
                       anchor=E)

        status.grid(column=2, columnspan=3, row=2, sticky=W + E)

    def back(image_number):
        global my_label
        global button_forward
        global button_back

        my_label.grid_forget()
        my_label = Label(image=image_list[image_number - 1])
        my_label.grid(column=0, columnspan=3, row=0)

        button_forward = Button(window_gallery, text=">>", command=lambda: forward(image_number + 1))
        button_back = Button(window_gallery, text="<<", command=lambda: back(image_number - 1))

        if image_number == 1:
            button_back = Button(window_gallery, text="<<", state=DISABLED)
            my_label.grid(row=0, column=0, columnspan=3)
            button_forward.grid(row=1, column=2)
            button_back.grid(row=1, column=0)

        status = Label(window_gallery, text="image" + str(image_number) + "OF" + str(len(image_list)), bd=1,
                       relief=SUNKEN,
                       anchor=E)

        status.grid(column=2, columnspan=3, row=2, sticky=W + E)

    button_back = Button(window_gallery, text="<<", command=back, state=DISABLED)
    button_exit = Button(window_gallery, text="EXIT", command=window_gallery.quit, fg="orange", bg="red")

    button_forward = Button(window_gallery, text=">>", command=lambda: forward(2))

    button_back.grid(row=1, column=0, pady=10, padx=10, ipadx=5)
    button_exit.grid(row=1, column=1, pady=10, padx=10, ipadx=5)
    button_forward.grid(row=1, column=2, pady=10, padx=10, ipadx=5)

    status.grid(row=4, column=2, columnspan=3, sticky=W + E)

    def popup():

        response = messagebox.askyesno("This is my pop up", "Hello ian")  # title and msg
        response_label = Label(window_gallery, text=response).grid()
        if response == 1:
            Label(window_gallery, text="You clicked YES").grid()
        else:
            Label(window_gallery, text="You clicked NO").grid()

    pop_btn = Button(window_gallery, text="POPUP", command=lambda: popup(), bg="green")
    pop_btn.grid(row=4, column=0)


def openPassword():
    # importing the tkinter module

    # importing the pyperclip module to use it to copy our generated
    # password to clipboard
    import pyperclip

    # random module will be used in generating the random password
    import random

    # initializing the tkinter

    # rootmain.withdraw()
    global password_window
    password_window = Toplevel(rootmain)
    password_window.title('Generate passsword')

    # setting the width and height of the gui
    password_window.geometry("400x400")  # x is small case here

    # declaring a variable of string type and this variable will be
    # used to store the password generated
    passstr = StringVar()

    # declaring a variable of integer type which will be used to
    # store the length of the password entered by the user
    passlen = IntVar()

    # setting the length of the password to zero initially
    passlen.set(0)

    # function to generate the password
    def generate():
        # storing the keys in a list which will be used to generate
        # the password
        pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
                 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
                 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&',
                 '*', '(', ')']

        # declaring the empty string
        password = " "

        # loop to generate the random password of the length entered
        # by the user
        for x in range(passlen.get()):
            password = password + random.choice(pass1)

        # setting the password to the entry widget
        passstr.set(password)

    # function to copy the password to the clipboard
    def copytoclipboard():
        random_password = passstr.get()
        pyperclip.copy(random_password)

    # Creating a text label widget
    Label(password_window, text="Password Generator Application", font="calibri 20 bold").pack()

    # Creating a text label widget
    Label(password_window, text="Enter password length").pack(pady=3)

    # Creating a entry widget to take password length entered by the
    # user
    Entry(password_window, textvariable=passlen).pack(pady=3)

    # button to call the generate function
    Button(password_window, text="Generate Password", command=lambda: generate()).pack(pady=7)

    # entry widget to show the generated password
    Entry(password_window, textvariable=passstr).pack(pady=3)

    # button to call the copytoclipboard function
    Button(password_window, text="Copy to clipboard", command=copytoclipboard).pack()

    # mainloop() is an infinite loop used to run the application when
    # it's in ready state


def openVoting():
    from tkinter import ttk
    from tkinter import messagebox

    import sqlite3 as sqltor
    import matplotlib.pyplot as plt
    conn = sqltor.connect('main.db')  # main database
    cursor = conn.cursor()  # main cursor
    cursor.execute("""CREATE TABLE IF NOT EXISTS poll
                        (name)""")

    def pollpage():  # page for polling
        def proceed():
            chose = choose.get()
            print(chose)
            command = 'update polling set votes=votes+1 where name=?'
            pd.execute(command, (chose,))
            pd.commit()
            messagebox.showinfo('Success!', 'You have voted')

        choose = StringVar()
        names = []
        pd = sqltor.connect(plname + '.db')  # poll database
        pcursor = pd.cursor()  # poll cursor
        pcursor.execute('select name from polling')
        data = pcursor.fetchall()
        for i in range(len(data)):
            data1 = data[i]
            ndata = data1[0]
            names.append(ndata)
        print(names)
        ppage = Toplevel()
        ppage.geometry('300x300')
        ppage.title('Poll')

        Label(ppage, text='Vote for any one person!').grid(row=1, column=3)
        i = ""
        for i in range(len(names)):
            Radiobutton(ppage, text=names[i], value=names[i], variable=choose).grid(row=2 + i, column=1)
        Button(ppage, text='Vote', command=proceed).grid(row=2 + i + 1, column=2)

    def polls():  # mypolls
        def proceed():
            global plname
            plname = psel.get()
            if plname == '-select-':
                return messagebox.showerror('Error', 'select poll')
            else:
                mpolls.destroy()
                pollpage()

        cursor.execute('select name from poll')
        data = cursor.fetchall()
        pollnames = ['-select-']
        for i in range(len(data)):
            data1 = data[i]
            ndata = data1[0]
            pollnames.append(ndata)
        psel = StringVar()
        mpolls = Toplevel()
        mpolls.geometry('270x200')
        mpolls.title('Voting Program')
        Label(mpolls, text='Select Poll', font='Helvetica 12 bold').grid(row=1, column=3)
        select = ttk.Combobox(mpolls, values=pollnames, state='readonly', textvariable=psel)
        select.grid(row=2, column=3)
        select.current(0)
        Button(mpolls, text='Proceed', command=proceed).grid(row=2, column=4)

    def create():
        def proceed():
            global pcursor
            pname = name.get()  # pollname
            can = cname.get()  # candidatename
            if pname == '':
                return messagebox.showerror('Error', 'Enter poll name')
            elif can == '':
                return messagebox.showerror('Error', 'Enter candidates')
            else:
                candidates = can.split(',')  # candidate list
                command = 'insert into poll (name) values (?);'
                cursor.execute(command, (pname,))
                conn.commit()
                pd = sqltor.connect(pname + '.db')  # poll database
                pcursor = pd.cursor()  # poll cursor
                pcursor.execute("""CREATE TABLE IF NOT EXISTS polling
                     (name TEXT,votes INTEGER)""")
                for i in range(len(candidates)):
                    command = 'insert into polling (name,votes) values (?, ?)'
                    data = (candidates[i], 0)
                    pcursor.execute(command, data)
                    pd.commit()
                pd.close()
                messagebox.showinfo('Success!', 'Poll Created')
                cr.destroy()

        name = StringVar()
        cname = StringVar()
        cr = Toplevel()
        cr.geometry('500x400')
        cr.title('Create a new poll')
        Label(cr, text='Enter Details', font='Helvetica 12 bold').grid(row=1, column=2)
        Label(cr, text='Enter Poll name: ').grid(row=2, column=1)
        Entry(cr, width=30, textvariable=name).grid(row=2, column=2)  # poll name
        Label(cr, text='(eg: captain elections)').place(x=354, y=25)
        Label(cr, text='Enter Candidates: ').grid(row=3, column=1)
        Entry(cr, width=45, textvariable=cname).grid(row=3, column=2)  # candidate name
        Label(cr, text='Note: Enter the candidate names one by one by putting commas').grid(row=4, column=2)
        Label(cr, text='eg: candidate1,candate2,candidate3....').grid(row=5, column=2)
        Button(cr, text='Proceed', command=proceed).grid(row=6, column=2)

    def selpl():  # pollresults
        def results():
            global i
            sel = sele.get()  # selected option
            if sel == '-select-':
                return messagebox.showerror('Error', 'Select Poll')
            else:
                pl.destroy()

                def project():
                    names = []
                    votes = []
                    for i in range(len(r)):
                        data = r[i]
                        names.append(data[0])
                        votes.append(data[1])
                        plt.title('Poll Result')
                    plt.pie(votes, labels=names, autopct='%1.1f%%', shadow=True, startangle=140)
                    plt.axis('equal')
                    plt.show()

                res = Toplevel()  # result-page
                res.geometry('300x300')
                res.title('Results!')
                Label(res, text='Here is the Result!', font='Helvetica 12 bold').grid(row=1, column=2)
                con = sqltor.connect(sel + '.db')
                pcursor = con.cursor()
                pcursor.execute('select * from polling')
                r = pcursor.fetchall()  # data-raw
                for i in range(len(r)):
                    data = r[i]
                    Label(res, text=data[0] + ': ' + str(data[1]) + ' votes').grid(row=2 + i, column=1)
                Button(res, text='Project Results', command=project).grid(row=2 + i + 1, column=2)

        cursor.execute('select name from poll')
        data = cursor.fetchall()
        pollnames = ['-select-']
        for i in range(len(data)):
            data1 = data[i]
            ndata = data1[0]
            pollnames.append(ndata)
        sele = StringVar()
        pl = Toplevel()
        pl.geometry('300x200')
        pl.title('Voting System')
        Label(pl, text='Select Poll', font='Helvetica 12 bold').grid(row=1, column=1)
        sel = ttk.Combobox(pl, values=pollnames, state='readonly', textvariable=sele)
        sel.grid(row=2, column=1)
        sel.current(0)
        Button(pl, text='Get Results', command=results).grid(row=2, column=2)

    def about():
        messagebox.showinfo('About', 'Developed by IAN')

    home = Toplevel(rootmain)
    home.geometry('400x400')
    home.title('Voting system')
    home['bg'] = '#49A'
    intr_message = '''A Python tkinter project with sqlite.
    This Voting System helps to cast votes to candidates 
    and view the poll results You can create polls,
    vote in them and view their results. We have used
    tkinter,sqlite & matplotlib library. You can also
    project the results in a pie-chart format. Sqlite is
     used to create databases and manage the data.

    When you create a new poll, a new database is
     created to store the casted votes. 
     I have created a sample poll: 'myelection' 
     which incudes 3 candidates'''

    Label(home, text='voting program made in python', font='Helvetica 12 bold', bg='#49A').grid(row=1, column=2)
    Button(home, text='Create new Poll +', command=create).grid(row=3, column=2)
    Button(home, text='My Polls', command=polls).grid(row=6, column=2)
    Button(home, text='Poll Results', command=selpl).grid(row=8, column=2)
    Label(home, text="The peoples choice", bg='#49A').grid(row=9, column=2)
    Label(home, text='Instagram:https://www.instagram.com/_iande_/', bg='#49A').grid(row=10, column=2)
    Button(home, text='About', command=about).grid(row=1, column=3)
    ian3 = Label(home, text="click READ ME for more")
    ian3.grid(column=1, row=7)

    def clicked():

        ian3.configure(text=intr_message, fg="orange")

    bt = Button(home, text="READ ME", command=clicked, bg="white", fg="red")
    bt.grid(column=1, row=5)
    home.mainloop()


def openCalendar():
    calendar_window = Toplevel(rootmain)
    calendar_window.title('Ian calendar')

    calendar_window.geometry("600x400")

    cal = Calendar(calendar_window, selectmode="day", year=2020, month=5, day=22)
    cal.pack(pady=20)

    # cal.pack(fill="both", expand=True)

    def date():
        my_label.config(text=cal.get_date())

    my_button = Button(calendar_window, text="Get date", command=date, bg="green")
    my_button.pack(pady=10)

    my_label = Label(calendar_window, text="")
    my_label.pack(pady=20)

    # ----------- main project------------------------------------------------------------------------------------------------------------------


# Add some buttons
bt_student_info = Button(rootmain, text="STUDENT INFO", command=openNewWindow, fg="white", bg="green")
bt_student_info.grid(row=20, column=1, columnspan=3, pady=10, padx=10, ipadx=3)

bt_instr = Button(rootmain, text="README", command=myClickentry, fg="white", bg="cyan")
bt_instr.grid(row=21, column=1, columnspan=3, pady=10, padx=10, ipadx=18)

bt_medical = Button(rootmain, text="MEDICAL", command=openMedical, fg="white", bg="orange")
bt_medical.grid(row=22, column=1, columnspan=3, pady=10, padx=10, ipadx=17)

bt_reminder = Button(rootmain, text="REMINDERS", command=openReminders, fg="white", bg="magenta")
bt_reminder.grid(row=24, column=1, columnspan=3, pady=10, padx=10, ipadx=10)

bt_alarm = Button(rootmain, text="ALARM", command=openAlarm, fg="white", bg="black")
bt_alarm.grid(row=25, column=1, columnspan=3, pady=10, padx=10, ipadx=22)

bt_gallery = Button(rootmain, text="GALLERY", command=openGallery, fg="white", bg="pink")
bt_gallery.grid(row=26, column=1, columnspan=3, pady=10, padx=10, ipadx=19)

bt_password = Button(rootmain, text="PASSWORD", command=openPassword, fg="white", bg="yellow")
bt_password.grid(row=27, column=1, columnspan=3, pady=10, padx=10, ipadx=10)

bt_exit = Button(rootmain, text="EXIT", command=rootmain.quit, fg="white", bg="red")
bt_exit.grid(row=29, column=5, columnspan=3, pady=10, padx=350, ipadx=30)

bt_voting = Button(rootmain, text="ELECTIONS", command=openVoting, fg="white", bg="maroon")
bt_voting.grid(row=28, column=1, columnspan=3, pady=10, padx=10, ipadx=13)

bt_cal = Button(rootmain, text="CALENDAR", command=openCalendar, fg="white", bg="skyblue")
bt_cal.grid(row=29, column=1, columnspan=3, pady=10, padx=10, ipadx=13)

bt_school = Button(rootmain, text="SCHOOL", command=click_openStudent, fg="white", bg="purple")
bt_school.grid(row=20, column=3, columnspan=3, pady=10, padx=250, ipadx=25)

bt_Accomodation = Button(rootmain, text="ACCOMODATION", command=click_Accomodation, fg="white", bg="lime")
bt_Accomodation.grid(row=21, column=3, columnspan=3, pady=10,padx=250, ipadx=2)

rootmain.mainloop()

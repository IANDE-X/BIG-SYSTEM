# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
rootmain = Tk()

# sets the geometry of main
# root window
rootmain.geometry("700x200")


# function to open a new window
# on a button click
def openNewWindow():
    # Toplevel object which will
    # be treated as a new window
    root = Toplevel(rootmain)

    # sets the title of the
    # Toplevel widget
    root.title("New Window")

    # sets the geometry of toplevel
    root.geometry("200x200")

    # A Label widget to show in toplevel
    Label(root,
          text="This is a new window").pack()


label = Label(rootmain,
              text="This is the main window")

label.pack(pady=10)

# a button widget which will open a
# new window on button click
btn = Button(rootmain,
             text="Click to open a new window",
             command=openNewWindow)
btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()
#

from tkinter import *

rootmain = Tk()
rootmain.title('Designed by Ian')

rootmain.geometry("800x500")

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
    instruction_label.grid(row=13, column=1)


# Create a label
my_label = Label(rootmain, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)
# Add something to the top of our image
my_text = Label(rootmain, text="Kenyans in Debrecen!", font=("Helvetica", 30), fg="red",bg="#2a1863")

my_text.grid(row=2, column=4)


# Create Edit function to update a record
def enter():
    rootmain = Tk()
    rootmain.withdraw()
    root = Tk()
    root.title('Student Database - Kenyans in Debrecen!')

    root.geometry("400x600")


# Add some buttons
bt_entry = Button(rootmain, text="ENTER", command=enter, fg="white", bg="green")
bt_entry.grid(row=20, column=1, pady=10, padx=10, )

bt_instr = Button(rootmain, text="README", command=myClickentry, fg="white", bg="cyan")
bt_instr.grid(row=20, column=2, pady=10, padx=10)

bt_exit = Button(rootmain, text="EXIT", command=rootmain.quit, fg="white", bg="red")
bt_exit.grid(row=20, column=3, pady=10, padx=10)
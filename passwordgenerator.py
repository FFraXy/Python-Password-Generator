# Importing the libraries
from tkinter import *
from tkinter import messagebox
import random
import string

# Creating the password generator itself
def passwordGenerator():
    try:
        passwordLength = int(textInput.get())
        if passwordLength <= 5:
            raise ValueError("The password length must be more than 5.")
    except ValueError:
        return
    # Checking if checkboxes are checkmarked or not 
    characters = ""
    if mark1.get() == True:
        characters += string.ascii_lowercase
    if mark2.get() == True:
        characters += string.ascii_uppercase
    if mark3.get() == True:
        characters += string.digits
    if not characters:
        label2.config(text="We suggest you to checkmark all 3 checkboxes to make a strong password.")
    # Generating the password
    password = "".join(random.choice(characters) for _ in range(passwordLength))
    label3.delete(0,END)
    label3.insert(0,password)

# Creating the copy to clipboard feature
def copy_to_clipboard():
    password = label3.get()
    if password == "":
        label2.config(text="You didn't generated the password.")
    else:
        app.clipboard_clear()
        app.clipboard_append(password)
        app.update()
        messagebox.showinfo("Success!", "Your password has been copied to clipboard")

# Setting up the main app window
app = Tk()
app.geometry("400x400")
app.title("Python Password Generator")

# Creating the marks
mark1 = BooleanVar()
mark2 = BooleanVar()
mark3 = BooleanVar()

# Creating the checkboxes
checkbox1 = Checkbutton(app, text="Use uppercase letters", variable=mark1)
checkbox2 = Checkbutton(app, text="Use capital letters", variable=mark2)
checkbox3 = Checkbutton(app, text="Use numbers", variable=mark3)

# Creating the buttons
btn = Button(app, text="Generate the Password", command=passwordGenerator)
label = Label(app, text="Write the password length you would like.")
label2 = Label(app, text="For a good strong password, checkmark all 3 checkboxes.")
label3 = Entry(app, text="Your generated password will be here.")
textInput = Entry(app, width=20)
copytoClipboard = Button(app, text="Copy the password", command=copy_to_clipboard)

# Calling the stuff i made
label.pack()
textInput.pack()
checkbox1.pack(anchor="w")
checkbox2.pack(anchor="w")
checkbox3.pack(anchor="w")
copytoClipboard.pack(pady=5)
btn.pack()
label3.pack()
label2.pack(side=BOTTOM, pady=25)

app.mainloop()
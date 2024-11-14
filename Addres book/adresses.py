from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter import messagebox 

window = Tk()
window.geometry("500x525")

myAddressBook={}

def update():
    key = nameinput.get()
    myAddressBook[key] = (addressinput.get(),mobileinput.get(),emailinput.get(),birthdayinput.get())
    listboxadres.insert(END,key)
    
def display(event):
    newwindow = Toplevel(window)
    
    index = listboxadres.curselection()
    contact = ""
    key = listboxadres.get(index)
    details = myAddressBook[key]
    contact = "Address : " +details[0]+"\n" + "Mobile : " +details[1]+"\n" + "Email: " +details[2]+"\n" + "Birthday : " +details[3]+"\n"
    
    contactshow = Label(newwindow)
    contactshow.grid(row = 0, column = 0)
    
    contactshow.config(text = contact)

def save():
    f = asksaveasfile(defaultextension = ".txt")
    print(myAddressBook,file = f)

def open():
    op = askopenfile(title = "dialogopen")
    if op: 
        myAddressBook = eval(op.read())
        for key in myAddressBook.keys():
            listboxadres.insert(END,key)
        booknameopen.configure(text = os.path.basename(op.name))
            
            
            
listboxadres = Listbox(window, width = 25, height = 19)
listboxadres.bind("<<ListboxSelect>>", display)

booknameopen = Label(window,text = "")
booknameopen.grid(row = 0, column = 0)

myadresbook = Label(window, text = "My address book")
name = Label(window,text = "Name", font =('calibri',17,'bold'))
address = Label(window,text = "Address", font =('calibri',17,'bold'))
mobile = Label(window,text = "Mobile", font =('calibri',17,'bold'))
email = Label(window,text = "Email", font =('calibri',17,'bold'))
birthday = Label(window,text = "Birthday", font =('calibri',17,'bold'))

nameinput = Entry(window)
addressinput = Entry(window)
mobileinput = Entry(window)
emailinput = Entry(window)
birthdayinput = Entry(window)

openbutton = Button(window,text = "Open", command = open)
editbutton = Button(window,text = "Edit")
deletebutton = Button(window,text = "Delete")
updateaddbutton = Button(window,text = "Update/Add", command = update)
savebutton = Button(window,text = "Save", command = save)

#labels
myadresbook.place(x = 150 , y = 30)
name.place(x = 290 , y = 90 )
address.place(x = 290 , y = 150)
mobile.place(x = 290, y = 220)
email.place(x = 290, y = 280 )
birthday.place(x = 290 , y = 340)

#buttons
openbutton.place(x = 270, y = 30)
editbutton.place(x = 30 , y = 400)
deletebutton.place(x = 80 , y = 400)
updateaddbutton.place(x = 420 , y = 400)
savebutton.place(x = 70 , y = 420)


#listbox
listboxadres.place(x = 30 , y = 60)

#entry
nameinput.place(x = 350, y = 90)
addressinput.place(x = 350 , y = 150)
mobileinput.place(x = 350 , y = 220)
emailinput.place(x = 350 , y = 280)
birthdayinput.place(x = 350 , y = 340)


window.mainloop()
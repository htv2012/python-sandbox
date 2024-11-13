from tkinter import *

# root = None
# namentry = None
# addressentry = None
# name = None
# address = None
uri_entry = None

def perform_rest() :
    global uri_entry
    print(('\n\nuri_entry: %s' % uri_entry))
    uri = uri_entry.get()
    print(('uri: %s' % uri))

root = Tk()
Label(root, text="&URI:").grid(row=0, sticky=W)
Label(root, text="User:").grid(row=1, sticky=W)
Label(root, text="Password:").grid(row=2, sticky=W)

uri_entry = Entry(root)
uri_entry.grid(row=0, column=1)
user_entry = Entry(root)
user_entry.grid(row=1, column=1)
password_entry = Entry(root)
password_entry.grid(row=2, column=1)

# Add an ok and cancel button
Button(root, text="Get", command=perform_rest).grid(row=8, column=0)
Button(root, text="Post", command=perform_rest).grid(row=8, column=1)
Button(root, text="Put", command=perform_rest).grid(row=8, column=2)
Button(root, text="Delete", command=perform_rest).grid(row=8, column=3)

root.mainloop()

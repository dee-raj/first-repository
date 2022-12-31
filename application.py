from tkinter import *
root=Tk()
root.title("VARTAK COLLEGE OF science")
root.geometry("500x500")

Label(root,text="Admission form",font="BOLD 35").grid(row=0,column=3)
# Entry(root).grid(row=0,column=3)

Label(root,text="Full Name").grid(row=1,column=2)
Entry(root).grid(row=1,column=3)

Label(root,text="Photo id proof").grid(row=2,column=2)
Entry(root).grid(row=2,column=3)

Label(root,text="Age").grid(row=3,column=2)
Entry(root).grid(row=3,column=3)

Label(root,text="email id").grid(row=4,column=2)
Entry(root).grid(row=4,column=3)

Label(root,text="Address").grid(row=5,column=2)
Entry(root).grid(row=5,column=3)

Label(root,text="Gender").grid(row=6,column=2)
Radiobutton(root,text="Male",value=1).grid(row=6,column=3)
Radiobutton(root,text="Female",value=2).grid(row=7,column=3)

Label(root,text="Qulification").grid(row=8,column=2)
Checkbutton(root,text="SSC").grid(row=8,column=3)
Checkbutton(root,text="HSC").grid(row=9,column=3)
Checkbutton(root,text="FYCS").grid(row=10,column=3)
Checkbutton(root,text="SYCS").grid(row=11,column=3)
Checkbutton(root,text="TYCS").grid(row=12,column=3)

def save():
    print("You have successfully submitted the application form.")
def quit():
    print("QUIT")
    import sys; sys.exit(quit)
Button(root,text="submit",bg="green",command=save,relief=SUNKEN).grid(row=13,column=2)
Button(root,text="exit",bg="red",command=quit,relief=RIDGE).grid(row=13,column=4)

root.mainloop()
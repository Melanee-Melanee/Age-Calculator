from tkinter import *
from datetime import date

root = Tk()
root.geometry('650x500')
root.title('Age Calculator')

def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntery.get()))
    age = today.year - birthDate.year - ((today.month,
                                   today.day) < (birthDate.month, birthDate.day))

    Label(text = f"{nameValue.get()} your age is {age}").grid(row=6, column=1)


Label(text = 'Name').grid(row=1, column=0, padx=90)
Label(text='Year').grid(row=2, column=0)
Label(text='Month').grid(row=3, column=0)
Label(text = 'Day').grid(row=4, column=0)
nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()
nameEntry = Entry(root, textvariable=nameValue)
yearEntry = Entry(root, textvariable=yearValue)
monthEntry = Entry(root, textvariable=monthValue)
dayEntery = Entry(root, textvariable=dayValue)
nameEntry.grid(row=1, column=1, pady=10)
yearEntry.grid(row=2, column=1, pady= 10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntery.grid(row=4, column=1, pady=10)
Button(text='Calculate age', command=calculateAge).grid(row=5, column= 1, pady=10)

root.mainloop()


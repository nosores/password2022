from tkinter import * 
import random
import string 

def generatePassword():
    lst=[]
    for i in range(1,13):
        alphabet_lower=list(string.ascii_lowercase)
        alphabet_upper=list(string.ascii_uppercase)
        alphabet_symbols=list(string.punctuation)
        str=alphabet_lower+alphabet_upper+alphabet_symbols
        character=random.choice(str)
        lst.append(character)
    a="".join(lst)
    print(a)
    Label.config(text=a)
windows = Tk()

windows.title("Generador de Password")

windows.geometry("500x500")

windows.resizable(0,0)

my_button = Button(windows, text='Generar',font='arial 15 bold',command=generatePassword).pack()
my_label=Label(windows, text='').pack()
exit_button=Button(windows,text='Salir', font='arial 15 bold',command=windows.destroy).pack()
my_label=Label(windows, text='').pack()
label_et=Label(windows,text="Este es el password : ")
label_et.pack()
Label=Label(windows,text="",font="arial 15 bold")
Label.pack()

windows.mainloop()

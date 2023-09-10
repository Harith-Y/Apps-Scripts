import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tmb
from fractions import Fraction

def F_fn(input1):
	z = float(input1.get())
	m = Fraction(z).limit_denominator()	
	tmb.showinfo(title="Fraction",message=m)
	
	return()
	
def D_fn(input2,input3):
	N = float(input2.get())
	D = float(input3.get())
	a = Fraction(N/D)
	tmb.showinfo(title="Decimal",message=float(a))
	
	return()
	
root = tk.Tk()

label1 = ttk.Label(master=root,text = "Enter a Decimal to convert into Fraction : ")
label1.grid(row=0,column=0)

entry1 = ttk.Entry(master=root)
entry1.grid(row=0,column=1)

button1 = ttk.Button(master=root,text="Convert")
button1.grid(row=1,column=0,columnspan=2,sticky='nsew')
button1.configure(command=lambda:F_fn(entry1))



label2 = ttk.Label(master=root,text = "Enter Numerator of Fraction to convert into Decimal : ")
label2.grid(row=3,column=0)

entry2 = ttk.Entry(master=root)
entry2.grid(row=3,column=1)

label3 = ttk.Label(master=root,text = "Enter Numerator of Fraction to convert into Decimal : ")
label3.grid(row=4,column=0)

entry3 = ttk.Entry(master=root)
entry3.grid(row=4,column=1)

button2 = ttk.Button(master=root,text="Convert")
button2.grid(row=5,column=0,columnspan=2,sticky='nsew')
button2.configure(command=lambda:D_fn(entry2,entry3))


root.mainloop()
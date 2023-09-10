import tkinter as tk
import tkinter.messagebox as tmb
import tkinter.ttk as ttk


def fact(num):

	factorial = 1
	if num < 0:
	   tmb.showerror(title="Error !",message="Factorial does not exist for negative numbers in the real world. Of Course it exists in the complex world !")
	elif num == 0:
		factorial = 1
	else:
	   for i in range(1,num + 1):
	       factorial = factorial*i
	return(factorial)

def permutation(input1,input2):
	n = int(input1.get())
	r = int(input2.get())

	if n >= 0 and r >= 0:
		if (n-r) >= 0 :
			x = fact(n)/fact(n-r)
			tmb.showinfo(title = "{} Permute {}".format(n,r),message="Number of ways of Arranging/Permuting {} out of {} is {}".format(n,r,x))

		else :
			tmb.showerror(title="Error !",message="Total ways must be greater than permuting ways i.e. n({}) must be greater than r({}). But the given values are not obeying the rule.".format(n,r))

	else:
		tmb.showerror(title="Error !",message="Factorial does not exist for negative numbers in the real world. Of Course it exists in the complex world !")

def combination(input1,input2):
	n = int(input1.get())
	r = int(input2.get())

	if n >= 0 and r >= 0:
		if (n-r) >= 0 :
			x = fact(n)/(fact(r)*fact(n-r))
			tmb.showinfo(title = "{} Choose {}".format(n,r),message="Number of ways of choosing {} out of {} ways is {}".format(n,r,x))

		else :
			tmb.showerror(title="Error !",message="Total ways must be greater than Combining ways i.e. n({}) must be greater than r({}). But the given values are not obeying the rule.".format(n,r))

	else:
		tmb.showerror(title="Error !",message="Factorial does not exist for negative numbers in the real world. Of Course it exists in the complex world !")		

root = tk.Tk()
root.title("Permutations And Combinations")

label1 = ttk.Label(master=root,text="Enter value of n : ")
label1.grid(row=0,column=0)

entry1 = ttk.Entry(master=root)
entry1.grid(row=0,column=1)

label2 = ttk.Label(master=root,text="Enter value of r : ")
label2.grid(row=1,column=0)

entry2 = ttk.Entry(master=root)
entry2.grid(row=1,column=1)

calc_button1 = ttk.Button(master=root,text="Calculate nPr")
calc_button1.grid(row=2,column=0)
calc_button1.configure(command=lambda:permutation(entry1,entry2))

calc_button2 = ttk.Button(master=root,text="Calculate nCr")
calc_button2.grid(row=2,column=1)
calc_button2.configure(command=lambda:combination(entry1,entry2))


root.mainloop()
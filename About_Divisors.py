import time
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tmb
import threading

M = 1000000007

timing = time.localtime()
time_string = time.strftime("%d-%B-%Y, %I:%M:%S %p", timing)

def div(input0,div_file,button):
	def FN():
		button.state(["disabled"])
		n = int(input0.get())

		print("App was Started at {}.".format(time_string),file=div_file)

		if n > 1:
			print("\nDivisors of {} are : ".format(n),file=div_file)
			for i in range(1,n+1):
				if (n%i == 0):
					time.sleep(0)
					print(i,file=div_file)
			print("\n",file=div_file)

		else:
			print("There are no possible factors for {}. \n".format(n),file=div_file)
		button.state(["disabled"])
		return()
	t1 = threading.Thread(target=FN,daemon=True)
	t1.start()
	return()
div_file = open("Divisors.txt","a+")

def countdiv(input0,button):
	def FN():
		button.state(["disabled"])
		tmb.showinfo(title="Wait",message="Please Wait !")
		n = int(input0.get())
		if n > 1:
			for i in range(n):
				x = len([i for i in range(1,n+1) if not n % i])

			tmb.showinfo(message="Number of Divisors of {} is {}.\nThe Divisors Of {} are saved in Divisors.txt.".format(n,x,n))
		else:
			tmb.showerror(title="Error !",message="Sorry ! Number of Divisors cannot be Calculated for {}".format(n))
		button.state(["!disabled"])
		return()

	t1 = threading.Thread(target=FN,daemon=True)
	t1.start()
	return()
def combine_fn(button):
	div(entry0,div_file,button)
	countdiv(entry0,button)

def sumdiv(input1):
	n = int(input1.get())
	if n > 1:
		divisors = [1]
		for i in range(2, n + 1):
			if (n % i)==0:
				divisors.append(i)
				x = sum(divisors)

		tmb.showinfo(message="The Sum of The Divisors of {} is {}".format(n,x))
	else:
		tmb.showerror(title="Error !",message="Sorry ! Sum of Divisors cannot be Calculated for {}".format(n))

def proddiv(input2):

	n = int(input2.get())
	if n > 1:
		prod = 1
		i = 1
		while i * i <= n:
			if (n % i == 0):
				# If factors are equal, # multiply only once
				if (n / i == i):
					prod = (prod * i) % M
					#Otherwise multiply both
				else:
					prod = (prod * i) % M
					prod = (prod * n / i) % M
			i = i + 1
		tmb.showinfo(message="Product of the Divisors of {} is {}".format(n,prod))
	else:
		tmb.showerror(title="Error !",message="Sorry ! We Cannot get the Product of Divisors for {}".format(n))

# def help_fn():
# 	tmb.showinfo(title="Note : ",message="If you open 'Divisors.txt' file, you will get the required Divisors of the input given in the first input box. After viewing 'Divisors.txt', if you want to clear the information in it, just delete the file 'Divisors.txt'. After each time you run the first button, 'Divisors.txt' will automatically be generated whenever deleted only. If not deleted, the new outputs will be appended in 'Divisors.txt'.")

root = tk.Tk()
root.title("Enter An Positive Integer only")

label0 = ttk.Label(master=root,text="Enter a Number to Find Number Of Divisors Of :")
label0.grid(row=0,column=0)
entry0 = ttk.Entry(master=root)
entry0.grid(row=0,column=1)
button0 = ttk.Button(master=root,text="Calculate",command=lambda:combine_fn(button0))
button0.grid(row=0,column=2)

label1 = ttk.Label(master=root,text=" Enter a Number to Find Sum Of Divisors Of       : ")
label1.grid(row=1,column=0)
entry1 = ttk.Entry(master=root)
entry1.grid(row=1,column=1)
button1 = ttk.Button(master=root,text="Calculate")
button1.grid(row=1,column=2)
button1.configure(command=lambda:sumdiv(entry1))

label2 = ttk.Label(master=root,text="Enter a Number to Find Product Of Divisors Of : ")
label2.grid(row=2,column=0)
entry2 = ttk.Entry(master=root)
entry2.grid(row=2,column=1)
button2 = ttk.Button(master=root,text="Calculate")
button2.grid(row=2,column=2)
button2.configure(command=lambda:proddiv(entry2))

# help_button = ttk.Button(master=root,text="Help !",command=help_fn)
# help_button.grid(row=3,column=0,columnspan=3,sticky='nsew')

root.mainloop()

div_file.close()
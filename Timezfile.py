import time
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tmb

def fn(inputs1,inputs2,timez_file):

# x = int(input("Enter A Number : "))
# y = str(input("Enter the Sentence : "))
	x = int(inputs1.get())
	y = str(inputs2.get())

	timie = time.localtime()
	timeis = time.strftime("%d-%B-%Y, %I:%M:%S %p", timie)

	print("App was Started at {}".format(timeis),file=timez_file)

	for i in range(x + 1):
		time.sleep(0)
		print(y,file = timez_file)

	print("Done",file=timez_file)
	tmb.showinfo(message="Done")

	return()

timez_file = open("Timezfile.txt","a+")

root = tk.Tk()

label1 = ttk.Label(master=root,text="Enter Number of Times : ")
label1.grid(row=0,column=0)

entry1 = ttk.Entry(master=root)
entry1.grid(row=0,column=1)

label2 = ttk.Label(master=root,text="Enter the Sentence : ")
label2.grid(row=1,column=0)

entry2 = ttk.Entry(master=root)
entry2.grid(row=1,column=1)

Finity_Button = ttk.Button(master=root,text="Click me")
Finity_Button.grid(row=2,column=0,columnspan=2,sticky='nsew')

Finity_Button.configure(command=lambda:fn(entry1,entry2,timez_file))


root.mainloop()


timez_file.close()
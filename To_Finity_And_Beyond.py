import time
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tmb


time.sleep(0.5)

def fn(Finity_file,input1,input2):

    timing = time.localtime()
    time_string = time.strftime("%d-%B-%Y, %I:%M:%S %p", timing)


    print("App was Started at {}".format(time_string),file=Finity_file)

    a = int(input1.get())
    ii = float(input2.get())

    if ii > 1 or ii < 0:
        tmb.showinfo(message="Timegap is preferable between 0 to 1")
    tmb.showinfo(message="Starting")
    if ii > 0 or ii == 0:
        for i in range(a+1):
            time.sleep(ii)
            print(i,file=Finity_file)
        tmb.showinfo(message="Done")
    else:
        tmb.showerror(message="Time gap cannot be negative")

    return()

Finity_file = open("Finity.txt","a+")

root = tk.Tk()

label1 = ttk.Label(master=root,text="Ending Number : ")
label1.grid(row=0,column=0)

entry1 = ttk.Entry(master=root)
entry1.grid(row=0,column=1)

label2 = ttk.Label(master=root,text="Time Gap : ")
label2.grid(row=1,column=0)

entry2 = ttk.Entry(master=root)
entry2.grid(row=1,column=1)

Finity_Button = ttk.Button(master=root,text="Click me")
Finity_Button.grid(row=2,column=0,columnspan=2,sticky='nsew')

Finity_Button.configure(command=lambda:fn(Finity_file,entry1,entry2))

root.mainloop()

Finity_file.close()



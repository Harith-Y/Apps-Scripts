import math
from fractions import Fraction
import tkinter as tk
import tkinter.messagebox as tmb
import tkinter.ttk as ttk

def ANGLE_COEFF (inputs):

    a1 = inputs[0]
    b1 = inputs[1]
    c1 = inputs[2]
    a2 = inputs[3]
    b2 = inputs[4]
    c2 = inputs[5]

    m1 = (-1)*(a1/b1)
    m2 = (-1)*(a2/b2)

    x = (m1) - (m2)
    y = 1 + ((m1)*(m2))
    z = x/y
    zz = Fraction(z).limit_denominator()
    aa = math.atan(z)

    a = math.degrees(aa)
    result = [zz,aa,a]
    result_name = ["tanθ","Angle Between The Two Given Lines In Radians","Angle between The Two Given Lines In Degrees"]
    return(result_name,result)



labels_list = [["a1","b1","c1","a2","b2","c2"]]

def BUTTON_FN (calc_fn,label_list):

    def CALC_FN (entry_list):

        inputs = []
        for i in range(len(entry_list)):
            try:
                inputs += [float(entry_list[i].get())]
            except:
                tmb.showerror(message="Please enter a valid number for {}".format(labels_list[i]))

        result_name,result = calc_fn(inputs)

        result_message = ""
        for i in range(len(result)):
            result_message += "{} = {}\n".format(result_name[i],result[i])

        tmb.showinfo(message=result_message)
        return()

    window = tk.Tk()
    window.title("Enter Values")

    entry_list = []
    for i in range(len(label_list)):
        random_label = ttk.Label(master=window,text=label_list[i])
        random_label.grid(row=i,column=0)
        random_entry = ttk.Entry(master=window)
        random_entry.grid(row=i,column=1)
        entry_list += [random_entry]

    calc_Button = ttk.Button(master=window,text="Calculate",command=lambda:CALC_FN(entry_list))
    calc_Button.grid(row=i+1,column=0,columnspan=2,sticky='nsew')

    window.mainloop()

    return()

root = tk.Tk()
root.title("Angle Finder")

Angle_Button = ttk.Button(master=root,text="Find the Angle",command=lambda:BUTTON_FN(ANGLE_COEFF,labels_list[0]))
Angle_Button.grid(row=0,column=0)

geo_button0_label = ttk.Label(master=root,text = "     Form of (a_n)x + (b_n)y + (c_n) = 0; ''_'' stands for subscript")
geo_button0_label.grid(row=0,column=1)


root.mainloop()

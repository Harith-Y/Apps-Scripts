import math
from fractions import Fraction
import tkinter as tk
import tkinter.messagebox as tmb
import tkinter.ttk as ttk

required = ["Distance Between two parallel lines","Length of Perpendicular from point(x1,y1) on the line ax + by + c = 0","Foot of Perpendicular from a point(x1,y1) to the line ax + by + c = 0","Image of a point with respect to the line ax + by + c = 0"]

def PARALLEL (inputs):
	a = inputs[0]
	b = inputs[1]
	c1 = inputs[2]
	c2 = inputs[3]
	
	d = c1 - c2
	f = ((a**2) + (b**2))**(0.5)
	if d > 0 or d == 0:
		m = d/f
		x2 = Fraction(m).limit_denominator()
		results = [m]
		result = [x2]
		result_names = ["Distance between two parallel lines"]
		return(result_names,results,result)
	else:
		m = (-1)*(d/f)
		x2 = Fraction(m).limit_denominator()
		results = [m]
		result = [x2]
		result_names = ["Distance between two parallel lines"]
		return(result_names,results,result)

def LENGTH (inputs):
	x1 = inputs[0]
	y1 = inputs[1]
	a = inputs[2]
	b = inputs[3]
	c = inputs[4]
	
	f = ((a**2) + (b**2))**(0.5)
	d = ((a)*(x1)) + ((b)*(y1)) + (c)
	g = d/f
	if g > 0 or g == 0:
		g = g
		x2 = Fraction(g).limit_denominator()
		results = [g]
		result_names = ["Length of the Perpendicular from a point(x1,y1) on the line"]
		result = [x2]
		return(result_names,results,result)

	else:
		k = (-1)*(g)
		x2 = Fraction(k).limit_denominator()
		results = [k]
		result_names = ["Length of the Perpendicular from a point(x1,y1) on the line"]
		result = [x2]
		return(result_names,results,result)

def POINT (inputs):
	x1 = inputs[0]
	y1 = inputs[1]
	a = inputs[2]
	b = inputs[3]
	c = inputs[4]
	
	d = (a**2) + (b**2)
	f = ((a)*(x1)) + ((b)*(y1)) + (c)
	
	x = x1 - ((a*f)/d)
	y = y1 - ((b*f)/d)
	
	x2 = Fraction(x).limit_denominator()
	y2 = Fraction(y).limit_denominator()
	results = [x,y]
	result_names = ["x Co-Ordinate of foot of the Perpendicular from a point(x1,y1) on the line","y Co-Ordinate of foot of the Perpendicular from a point(x1,y1) on the line"]
	result = [x2,y2]
	return(result_names,results,result)

def IMAGE (inputs):
	x1 = inputs[0]
	y1 = inputs[1]
	a = inputs[2]
	b = inputs[3]
	c = inputs[4]
	
	d = (a**2) + (b**2)
	f = ((a)*(x1)) + ((b)*(y1)) + (c)
	
	x = (((-2)*(a)*(f))/d) + x1
	y = (((-2)*(b)*(f))/d) + y1
	
	x2 = Fraction(x).limit_denominator()
	y2 = Fraction(y).limit_denominator()
	result_names = ["x Co-ordinate of Image of a point with respect to a line","y Co-ordinate of Image of a point with respect to a line"]
	results = [x,y]
	result = [x2,y2]
	return(result_names,results,result)
	
calc_fns = [PARALLEL,LENGTH,POINT,IMAGE]
labels_list = [["Coefficient of x","Coefficient of y","Constant1","Constant2"],["x Co-Ordinate of point","y Co-Ordinate of point","Coefficient of x","Coefficient of y","Constant"],["x Co-Ordinate of point","y Co-Ordinate of point","Coefficient of x","Coefficient of y","Constant"],["x Co-Ordinate of point","y Co-Ordinate of point","Coefficient of x","Coefficient of y","Constant"]]

def BUTTON_FN (calc_fn,label_list) :

    def CALC_FN (entry_list):

        inputs = []
        for i in range(len(entry_list)):
            try:
                inputs += [float(entry_list[i].get())]
            except:
                tmb.showerror(message="Please enter valid number for {}".format(label_list[i]))

        result_names,results,result = calc_fn(inputs)

        result_message = ""
        for i in range(len(results)):
            result_message += "{} = {} = {}\n".format(result_names[i],results[i],result[i])

        tmb.showinfo(message=result_message)

        return()

    swindow = tk.Tk()
    swindow.title("Enter Inputs")

    entry_list = []
    for i in range(len(label_list)):
        label_widget = ttk.Label(master=swindow,text=label_list[i])
        label_widget.grid(row=i,column=0)
        entry_widget = ttk.Entry(master=swindow)
        entry_widget.grid(row=i,column=1)
        entry_list += [entry_widget]

    calc_button = ttk.Button(master=swindow,text="Calculate",command=lambda:CALC_FN(entry_list))
    calc_button.grid(row=i+1,column=0,columnspan=2,sticky='nsew')

    swindow.mainloop()
    
        
root = tk.Tk()
root.title("CG 9 and 10")          

geo_button0 = ttk.Button(master=root,text=required[0],command=lambda:BUTTON_FN(calc_fns[0],labels_list[0]))
geo_button0.grid(row=0,column=0)

geo_button1 = ttk.Button(master=root,text=required[1],command=lambda:BUTTON_FN(calc_fns[1],labels_list[1]))
geo_button1.grid(row=1,column=0)

geo_button2 = ttk.Button(master=root,text=required[2],command=lambda:BUTTON_FN(calc_fns[2],labels_list[2]))
geo_button2.grid(row=2,column=0)

geo_button3 = ttk.Button(master=root,text=required[3],command=lambda:BUTTON_FN(calc_fns[3],labels_list[3]))
geo_button3.grid(row=3,column=0)

root.mainloop()                              
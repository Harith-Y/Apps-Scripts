import math
import tkinter as tk
import tkinter.messagebox as tmb
import tkinter.ttk as ttk

calculations = ["Circumcentre","Orthocentre","In-Centre","Centroid","Ex-Centres"]

def CIRCUMCENTRE (inputs):
    x1 = inputs[0]
    y1 = inputs[1]
    x2 = inputs[2]
    y2 = inputs[3]
    x3 = inputs[4]
    y3 = inputs[5]

    m1 = (y3 - y1)/(x3 - x1)
    m2 = (y3 - y2)/(x3 - x2)
    m3 = (y2 - y1)/(x2 - x1)

    if m1 != m2 and m2 != m3 and m1 != m3:
        x4 = (((m2)*(x1 +x2)) - ((m1)*(x2 + x3)) + ((m1)*(m2)*(y1 - y3)))/(2*(m2 - m1))
        y4 = (((m1)*(y1 + y2)) - ((m2)*(y2 + y3)) + x1 - x3)/(2*(m1 - m2))

        results = [x4,y4]
        result_names = ["x Co-ordinate of the Circumcentre","y Co-ordinate of the Circumcentre"]
        return(result_names,results)

    else:
        tmb.showerror(title = "Error !",message="The given points cannot form a triangle !")

def ORTHOCENTRE (inputs):
    x1 = inputs[0]
    y1 = inputs[1]
    x2 = inputs[2]
    y2 = inputs[3]
    x3 = inputs[4]
    y3 = inputs[5]

    m1 = (y3 - y1)/(x3 - x1)
    m2 = (y3 - y2)/(x3 - x2)
    m3 = (y2 - y1)/(x2 - x1)

    if m1 != m2 and m2 != m3 and m1 != m3:
        x4 = (((m1)*(x1)) - ((m2)*(x2)) + ((m1)*(m2)*(y1 - y2)))/((m1 - m2))
        y4 = (((m2)*(y1)) - ((m1)*(y2)) + x1 - x2)/((m2 - m1))

        results = [x4,y4]
        result_names = ["x Co-ordinate of the Orthocentre","y Co-ordinate of the Orthocentre"]
        return(result_names,results)

    else:
        tmb.showerror(title = "Error !",message="The given points cannot form a triangle !")

def INCENTRE (inputs):

    x1 = inputs[0]
    y1 = inputs[1]
    x2 = inputs[2]
    y2 = inputs[3]
    x3 = inputs[4]
    y3 = inputs[5]

    m1 = (y3 - y1)/(x3 - x1)
    m2 = (y3 - y2)/(x3 - x2)
    m3 = (y2 - y1)/(x2 - x1)

    if m1 != m2 and m2 != m3 and m1 != m3:
        c = (((y2 - y1)**2) + ((x2 - x1)**2))**(0.5)
        a = (((y3 - y2)**2) + ((x3 - x2)**2))**(0.5)
        b = (((y3 - y1)**2) + ((x3 - x1)**2))**(0.5)
        Sum1 = (a + b + c)
        x = ((a*x1) + (b*x2) + (c*x3))/Sum1
        y = ((a*y1) + (b*y2) + (c*y3))/Sum1

        results = [x,y]
        result_names = ["x Co-ordinate of the In-Centre","y Co-ordinate of the In-Centre"]
        return(result_names,results)

    else:
        tmb.showerror(title = "Error !",message="The given points cannot form a triangle !")

def CENTROID (inputs):
    x1 = inputs[0]
    y1 = inputs[1]
    x2 = inputs[2]
    y2 = inputs[3]
    x3 = inputs[4]
    y3 = inputs[5]

    m1 = (y3 - y1)/(x3 - x1)
    m2 = (y3 - y2)/(x3 - x2)
    m3 = (y2 - y1)/(x2 - x1)

    if m1 != m2 and m2 != m3 and m1 != m3:
        x = (x1 + x2 + x3)/3
        y = (y1 + y2 + y3)/3

        results = [x,y]
        result_names = ["x Co-ordinate of the Centroid","y Co-ordinate of the Centroid"]
        return(result_names,results)

    else:
        tmb.showerror(title = "Error !",message="The given points cannot form a triangle !")

def EXCENTRES (inputs):

    x1 = inputs[0]
    y1 = inputs[1]
    x2 = inputs[2]
    y2 = inputs[3]
    x3 = inputs[4]
    y3 = inputs[5]

    m1 = (y3 - y1)/(x3 - x1)
    m2 = (y3 - y2)/(x3 - x2)
    m3 = (y2 - y1)/(x2 - x1)

    if m1 != m2 and m2 != m3 and m1 != m3:
        c = (((y2 - y1)**2) + ((x2 - x1)**2))**(0.5)
        a = (((y3 - y2)**2) + ((x3 - x2)**2))**(0.5)
        b = (((y3 - y1)**2) + ((x3 - x1)**2))**(0.5)
        x_a = (-(a*x1) + (b*x2) + (c*x3))/-(a + b + c)
        y_a = (-(a*y1) + (b*y2) + (c*y3))/(-a + b + c)
        x_b = ((a*x1) - (b*x2) + (c*x3))/(a - b + c)
        y_b = ((a*y1) - (b*y2) + (c*y3))/(a - b + c)
        x_c = ((a*x1) + (b*x2) - (c*x3))/(a + b - c)
        y_c = ((a*y1) + (b*y2) - (c*y3))/(a + b - c)

        results = [x_a,y_a,x_b,y_b,x_c,y_c]
        result_names = ["x Co-ordinate of Ex-centre opposite of vertex 1","y Co-ordinate of Ex-centre opposite of vertex 1","x Co-ordinate of Ex-centre opposite of vertex 2","y Co-ordinate of Ex-centre opposite of vertex 2","x Co-ordinate of Ex-centre opposite of vertex 3","y Co-ordinate of Ex-centre opposite of vertex 3"]
        return(result_names,results)

    else:
        tmb.showerror(title = "Error !",message="The given points cannot form a triangle !")

calc_fns = [CIRCUMCENTRE,ORTHOCENTRE,INCENTRE,CENTROID,EXCENTRES]
labels_list = [["x Co-ordinate of vertex 1","y Co-ordinate of vertex 1","x Co-ordinate of vertex 2","y Co-ordinate of vertex 2","x Co-ordinate of vertex 3","y Co-ordinate of vertex 3"],["x Co-ordinate of vertex 1","y Co-ordinate of vertex 1","x Co-ordinate of vertex 2","y Co-ordinate of vertex 2","x Co-ordinate of vertex 3","y Co-ordinate of vertex 3"],["x Co-ordinate of vertex 1","y Co-ordinate of vertex 1","x Co-ordinate of vertex 2","y Co-ordinate of vertex 2","x Co-ordinate of vertex 3","y Co-ordinate of vertex 3"],["x Co-ordinate of vertex 1","y Co-ordinate of vertex 1","x Co-ordinate of vertex 2","y Co-ordinate of vertex 2","x Co-ordinate of vertex 3","y Co-ordinate of vertex 3"],["x Co-ordinate of vertex 1","y Co-ordinate of vertex 1","x Co-ordinate of vertex 2","y Co-ordinate of vertex 2","x Co-ordinate of vertex 3","y Co-ordinate of vertex 3"]]

def BUTTON_FN (calc_fn,label_list) :

    def CALC_FN (entry_list):

        inputs = []
        for i in range(len(entry_list)):
            try:
                inputs += [float(entry_list[i].get())]
            except:
                tmb.showerror(message="Please enter valid number for {}".format(label_list[i]))

        result_names,results = calc_fn(inputs)

        result_message = ""
        for i in range(len(results)):
            result_message += "{} = {}\n".format(result_names[i],results[i])

        tmb.showinfo(message=result_message)

        return()

    swindow = tk.Tk()
    swindow.title("Calculating...")

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
root.title("Circumcentre Calculator")

#Circumcentre
geo_button0 = ttk.Button(master=root,text=calculations[0],command=lambda:BUTTON_FN(calc_fns[0],labels_list[0]))
geo_button0.grid(row=0,column=0)

#Orthocentre
geo_button1 = ttk.Button(master=root,text=calculations[1],command=lambda:BUTTON_FN(calc_fns[1],labels_list[1]))
geo_button1.grid(row=1,column=0)

#In-Centre
geo_button2 = ttk.Button(master=root,text=calculations[2],command=lambda:BUTTON_FN(calc_fns[2],labels_list[2]))
geo_button2.grid(row=2,column=0)

#Centroid
geo_button3 = ttk.Button(master=root,text=calculations[3],command=lambda:BUTTON_FN(calc_fns[3],labels_list[3]))
geo_button3.grid(row=3,column=0)

#Ex-Centres
geo_button4 = ttk.Button(master=root,text=calculations[4],command=lambda:BUTTON_FN(calc_fns[4],labels_list[4]))
geo_button4.grid(row=4,column=0)

root.mainloop()

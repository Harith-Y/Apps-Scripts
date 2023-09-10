import math
import tkinter as tk
import tkinter.messagebox as tmb
import tkinter.ttk as ttk

required = ["FIND VERTICES OF A TRIANGLE","CONCURRENCY TEST"]
# The equations of sides of a triangle is given by:
# (a1)x + (b1)y + (c1) = 0
# (a2)x + (b2)y + (c2) = 0
# (a3)x + (b3)y + (c3) = 0
def FIND_VERTICES (inputs):
    a1 = inputs[0]
    b1 = inputs[1]
    c1 = inputs[2]
    a2 = inputs[3]
    b2 = inputs[4]
    c2 = inputs[5]
    a3 = inputs[6]
    b3 = inputs[7]
    c3 = inputs[8]
    #Making calculations easy :
    m1 = (b1/a1)
    m2 = (b2/a2)
    n1 = (c1/a1)
    n2 = (c2/a2)
    ac1 = (c1*a3) - (c3*a1)
    ac2 = (c1*a2) - (c2*a1)
    ac3 = (c2*a3) - (c3*a2)
    ab1 = (b1*a3) - (b3*a1)
    ab2 = (b1*a2) - (b2*a1)
    ab3 = (b2*a3) - (b3*a2)

    #Co-Ordinates of A :
    x1 = m1*(ac1/ab1) - n1
    y1 = (-1)*(ac1/ab1)

    #Co-Ordinates of B :
    x2 = m1*(ac2/ab2) - n1
    y2 = (-1)*(ac2/ab2)

    #Co-Ordinates of C :
    x3 = m2*(ac3/ab3) - n2
    y3 = (-1)*(ac3/ab3)

    results = [x1,y1,x2,y2,x3,y3]
    result_names = ["x Co-ordinate of Vertex 1","y Co-ordinate of Vertex 1","x Co-ordinate of Vertex 2","y Co-ordinate of Vertex 2","x Co-ordinate of Vertex 3","y Co-ordinate of Vertex 3"]

    return(result_names,results)

def CONCURRENCY (inputs):
    a1 = inputs[0]
    b1 = inputs[1]
    c1 = inputs[2]
    a2 = inputs[3]
    b2 = inputs[4]
    c2 = inputs[5]
    a3 = inputs[6]
    b3 = inputs[7]
    c3 = inputs[8]

    x = (a1*((b2*c3)-(b3*c2))) - (b1*((a2*c3) - (a3*c2))) + (c1*((a2*b3) - (a3*b2)))

    if x == 0:
        tmb.showinfo(title="Concurrency Test",message="The Given Lines Are Concurrent")
    else:
        tmb.showerror(title="Error !",message="The Given Lines Are Not Concurrent")
    
calc_fns = [FIND_VERTICES,CONCURRENCY]
labels_list = [["a1","b1","c1","a2","b2","c2","a3","b3","c3"],["a1","b1","c1","a2","b2","c2","a3","b3","c3"]]

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
root.title("Finding Vertices")

geo_button0 = ttk.Button(master=root,text=required[0],command=lambda:BUTTON_FN(calc_fns[0],labels_list[0]))
geo_button0.grid(row=0,column=0)

geo_button0_label = ttk.Label(master=root,text = "Form of (a_n)x + (b_n)y + (c_n) = 0; ''_'' stands for subscript")
geo_button0_label.grid(row=0,column=1)

geo_button1 = ttk.Button(master=root,text=required[1],command=lambda:BUTTON_FN(calc_fns[1],labels_list[1]))
geo_button1.grid(row=1,column=0)

geo_button1_label = ttk.Label(master=root,text = "Form of (a_n)x + (b_n)y + (c_n) = 0; ''_'' stands for subscript")
geo_button1_label.grid(row=1,column=1)


root.mainloop()
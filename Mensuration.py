import math
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tmb

geometries = ["Hemisphere","Sphere","Cube","Cuboid","Cylinder","Hollow Cylinder","Cone","Frustum","Rectangular Prism","Square Prism","Triangular Prism","Other Prisms","Right Pyramid","Regular Tetrahedron","Regular Octahedron","Torus","Ellipsoid","Dodecahedron","Icosahedron"]

def HEMISPHERE (inputs):

    radius = inputs[0]
    if radius > 0:
        Lateral_Surface_area = 2*math.pi*(radius**2)
        Total_Surface_area = 3*math.pi*(radius**2)
        volume = (2/3)*math.pi*(radius**3)

        results = [Lateral_Surface_area, Total_Surface_area, volume]
        result_names = ["Lateral Surface area","Total Surface area","Volume"]

        return(result_names,results)

    else :
        tmb.showerror(title="Error !",message="Radius has to be positive")

def SPHERE (inputs):

    radius = inputs[0]
    if radius > 0:
        area = 4*math.pi*(radius**2)
        volume = (4/3)*math.pi*(radius**3)

        results = [area,volume]
        result_names = ["Area","Volume"]

        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Radius has to be positive !")

def CUBE (inputs):

    side = inputs[0]
    if side > 0:
        L_area = 4*(side**2)
        T_area = 6*(side**2)
        volume = side**3
        diagonal = side*(3**0.5)

        results = [L_area,T_area,volume,diagonal]
        result_names = ["Lateral Surface Area","Total Surface Area","Volume","Diagonal"]

        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Length of the Edge has to be positive !")

def CUBOID (inputs):
    Length = inputs[0]
    Breadth = inputs[1]
    Height = inputs[2]
    
    if Length > 0 and Breadth > 0 and Height > 0:
        L_area = 2*Height*(Length + Breadth)
        T_area = 2*((Length*Breadth)+(Breadth*Height)+(Length*Height))
        volume = Length*Breadth*Height
        diagonal = ((Length**2)+(Breadth**2)+(Height**2))**(0.5)

        results = [L_area,T_area,volume,diagonal]
        result_names = ["Lateral Surface Area","Total Surface Area","Volume","Diagonal"]

        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Inputs have to be positive !")

def CYLINDER (inputs):
    radius_of_base = inputs[0]
    height = inputs[1]

    if radius_of_base > 0 and height > 0:
        Curved_Surface_area = 2*(math.pi)*(radius_of_base)*(height)
        Total_Surface_area = (2*(math.pi)*(radius_of_base))*(radius_of_base + height)
        volume = (math.pi)*(radius_of_base**2)*(height)

        results = [Curved_Surface_area, Total_Surface_area, volume]
        result_names = ["Curved Surface area","Total Surface area","Volume"]
        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Radius of Base and Height have to be positive !")

def HOLLOW_CYLINDER (inputs):
    Internal_Radius = inputs[0]
    External_Radius = inputs[1]
    Height = inputs[2]
    #Just for Easy Calculation purposes, Calculating "Total Radius" value
    if Internal_Radius > 0 and External_Radius > 0 and Height > 0:
        Total_Radius = Internal_Radius + External_Radius
        Thickness = External_Radius - Internal_Radius
        volume = (math.pi)*(Height)*(Thickness)*(Total_Radius)
        Curved_Surface_area = 2*math.pi*Height*Total_Radius
        Total_Surface_area = 2*math.pi*Total_Radius*(Height + Thickness)
        Area_Of_Each_Base_Ring = (math.pi)*(Thickness)*(Total_Radius)

        if Internal_Radius >= External_Radius:
            tmb.showerror(title="Error !",message="Internal Radius Can Never Be Greater Than Or Equal To External Radius As Such A Hollow Cylinder Doesn't Exist.")
        else:
            results = [Thickness,volume,Curved_Surface_area,Total_Surface_area,Area_Of_Each_Base_Ring]
            result_names = ["Thickness","Volume","Curved Surface Area","Total Surface Area","Area Of Each Base Ring"]
        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Inputs have to be positive !")

def CONE (inputs):
    radius_of_base = inputs[0]
    Height = inputs[1]
    if radius_of_base > 0 and Height > 0:
        #Just for Easy Calculation purposes, Calculating "Slant Height" value
        Slant_height = ((Height**2)+(radius_of_base**2))**(0.5)
        Curved_Surface_area = math.pi*radius_of_base*Slant_height
        Total_Surface_area = (math.pi*radius_of_base)*(radius_of_base+Slant_height)
        volume =(1/3)*(math.pi)*(radius_of_base**2)*(Height)

        results = [Curved_Surface_area,Total_Surface_area,volume]
        result_names = ["Curved Surface Area","Total Surface Area","Volume"]
        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Radius of Base and Height have to be positive !")

#When a cone is cut with a plane parallel to it's base and remove the cone that is formed on one side of that plane, the part which is left over on the other side of the plane is called frustum of the cone.
def FRUSTUM (inputs):
    radius_of_lower_base = inputs[0]
    radius_of_upper_base = inputs[1]

    if radius_of_lower_base > 0 and radius_of_upper_base > 0:
        if radius_of_lower_base > radius_of_upper_base:
            x = radius_of_lower_base - radius_of_upper_base
        elif radius_of_lower_base < radius_of_upper_base:
                x = radius_of_upper_base - radius_of_lower_base
        if radius_of_upper_base == radius_of_lower_base:
            tmb.showerror(title="Error !",message="Such A Frustum Does Not Exist, The Given Values Pertain To Cylider !")

        SumRadius = ((radius_of_upper_base)**2) + ((radius_of_lower_base)**2) + (radius_of_lower_base)*(radius_of_upper_base)
        Height = inputs[2]
        Slant_height = ((Height**2)+(x**2))**(0.5)
        lateral_surface_area = math.pi*Slant_height*(radius_of_upper_base + radius_of_lower_base)
        Total_surface_area = lateral_surface_area + ((math.pi)*(((radius_of_upper_base)**2) + ((radius_of_lower_base)**2)))
        volume = (1/3)*math.pi*(Height)*(SumRadius)
        # center_of_gravity = ((Height)*(SumRadius + (2*(radius_of_upper_base**2)) + ((radius_of_lower_base)*(radius_of_upper_base))))/(4*SumRadius)

        results = [lateral_surface_area,Total_surface_area,volume]
        result_names = ["Lateral Surface Area","Total Surface Area","Volume"]
        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Both the Radii have to be positive !")

#There are different types of Prisms :

#Rectangular Prism is Cuboid Hence thought of Not mentioning, but if you want it...
def PRISM0 (inputs):
    Length = inputs[0]
    Breadth = inputs[1]
    Height = inputs[2]

    if Length > 0 and Breadth > 0 and Height > 0:
        L_area = 2*Height*(Length + Breadth)
        T_area = 2*((Length*Breadth)+(Breadth*Height)+(Length*Height))
        volume = Length*Breadth*Height
        diagonal = ((Length**2)+(Breadth**2)+(Height**2))**(0.5)

        results = [L_area,T_area,volume,diagonal]
        result_names = ["Lateral Surface Area","Total Surface Area","Volume","Diagonal"]

        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Inputs have to be positive !")

#Square Prism i.e Cube in which Length and Breadth are same and both different from Height values.
def PRISM1 (inputs):
    Base_edge = inputs[0]
    Height = inputs[1]

    if Base_edge > 0 and Height > 0:
        lateral_surface_area = (4*Base_edge*Height)
        Total_Surface_area = (((4*Base_edge)*(Height))+(2*(Base_edge**2)))
        volume = (Base_edge**2)*Height

        results = [lateral_surface_area,Total_Surface_area,volume]
        result_names = ["Lateral Surface Area","Total Surface Area","Volume"]

        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Base Edge and Height have to be positive !")

def PRISM2 (inputs):
    Height = inputs[0]
    s1 = inputs[1] #base_triangle_side1
    s2 = inputs[2] #base_triangle_side2
    s3 = inputs[3] #base_triangle_side3
    #sum1, s base_area are defined as to make calculations easier and coding faster

    if Height > 0 and s1 > 0 and s2 > 0 and s3 > 0:
        sum1 = s1 + s2 +s3
        s = (0.5)*(sum1)
        base_area = ((s)*(s-s1)*(s-s2)*(s-s3))**(0.5)
        lateral_surface_area = (Height)*(sum1)
        Total_surface_area = ((Height)*(sum1)) + 2*(base_area)
        volume = (base_area)*(Height)

        results = [lateral_surface_area,Total_surface_area,volume]
        result_names = ["Lateral Surface Area","Total Surface Area","Volume"]

        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Height and Sides of the Triangle have to be positive !")

def PRISM3 (inputs):
    perimetre_base = inputs[0]
    area_base = inputs[1]
    height = inputs[2]

    if perimetre_base > 0 and area_base > 0 and height > 0:
        lateral_surface_area = perimetre_base*height
        Total_surface_area = (perimetre_base*height) + (2*area_base)
        volume = area_base*height

        results = [lateral_surface_area,Total_surface_area,volume]
        result_names = ["Lateral Surface Area","Total Surface Area","Volume"]
        return(result_names,results)
    
    else:
        tmb.showerror(title="Error !",message="Inputs have to be positive !")

def RIGHT_PYRAMID (inputs):

    perimetre_base = inputs[0]
    area_base = inputs[1]
    height = inputs[2]
    Slant_height = inputs[3]

    if perimetre_base > 0 and area_base > 0 and height > 0 and Slant_height > 0:
        lateral_surface_area = (0.5)*perimetre_base*Slant_height
        Total_surface_area = ((0.5)*perimetre_base*Slant_height) + area_base
        volume = (1/3)*area_base*height

        results = [lateral_surface_area,Total_surface_area,volume]
        result_names = ["Lateral Surface Area","Total Surface Area","Volume"]
        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Inputs have to be positive !")

def REGULAR_TETRAHEDRON (inputs):
    a = inputs[0]
    if a > 0:
        height = a*((2/3)**(0.5))
        area = (1/4)*(3**(0.5))*(a**2)
        r_c = (1/4)*(6**(0.5))*a
        r_i = a/(24**(0.5))
        r_m = a/(8**(0.5))
        lateral_surface_area = 3*(1/4)*(3**(0.5))*(a**2)
        Total_surface_area = (3**(0.5))*(a**2)
        volume = (1/12)*(2**(0.5))*(a**3)

        results = [height,area,r_c,r_i,r_m,lateral_surface_area,Total_surface_area,volume]
        result_names = ["Height","Area Of Each Face","Circumradius","Inradius","Midradius","Lateral Surface Area","Total Surface Area","Volume"]
        return(result_names,results)
    else:
        tmb.showerror(title="Error !",message="Edge length has to be positive !")

def REGULAR_OCTAHEDRON (inputs):
    a = inputs[0]
    if a > 0:
        height = ((a**2) - ((a/2)**2))**(0.5)
        area = (1/4)*(3**(0.5))*(a**2)
        r_c = a/(2**(0.5))
        r_i = a/(6**(0.5))
        r_m = a/2
        Total_surface_area = 2*(3**(0.5))*(a**2)
        volume = (1/3)*(2**(0.5))*(a**3)

        results = [height,area,r_c,r_i,r_m,Total_surface_area,volume]
        result_names = ["Height","Area Of Each Face","Circumradius","Inradius","Midradius","Total Surface Area","Volume"]
        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Edge length has to be positive !")

def TORUS (inputs):

    r_out = inputs[0]
    r_in = inputs[1]

    if r_out > r_in and r_in > 0 and r_out > 0:
        Total_surface_area = ((math.pi)**2)*(r_out + r_in)*(r_out - r_in)
        volume = ((math.pi)**2)*(1/4)*(r_out + r_in)*((r_out - r_in)**2)

        results = [Total_surface_area,volume]
        result_names = ["Total Surface Area","Volume"]
        return(result_names,results)
    else :
        tmb.showerror(title="Error !",message="Outer Radius Cannot Be Equal Or Less Than The Inner Radius and both the values have to be positive.")

def ELLIPSOID (inputs):

    a = inputs[0]
    b = inputs[1]
    c = inputs[2]
    p = 1.6075
    Total_surface_area = 4*(math.pi)*(((((a**p)*(b**p)) + ((a**p)*(c**p)) + ((b**p)*(c**p)))/3)**(1/p))
    volume = (4/3)*(math.pi)*(a)*(b)*(c)

    results = [Total_surface_area,volume]
    result_names = ["Total Surface Area","Volume"]
    return(result_names,results)

#Dodecahedron is a regular polyhedron with 12 faces.
def DODECAHEDRON (inputs):

    a = inputs[0]
    if a > 0:
        area = ((25 + (10*(5**(0.5))))**(0.5))*(a**2)*(1/4)
        r_c = (a/4)*((3**(0.5)) + (15**(0.5)))
        r_i = (a)*((25 + (11*(5**(0.5))))/40)**(0.5)
        r_m = (a/4)*(3 + (5**(0.5)))
        Total_surface_area = ((25 + (10*(5**(0.5))))**(0.5))*(a**2)*(1/4)*(12)
        volume = (1/4)*(a**3)*(15 + (7*(5**(0.5))))

        results = [area,r_c,r_i,r_m,Total_surface_area,volume]
        result_names = ["Area of Each Face","Circumradius","Inradius","Midradius","Total Surface Area","Volume"]
        return(result_names,results)

    else:
        tmb.showerror(title="Error !",message="Input has to be positive !")

#Icosahedron is a regular polyhedron with 20 faces.
def ICOSAHEDRON (inputs):

    a = inputs[0]
    if a > 0:

        area = (1/4)*(3**(0.5))*(a**2)
        r_c = (a/4)*((10 + (2*(5**(0.5))))**(0.5))          #sin(72 degrees)*a
        r_i = (a/12)*((3*(3**(0.5))) + (15**(0.5)))
        r_m = (a/4)*(1 + (5**(0.5)))
        Total_surface_area = (5*(3**(0.5)))*(a**2)
        volume = (1/12)*(a**3)*(15 + (5*(5**(0.5))))

        results = [area,r_c,r_i,r_m,Total_surface_area,volume]
        result_names = ["Area of Each Face","Circumradius","Inradius","Midradius","Total Surface Area","Volume"]
        return(result_names,results)
    
    else:
        tmb.showerror(title="Error !",message="Input has to be positive !")


calc_fns = [HEMISPHERE,SPHERE,CUBE,CUBOID,CYLINDER,HOLLOW_CYLINDER,CONE,FRUSTUM,PRISM0,PRISM1,PRISM2,PRISM3,RIGHT_PYRAMID,REGULAR_TETRAHEDRON,REGULAR_OCTAHEDRON,TORUS,ELLIPSOID,DODECAHEDRON,ICOSAHEDRON]
labels_list = [["Radius"],["Radius"],["Side"],["Length","Breadth","Height"],["Radius Of Base","Height"],["Internal Radius","External Radius","Height"],["Radius Of Base","Height"],["Radius Of Lower Base","Radius Of Upper Base","Height"],["Length","Breadth","Height"],["Base Edge","Height"],["Height","BASE SIDE1","BASE SIDE2","BASE SIDE3"],["Perimetre Of Base","Area Of Base","Height"],["Perimetre Of Base","Area Of Base","Height","Slant Height"],["Length of Each Edge"],["Length of Each Edge"],["Outer Radius","Inner Radius"],["Radius of Ellipsoid along x-axis","Radius of Ellipsoid along y-axis","Radius of Ellipsoid along z-axis"],["Length of Each Edge"],["Length of Each Edge"]]


def BUTTON_FN (calc_fn,label_list):

    def CALC_FN (entry_list):

        inputs = []
        for i in range(len(entry_list)):
            try:
                inputs += [float(entry_list[i].get())]
            except:
                tmb.showerror(message="Please enter valid number for {}".format(label_list[i]))
            # print(inputs)
        #     print(float(entry_list[i].get()))
        # print(entry_list)
        result_names,results = calc_fn(inputs)
        # print(calc_fn(inputs))

        result_message = ""
        for i in range(len(results)):
            result_message += "{} = {}\n".format(result_names[i],results[i])

        tmb.showinfo(message=result_message)

        return()

    swindow = tk.Tk()
    swindow.title("Enter The Values")

    entry_list = []
    for i in range(len(label_list)):
        label_widget = ttk.Label(master=swindow,text=label_list[i])
        label_widget.grid(row=i,column=0)
        entry_widget = ttk.Entry(master=swindow)
        entry_widget.grid(row=i,column=1)
        entry_list += [entry_widget]

    calc_button = ttk.Button(master=swindow,text="Calculate",command=lambda:CALC_FN(entry_list))
    calc_button.grid(row=i+1,column=0,columnspan=3,sticky='nsew')

    swindow.mainloop()

    return()

root = tk.Tk()
root.title("Geometrical Calculations")

#Hemisphere
geo_button0 = ttk.Button(master=root,text=geometries[0],command=lambda:BUTTON_FN(calc_fns[0],labels_list[0]))
geo_button0.grid(row=0,column=0)

#Sphere
geo_button1 = ttk.Button(master=root,text=geometries[1],command=lambda:BUTTON_FN(calc_fns[1],labels_list[1]))
geo_button1.grid(row=1,column=0)

#Cube
geo_button2 = ttk.Button(master=root,text=geometries[2],command=lambda:BUTTON_FN(calc_fns[2],labels_list[2]))
geo_button2.grid(row=2,column=0)

#Cuboid
geo_button3 = ttk.Button(master=root,text=geometries[3],command=lambda:BUTTON_FN(calc_fns[3],labels_list[3]))
geo_button3.grid(row=3,column=0)

#Cylinder
geo_button4 = ttk.Button(master=root,text=geometries[4],command=lambda:BUTTON_FN(calc_fns[4],labels_list[4]))
geo_button4.grid(row=4,column=0)

#Hollow Cylinder
geo_button5 = ttk.Button(master=root,text=geometries[5],command=lambda:BUTTON_FN(calc_fns[5],labels_list[5]))
geo_button5.grid(row=5,column=0)

#Cone
geo_button6 = ttk.Button(master=root,text=geometries[6],command=lambda:BUTTON_FN(calc_fns[6],labels_list[6]))
geo_button6.grid(row=6,column=0)

#Frustum
geo_button7 = ttk.Button(master=root,text=geometries[7],command=lambda:BUTTON_FN(calc_fns[7],labels_list[7]))
geo_button7.grid(row=7,column=0)

#Rectangular Prism as PRISM0
geo_button8 = ttk.Button(master=root,text=geometries[8],command=lambda:BUTTON_FN(calc_fns[8],labels_list[8]))
geo_button8.grid(row=8,column=0)

#Square Prism as PRISM1
geo_button9 = ttk.Button(master=root,text=geometries[9],command=lambda:BUTTON_FN(calc_fns[9],labels_list[9]))
geo_button9.grid(row=9,column=0)

# Triangular Prism as PRISM2
geo_button10 = ttk.Button(master=root,text=geometries[10],command=lambda:BUTTON_FN(calc_fns[10],labels_list[10]))
geo_button10.grid(row=10,column=0)

# Other Prism as PRISM3
geo_button11 = ttk.Button(master=root,text=geometries[11],command=lambda:BUTTON_FN(calc_fns[11],labels_list[11]))
geo_button11.grid(row=11,column=0)

#Right Pyramid
geo_button12 = ttk.Button(master=root,text=geometries[12],command=lambda:BUTTON_FN(calc_fns[12],labels_list[12]))
geo_button12.grid(row=12,column=0)

#Regular Tetrahedron
geo_button13 = ttk.Button(master=root,text=geometries[13],command=lambda:BUTTON_FN(calc_fns[13],labels_list[13]))
geo_button13.grid(row=13,column=0)

#Regular Octahedron
geo_button14 = ttk.Button(master=root,text=geometries[14],command=lambda:BUTTON_FN(calc_fns[14],labels_list[14]))
geo_button14.grid(row=14,column=0)

#Torus
geo_button15 = ttk.Button(master=root,text=geometries[15],command=lambda:BUTTON_FN(calc_fns[15],labels_list[15]))
geo_button15.grid(row=15,column=0)

#Ellipsoid
geo_button16 = ttk.Button(master=root,text=geometries[16],command=lambda:BUTTON_FN(calc_fns[16],labels_list[16]))
geo_button16.grid(row=16,column=0)

#Dodecahedron
geo_button17 = ttk.Button(master=root,text=geometries[17],command=lambda:BUTTON_FN(calc_fns[17],labels_list[17]))
geo_button17.grid(row=17,column=0)

#Icosahedron
geo_button18 = ttk.Button(master=root,text=geometries[18],command=lambda:BUTTON_FN(calc_fns[18],labels_list[18]))
geo_button18.grid(row=18,column=0)


root.mainloop()
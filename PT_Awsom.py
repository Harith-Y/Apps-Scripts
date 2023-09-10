import tkinter as tk

import tkinter.ttk as ttk

import tkinter.messagebox as tmb



def mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26):


	def fn0 (a1):


		tmb.showinfo(title="Year Discovered",message="Year Discovered : {}".format(a1))


	def fn1 (a2):


		tmb.showinfo(title="Latin Name",message="Latin Name : {}".format(a2))


	def fn2 (a3):


		tmb.showinfo(title="Atomic Number",message="Atomic number : {}".format(a3))


	def fn3 (a4):


		tmb.showinfo(title="Atomic Mass",message="Atomic Mass : {}".format(a4))


	def fn4 (a5):


		tmb.showinfo(title="Density",message="Density : {}".format(a5))


	def fn5 (a6):


		tmb.showinfo(title="State of Matter",message="State of Matter : {}".format(a6))


	def fn6 (a7):


		tmb.showinfo(title="Melting Point",message="Melting Point : {}".format(a7))


	def fn7 (a8):


		tmb.showinfo(title="Boiling Point",message="Boiling Point : {}".format(a8))


	def fn8 (a9):


		tmb.showinfo(title="Type",message="Type : {}".format(a9))


	def fn9 (a10):


		tmb.showinfo(title="Shell Configuration",message="Shell configuration : {}".format(a10))


	def fn10 (a11):


		tmb.showinfo(title="Electronic Configuration",message="Electronic Configuration : {}".format(a11))


	def fn11 (a12):


		tmb.showinfo(title="Electronegativity",message="Electronegativity : {}".format(a12))


	def fn12 (a13):


		tmb.showinfo(title="Electron Affinity",message="Electron Affinity : {}".format(a13))


	def fn13 (a14):


		tmb.showinfo(title="Valency",message="Valency : {}".format(a14))


	def fn14 (a15):


		tmb.showinfo(title="Oxidation States",message="Oxidation States : {}".format(a15))


	def fn15 (a16):


		tmb.showinfo(title="Atomic Radius",message="Atomic Radius : {}".format(a16))


	def fn16 (a17):


		tmb.showinfo(title="Covalent Radius",message="Covalent Radius : {}".format(a17))


	def fn17 (a18):


		tmb.showinfo(title="Van der Waals radius",message="Van der Waals Radius : {}".format(a18))


	def fn18 (a19):


		tmb.showinfo(title="Magnetic Type",message="Magnetic Type : {}".format(a19))


	def fn19 (a20):


		tmb.showinfo(title="Group",message="Group : {}".format(a20))


	def fn20(a21):


		tmb.showinfo(title="Latent Heat Of Fusion",message="Latent Heat of Fusion : {}".format(a21))


	def fn21(a22):


		tmb.showinfo(title="Latent Heat Of Vapourisation",message="Latent Heat of Vapourisation : {}".format(a22))


	def fn22(a23):


		tmb.showinfo(title="Specific Heat",message="Specific Heat : {}".format(a23))


	def fn23(a24):


		tmb.showinfo(title="Sound Speed",message="Sound Speed : {}".format(a24))


	def fn24(a25):


		tmb.showinfo(title="Half Life",message="Non Radioactive Elements have Half life periods as ∞. Half Life Period : {}".format(a25))


	def fn25(a26):


		tmb.showinfo(title="Lifetime",message="Non Radioactive Elements have lifetime periods as ∞. Lifetime : {}".format(a26))

	win = tk.Tk()


	win.title(x)


	buttons00 = ttk.Button(master=win,text="Discovery Year",command=lambda:fn0(a1))


	buttons00.grid(row=0,column=0)




	buttons0 = ttk.Button(master=win,text="Latin Name",command=lambda:fn1(a2))


	buttons0.grid(row=1,column=0)





	buttons1 = ttk.Button(master=win,text="Atomic Number",command=lambda:fn2(a3))


	buttons1.grid(row=2,column=0)





	buttons2 = ttk.Button(master=win,text="Atomic Mass",command=lambda:fn3(a4))


	buttons2.grid(row=3,column=0)





	buttons3 = ttk.Button(master=win,text="Density",command=lambda:fn4(a5))


	buttons3.grid(row=4,column=0)





	buttons4 = ttk.Button(master=win,text="State of matter",command=lambda:fn5(a6))


	buttons4.grid(row=5,column=0)


	


	buttons5 = ttk.Button(master=win,text="Melting Point",command=lambda:fn6(a7))


	buttons5.grid(row=6,column=0)


	


	buttons6 = ttk.Button(master=win,text="Boiling Point",command=lambda:fn7(a8))


	buttons6.grid(row=7,column=0)


	


	buttons7 = ttk.Button(master=win,text="Type",command=lambda:fn8(a9))


	buttons7.grid(row=8,column=0)


	


	buttons8 = ttk.Button(master=win,text="Shell configuration",command=lambda:fn9(a10))


	buttons8.grid(row=9,column=0)


	


	buttons9 = ttk.Button(master=win,text="Electronic Configuration",command=lambda:fn10(a11))


	buttons9.grid(row=0,column=1)


	


	buttons10 = ttk.Button(master=win,text="Electronegativity",command=lambda:fn11(a12))


	buttons10.grid(row=1,column=1)


	


	buttons11 = ttk.Button(master=win,text="Electron Affinity",command=lambda:fn12(a13))


	buttons11.grid(row=2,column=1)


	


	buttons12 = ttk.Button(master=win,text="Valency",command=lambda:fn13(a14))


	buttons12.grid(row=3,column=1)


	


	buttons13 = ttk.Button(master=win,text="Oxidation States",command=lambda:fn14(a15))


	buttons13.grid(row=4,column=1)


	


	buttons14 = ttk.Button(master=win,text="Atomic Radius",command=lambda:fn15(a16))


	buttons14.grid(row=5,column=1)


	


	buttons15 = ttk.Button(master=win,text="Covalent Radius",command=lambda:fn16(a17))


	buttons15.grid(row=6,column=1)


	


	buttons16 = ttk.Button(master=win,text="Van der Waals Radius",command=lambda:fn17(a18))


	buttons16.grid(row=7,column=1)


	


	buttons17 = ttk.Button(master=win,text="Magnetic Type",command=lambda:fn18(a19))


	buttons17.grid(row=8,column=1)


	


	buttons18 = ttk.Button(master=win,text="Group",command=lambda:fn19(a20))


	buttons18.grid(row=9,column=1)


	


	buttons19 = ttk.Button(master=win,text="Fusion Heat",command=lambda:fn20(a21))


	buttons19.grid(row=10,column=0)


	


	buttons20 = ttk.Button(master=win,text="Vapourisation Heat",command=lambda:fn21(a22))


	buttons20.grid(row=10,column=1)


	


	buttons21 = ttk.Button(master=win,text="Specific Heat",command=lambda:fn22(a23))


	buttons21.grid(row=11,column=0)


	


	buttons22 = ttk.Button(master=win,text="Speed of sound",command=lambda:fn23(a24))


	buttons22.grid(row=11,column=1)


	


	buttons23 = ttk.Button(master=win,text="Half Life",command=lambda:fn24(a25))


	buttons23.grid(row=12,column=0)


	


	buttons24 = ttk.Button(master=win,text="Lifetime",command=lambda:fn25(a26))


	buttons24.grid(row=12,column=1)


	


	win.mainloop()


	return()











def H ():


	x = "Hydrogen"


	a1 = "1766"


	a2 = "Hydrogenium"


	a3 = "1"


	a4 = "1.0079 g/mol"


	a5 = "0.000089 g/cm³"


	a6 = "Gas"


	a7 = "-259.14 °C (14.01 K, -434.45 °F)"


	a8 = "-252.87 °C (20.28 K, -423.17 °F)"


	a9 = "Non Metal"


	a10 = "1"


	a11 = "1s¹"


	a12 = "2.2"


	a13 = "72.8 kJ/mole"


	a14 = "1"


	a15 = "-1, +1"


	a16 = "53 pm"


	a17 = "38 pm"


	a18 = "120 pm"


	a19 = "Diamagnetic"


	a20 = "1A (Alkali Metals)"

	a21 = "0.558 kJ•mol"


	a22 = "0.452 kJ•mol"


	a23 = "14300 J/(kg•K)"


	a24 = "1270 m/s"


	a25 = "∞"


	a26 = "∞"




	mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


	return()





def He ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime

    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Li ():


	x = "Lithium"


	a1 = "1817"


	a2 = "Lithium"


	a3 = "3"


	a4 = "6.941 g/mol"


	a5 = "0.534 g/cm³"


	a6 = "Solid"


	a7 = "180.5 °C (453.65 K, 356.9 °F)"


	a8 = "1342 °C (1615.15 K, 2447.6 °F)"


	a9 = "Non Metal"


	a10 = "2,1"


	a11 = "1s² 2s¹"


	a12 = "0.98"


	a13 = "59.6 kJ/mol"


	a14 = "1"


	a15 = "+1"


	a16 = "145 pm"


	a17 = "134 pm"


	a18 = "182 pm"


	a19 = "Paramagnetic"


	a20 = "" #Group with common name in brackets
	a21 = "" #Latent Heat of Fusion
	a22 = "" #Latent Heat of Vapourisation
	a23 = "" #Specific heat
	a24 = "" #Sound Speed
	a25 = "" #Half-life
	a26 = "" #Lifetime


	mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


	return()





def Be ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def B ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def C ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def N ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def O ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def F ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ne ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Na ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Mg ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Al ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Si ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def P ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def S ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Cl ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ar ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()









































def K ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()








def Ca ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Sc ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ti ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def V ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Cr ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Mn ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Fe ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Co ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ni ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Cu ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Zn ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ga ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ge ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def As ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Se ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Br ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Kr ():


    x = "" #Element Name


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Rb ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Sr ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Y ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Zr ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Nb ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Mo ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Tc ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ru ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Rh ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Pd ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ag ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Cd ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def In ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Sn ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Sb ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Te ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def I ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Xe ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Cs ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ba ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def La ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Hf ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ta ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def W ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Re ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Os ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ir ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Pt ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Au ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Hg ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Tl ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Pb ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Bi ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Po ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def At ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Rn ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Fr ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ra ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ac ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Rf ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Db ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Sg ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Bh ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Hs ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Mt ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ds ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Rg ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Cn ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Nh ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Fl ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Mc ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Lv ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ts ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Og ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





#Lanthanoids


def Ce ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime



    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Pr ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Nd ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Pm ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Sm ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Eu ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Gd ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Tb ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Dy ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Ho ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Er ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Tm ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Yb ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Lu ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





#Actinoids


def Th ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Pa ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def U ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Np ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Pu ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Am ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Cm ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Bk ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Cf ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Es ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Fm ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Md ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def No ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()





def Lr ():


    x = "" #Element Name


    a1 = "" # Year of Discovery


    a2 = "" #Element Latin Name


    a3 = "" #Atomic Number


    a4 = " g/mol" #Atomic Weight


    a5 = " g/cm³" #Density


    a6 = "" #State of Matter


    a7 = " °C ( K,  °F)" #Melting Point


    a8 = " °C ( K,  °F)" #Boiling Point


    a9 = "" #Type i.e. Metal/Mettaloid/Non Metal


    a10 = "" #Shell Configuration


    a11 = "" #Electronic Configuration


    a12 = "" #Electronegativity


    a13 = "" #Electron Affinity


    a14 = "" #Valency


    a15 = "" #Oxidation States


    a16 = " pm" #Atomic Radius


    a17 = " pm" #Covalent Radius


    a18 = " pm" #Van der Waals Radius


    a19 = "" #Magnetic Type


    a20 = "" #Group with common name in brackets
    a21 = "" #Latent Heat of Fusion
    a22 = "" #Latent Heat of Vapourisation
    a23 = "" #Specific heat
    a24 = "" #Sound Speed
    a25 = "" #Half-life
    a26 = "" #Lifetime


    mfn (x,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25,a26)


    return()








root = tk.Tk()


root.title("Periodic Table")


root.resizable(height=True,width=True)








# style = ttk.Style()


# style.configure('TButton',background='blue')





for i in range(1,19):


    Label1 = ttk.Label(master=root,text=i)


    Label1.grid(row=0,column=i)





for k in range(1,8):


    Label2 = ttk.Label(master=root,text=k)


    Label2.grid(row=k,column=0)





Label21 = ttk.Label(master=root,text="6")


Label21.grid(row=8,column=0)





Label22 = ttk.Label(master=root,text="7")


Label22.grid(row=9,column=0)





#1st Row


Button11 = ttk.Button(master=root,text="1\nH",command=H)#,width=9,bg='Blue')


Button11.grid(row=1,column=1)





Button119 = ttk.Button(master=root,text="2\nHe",command=He)


Button119.grid(row=1,column=18)





#2nd Row


Button21 = ttk.Button(master=root,text="3\nLi",command=Li)


Button21.grid(row=2,column=1)





Button22 = ttk.Button(master=root,text="4\nBe",command=Be)


Button22.grid(row=2,column=2)





Button214 = ttk.Button(master=root,text="5\nB",command=B)


Button214.grid(row=2,column=13)





Button215 = ttk.Button(master=root,text="6\nC",command=C)


Button215.grid(row=2,column=14)





Button216 = ttk.Button(master=root,text="7\nN",command=N)


Button216.grid(row=2,column=15)





Button217 = ttk.Button(master=root,text="8\nO",command=O)


Button217.grid(row=2,column=16)





Button218 = ttk.Button(master=root,text="9\nFe",command=F)


Button218.grid(row=2,column=17)





Button219 = ttk.Button(master=root,text="10\nNe",command=Ne)


Button219.grid(row=2,column=18)





#3rd Row


Button31 = ttk.Button(master=root,text="11\nNa",command=Na)


Button31.grid(row=3,column=1)





Button32 = ttk.Button(master=root,text="12\nMg",command=Mg)


Button32.grid(row=3,column=2)





Button314 = ttk.Button(master=root,text="13\nAl",command=Al)


Button314.grid(row=3,column=13)





Button315 = ttk.Button(master=root,text="14\nSi",command=Si)


Button315.grid(row=3,column=14)





Button316 = ttk.Button(master=root,text="15\nP",command=P)


Button316.grid(row=3,column=15)





Button317 = ttk.Button(master=root,text="16\nS",command=S)


Button317.grid(row=3,column=16)





Button318 = ttk.Button(master=root,text="17\nCl",command=Cl)


Button318.grid(row=3,column=17)





Button319 = ttk.Button(master=root,text="18\nAr",command=Ar)


Button319.grid(row=3,column=18)





#4rth Row


Button41 = ttk.Button(master=root,text="19\nK",command=K)


Button41.grid(row=4,column=1)





Button42 = ttk.Button(master=root,text="20\nCa",command=Ca)


Button42.grid(row=4,column=2)





Button43 = ttk.Button(master=root,text="21\nSc",command=Sc)


Button43.grid(row=4,column=3)





Button44 = ttk.Button(master=root,text="22\nTi",command=Ti)


Button44.grid(row=4,column=4)





Button45 = ttk.Button(master=root,text="23\nV",command=V)


Button45.grid(row=4,column=5)





Button46 = ttk.Button(master=root,text="24\nCr",command=Cr)


Button46.grid(row=4,column=6)





Button47 = ttk.Button(master=root,text="25\nMn",command=Mn)


Button47.grid(row=4,column=7)





Button48 = ttk.Button(master=root,text="26\nFe",command=Fe)


Button48.grid(row=4,column=8)





Button49 = ttk.Button(master=root,text="27\nCo",command=Co)


Button49.grid(row=4,column=9)





Button410 = ttk.Button(master=root,text="28\nNi",command=Ni)


Button410.grid(row=4,column=10)





Button411 = ttk.Button(master=root,text="29\nCu",command=Cu)


Button411.grid(row=4,column=11)





Button412 = ttk.Button(master=root,text="30\nZn",command=Zn)


Button412.grid(row=4,column=12)





Button413 = ttk.Button(master=root,text="31\nGa",command=Ga)


Button413.grid(row=4,column=13)





Button414 = ttk.Button(master=root,text="32\nGe",command=Ge)


Button414.grid(row=4,column=14)





Button415 = ttk.Button(master=root,text="33\nAs",command=As)


Button415.grid(row=4,column=15)





Button416 = ttk.Button(master=root,text="34\nSe",command=Se)


Button416.grid(row=4,column=16)





Button417 = ttk.Button(master=root,text="35\nBr",command=Br)


Button417.grid(row=4,column=17)





Button418 = ttk.Button(master=root,text="36\nKr",command=Kr)


Button418.grid(row=4,column=18)





#5th Row


Button51 = ttk.Button(master=root,text="37\nRb",command=Rb)


Button51.grid(row=5,column=1)





Button52 = ttk.Button(master=root,text="38\nSr",command=Sr)


Button52.grid(row=5,column=2)





Button53 = ttk.Button(master=root,text="39\nY",command=Y)


Button53.grid(row=5,column=3)





Button54 = ttk.Button(master=root,text="40\nZr",command=Zr)


Button54.grid(row=5,column=4)





Button55 = ttk.Button(master=root,text="41\nNb",command=Nb)


Button55.grid(row=5,column=5)





Button56 = ttk.Button(master=root,text="42\nMo",command=Mo)


Button56.grid(row=5,column=6)





Button57 = ttk.Button(master=root,text="43\nTc",command=Tc)


Button57.grid(row=5,column=7)





Button58 = ttk.Button(master=root,text="44\nRu",command=Ru)


Button58.grid(row=5,column=8)





Button59 = ttk.Button(master=root,text="45\nRh",command=Rh)


Button59.grid(row=5,column=9)





Button510 = ttk.Button(master=root,text="46\nPd",command=Pd)


Button510.grid(row=5,column=10)





Button511 = ttk.Button(master=root,text="47\nAg",command=Ag)


Button511.grid(row=5,column=11)





Button512 = ttk.Button(master=root,text="48\nCd",command=Cd)


Button512.grid(row=5,column=12)





Button513 = ttk.Button(master=root,text="49\nIn",command=In)


Button513.grid(row=5,column=13)





Button514 = ttk.Button(master=root,text="50\nSn",command=Sn)


Button514.grid(row=5,column=14)





Button515 = ttk.Button(master=root,text="51\nSb",command=Sb)


Button515.grid(row=5,column=15)





Button516 = ttk.Button(master=root,text="52\nTe",command=Te)


Button516.grid(row=5,column=16)





Button517 = ttk.Button(master=root,text="53\nI",command=I)


Button517.grid(row=5,column=17)





Button518 = ttk.Button(master=root,text="54\nXe",command=Xe)


Button518.grid(row=5,column=18)





#6th Row


Button61 = ttk.Button(master=root,text="55\nCs",command=Cs)


Button61.grid(row=6,column=1)





Button62 = ttk.Button(master=root,text="56\nBa",command=Ba)


Button62.grid(row=6,column=2)





Button63 = ttk.Button(master=root,text="57\nLa",command=La)


Button63.grid(row=6,column=3)





Button64 = ttk.Button(master=root,text="72\nHf",command=Hf)


Button64.grid(row=6,column=4)





Button65 = ttk.Button(master=root,text="73\nTa",command=Ta)


Button65.grid(row=6,column=5)





Button66 = ttk.Button(master=root,text="74\nW",command=W)


Button66.grid(row=6,column=6)





Button67 = ttk.Button(master=root,text="75\nRe",command=Re)


Button67.grid(row=6,column=7)





Button68 = ttk.Button(master=root,text="76\nOs",command=Os)


Button68.grid(row=6,column=8)





Button69 = ttk.Button(master=root,text="77\nIr",command=Ir)


Button69.grid(row=6,column=9)





Button610 = ttk.Button(master=root,text="78\nPt",command=Pt)


Button610.grid(row=6,column=10)





Button611 = ttk.Button(master=root,text="79\nAu",command=Au)


Button611.grid(row=6,column=11)





Button612 = ttk.Button(master=root,text="80\nHg",command=Hg)


Button612.grid(row=6,column=12)





Button613 = ttk.Button(master=root,text="81\nTl",command=Tl)


Button613.grid(row=6,column=13)





Button614 = ttk.Button(master=root,text="82\nPb",command=Pb)


Button614.grid(row=6,column=14)





Button615 = ttk.Button(master=root,text="83\nBi",command=Bi)


Button615.grid(row=6,column=15)





Button616 = ttk.Button(master=root,text="84\nPo",command=Po)


Button616.grid(row=6,column=16)





Button617 = ttk.Button(master=root,text="85\nAt",command=At)


Button617.grid(row=6,column=17)





Button618 = ttk.Button(master=root,text="86\nRn",command=Rn)


Button618.grid(row=6,column=18)





#7th Row


Button71 = ttk.Button(master=root,text="87\nFr",command=Fr)


Button71.grid(row=7,column=1)





Button72 = ttk.Button(master=root,text="88\nRa",command=Ra)


Button72.grid(row=7,column=2)





Button73 = ttk.Button(master=root,text="89\nAc",command=Ac)


Button73.grid(row=7,column=3)





Button74 = ttk.Button(master=root,text="104\nRf",command=Rf)


Button74.grid(row=7,column=4)





Button75 = ttk.Button(master=root,text="105\nDb",command=Db)


Button75.grid(row=7,column=5)





Button76 = ttk.Button(master=root,text="106\nSg",command=Sg)


Button76.grid(row=7,column=6)





Button77 = ttk.Button(master=root,text="107\nBh",command=Bh)


Button77.grid(row=7,column=7)





Button78 = ttk.Button(master=root,text="108\nHs",command=Hs)


Button78.grid(row=7,column=8)





Button79 = ttk.Button(master=root,text="109\nMt",command=Mt)


Button79.grid(row=7,column=9)





Button710 = ttk.Button(master=root,text="110\nDs",command=Ds)


Button710.grid(row=7,column=10)





Button711 = ttk.Button(master=root,text="111\nRg",command=Rg)


Button711.grid(row=7,column=11)





Button712 = ttk.Button(master=root,text="112\nCn",command=Cn)


Button712.grid(row=7,column=12)





Button713 = ttk.Button(master=root,text="113\nNh",command=Nh)


Button713.grid(row=7,column=13)





Button714 = ttk.Button(master=root,text="114\nFl",command=Fl)


Button714.grid(row=7,column=14)





Button715 = ttk.Button(master=root,text="115\nMc",command=Mc)


Button715.grid(row=7,column=15)





Button716 = ttk.Button(master=root,text="116\nLv",command=Lv)


Button716.grid(row=7,column=16)





Button717 = ttk.Button(master=root,text="117\nTs",command=Ts)


Button717.grid(row=7,column=17)





Button718 = ttk.Button(master=root,text="118\nOg",command=Og)


Button718.grid(row=7,column=18)





#Lanthanoid Series


Label3 = ttk.Label(master=root,text="Lanthanoids")


Label3.grid(row=8,column=1)





Button84 = ttk.Button(master=root,text="58\nCe",command=Ce)


Button84.grid(row=8,column=4)





Button85 = ttk.Button(master=root,text="59\nPr",command=Pr)


Button85.grid(row=8,column=5)





Button86 = ttk.Button(master=root,text="60\nNd",command=Nd)


Button86.grid(row=8,column=6)





Button87 = ttk.Button(master=root,text="61\nPm",command=Pm)


Button87.grid(row=8,column=7)





Button88 = ttk.Button(master=root,text="62\nSm",command=Sm)


Button88.grid(row=8,column=8)





Button89 = ttk.Button(master=root,text="63\nEu",command=Eu)


Button89.grid(row=8,column=9)





Button810 = ttk.Button(master=root,text="64\nGd",command=Gd)


Button810.grid(row=8,column=10)





Button811 = ttk.Button(master=root,text="65\nTb",command=Tb)


Button811.grid(row=8,column=11)





Button812 = ttk.Button(master=root,text="66\nDy",command=Dy)


Button812.grid(row=8,column=12)





Button813 = ttk.Button(master=root,text="67\nHo",command=Ho)


Button813.grid(row=8,column=13)





Button814 = ttk.Button(master=root,text="68\nEr",command=Er)


Button814.grid(row=8,column=14)





Button815 = ttk.Button(master=root,text="69\nTm",command=Tm)


Button815.grid(row=8,column=15)





Button816 = ttk.Button(master=root,text="70\nYb",command=Yb)


Button816.grid(row=8,column=16)





Button817 = ttk.Button(master=root,text="71\nLu",command=Lu)


Button817.grid(row=8,column=17)





#Actinoid Series


Label4 = ttk.Label(master=root,text="Actinoids")


Label4.grid(row=9,column=1)





Button94 = ttk.Button(master=root,text="90\nTh",command=Th)


Button94.grid(row=9,column=4)





Button95 = ttk.Button(master=root,text="91\nPa",command=Pa)


Button95.grid(row=9,column=5)





Button96 = ttk.Button(master=root,text="92\nU",command=U)


Button96.grid(row=9,column=6)





Button97 = ttk.Button(master=root,text="93\nNp",command=Np)


Button97.grid(row=9,column=7)





Button98 = ttk.Button(master=root,text="94\nPu",command=Pu)


Button98.grid(row=9,column=8)





Button99 = ttk.Button(master=root,text="95\nAm",command=Am)


Button99.grid(row=9,column=9)





Button910 = ttk.Button(master=root,text="96\nCm",command=Cm)


Button910.grid(row=9,column=10)





Button911 = ttk.Button(master=root,text="97\nBk",command=Bk)


Button911.grid(row=9,column=11)





Button912 = ttk.Button(master=root,text="98\nCf",command=Cf)


Button912.grid(row=9,column=12)





Button913 = ttk.Button(master=root,text="99\nEs",command=Es)


Button913.grid(row=9,column=13)





Button914 = ttk.Button(master=root,text="100\nFm",command=Fm)


Button914.grid(row=9,column=14)





Button915 = ttk.Button(master=root,text="101\nMd",command=Md)


Button915.grid(row=9,column=15)





Button916 = ttk.Button(master=root,text="102\nNo",command=No)


Button916.grid(row=9,column=16)





Button917 = ttk.Button(master=root,text="103\nLr",command=Lr)


Button917.grid(row=9,column=17)





root.mainloop()
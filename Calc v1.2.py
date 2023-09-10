#Simple Calculator by Making Functions
# Program make a simple calculator
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as tmb
import threading
import math as m

def add(x, y):
   return (x + y)

def subtract(x, y):
   return (x - y)

def multiply(x, y):
   return (x * y)

def divide(x, y):
   return (x / y)

def remainder(x,y):
	return(x%y)

def exponential(x,y):
   return(x**y)

def hcf_fn(x,y):
   if x > y:
        smaller = y
   else:
        smaller = x
   for i in range(1, int(smaller+1)):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
   return(hcf)

def lcm_fn(x,y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return(lcm)

def fact(num):

	factorial = 1
	if num < 0:
	   tmb.showerror(title="Error !",message="Factorial does not exist for negative numbers in the real world. Of Course it exists in the complex world !")
	elif num == 0:
		factorial = 1
	else:
	   for i in range(1,int(num + 1)):
	       factorial = factorial*i
	return(factorial)

def roots(x,y):
	a = (x**(1/y))
	tmb.showinfo(title="Root",message="{}th root of {} is {}".format(y,x,a))
	
def loggin(x,y):
	if y > 1:
		if x > 0:
			a = (m.log(x))/(m.log(y))
			tmb.showinfo(title="Log",message="log {} to the base {} is {}".format(x,y,a))
		elif x == 0:
			tmb.showinfo(title="Log",message="log 0 to the base {} is -∞".format(y))
		else:
			tmb.showerror(title="Error",message="log {} to the base {} cannot be obtained in the real world.".format(x,y))
	else:
		tmb.showerror(title="Error",message="log {} to the base {} cannot be obtained in the real world.".format(x,y))
		
def elo(x):
	n = float(x.get())
	if n > 0:
		a = m.log(n)
		tmb.showinfo(title="Log",message="Natural log of {} is {}".format(n,a))
	elif x == 0:
		tmb.showinfo(title="Log",message="Natural log of 0 is -∞")
	else:
		tmb.showerror(title="Error",message="Natural log of {} cannot be obtained in the real world.".format(n))
	
def permutation(n,r):
	# n = int(x.get())
	# r = int(y.get())

	if n >= 0 and r >= 0:
		if (n-r) >= 0 :
			x = fact(n)/fact(n-r)
			tmb.showinfo(title = "{} Permute {}".format(n,r),message="Number of ways of Arranging/Permuting {} out of {} is {}".format(n,r,x))

		else :
			tmb.showerror(title="Error !",message="Total ways must be greater than permuting ways i.e. n({}) must be greater than r({}). But the given values are not obeying the rule.".format(n,r))

	else:
		tmb.showerror(title="Error !",message="Factorial does not exist for negative numbers in the real world. Of Course it exists in the complex world !")

def combination(n,r):
	# n = int(x.get())
	# r = int(y.get())

	if n >= 0 and r >= 0:
		if (n-r) >= 0 :
			x = fact(n)/(fact(r)*fact(n-r))
			tmb.showinfo(title = "{} Choose {}".format(n,r),message="Number of ways of choosing {} out of {} ways is {}".format(n,r,x))

		else :
			tmb.showerror(title="Error !",message="Total ways must be greater than Combining ways i.e. n({}) must be greater than r({}). But the given values are not obeying the rule.".format(n,r))

	else:
		tmb.showerror(title="Error !",message="Factorial does not exist for negative numbers in the real world. Of Course it exists in the complex world !")		

def bw_primes(x,y):
   if x < y:
      for num in range(int(x) + 1,int(y)):
         if num > 1:
            for i in range(2, num):
               if (num % i) == 0:
                  break
            else:
               tmb.showinfo(message=num)
         # if num == 0:
         #    tmb.showerror(title="Error !",message="There are no primes in between {} and {}".format(x,y))
   else:
      tmb.showerror(title="Error !",message="lower limit has to be lesser than upper limit")

def prime(input1,button):

   def FN():

      button.state(["disabled"])
      tmb.showinfo(title="Wait",message="Please Wait !")

      num = int(input1.get())
      if num > 1:
         for i in range(2,num):
            if (num % i) == 0:
               tmb.showerror(title="Nope !",message="{} is not a prime number\n{} times {} = {}".format(num,i,num//i,num))
               break
         else:
               tmb.showinfo(title="Yep !",message="{} is a prime number".format(num))

      else:
         tmb.showerror(title="Obviously",message="{} is Obviously not a prime number".format(num))

      button.state(["!disabled"])

      return()

   t1 = threading.Thread(target=FN,daemon=True)
   t1.start()

   return()
	


def help_fn():
   # tmb.showinfo(title="Help Window",message="1.Add \n 2.Subtract \n 3.Multiply \n 4.Divide \n 5.Remainder \n 6.Exponential ")
   window =tk.Tk()
   window.title("Help Window")
   window.geometry("260x332") #"240x155" without nPr and nCr

   label11 = ttk.Label(master=window,text="1 Stands For : ")
   label11.grid(row=0,column=0)
   label12 = ttk.Label(master=window,text="Addition (a + b)")
   label12.grid(row=0,column=1)

   label21 = ttk.Label(master=window,text="2 Stands For : ")
   label21.grid(row=1,column=0)
   label22 = ttk.Label(master=window,text="Subtraction (a - b)")
   label22.grid(row=1,column=1)

   label31 = ttk.Label(master=window,text="3 Stands For : ")
   label31.grid(row=2,column=0)
   label32 = ttk.Label(master=window,text="Multiplication (a x b)")
   label32.grid(row=2,column=1)

   label41 = ttk.Label(master=window,text="4 Stands For : ")
   label41.grid(row=3,column=0)
   label42 = ttk.Label(master=window,text="Decimal (a / b)")
   label42.grid(row=3,column=1)

   label51 = ttk.Label(master=window,text="5 Stands For : ")
   label51.grid(row=4,column=0)
   label52 = ttk.Label(master=window,text="Remainder (when a / b)")
   label52.grid(row=4,column=1)

   label61 = ttk.Label(master=window,text="6 Stands For : ")
   label61.grid(row=5,column=0)
   label62 = ttk.Label(master=window,text="Exponential (a ^ b)")
   label62.grid(row=5,column=1)

   label71 = ttk.Label(master=window,text="7 Stands For : ")
   label71.grid(row=6,column=0)
   label72 = ttk.Label(master=window,text="H.C.F (of a and b)")
   label72.grid(row=6,column=1)

   label81 = ttk.Label(master=window,text="8 Stands For : ")
   label81.grid(row=7,column=0)
   label82 = ttk.Label(master=window,text="L.C.M (of a and b)")
   label82.grid(row=7,column=1)

   label91 = ttk.Label(master=window,text="9 Stands For : ")
   label91.grid(row=8,column=0)
   label92 = ttk.Label(master=window,text="aPb (a Permute b)")
   label92.grid(row=8,column=1)

   label101 = ttk.Label(master=window,text="10 Stands For : ")
   label101.grid(row=9,column=0)
   label102 = ttk.Label(master=window,text="aCb (a Choose b)")
   label102.grid(row=9,column=1)

   label111 = ttk.Label(master=window,text="11 Stands For : ")
   label111.grid(row=10,column=0)
   label112 = ttk.Label(master=window,text="Primes between (a and b)")
   label112.grid(row=10,column=1)
   
   label121 = ttk.Label(master=window,text="12 Stands For : ")
   label121.grid(row=11,column=0)
   label122 = ttk.Label(master=window,text="Root (bth root of a)")
   label122.grid(row=11,column=1)
   
   label131 = ttk.Label(master=window,text="13 Stands For : ")
   label131.grid(row=11,column=0)
   label132 = ttk.Label(master=window,text="Log a to the base b")
   label132.grid(row=11,column=1)

   ebutton = ttk.Button(master=window,text="logₑx")
   ebutton.grid(row=12,column=1)
   ebutton.configure(command=lambda:elo(eentry))
   eentry = ttk.Entry(master=window)
   eentry.grid(row=12,column=0)



   window.mainloop()

def fn(input1,input2,input3):

   choice = input1.get()
   num1 = float(input2.get())
   num2 = float(input3.get())

   if int(choice) == 1:
      tmb.showinfo(title="Addition",message="{} + {} = {}".format(num1,num2,add(num1,num2)))
   elif int(choice) == 2:
      tmb.showinfo(title="Subtraction",message="{} - {} = {}".format(num1,num2,subtract(num1,num2)))
   elif int(choice) == 3:
      tmb.showinfo(title="Multiplication",message="{} x {} = {}".format(num1,num2,multiply(num1,num2)))
   elif int(choice) == 4:
      tmb.showinfo(title="Decimal form",message="{} / {} = {}".format(num1,num2,divide(num1,num2)))
   elif int(choice) == 5:
      tmb.showinfo(title="Remainder",message="{} % {} = {}".format(num1,num2,remainder(num1,num2)))
   elif int(choice) == 6:
      tmb.showinfo(title="Exponential",message="{} ^ {} = {}".format(num1,num2,exponential(num1,num2)))
   elif int(choice) == 7:
      tmb.showinfo(title="H.C.F",message="H.C.F OF {} AND {} = {}".format(num1,num2,hcf_fn(num1,num2)))
   elif int(choice) == 8:
      tmb.showinfo(title="L.C.M",message="L.C.M OF {} AND {} = {}".format(num1,num2,lcm_fn(num1,num2)))
   elif int(choice) == 9:
      permutation(num1,num2)
   elif int(choice) == 10:
      combination(num1,num2)
   elif int(choice) == 11:
      bw_primes(num1,num2)
   elif int(choice) == 12:
   	roots(num1,num2)
   elif int(choice) == 13:
   	loggin(num1,num2)
   else:
      tmb.showerror(title="Error",message="Please Enter A Valid Input Or Press Help! Button")

def trig():

   def sind(x):
      l = float(x.get())
      n = m.sin(l*m.pi/180)
      tmb.showinfo(title="Sinθ",message="sin({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
      #degrees
      
   def sinr(x):
   	l = float(x.get())
   	n = m.sin(l)
   	tmb.showinfo(title="Sinθ",message="sin({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
   
   def sinhf(x):
   	l = float(x.get())
   	n = m.sinh(l)
   	tmb.showinfo(title="Sinhθ",message="sinh({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
		
   def cosd(x):
      l = float(x.get())
      n = m.cos(l*m.pi/180)
      tmb.showinfo(title="Cosθ",message="cos({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
      #degrees
    
   def cosr(x):
       l = float(x.get())
       n = m.cos(l)
       tmb.showinfo(title="Cosθ",message="cos({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
       
   def coshf(x):
    	l = float(x.get())
    	n = m.cosh(l)
    	tmb.showinfo(title="Coshθ",message="cosh({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))

   def tand(x):
      l = float(x.get())
      n = m.tan(l*m.pi/180)
      tmb.showinfo(title="Tanθ",message="tan({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
      #degrees
      
   def tanr(x):
       l = float(x.get())
       n = m.tan(l)
       tmb.showinfo(title="Tanθ",message="tan({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
       
   def tanhf(x):
   	l = float(x.get())
   	n = m.tanh(l)
   	tmb.showinfo(title="Tanhθ",message="tanh({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))

   def cscd(x):
      l = float(x.get())
      n = 1/m.sin(l*m.pi/180)
      tmb.showinfo(title="Cosecθ",message="cosec({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
      #degrees
      
   def cscr(x):
       l = float(x.get())
       n = 1/m.sin(l)
       tmb.showinfo(title="Cosecθ",message="cosec({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
       
   def cschf(x):
   	l = float(x.get())
   	n = 1/m.sinh(l)
   	tmb.showinfo(title="Cosechθ",message="cosech({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))

   def secd(x):
      l = float(x.get())
      n = 1/m.cos(l*m.pi/180)
      tmb.showinfo(title="Secθ",message="sec({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
      #degrees
      
   def secr(x):
       l = float(x.get())
       n = 1/m.cos(l)
       tmb.showinfo(title="Secθ",message="sec({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
       
   def sechf(x):
    	l = float(x.get())
    	n = 1/m.cosh(l)
    	tmb.showinfo(title="Sechθ",message="sech({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))

   def cotd(x):
      l = float(x.get())
      n = 1/m.tan(l*m.pi/180)
      tmb.showinfo(title="Cotθ",message="cot({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
      #degrees
      
   def cotr(x):
      l = float(x.get())
      n = 1/m.tan(l)
      tmb.showinfo(title="Cotθ",message="cot({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))
      
   def cothf(x):
      l = float(x.get())
      n = 1/m.tanh(l)
      tmb.showinfo(title="Cothθ",message="coth({}) = {}.\nx.9999... can be taken as x + 1\nx.0000... can be taken as x".format(l,n))

   trigs = tk.Tk()
   trigs.title("Trig")

   labeld = ttk.Label(master=trigs,text="Degrees")
   labeld.grid(row=0,column=1)
   
   labelr = ttk.Label(master=trigs,text="Radians")
   labelr.grid(row=0,column=2)
   
   labelh = ttk.Label(master=trigs,text="Hyperbolics")
   labelh.grid(row=0,column=3)
   
   Entry0 = ttk.Entry(master=trigs)
   Entry0.grid(row=1,column=0)
   Entry1 = ttk.Entry(master=trigs)
   Entry1.grid(row=2,column=0)
   Entry2 = ttk.Entry(master=trigs)
   Entry2.grid(row=3,column=0)
   Entry3 = ttk.Entry(master=trigs)
   Entry3.grid(row=4,column=0)
   Entry4 = ttk.Entry(master=trigs)
   Entry4.grid(row=5,column=0)
   Entry5 = ttk.Entry(master=trigs)
   Entry5.grid(row=6,column=0)

   Button1 = ttk.Button(master=trigs,text="Sinθ")
   Button1.grid(row=1,column=1)
   Button1.configure(command=lambda:sind(Entry0))
   Button11 = ttk.Button(master=trigs,text="Sinθ")
   Button11.grid(row=1,column=2)
   Button11.configure(command=lambda:sinr(Entry0))
   Button111 = ttk.Button(master=trigs,text="Sinhθ")
   Button111.grid(row=1,column=3)
   Button111.configure(command=lambda:sinhf(Entry0))
   
   Button2 = ttk.Button(master=trigs,text="Cosθ")
   Button2.grid(row=2,column=1)
   Button2.configure(command=lambda:cosd(Entry1))
   Button22 = ttk.Button(master=trigs,text="Cosθ")
   Button22.grid(row=2,column=2)
   Button22.configure(command=lambda:cosr(Entry1))
   Button222 = ttk.Button(master=trigs,text="Coshθ")
   Button222.grid(row=2,column=3)
   Button222.configure(command=lambda:coshf(Entry1))
   
   Button3 = ttk.Button(master=trigs,text="Tanθ")
   Button3.grid(row=3,column=1)
   Button3.configure(command=lambda:tand(Entry2))
   Button33 = ttk.Button(master=trigs,text="Tanθ")
   Button33.grid(row=3,column=2)
   Button33.configure(command=lambda:tanr(Entry2))
   Button333 = ttk.Button(master=trigs,text="Tanhθ")
   Button333.grid(row=3,column=3)
   Button333.configure(command=lambda:tanhf(Entry2))
   
   Button4 = ttk.Button(master=trigs,text="Cosecθ")
   Button4.grid(row=4,column=1)
   Button4.configure(command=lambda:cscd(Entry3))
   Button44 = ttk.Button(master=trigs,text="Cosecθ")
   Button44.grid(row=4,column=2)
   Button44.configure(command=lambda:cscr(Entry3))
   Button444 = ttk.Button(master=trigs,text="Cosechθ")
   Button444.grid(row=4,column=3)
   Button444.configure(command=lambda:cschf(Entry3))
   
   Button5 = ttk.Button(master=trigs,text="Secθ")
   Button5.grid(row=5,column=1)
   Button5.configure(command=lambda:secd(Entry4))
   Button55 = ttk.Button(master=trigs,text="Secθ")
   Button55.grid(row=5,column=2)
   Button55.configure(command=lambda:secr(Entry4))
   Button555 = ttk.Button(master=trigs,text="Sechθ")
   Button555.grid(row=5,column=3)
   Button555.configure(command=lambda:sechf(Entry4))
   
   Button6 = ttk.Button(master=trigs,text="Cotθ")
   Button6.grid(row=6,column=1)
   Button6.configure(command=lambda:cotd(Entry5))
   Button66 = ttk.Button(master=trigs,text="Cotθ")
   Button66.grid(row=6,column=2)
   Button66.configure(command=lambda:cotr(Entry5))
   Button666 = ttk.Button(master=trigs,text="Cothθ")
   Button666.grid(row=6,column=3)
   Button666.configure(command=lambda:cothf(Entry5))
   
   
   trigs.mainloop()

   return()

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("375x160")

label1 = ttk.Label(master=root,text="Enter Choice As Integer ONLY   : ")
label1.grid(row=0,column=0)
entry1 = ttk.Entry(master=root)
entry1.grid(row=0,column=1)

label2 = ttk.Label(master=root,text="Enter First Number                 (a) : ")
label2.grid(row=1,column=0)
entry2 = ttk.Entry(master=root)
entry2.grid(row=1,column=1)

label3 = ttk.Label(master=root,text="Enter Second Number           (b) : ")
label3.grid(row=2,column=0)
entry3 = ttk.Entry(master=root)
entry3.grid(row=2,column=1)

calc_button = ttk.Button(master=root,text="Calculate")
calc_button.grid(row=3,column=1,sticky='nsew')
calc_button.configure(command=lambda:fn(entry1,entry2,entry3))

help_button = ttk.Button(master=root,text="Help !")
help_button.grid(row=3,column=0,sticky='nsew')
help_button.configure(command=help_fn)

label4 = ttk.Label(master=root,text="Enter An Integer To Check If It Is Prime Or Not:")
label4.grid(row=4,column=0)
entry4 = ttk.Entry(master=root)
entry4.grid(row=4,column=1)

button1 = ttk.Button(master=root,text="Calculate")
button1.grid(row=5,column=0,columnspan=2,sticky='nsew')
button1.configure(command=lambda:prime(entry4,button1))

label11 = ttk.Label(master=root,text="For Trigonometrical Functions : ")
label11.grid(row=6,column=0)

button2 = ttk.Button(master=root,text="Trigonometry")
button2.grid(row=6,column=1,sticky='nsew')
button2.configure(command=trig)

root.mainloop()
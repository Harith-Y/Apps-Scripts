import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
import tkinter.messagebox as tmb
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import webbrowser

def fn():
    # Validate inputs to ensure they are floats
    inputs = [entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(),
              entry6.get(), entry7.get(), entry8.get(), entry9.get(), entry10.get(), entry11.get()]

    for value in inputs: #Error is displayed if anything other than a float is inputted.
        try:
            float(value)
        except ValueError:
            tmb.showerror("Error !", "Please enter valid numerical values.")
            return

    # Perform calculations if all inputs are valid floats
    q = float(entry2.get())
    m = float(entry1.get())
    qm = q / m
    Ex = float(entry3.get())
    Ey = float(entry4.get())
    Ez = float(entry5.get())
    Bx = float(entry6.get())
    By = float(entry7.get())
    Bz = float(entry8.get())
    ux = float(entry9.get())
    uy = float(entry10.get())
    uz = float(entry11.get())

    t = np.linspace(0, 40, 2000)

    def fx(t, x): #Defines the derivative function fx that represents the equations of motion for the charged particle in the presence of electric and magnetic fields.
        return [x[1], qm * (Ex + x[3] * Bz - x[5] * By),
                x[3], qm * (Ey + x[5] * Bx - x[1] * Bz),
                x[5], qm * (Ez + x[1] * By - x[3] * Bx)]

    t0 = 0 #Initial Time
    x0 = [0, ux, 0, uy, 0, uz] #Velocity at a specific position, i.e. here (0,0,0)

    x = np.zeros((6, len(t))) #Initializes an array x to store the positions and velocities of the particle at different time steps.
    x[:, 0] = x0

    for i in range(len(t) - 1): #Iterates through time steps to calculate the particle's trajectory using the Runge-Kutta 4th order method.
        h = t[i + 1] - t[i]
        k1 = np.array(fx(t[i], x[:, i]))
        k2 = np.array(fx(t[i] + h / 2, x[:, i] + (h / 2) * k1))
        k3 = np.array(fx(t[i] + h / 2, x[:, i] + (h / 2) * k2))
        k4 = np.array(fx(t[i] + h, x[:, i] + h * k3))
        x[:, i + 1] = x[:, i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)

    X, Y, Z = x[0, :], x[2, :], x[4, :] #Extracts the particle's positions along the x, y, and z axes from the x array.

    fig = plt.figure() #Creates a 3D plot with the particle's trajectory using Matplotlib.
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X, Y, Z, marker='o', edgecolors='black', facecolors=[0, 0.8, 0.8])
    ax.scatter(0, 0, 0, color='black', s=100, label='Origin')

    # Arrows to represent the Magnetic Field, Electric Field and Initial Velocity
    ax.quiver(0, 0, 0, 500 * Bx, 500 * By, 500 * Bz, length=1, normalize=True, color='red', arrow_length_ratio=0.3)
    ax.quiver(0, 0, 0, 500 * Ex, 500 * Ey, 500 * Ez, length=10, normalize=True, color='blue', arrow_length_ratio=0.05)
    ax.quiver(0, 0, 0, ux, uy, uz, length=2, normalize=True, color='green', arrow_length_ratio=0.3)

    ax.set_xlabel('x(t)') #Sets axis labels, title, and displays the 3D plot.
    ax.set_ylabel('y(t)')
    ax.set_zlabel('z(t)')
    ax.set_title('Trajectory of the Charged Particle')

    plt.show()

def open_link(): #Opening GitHub Repository Link
    webbrowser.open("https://github.com/Harith-Y/Apps-Scripts.git")

def open_email(): #To mail
    email_address = "cs23i1027@iiitdm.ac.in"  # Replace with the recipient's email address
    webbrowser.open("mailto:" + email_address)

def open_about():
    # tmb.showinfo("About", "**About This Application :**\n\nThis application simulates the motion of charged particles in an electromagnetic field using numerical methods.\nIt calculates the trajectory of a charged particle in the presence of electric and magnetic fields, providing visual insights into its motion over time.\n\n\n\n\n**Contact for Updates or Contributions :**\n\nIf you have any feedback, suggestions, or would like to contribute to this project, feel free to reach out:\n\n- Email: cs23i1027@iiitdm.ac.in\n- GH Repository: https://github.com/Harith-Y/Apps-Scripts.git\n\n\n\n\n**Acknowledgements :**\n\nSpecial thanks to the First question of EM Assignment 2 for inspiration in developing this simulation.\n\n---")
    About_window = tk.Toplevel()
    About_window.title("About")
    About_window.geometry("810x380")  # Change width, height, x_offset, and y_offset as needed

    # Menu Bar
    sub_menu_bar = tk.Menu(About_window)
    file_menu = tk.Menu(sub_menu_bar, tearoff=0)
    file_menu.add_command(label="Close", command=About_window.destroy)
    sub_menu_bar.add_cascade(label="File", menu=file_menu)
    About_window.config(menu=sub_menu_bar)

    # Links menu
    link_menu = tk.Menu(sub_menu_bar, tearoff=0)
    link_menu.add_command(label="GH Repo", command=open_link)
    link_menu.add_command(label="Email", command=open_email)
    sub_menu_bar.add_cascade(label="Links", menu=link_menu)

    label = tk.Label(About_window, text="**About This Application :**\n\nThis Application Simulates the motion of Charged particles in an Electromagnetic Field using numerical methods.\nIt Calculates the Trajectory of a Charged particle in the presence of Electric and Magnetic fields, providing visual insights into its motion over time.\n\n\n\n\n**Contact for Updates or Contributions :**\n\nIf you have any Feedback, Suggestions, or would like to contribute to this Project, feel free to reach out:\n\n- Email: cs23i1027@iiitdm.ac.in\n- GH Repository: https://github.com/Harith-Y/Apps-Scripts.git\n\n\n\n\n**Acknowledgements :**\n\nSpecial Thanks to the First question of EM Assignment 2 for Inspiration in developing this Simulation.\n\n---")
    label.pack(padx=20, pady=10)

    About_window.transient(root) # Set the parent window
    About_window.grab_set() # Make the dialog modal
    root.wait_window(About_window) # Wait for the dialog to close before continuing

# Main Window
root = tk.Tk()
root.title("Charged Particle Motion")
root.geometry("860x220")

# Menu Bar
menu_bar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About",command=open_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# Labels and Entries for particle parameters
particle_params1 = [
    ("E in x direction (V/m) :", 2),
    ("E in y direction (V/m) :", 3),
    ("E in z direction (V/m) :", 4), 
]
particle_params2 = [
    ("          B in x direction (T) :", 2),
    ("          B in y direction (T) :", 3),
    ("          B in z direction (T) :", 4)
]

particle_params3 = [
    ("u in x direction (m/s) :", 2),
    ("u in y direction (m/s) :", 3),
    ("u in z direction (m/s) :", 4)
]

entries = []

arrowlabel1 = ttk.Label(master=root, text="Green Arrow repersents u")
arrowlabel1.grid(row=5, column=5)

arrowlabel2 = ttk.Label(master=root, text="Blue Arrow represents E")
arrowlabel2.grid(row=5, column=1)

arrowlabel2 = ttk.Label(master=root, text="Red Arrow represents B ")
arrowlabel2.grid(row=5, column=3)

label1 = ttk.Label(master=root, text="Enter mass of the particle (kg) : ")
label1.grid(row=0, column=2, padx=5, pady=5, sticky='w')
entry1 = ttk.Entry(master=root)
entry1.grid(row=0, column=3, padx=5, pady=5, sticky='ew')
entries.append(entry1)

label2 = ttk.Label(master=root, text="Enter charge of the particle (C) : ")
label2.grid(row=1, column=2, padx=5, pady=5, sticky='w')
entry2 = ttk.Entry(master=root)
entry2.grid(row=1, column=3, padx=5, pady=5, sticky='ew')
entries.append(entry2)

for text, row in particle_params1:
    label = ttk.Label(root, text=text)
    label.grid(row=row, column=0, padx=5, pady=5, sticky='w')

    entry = ttk.Entry(root)
    entry.grid(row=row, column=1, padx=5, pady=5, sticky='ew')
    entries.append(entry)

for text, row in particle_params2:
    label = ttk.Label(root, text=text)
    label.grid(row=row, column=2, padx=5, pady=5, sticky='w')

    entry = ttk.Entry(root)
    entry.grid(row=row, column=3, padx=5, pady=5, sticky='ew')
    entries.append(entry)

for text, row in particle_params3:
    label = ttk.Label(root, text=text)
    label.grid(row=row, column=4, padx=5, pady=5, sticky='w')

    entry = ttk.Entry(root)
    entry.grid(row=row, column=5, padx=5, pady=5, sticky='ew')
    entries.append(entry)

# Calculate button
calc_button = ttk.Button(root, text="Calculate", command=fn)
calc_button.grid(row=7, column=2, padx=5, pady=15, sticky='nsew')

entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11 = entries

root.mainloop()
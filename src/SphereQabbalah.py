import tkinter as tk
from tkinter import *
from tkinter import ttk
from Buttons import Buttons
#program by Desmond Watts in collaboration with André Consciência 

class App(tk.Tk):
    def __init__(self):

        #Main setup
        super().__init__()
        self.title("Sphere Qabbalah Calculator")

        #widgets
        self.calculator = Calculator(self)
        self.description= Description(self)

        # run
        self.mainloop()

#Creates and contains Calculator on right side of window
class Calculator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self).pack(padx = 20, pady = 20)# right side
        self.Buttons = Buttons(self)
        self.Description = Description(self)
        self.pack(side = RIGHT, expand = True, fill = BOTH)

#Creates and contains Description on left side of window
class Description(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.my_text = Text(self, width=50,height=50,wrap=WORD)
        self.create_description()
        self.my_text.config(state=DISABLED)

        self.my_text.grid(row=0,column=0)#don't delete it removes description column entirely
        self.my_text.tag_configure('header',font=('Verdana',20,'bold'))
        self.my_text.tag_configure('description',font=('Verdana',15))
        self.pack(side=LEFT, expand=1,pady=50,padx=50)

    def create_description(self):
        self.my_text.insert(END,"Based on André Consciência's: "+"\n"+" 'A Guide to Sphere Qabbalah'"+"\n",'description')
        self.my_text.insert(END,"Mental: 1(ones)" + "\n",'header')
        self.my_text.insert(END,"Astral: 1x(tens)" + "\n",'header')
        self.my_text.insert(END,"Physical: 1xx(hundreds)" + "\n",'header')
        self.my_text.insert(END,"=================================================="+"\n")

        self.my_text.insert(END,"Sum" + "\n",'header')
        self.my_text.insert(END,"Conjunction(Conjunctio): is where in the alchemical process; two elements are united to create something greater than the sum of their parts. The merging of elements is a synthesis where a new essence emerges."+ "\n",'description')
        self.my_text.insert(END,"=================================================="+"\n")

        self.my_text.insert(END,"Subtraction" + "\n",'header') 
        self.my_text.insert(END,"Separation(Separatio): is the alchemical process of refinement, where what is unnecessary is removed so that the true essence can emerge."+"\n",'description')
        self.my_text.insert(END,"=================================================="+"\n")

        self.my_text.insert(END,"Multiplication" + "\n",'header') 
        self.my_text.insert(END,"Fermentation(Fermentatio): is the alchemical process where a substance undergoes a transformation through the introduction of a new,divine spark that infuses it with life"+ "\n",'description')
        self.my_text.insert(END,"=================================================="+"\n")

        self.my_text.insert(END,"Division" + "\n",'header') 
        self.my_text.insert(END,"Dissolution(Solutio): is the alchemical process of breaking down the rigid structures into a fluid state, where what remains is now softened, dissolved, and made malleable."+"\n", 'description')
        self.my_text.insert(END,"=================================================="+"\n")

App()

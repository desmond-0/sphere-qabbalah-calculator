import tkinter as tk
from tkinter import *
from tkinter import ttk
from Translator import translator
import string

class App(tk.Tk):
    def __init__(self):

        #Main setup
        super().__init__()
        self.title("Sphere Qabbalah Calculator")

        #widgets
        self.results = Results(self)
        self.calculator = Calculator(self)

        # run
        self.mainloop()

class Results(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self).pack(padx = 20, pady = 20)# left side
        self.pack(side = LEFT, expand = True, fill = BOTH)

class Calculator(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        ttk.Label(self).pack(padx = 20, pady = 20)# right side
        self.Buttons = Buttons(self)
        self.Description = Description(self)

        self.pack(side = RIGHT, expand = True, fill = BOTH)

class Description(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.my_text = Text(self, width=50,height=50,wrap=WORD)
        self.create_description()
        self.my_text.config(state=DISABLED)

        self.my_text.grid(row=0,column=0)#don't delete it removes description column entirely
        self.my_text.tag_configure('header',font=('Verdana',20,'bold'))
        self.my_text.tag_configure('description',font=('Verdana',15))
        self.pack(side=RIGHT, expand=1,pady=50,padx=50)

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

class Buttons(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.create_widgets()
        self.first_num = 0
        self.second_number = 0
        self.pack(side=RIGHT, expand = 1, pady=50, padx=50)

        global text
        self.result = 0
        self.my_text = Text(self,width=99,height=50)
        self.my_text.pack(padx=19,pady=20)

        self.my_text.tag_configure('operand',font=('Verdana',20,'bold'))
        self.my_text.tag_configure('planes',font=('Verdana',15))
        self.my_text.tag_configure('attributes',font=('Verdana',15))

    def display_text(self,operation):
        first = translator(self.first_num)
        second = translator(self.second_number)
        result = translator(self.result)

        if result == None:
            self.my_text.insert(END,"Enter a smaller number!",'operand')
        else:
            self.my_text.insert(END,str(self.first_num) + "\n",'operand')
            self.my_text.insert(END,"Mental: "+first[2] + "\n",'planes')
            self.my_text.insert(END,"Astral: "+first[1] + "\n",'planes')
            self.my_text.insert(END,"Physical: "+first[0] + "\n",'planes')
            self.my_text.insert(END,operation + "\n" ,'operand')

            #Second Operand
            self.my_text.insert(END,str(self.second_number) + "\n",'operand')
            self.my_text.insert(END,"Mental: " + second[2] + "\n",'planes')
            self.my_text.insert(END,"Astral: " + second[1] + "\n",'planes')
            self.my_text.insert(END,"Physical: " + second[0] + "\n",'planes')

            #Result
            self.my_text.insert(END,str(self.result) + "\n",'operand')
            self.my_text.insert(END,"Mental:  " + result[2] + "\n",'planes')
            self.my_text.insert(END,"Astral: " + result[1] + "\n",'planes')
            self.my_text.insert(END,"Physical: " + result[0] + "\n",'planes')
            self.my_text.insert(END,"===================================================================================================")

    def button_click(self,number):
        #e.delete(0, END)
        current = e.get()
        e.delete(0, END)
        e.insert(0, str(current) + str(number))

    def button_add(self):
        self.first_num = e.get()
        global f_num
        global math
        math = "addition"
        f_num = int(self.first_num)
        e.delete(0, END)

    def button_subtraction(self):
        self.first_num = e.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(self.first_num)
        e.delete(0,END)

    def button_multiplication(self):
        self.first_num = e.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(self.first_num)
        e.delete(0,END)

    def button_division(self):
        self.first_num = e.get()
        global f_num
        global math
        math = "division"
        f_num = int(self.first_num)
        e.delete(0,END)

    def button_clear(self):
        self.my_text.delete('1.0',END)
        e.delete(0,END)

    def button_equal(self):
        self.second_number = e.get()
        e.delete(0, END)

        if math == "addition":
            operation = "+"
            self.result = f_num + int(self.second_number)
            self.display_text(operation)

        if math == "subtraction":
            operation = "-"
            self.result = f_num - int(self.second_number)
            self.display_text(operation)

        if math == "multiplication":
            operation = "*"
            self.result = f_num * int(self.second_number)
            self.display_text(operation)

        if math == "division":
            operation = "/"
            self.result = f_num / int(self.second_number)
            self.display_text(operation)

    def create_widgets(self):
        frame = Frame(self)
        frame.pack(side=RIGHT,expand=TRUE,fill=BOTH)
        #This fixes not being able to mix layout managers
        frame_2 = Frame(frame)
        frame_2.pack(side=RIGHT,expand=TRUE,fill=BOTH)

        global e
        e = Entry(frame_2,width=35, borderwidth=5)
        e.grid(row=0,column=0,columnspan=5)

        button_1 = Button(frame_2,text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        button_2 = Button(frame_2, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        button_3 = Button(frame_2, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        button_4 = Button(frame_2, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        button_5 = Button(frame_2, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        button_6 = Button(frame_2, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        button_7 = Button(frame_2, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        button_8 = Button(frame_2, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        button_9 = Button(frame_2, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        button_0 = Button(frame_2, text="0", padx=40, pady=20, command=lambda: self.button_click(0))

        #operations
        button_add = Button(frame_2, text="+", padx=39, pady=20, command=self.button_add)
        button_subtraction = Button(frame_2, text="-", padx=39, pady=20, command=self.button_subtraction)
        button_multiplication = Button(frame_2, text="*", padx=39, pady=20, command=self.button_multiplication)
        button_division = Button(frame_2, text="/", padx=39, pady=20, command=self.button_division)
        button_equal = Button(frame_2, text="=", padx=91, pady=20, command=self.button_equal)
        button_clear= Button(frame_2, text="Clear", padx=79, pady=20, command=self.button_clear)

        #place the widgets
        button_1.grid(row=3, column=0)
        button_2.grid(row=3, column=1)
        button_3.grid(row=3, column=2)
        button_4.grid(row=2, column=0)
        button_5.grid(row=2, column=1)
        button_6.grid(row=2, column=2)
        button_7.grid(row=1, column=0)
        button_8.grid(row=1, column=1)
        button_9.grid(row=1, column=2)
        button_0.grid(row=4, column=0)

        button_add.grid(row=1, column=3)
        button_subtraction.grid(row=2, column=3)
        button_multiplication.grid(row=3, column=3)
        button_division.grid(row=4, column=3)
        button_equal.grid(row=5, column=1, columnspan=2)
        button_clear.grid(row=4, column=1, columnspan=2)

App()

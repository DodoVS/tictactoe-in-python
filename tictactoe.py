from tkinter import *

import random
import tkinter.messagebox
from tkinter.simpledialog import askstring
tk = Tk()
tk.title("Kółko i krzyżyk")


click = random.choice([True, False])
x = 0
o = 0
r = 0
rm = 1

def koniec():
	global x
	global o
	if(x>o):
		tkinter.messagebox.showinfo("Wygrywa X",("X","zdobył",x,"punktów","a","O","zdobył",o,"punktów!"))
	elif(x<o):
		tkinter.messagebox.showinfo("Wygrywa O",("O","zdobył",o,"punktów","a","X","zdobył",x,"punktów!"))
	elif(x==o):
		tkinter.messagebox.showinfo("Remix",("Obie","strony","zdobyły","po",x,"punktów!"))
	restart()
	x=0
	label3["text"] = x
	o=0
	label4["text"] = o
	podajrundy()

def podajrundy():
	global rm
	global r
	rm = 1
	r=0
	try:
		r = int(askstring('Runda', 'Ile chcesz rozgrywać rund?'))
	except:
		tk.destroy()
                        
def nowarunda():
	global rm
	global r
	if(r>rm):
		rm = rm +1
	elif(r<=rm):
		koniec()
		rm = 1
	
def restart():
	button1["text"] = " "
	button2["text"] = " "
	button3["text"] = " "
	button4["text"] = " "
	button5["text"] = " "
	button6["text"] = " "
	button7["text"] = " "
	button8["text"] = " "
	button9["text"] = " "

def tura():
    if click == True:
        label2.config(fg='red')
        label2["text"] = "Obecnie jest tura dla X"
    elif click == False:
        label2.config(fg='green')
        label2["text"] = "Obecnie jest tura dla O"

def checker(buttons):
	global click
	global x
	global o
	if buttons["text"] == " " and click == True:
		buttons["text"] = "X"
		buttons.config(fg='red')
		click = False
	elif buttons["text"] == " " and click == False:
		buttons["text"] = "O"
		buttons.config(fg='green')
		click = True
	if (button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
		button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
		button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
		button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X" or
		button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
		button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
		button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
		button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X"):
		tkinter.messagebox.showinfo("Zwycięzca to X","Właśnie wygrałeś grę")
		x += 1
		label3["text"] = x
		nowarunda()
		restart()
	elif (button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
		button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
		button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
		button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O" or
		button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
		button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
		button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
		button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O"):
		tkinter.messagebox.showinfo("Zwycięzca to O","Właśnie wygrałeś grę")
		o += 1
		label4["text"] = o
		nowarunda()
		restart()
	elif (button1["text"] != " " and button2["text"] != " " and button3["text"] != " " and
		button4["text"] != " " and button5["text"] != " " and button6["text"] != " " and
		button7["text"] != " " and button8["text"] != " " and button9["text"] != " "):
		tkinter.messagebox.showinfo("Remis","Brak zwycięzcy")
		nowarunda()
		restart()
	tura()
	label6_2["text"] = rm

buttons=StringVar()

button1 = Button(tk, text=" ", font=('Times 26 bold'), bg='#fbfed2', height=4, width=8, command=lambda:checker(button1))
button1.grid(row=2, column=1,rowspan=3, sticky = S+N+E+W)

button2 = Button(tk, text=" ", font=('Times 26 bold'),bg='#fbfed2', height=4, width=8, command=lambda:checker(button2))
button2.grid(row=2, column=2,rowspan=3, sticky = S+N+E+W)

button3 = Button(tk, text=" ", font=('Times 26 bold'),bg='#fbfed2', height=4, width=8, command=lambda:checker(button3))
button3.grid(row=2, column=3,rowspan=3, sticky = S+N+E+W)


button4 = Button(tk, text=" ", font=('Times 26 bold'),bg='#fbfed2', height=4, width=8, command=lambda:checker(button4))
button4.grid(row=5, column=1,rowspan=3, sticky = S+N+E+W)

button5 = Button(tk, text=" ", font=('Times 26 bold'),bg='#fbfed2', height=4, width=8, command=lambda:checker(button5))
button5.grid(row=5, column=2,rowspan=3, sticky = S+N+E+W)

button6 = Button(tk, text=" ", font=('Times 26 bold'),bg='#fbfed2', height=4, width=8, command=lambda:checker(button6))
button6.grid(row=5, column=3,rowspan=3, sticky = S+N+E+W)


button7 = Button(tk, text=" ", font=('Times 26 bold'),bg='#fbfed2', height=4, width=8, command=lambda:checker(button7))
button7.grid(row=8, column=1,rowspan=3, sticky = S+N+E+W)

button8 = Button(tk, text=" ", font=('Times 26 bold'),bg='#fbfed2', height=4, width=8, command=lambda:checker(button8))
button8.grid(row=8, column=2,rowspan=3, sticky = S+N+E+W)

button9 = Button(tk, text=" ", font=('Times 26 bold'),bg='#fbfed2', height=4, width=8, command=lambda:checker(button9))
button9.grid(row=8, column=3,rowspan=3, sticky = S+N+E+W)


label1 = Label(tk, text="Damian Adamiak @ 2018", font=('Consolas', 25,"bold"),bg='#f6ee65')
label1.grid(row=11, column=0, columnspan=5, sticky = S+N+E+W)

label2 = Label(tk, text=" ", font=('Consolas', 25,"bold"),bg='#f6ee65')
label2.grid(row=1, column=0, columnspan=5, sticky = S+N+E+W)


label5_1 = Label(tk, text=" ", bg='#f6ee65')
label5_1.grid(row=1, column=0, rowspan=12, sticky = S+N+E+W)
label5_2 = Label(tk, text=" ", bg='#f6ee65')
label5_2.grid(row=1, column=4, rowspan=12, sticky = S+N+E+W)


label3 = Label(tk, text=x, font=('Consolas', 25,"bold"),bg='#f6ee65', fg='red')
label3.grid(row=6, column=0, sticky = S+N+E+W)
label3_1 = Label(tk, text="X:", font=('Consolas', 25,"bold"), bg='#f6ee65', fg='red')
label3_1.grid(row=5, column=0, sticky = S+N+E+W)

label4 = Label(tk, text=o, font=('Consolas', 25,"bold"),bg='#f6ee65', fg='green')
label4.grid(row=6, column=4, sticky = S+N+E+W)
label4_1 = Label(tk, text="O:", font=('Consolas', 25,"bold"),bg='#f6ee65', fg='green')
label4_1.grid(row=5, column=4, sticky = S+N+E+W)

label6 = Label(tk, text=" ", font=('Consolas', 25,"bold"),bg='#f6ee65', fg='black')
label6.grid(row=0, column=0, columnspan=5, sticky = S+N+E+W)
label6_1 = Label(tk, text="Runda:", font=('Consolas', 25,"bold"),bg='#f6ee65', fg='black')
label6_1.grid(row=0, column=1, sticky = S+N+E+W)
label6_2 = Label(tk, text=rm, font=('Consolas', 25,"bold"),bg='#f6ee65', fg='black')
label6_2.grid(row=0, column=3, sticky = S+N+E+W)


podajrundy()
tura()

tk.mainloop()

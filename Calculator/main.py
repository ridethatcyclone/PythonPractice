from tkinter import * 
from tkinter import ttk

# Simple Calculator app (tkinter practice)
# Author: Abby Horner
# Last Edited: 16. July 2025
# 
# TODO: add some error checking
# TODO: the loop is a bit weird and you can't continue to manipulate numbers after you hit the first enter, it will start over. Ideally, you should be able to start adding to the val again
#

val = ""

def calc():
    # Required
    root = Tk() 

    # Configure the window
    root.title("Calculator")
    root.geometry("240x290")

    # Frames 
    topFrame = ttk.Frame(root,padding="12 4 12 12")
    topFrame.grid(column=0,row=0,sticky=(N,W,E,S))
    root.columnconfigure(0,weight=1)
    root.rowconfigure(0,weight=1)

    # Widgets 
    ## Text entry box
    display = StringVar()
    entry = Entry(topFrame,textvariable=display)
    entry.grid(columnspan=4,ipadx=40,ipady=10,pady=10)

    ## Number buttons
    def pressButton(key):
        global val 
        val += str(key)
        display.set(val)

    def enter():
        global val 
        try: 
            result = str(eval(val))
            display.set(result)
            val = ""
        except:
            display.set("ERROR")
            val=""
    
    def clear():
        global val 
        val = ""
        display.set(val)


    btn7 = Button(topFrame,text='7',command=lambda: pressButton(7), width=5,height=2)
    btn7.grid(column=0,row=2,sticky=(N,W,E,S))
    btn8 = Button(topFrame,text='8',command=lambda: pressButton(8), width=5,height=2)
    btn8.grid(column=1,row=2,sticky=(N,W,E,S))
    btn9 = Button(topFrame,text='9',command=lambda: pressButton(9), width=5,height=2)
    btn9.grid(column=2,row=2,sticky=(N,W,E,S))

    btn4 = Button(topFrame,text='4',command=lambda: pressButton(4), width=5,height=2)
    btn4.grid(column=0,row=3,sticky=(N,W,E,S))
    btn5 = Button(topFrame,text='5',command=lambda: pressButton(5), width=5,height=2)
    btn5.grid(column=1,row=3,sticky=(N,W,E,S))
    btn6 = Button(topFrame,text='6',command=lambda: pressButton(6), width=5,height=2)
    btn6.grid(column=2,row=3,sticky=(N,W,E,S))

    btn1 = Button(topFrame,text='1',command=lambda: pressButton(1), width=5,height=2)
    btn1.grid(column=0,row=4,sticky=(N,W,E,S))
    btn2 = Button(topFrame,text='2',command=lambda: pressButton(2), width=5,height=2)
    btn2.grid(column=1,row=4,sticky=(N,W,E,S))
    btn3 = Button(topFrame,text='3',command=lambda: pressButton(3), width=5,height=2)
    btn3.grid(column=2,row=4,sticky=(N,W,E,S))

    btn0 = Button(topFrame,text='0',command=lambda: pressButton(0), width=10,height=2)
    btn0.grid(column=0,row=5,columnspan=2,sticky=(N,W,E,S))
    
    ## Symbol buttons
    addBtn = Button(topFrame,text='+',command=lambda: pressButton('+'), width=5)
    addBtn.grid(column=3,row=2,rowspan=2,sticky=(N,W,E,S))

    decBtn = Button(topFrame, text=".",command=lambda: pressButton('.'),width=5,height=2)
    decBtn.grid(column=2,row=5,sticky=(N,W,E,S))

    enterBtn = Button(topFrame,text="Enter",command=lambda: enter(),width=5)
    enterBtn.grid(column=3,row=4,rowspan=2,sticky=(N,W,E,S))

    clearBtn = Button(topFrame,text='C',command=lambda:clear(),width=5,height=2)
    clearBtn.grid(column=0,row=1,stick=(N,W,E,S))

    divBtn = Button(topFrame,text="/",command=lambda: pressButton("/"),width=5,height=2)
    divBtn.grid(column=1,row=1,sticky=(N,W,E,S))

    multBtn = Button(topFrame,text="*",command=lambda:pressButton("*"),width=5,height=2)
    multBtn.grid(column=2,row=1,sticky=(N,W,E,S))

    subBtn = Button(topFrame,text="-",command=lambda:pressButton("-"),width=5,height=2)
    subBtn.grid(column=3,row=1,sticky=(N,W,E,S))

    ## Keyboard presses
    root.bind(1,lambda event: pressButton(1))
    root.bind(2,lambda event: pressButton(2))
    root.bind(3,lambda event: pressButton(3))
    root.bind(4,lambda event: pressButton(4))
    root.bind(5,lambda event: pressButton(5))
    root.bind(6,lambda event: pressButton(6))
    root.bind(7,lambda event: pressButton(7))
    root.bind(8,lambda event: pressButton(8))
    root.bind(9,lambda event: pressButton(9))
    root.bind(0,lambda event: pressButton(0))
    root.bind("+",lambda event:pressButton('+'))
    root.bind("-",lambda event: pressButton("-"))
    root.bind("/",lambda event:pressButton("/"))
    root.bind("*",lambda event: pressButton("*"))
    root.bind("c",lambda event:clear())
    root.bind("<Return>",lambda event: enter())

    # Loop launches the window
    root.mainloop()

def main():
    calc()

if __name__ == "__main__":
    main()

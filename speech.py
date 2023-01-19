import os
from gtts import gTTS
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
from tkinter import END, Button, Label, Menu, filedialog,ttk
def voice():
    if monthchoosen.get()=='malayalam':
        lan='ml'
    elif monthchoosen.get()=='english':
        lan='en'
    else:
        tkinter.messagebox.showerror('ERROR!!','languge is not valid')

    k=open(inpu.get(),'r').read()
    
    out=gTTS(text=k,lang=lan,slow=False)
    out.save('output.mp3')#output file
    os.system('afplay output.mp3')



def browse():
    filenameis= filedialog.askopenfilename(initialdir="/",title="Input file please mention here")
    inpu.insert(0,filenameis)
def clearall():
    inpu.delete(0,END)
window=tk.Tk()
window.geometry("430x140")

window.title("Voice over engine")
my=Menu(window)
tk.Label(window,text='enter text file address',fg='green').grid(row=0,column=0)
inpu=tk.Entry(window)
inpu.grid(row=0,column=1)
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width = 20, textvariable = n)
  
# Adding combobox drop down list
monthchoosen['values'] = ('english', 
                          'malayalam')
monthchoosen.grid(column = 1, row =1)
monthchoosen.current()
print(monthchoosen)
tk.Label(window,text='Choose language',fg='blue').grid(row=1,column=0)
tk.Button(window,text="browse",bg='blue',activebackground="red",command=lambda:browse()).grid(row=0,column=2)
image = Image.open('111.png')#give your icon image at 111.png
# The (450, 350) is (height, width)
image = image.resize((50, 50), Image.ANTIALIAS)
my_img = ImageTk.PhotoImage(image)
tk.Button(window,image=my_img,command=lambda:voice()).grid(row=3,column=1)
Button(window,text='clear',bg='red',command=lambda:clearall()).grid(row=3,column=2)
Button(window,text="Stop",bg="red",command=window.distroy()).grid(row=4,column=2)
window.mainloop()

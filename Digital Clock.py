from tkinter import Label, PhotoImage, Tk 
import time

root = Tk() 
root.title("Simple Digital Clock") 
root.geometry("430x150") 
root.resizable('False','False')

text_font= ("Digital", 72, 'bold')
background = "#C0C0C0"
foreground= "#000000"
border_width = 25

label = Label(root, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock(): 
   local_time = time.strftime("%H:%M:%S")
   label.config(text=local_time) 
   label.after(200, digital_clock)

digital_clock()
root.mainloop()
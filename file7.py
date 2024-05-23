
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="grey")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("neutral")
def play_song():
    from playsound import playsound
    playsound('Netural_song/aj mai upar.mp3')
    
def play_song1():
    from playsound import playsound
    playsound('Netural_song/baarish ki jaaye.mp3')   
    
def play_song2():
    from playsound import playsound
    playsound('Netural_song/laal ishq.mp3')   
    
def play_song3():
    from playsound import playsound
    playsound('Netural_song/mere nishaan.mp3')    
    
    
def play_song4():
    from playsound import playsound
    playsound('Netural_song/pal har pal har.mp3')  
    
def play_song5():
    from playsound import playsound
    playsound('Netural_song/tum se hi.mp3')    

def play_song6():
    from playsound import playsound
    playsound('Netural_song/Tum Se Hi.mp3')  

def play_song7():
    from playsound import playsound
    playsound('Masakali.mp3')

# #
label_l1 = tk.Label(root, text="!!___Neutral Face Detected___!!",font=("Algerian", 35, 'bold'),bg="#ffccff",fg="black")
label_l1.place(x=350, y=10)

frame_alpr = tk.LabelFrame(root, text=" --Recommended song-- ", width=1500, height=820, bd=5, font=('Algerian', 14, ' bold '),bg="white")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=40, y=100)

image3 = Image.open(r'Netural_song/aj mai upar.jpg')
image3 = image3.resize((100, 100), Image.ANTIALIAS)
background_image3 = ImageTk.PhotoImage(image3)
background_label3 = tk.Label(root, image=background_image3,text="aj mai upar ",compound='bottom')
background_label3.image = background_image3
background_label3.place(x=70, y=140)
button1 = tk.Button(root, text="Play ",command=play_song, height=1,width=10,font=('times', 15, ' bold '), bg="brown4", fg="white")
button1.place(x=60, y=250)   

   
image4 = Image.open(r'Netural_song/baarish ki jaaye.jpg')
image4 = image4.resize((100, 100))
background_image4 = ImageTk.PhotoImage(image4)
background_label4 = tk.Label(root, image=background_image4,text="baarish ki jaaye",compound='bottom')
background_label4.image = background_image4
background_label4.place(x=450, y=140)
button2 = tk.Button(root, text="Play ",command=play_song1, height=1,width=10,font=('times', 15, ' bold '), bg="brown4", fg="white")
button2.place(x=450, y=250)   
    
    
image5 = Image.open(r'Netural_song/laal ishq.jpg')
image5 = image5.resize((100, 100), Image.ANTIALIAS)
background_image5 = ImageTk.PhotoImage(image5)
background_label5 = tk.Label(root, image=background_image5,text="laal ishq",compound='bottom')
background_label5.image = background_image5
background_label5.place(x=850, y=140)
button3 = tk.Button(root, text="Play ",command=play_song2, height=1,width=10,font=('times', 15, ' bold '), bg="brown4", fg="white")
button3.place(x=850, y=250)  

    
image6 = Image.open(r'Netural_song/mere nishaan.jpg')
image6 = image6.resize((100, 100), Image.ANTIALIAS)
background_image6 = ImageTk.PhotoImage(image6)
background_label6 = tk.Label(root, image=background_image6,text="mere nishaan",compound='bottom')
background_label6.image = background_image6
background_label6.place(x=60, y=340)
button4 = tk.Button(root, text="Play ",command=play_song3, height=1,width=10,font=('times', 15, ' bold '), bg="brown4", fg="white")
button4.place(x=60, y=450)



image7 = Image.open(r'Netural_song/pal har pal har.jpg')
image7 = image7.resize((100, 100), Image.ANTIALIAS)
background_image7 = ImageTk.PhotoImage(image7)
background_label7 = tk.Label(root, image=background_image7,text="pal har pal har",compound='bottom')
background_label7.image = background_image7
background_label7.place(x=455, y=340)
button5 = tk.Button(root, text="Play ",command=play_song4, height=1,width=10,font=('times', 15, ' bold '), bg="brown4", fg="white")
button5.place(x=440, y=450)


image8 = Image.open(r'Netural_song/tum se hi.jpg')
image8 = image8.resize((100, 100), Image.ANTIALIAS)
background_image8 = ImageTk.PhotoImage(image8)
background_label8 = tk.Label(root, image=background_image8,text="tum se hi",compound='bottom')
background_label8.image = background_image8
background_label8.place(x=850, y=340)
button6 = tk.Button(root, text="Play ",command=play_song5, height=1,width=10,font=('times', 15, ' bold '), bg="brown4", fg="white")
button6.place(x=850, y=450)
   
# image9 = Image.open(r'Tum Se Hi quote.jpg')
# image9 = image9.resize((200, 200), Image.ANTIALIAS)
# background_image9 = ImageTk.PhotoImage(image9)
# background_label9 = tk.Label(root, image=background_image9,text="Tum Se Hi",compound='bottom')
# background_label9.image = background_image9
# background_label9.place(x=850, y=490)
# button7 = tk.Button(root, text="Play ",command=play_song6, height=1,width=10,font=('times', 25, ' bold '), bg="brown4", fg="white")
# button7.place(x=850, y=720)
    
    
# image10 = Image.open(r'mask.jpg')
# image10 = image10.resize((200, 200), Image.ANTIALIAS)
# background_image10 = ImageTk.PhotoImage(image10)
# background_label10 = tk.Label(root, image=background_image10,text="MUNA BHAI MBBS",compound='bottom')
# background_label10.image = background_image10
# background_label10.place(x=1300, y=490)
# button8 = tk.Button(root, text="Play ",command=play_song7, height=1,width=10,font=('times', 25, ' bold '), bg="brown4", fg="white")
# button8.place(x=1300, y=720)
    

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#################################################################################################################
def window():
    root.destroy()



root.mainloop()
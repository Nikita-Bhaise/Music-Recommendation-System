# -*- coding: utf-8 -*-

from subprocess import call
import tkinter as tk
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from PIL import Image, ImageTk
from tkinter import ttk
from sklearn.decomposition import PCA
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from tkinter.filedialog import askopenfilename
import pygame
# Program to extract number of
# columns in Python
import xlrd


import xlwt
import xlrd
root = tk.Tk()
root.title("music Genery")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
lbl = tk.Label(root, text="credit risk analysis", font=('times', 35,' bold '), height=2, width=62,bg="violet Red",fg="Black")
lbl.place(x=0, y=0)
def test():
    fileName = askopenfilename(initialdir='/genres_original', title='Select image',
                           filetypes=[("all files", "*.*")])
    fnn=os.path.basename(fileName)
    # fnn=fileName
    print(fnn)
    
    pygame.mixer.init()
    crash_sound = pygame.mixer.Sound("*.*.wav")
    crash_sound.play()
    
    
    # loc = ("E://music genery svm//music genery svm//archive (1)//Data//genres_original")
 
    # wb = xlrd.open_workbook(loc)
    # sheet = wb.sheet_by_index(0)
 
    # sheet.cell_value(0, 0)
 
    #print(sheet.row_values(1))
    #workbook = xlrd.open_workbook('/home/vanx/Documents/features_30_sec.xlsx')
    #sheet = workbook.sheet_by_name('data')
    # import openpyxl

    # theFile = openpyxl.load_workbook('E:/music genery svm/music genery svm/archive (1)/f.xlsx')
    # allSheetNames = theFile.sheetnames
    
    # print("All sheet names {} " .format(theFile.sheetnames))
    
    
    # for sheet in allSheetNames:
    #     print("Current sheet name is {}" .format(sheet))
    #     currentSheet = theFile[sheet]
        
        
        
    #     # print(currentSheet['B4'].value)
    
    #     #print max numbers of wors and colums for each sheet
    #     #print(currentSheet.max_row)
    #     #print(currentSheet.max_column)
    
    #     for row in range(1, currentSheet.max_row + 1):
    #         #print(row)
    #         for column in fnn:  # Here you can add or reduce the columns
    #             cell_name = "{}{}".format(column, row)
    #             print(cell_name)
    #             print("cell position {} has value {}".format(cell_name, currentSheet[cell_name].value))


button3 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
                    text="Upload Audio File", command=test, width=15, height=2)
button3.place(x=5, y=200)





def window():
    root.destroy()

# # button2 = tk.Button(root, foreground="white", background="black", font=("Tempus Sans ITC", 14, "bold"),
# #                     text="Data_Preprocessing", command=Data_Preprocessing, width=15, height=2)
# # button2.place(x=5, y=120)

# button3 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
#                     text="Model Training", command=Model_Training, width=15, height=2)
# button3.place(x=5, y=200)

# # button4 = tk.Button(root, foreground="white", background="#560319", font=("Tempus Sans ITC", 14, "bold"),
# #                     text="Credit Analysis", command=call_file, width=15, height=2)
# button4.place(x=5, y=280)
# exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('times', 15, ' bold '),bg="red",fg="white")
# exit.place(x=5, y=380)

root.mainloop()
from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox
############CSV###############
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']


def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
##############################

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') # นี่คือชื่อโปรแกรม
GUI.geometry('900x400') # นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกสินค้าคงคลัง',font=('Arial Unicode MS',25),fg='#01A6BA')
L1.place(x=30,y=20)
########################

##########บันทึกข้อมูลสินค้า#################
LF1 = ttk.LabelFrame(GUI,text='กรอกชื่อและจำนวนของสินค้า')
LF1.place(x=50,y=100)

v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Arial Unicode MS',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] #[เวลา,ข้อมูลที่ได้จาการกรอก]
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

B1 = ttk.Button(LF1,text='บันทึกข้อมูล',command=SaveData)
B1.pack(ipadx=20,ipady=15)



GUI.mainloop()
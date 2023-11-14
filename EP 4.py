from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox
##############CSV############### ถูก
import csv

def writecsv(datalist):
    with open('data','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen','pencil','eraser']


def readcsv():
    with open('data',encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fr = file reader
        data = list(fr)
    return data
############################# ถูก

GUI = Tk()  # หน้าจอโปรแกรม
GUI.title("ดูดวงสาขาสยาม")  # ชื่อโปรแกรม
GUI.geometry("1000x400")  # ตั้งค่าขนาดหน้าต่าง



L1 = Label(GUI,text="ดูดวงเด็กสาขาสยามวันนี้",font=("Angsana New",16),fg="gray")
L1.place(x=230,y=0)


#L2 = Label(GUI,text="เมย์เป็นเด็กดี",font=("Angsana New",16),fg="red")
#L2.place(x=230,y=200)
           
###
def Button1():
    text = "ครูเฟินเลี้ยงขนมและพักเพิ่ม 10 นาที"
    messagebox.showinfo("ผลลัพธ์",text)

FB1 = Frame(GUI) #กระดาน
FB1.place(x=100,y=50)
B1 = ttk.Button(FB1, text="กดที่นี้",command=Button1)
B1.pack(ipadx=10,ipady=0)
#########
def AKA():
    text = "งดพักเบรค"
    messagebox.showerror("ผลลัพธ์",text)
FB2 = Frame(GUI)
FB2.place(x=250,y=50)
B2 = ttk.Button(FB2, text="กดที่นี้",command=AKA)
B2.pack(ipadx=10,ipady=0)
#########
def DS():
    text = "ลดเวลาพัก"
    messagebox.showwarning("ผลลัพธ์",text)
FB3 = Frame(GUI)
FB3.place(x=400,y=50)
B3 = ttk.Button(FB3, text="กดที่นี้",command=DS)
B3.pack(ipadx=10,ipady=0)



##########SECTION RIGHT##########
LF1 = ttk.LabelFrame(GUI,text='ช่องสุ่ม')
LF1.place(x=510,y=50)

v_data = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

B4 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B4.pack(ipadx=20,ipady=20)



GUI.mainloop()
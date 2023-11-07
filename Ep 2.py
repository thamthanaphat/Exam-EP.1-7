from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()  # หน้าจอโปรแกรม
GUI.title("ดูดวงสาขาสยาม")  # ชื่อโปรแกรม
GUI.geometry("600x400")  # ตั้งค่าขนาดหน้าต่าง



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




GUI.mainloop()

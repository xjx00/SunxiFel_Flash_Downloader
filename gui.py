#!/usr/bin/python
# -*- coding: UTF-8 -*-

from tkinter import *
from tkinter.filedialog import askopenfilename
import subprocess
import tkinter.messagebox
import os

cwd=os.getcwd()

def cmd(file,addr):
    if(addr.get()!="" and file.get()!=""):
        str1=cwd+"/sunxi-fel.exe -p spiflash-write "+addr.get()+" "+file.get()
        print(str1)
        cmd=subprocess.call(str1)
        if(cmd != 0):
            tkinter.messagebox.askquestion(title='Complete', message='Flash Done')
        else:
            tkinter.messagebox.askquestion(title='ERROR', message='Flash Error')
    else:
        tkinter.messagebox.askquestion(title='ERROR', message='Input cannot be none')

def download():
    if(d1.get()):
        cmd(path1,addr1)
    if(d2.get()):
        cmd(path2,addr2)
    if(d3.get()):
        cmd(path3,addr3)
    if(d4.get()):
        cmd(path4,addr4)

#检测flash大小
def checkflash():
    p=os.popen(cwd+"/sunxi-fel spiflash-info").read()
    try:
        Mbyte=int(p.split(" ")[6])/1024/1024
    except IndexError:
        var1.set("No device found!")
    else:
        var1.set("FlashSize:"+str(Mbyte)+"Mbyte")
    addr1.set("0x0000000")
    addr2.set("0x0100000")
    addr3.set("0x0110000")
    addr4.set("0x0510000")


root = Tk()
root.geometry('380x150')
root.resizable(width=False, height=False)
root.title("SunxiFel SPIFlash Downloader")

#声明4个复选框
d1=IntVar()
d2=IntVar()
d3=IntVar()
d4=IntVar()

Checkbutton(root,variable=d1,onvalue=1,offvalue=0).grid(row=1,column=1)
Checkbutton(root,variable=d2,onvalue=1,offvalue=0).grid(row=2,column=1)
Checkbutton(root,variable=d3,onvalue=1,offvalue=0).grid(row=3,column=1)
Checkbutton(root,variable=d4,onvalue=1,offvalue=0).grid(row=4,column=1)

#声明文件选择器
path1=StringVar()
path2=StringVar()
path3=StringVar()
path4=StringVar()

addr1=StringVar()
addr2=StringVar()
addr3=StringVar()
addr4=StringVar()

var1 = StringVar()

Entry(root,textvar=path1).grid(row=1,column=2)
Button(root,text="...",command=lambda:path1.set(askopenfilename())).grid(row=1,column=3)
Label(root,text="@").grid(row=1,column=4)
Entry(root,textvar=addr1).grid(row=1,column=5)

Entry(root,textvar=path2).grid(row=2,column=2)
Button(root,text="...",command=lambda:path2.set(askopenfilename())).grid(row=2,column=3)
Label(root,text="@").grid(row=2,column=4)
Entry(root,textvar=addr2).grid(row=2,column=5)

Entry(root,textvar=path3).grid(row=3,column=2)
Button(root,text="...",command=lambda:path3.set(askopenfilename())).grid(row=3,column=3)
Label(root,text="@").grid(row=3,column=4)
Entry(root,textvar=addr3).grid(row=3,column=5)

Entry(root,textvar=path4).grid(row=4,column=2)
Button(root,text="...",command=lambda:path4.set(askopenfilename())).grid(row=4,column=3)
Label(root,text="@").grid(row=4,column=4)
Entry(root,textvar=addr4).grid(row=4,column=5)

lb1=Label(root,textvariable=var1).grid(row=5,column=2)
Button(root,text="下载",command=download).grid(row=5,column=3)

checkflash()
root.mainloop()

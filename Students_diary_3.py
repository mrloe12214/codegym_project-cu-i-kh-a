from tkinter import *
import os
import pandas as pd
import matplotlib as plt

#Kết nối API ggsheet
import gspread
sa = gspread.service_account()
sh = sa.open("SStudent_Manager")

root = Tk()
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#Cài đặt font
from tkinter.font import Font
fontt = Font(family="Segoe UI",size=36,weight="bold", slant = "roman", underline = 0, overstrike = 0)
font1 = Font(family="Segoe UI",size=16,weight="bold", slant = "roman", underline = 0, overstrike = 0)
font2 = Font(family="Segoe UI",size=16,weight="bold", slant = "italic", underline = 0, overstrike = 0)
font3 = Font(family="Segoe UI",size=12,weight="normal", slant = "roman", underline = 0, overstrike = 0)
#Home
home_scr = Frame(root, background = "light blue")
Lb_Home_screen = Label(home_scr, text = "Special Student Diary", font = fontt, fg = "blue", bg = "light blue")
Lb_Home_screen.pack(padx = 100, pady = 100, fill = BOTH, expand = True)
But_info = Button(home_scr, text = "THÔNG TIN HỌC SINH",font = font1, fg = "black" , bg = "light gray", activebackground = "gray",command = lambda:show_frame(info))
But_info.pack(padx = 10, pady = 10, fill = BOTH, expand = True)
But_Sche = Button(home_scr, text = "THỜI KHÓA BIỂU", font = font1, fg = "black" , bg = "light gray", activebackground = "gray", command = lambda:show_frame(sche))
But_Sche.pack(padx = 10, pady = 10, fill = BOTH, expand = True)
But_homework = Button(home_scr, text = "BÀI TẬP VỀ NHÀ",font = font1, fg = "black" , bg = "light gray", activebackground = "gray", command = lambda:show_frame(hw))
But_homework.pack(padx = 10, pady = 10, fill = BOTH, expand = True)

#info
info = Frame(root)
Lb_info = Label(info, text = "THÔNG TIN HỌC SINH",font = font1, fg = 'blue')
Lb_info.place(anchor = NW)

But_home = Button(info, text = "Trang chủ",fg = "black" , bg = "light blue", activebackground = "light gray", command = lambda:show_frame(home_scr))
But_home.place(x = 10, y = 100, width = 80, height = 35)
But_search = Button(info, text = "Tìm kiếm",fg = "black" , bg = "light blue", activebackground = "light gray")
But_search.place(x = 100, y = 100, width = 80, height = 35)

#Schedule
sche = Frame(root)
lb_sche = Label(sche, text = "THỜI KHÓA BIỂU",font = font1, fg = 'blue')
lb_sche.place(anchor = NW)

#Homework
hw = Frame(root)
lb_hw = Label(hw, text = "BÀI TẬP VỀ NHÀ",font = font1, fg = 'blue')
lb_hw.place(anchor = NW)

for frame in (home_scr, info, sche, hw):
    frame.grid(row=0, column = 0, sticky = "nsew")

def show_frame(frame):
    frame.tkraise()

show_frame(home_scr)


root.mainloop() 

# import thu vien tkinter
from tkinter import *
from tkinter import ttk
import json

def submit():
    msg = {
        "tenDayChuyen":f1int1.get(),
        "tenMay":f1int2.get(),
        "ca":f1int3.get(),
        "maSanPham":f1int4.get(),
        "tenSanPham":f1int5.get(),
        "speed":f2int1.get(),
        "timeDungMay":f2int2.get(),
        "timeChapNhanGoi":f2int2.get(),
        "timeTinhGoiCan":f2int3.get(),
        "timeDayGoiCan":f2int4.get(),
        "timePLC":f2int5.get(),
    }
    msg=json.dumps(msg)
    print(msg)
#khoi tao dashboad
dashboad = Tk()
dashboad.title("cài đặt thông số")
frame1 = Frame(dashboad, borderwidth=1, relief=RAISED)
frame1.pack()
frame2 = Frame(dashboad, borderwidth=1, relief=RAISED)
frame2.pack()
frame3 = Frame(dashboad, borderwidth=1, relief=RAISED)
frame3.pack()
#fram1
lb1 = Label(frame1, text="tên dây chuyền").grid(row=0, column=0)
f1int1 = StringVar()
c1 = ttk.Combobox(frame1, textvariable = f1int1, values=("line1","line2","line3","line4")).grid(row=0, column=1)
lb2 = Label(frame1, text="tên máy").grid(row=1, column=0)
f1int2 = StringVar()
c2 = ttk.Combobox(frame1, textvariable = f1int2, values=("may 1","may 2","may 3","may 4")).grid(row=1, column=1)
lb3 = Label(frame1, text="ca").grid(row=2, column=0)
f1int3 = StringVar()
c3 = ttk.Combobox(frame1, textvariable = f1int3, values=("ca 1","ca 2","ca 3","ca 4")).grid(row=2, column=1)
lb4 = Label(frame1, text="mã sản phẩm").grid(row=3, column=0)
f1int4 = StringVar()
c4 = ttk.Combobox(frame1, textvariable = f1int4, values=("Sp 1","Sp 2","Sp 3","Sp 4")).grid(row=3, column=1)
lb5 = Label(frame1, text="tên sản phẩm").grid(row=4, column=0)
f1int5 = StringVar()
c5 = ttk.Combobox(frame1, textvariable = f1int5, values=("san pham 1","san pham 2","san pham 3","san pham 4")).grid(row=4, column=1)

#frame2
lb1 = Label(frame2, text="tốc độ chuẩn (gói/phút)").grid(row=0, column=0)
f2int1 = IntVar()
e1 = Entry(frame2, textvariable=f2int1).grid(row=0, column=1)
lb2 = Label(frame2, text="thời gian tính dừng máy (x0.1s)").grid(row=1, column=0)
f2int2 = IntVar()
e2 = Entry(frame2, textvariable=f2int2).grid(row=1, column=1)
lb3 = Label(frame2, text="thời gian chấp nhận gói (x0.1s)").grid(row=2, column=0)
f2int3 = IntVar()
e3 = Entry(frame2, textvariable=f2int3).grid(row=2, column=1)
lb4 = Label(frame2, text="thời gian tính gói cấn (x0.1s)").grid(row=3, column=0)
f2int4 = IntVar()
e4 = Entry(frame2, textvariable=f2int4).grid(row=3, column=1)
lb5 = Label(frame2, text="thời gian đầy gói cấn (x0.1s)").grid(row=4, column=0)
f2int5 = IntVar()
e5 = Entry(frame2, textvariable=f2int5).grid(row=4, column=1)
lb6 = Label(frame2, text="thời gian cập nhật từ PLC (s)").grid(row=5, column=0)
f2int6 = IntVar()
e6 = Entry(frame2, textvariable=f2int6).grid(row=5, column=1)

#fram3
b1 = Button(frame3, text="cài đặt", command=submit).grid(row=0, column=0)
b2 = Button(frame3, text="đóng", command=dashboad.quit).grid(row=0, column=1)


#run dashboad
dashboad.mainloop()
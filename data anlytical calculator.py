from tkinter import *



root=Tk()
root.geometry("900x600")
root.maxsize(900,600)
root.title("Industrial Analyser")
root.wm_iconbitmap("1.ico")
root.configure(background="light blue")

def click(event):
    global scv
    text= event.widget.cget("text")
    print(text)
    if text =="  C  ":
        scv.set('')
        screen.update()
        pass
    elif text=="Ans":
        if scv.get().isdigit():
            r=int(scv.get())
        else:
            try:
                r=eval(scv.get())
            except:
                r='Math Error'
        scv.set(r)
        screen.update()
        pass
    else:
        scv.set(scv.get() + text)
        screen.update()


T1 = Label(text='Basic Calculation', bg="black", fg="white", padx=5,font="lucida 20 bold", pady=5)
T1.pack()

scv=StringVar()
scv.set("")
screen=Entry(root,textvariable= scv,font="lucida 15 bold")
screen.pack(fill=X,ipadx=8,pady=10,padx=10)
frame=Frame(root,borderwidth=5,bg="grey")
frame1=Frame(root,borderwidth=5,bg="grey")


b1=Button(frame,fg='black',text="9",font="lucida 20 bold",padx=5,pady=8)
b1.bind('<Button-1>',click)
b1.pack(side=LEFT,padx=5,pady=5)

b2=Button(frame,fg='black',text="8",font="lucida 20 bold",padx=5,pady=8)
b2.bind('<Button-1>',click)
b2.pack(side=LEFT,padx=5,pady=5)

b3=Button(frame,fg='black',text="7",font="lucida 20 bold",padx=5,pady=8)
b3.bind('<Button-1>',click)
b3.pack(side=LEFT,padx=5,pady=5)

b4=Button(frame,fg='black',text="6",font="lucida 20 bold",padx=5,pady=8)
b4.bind('<Button-1>',click)
b4.pack(side=LEFT,padx=5,pady=5)

b5=Button(frame,fg='black',text="5",font="lucida 20 bold",padx=5,pady=8)
b5.bind('<Button-1>',click)
b5.pack(side=LEFT,padx=5,pady=5)

b6=Button(frame,fg='black',text="4",font="lucida 20 bold",padx=5,pady=8)
b6.bind('<Button-1>',click)
b6.pack(side=LEFT,padx=5,pady=5)

b6=Button(frame,fg='black',text="3",font="lucida 20 bold",padx=5,pady=8)
b6.bind('<Button-1>',click)
b6.pack(side=LEFT,padx=5,pady=5)

b7=Button(frame,fg='black',text="2",font="lucida 20 bold",padx=5,pady=8)
b7.bind('<Button-1>',click)
b7.pack(side=LEFT,padx=5,pady=5)

b8=Button(frame,fg='black',text="1",font="lucida 20 bold",padx=5,pady=8)
b8.bind('<Button-1>',click)
b8.pack(side=LEFT,padx=5,pady=5)

b8=Button(frame,fg='red',text="0",font="lucida 20 bold",padx=5,pady=8)
b8.bind('<Button-1>',click)
b8.pack(side=LEFT,padx=5,pady=5)


b9=Button(frame1,fg='red',bg='black',text="  C  ",font="lucida 20 bold",padx=5,pady=8)
b9.bind('<Button-1>',click)
b9.pack(side=LEFT,padx=5,pady=5)

b9=Button(frame1,fg='red',text=".",font="lucida 20 bold",padx=5,pady=8)
b9.bind('<Button-1>',click)
b9.pack(side=LEFT,padx=5,pady=5)

b9=Button(frame1,fg='red',text=",",font="lucida 20 bold",padx=5,pady=8)
b9.bind('<Button-1>',click)
b9.pack(side=LEFT,padx=5,pady=5)



b9=Button(frame1,fg='red',text="+",font="lucida 20 bold",padx=5,pady=8)
b9.bind('<Button-1>',click)
b9.pack(side=LEFT,padx=5,pady=5)

b10=Button(frame1,fg='red',text="-",font="lucida 20 bold",padx=5,pady=8)
b10.bind('<Button-1>',click)
b10.pack(side=LEFT,padx=5,pady=5)

b11=Button(frame1,fg='red',text="*",font="lucida 20 bold",padx=5,pady=8)
b11.bind('<Button-1>',click)
b11.pack(side=LEFT,padx=5,pady=5)

b12=Button(frame1,fg='red',text="/",font="lucida 20 bold",padx=5,pady=8)
b12.bind('<Button-1>',click)
b12.pack(side=LEFT,padx=5,pady=5)


b9=Button(frame1,fg='red',text="Ans",bg='black',font="lucida 20 bold",padx=5,pady=8)
b9.bind('<Button-1>',click)
b9.pack(side=LEFT,padx=5,pady=5)



frame.pack(side=TOP)

frame1.pack(side=TOP)



T3 = Label(text='Developer: Md Shamim Hasan', bg="red", fg="white", padx=5, pady=5)
T3.place(x=400, y=550)


root.mainloop()
from tkinter import *
import time
def animation():
    i = 0
    root.update()
    for _ in range(5):
        p = 0
        recr = shape.create_rectangle(120, 50 + i, 170, 90 + i, fill='green')
        root.update()
        for _ in range(5):
            shape.move(recr, p, 0)
            root.update()
            time.sleep(.5)
            p = 50
        i += 40
        shape.delete(recr)

root = Tk()

root.title('Mattrix Traverse')
shape = Canvas(root,width=500,height=300)
shape.pack()
p = 50
inc = 0
for i in range(5):
    name = Label(root,text=i,font=('10'))
    name.pack()
    name.place(x=140+inc,y=25)
    inc+=50
inc = 0
for i in range(5):
    name = Label(root,text=i,font=('10'))
    name.pack()
    name.place(x=90,y=60+inc)
    inc+=40
inc = 0
for i in range(5):
    if(i==1 or i==2):
        name = Label(root, text='1')
        name.pack()
        name.place(x=140 + inc, y=60)
    else:
        name = Label(root, text='0')
        name.pack()
        name.place(x=140 + inc, y=60)
    inc += 50

inc = 0
for i in range(5):
    if(i==3 or i==2):
        name = Label(root, text='1')
        name.pack()
        name.place(x=140 + inc, y=100)
    else:
        name = Label(root, text='0')
        name.pack()
        name.place(x=140 + inc, y=100)
    inc += 50

inc = 0
for i in range(5):
    if(i==3 or i==1):
        name = Label(root, text='1')
        name.pack()
        name.place(x=140 + inc, y=140)
    else:
        name = Label(root, text='0')
        name.pack()
        name.place(x=140 + inc, y=140)
    inc += 50

inc = 0
for i in range(5):
    if(i==4):
        name = Label(root, text='1')
        name.pack()
        name.place(x=140 + inc, y=180)
    else:
        name = Label(root, text='0')
        name.pack()
        name.place(x=140 + inc, y=180)
    inc += 50

inc = 0
for i in range(5):
    if(i==1):
        name = Label(root, text='1')
        name.pack()
        name.place(x=140 + inc, y=220)
    else:
        name = Label(root, text='0')
        name.pack()
        name.place(x=140 + inc, y=220)
    inc += 50


for _ in range(6):
    line = shape.create_line(120,p,370,p,fill='blue')
    p = p+40
p = 30
for _ in range(6):
    line = shape.create_line(90+p,50,90+p,250,fill='blue')
    p+=50

animation()
lable = Label(root,text='Process is complete ')
lable.pack()



button = Button(root,text="Exit",command=root.destroy,width=10,bd=5,fg='green')
button2 = Button(root,text="START ",command=animation,width=10,bd=5,fg='green')
button2.pack(side=TOP)
button.pack()
root.mainloop()












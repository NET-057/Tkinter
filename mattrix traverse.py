from tkinter import *
import time
def animation():
    i = 0
    root.update()
    for _ in range(6):
        p = 0
        recr = shape.create_rectangle(120 + p, 50 + i, 160 + p, 80 + i, fill='green')
        root.update()
        for _ in range(6):
            shape.move(recr, p, 0)
            root.update()
            time.sleep(.3)
            p = 40
        i += 30
        shape.delete(recr)

root = Tk()
root.title('Mattrix Traverse')
shape = Canvas(root,width=500,height=300)
shape.pack()
p = 50
for _ in range(7):
    line = shape.create_line(120,p,360,p,fill='blue')
    p = p+30
p = 30
for _ in range(7):
    line = shape.create_line(90+p,50,90+p,230,fill='blue')
    p+=40

animation()

lable = Label(root,text='Process is complete ')
lable.pack()

button = Button(root,text="Exit",command=root.destroy,width=10,bd=5,fg='green')
button2 = Button(root,text="RESTART ",command=animation,width=10,bd=5,fg='green')
button2.pack(side=TOP)
button.pack()
root.mainloop()












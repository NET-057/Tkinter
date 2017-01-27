from tkinter import *
import time
root = Tk()
root.title('Graph Traversal ')
shape = Canvas(root,width=1000,height=400,bg='#6495ED')

shape.pack()

cir1 = shape.create_oval(280,50,350,80,fill='white')
say = Label(root,text='Depth-first \n Tree Traversal ',font=("Helvetica", 25))
say.pack()
say.place(x=10,y=20)
#say.config(fontsize='30')
say = Label(root,text="0",fg='red',font=(10),bg='white')
say.pack()
say.place(x=310,y=53)
say = Label(root,text="1",fg='red',font=(10),bg='white')
say.pack()
say.place(x=557,y=53)
say = Label(root,text="2",fg='red',font=(10),bg='white')
say.pack()
say.place(x=310,y=253)
say = Label(root,text="3",fg='red',font=(10),bg='white')
say.pack()
say.place(x=557,y=253)
say = Label(root,text="4",fg='red',font=(10),bg='white')
say.pack()
say.place(x=730,y=153)
cir2 = shape.create_oval(530,50,600,80,fill='white')
cir4 = shape.create_oval(530,250,600,280,fill='white')
cir3 = shape.create_oval(280,250,350,280,fill='white')
cir5 = shape.create_oval(700,150,770,180,fill='white' )
line12 = shape.create_line(350,65,530,65)
line121 = shape.create_line(525,60,530,65)
line122 = shape.create_line(525,70,530,65)
line23 = shape.create_line(530,70,350,260,)
line231 = shape.create_line(350,260,350,250)
line23 = shape.create_line(350,260,360,260)

line24 = shape.create_line(550,250,550,78,)
line241 = shape.create_line(550,250,540,245,)
line242 = shape.create_line(550,250,560,245,)

line31 = shape.create_line(300,250,300,80)
line311 = shape.create_line(291,85,300,80)
line312 = shape.create_line(300,80,310,85)
line13 = shape.create_line(330,250,330,80)
line131 = shape.create_line(330,250,320,240)
line132 = shape.create_line(330,250,340,240)
line34 = shape.create_line(350,269,530,269)
line341 = shape.create_line(525,264,530,269)
line342 = shape.create_line(530,269,525,275)
line45 = shape.create_line(600,265,730,180)
line451 = shape.create_line(730,180,717,182)
line452 = shape.create_line(730,180,720,193)

line52 = shape.create_line(581,80,710,157)
line521 = shape.create_line(581,80,581,90)
line522 = shape.create_line(581,80,591,80)
def animation(a):
    p = 0
    i = 0
    if a==0:
        for _ in range(5):
            cir121 = shape.create_oval(280 + p, 50 + i, 350 + p, 80 + i, fill='green')
            shape.update()
            time.sleep(1)
            if(p==250 and i==0):
                p = 0
                i = 200
            elif (i == 0 and p==0):
                 p = 250
            elif(p==0 and i==200):
                 p = 250
            elif(p==250 and i==200):
                p = 420
                i = 100
            shape.delete(cir121)

    elif a==1:
        if (a == 1):
            for _ in range(5):
                cir121 = shape.create_oval(530 + p, 50 + i, 600 + p, 80 + i, fill='green')
                shape.update()
                time.sleep(1)
                if (i == 0 and p == 0):
                    p = -250
                    i = 200
                elif (p == -250 and i == 200):
                    i = 0
                elif (p == -250 and i == 0):
                    p = 0
                    i = 200
                elif (p == 0 and i == 200):
                    p = 170
                    i = 100
                shape.delete(cir121)
    elif a==2:
        cir31 = shape.create_oval(280, 250, 350, 280, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir31)
        cir121 = shape.create_oval(280, 50, 350, 80, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir121)
        cir21 = shape.create_oval(530, 50, 600, 80, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir21)
        cir47 = shape.create_oval(530, 250, 600, 280, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir47)
        cir57 = shape.create_oval(700, 150, 770, 180, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir57)
    elif a==3:
        cir47 = shape.create_oval(530, 250, 600, 280, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir47)
        cir57 = shape.create_oval(700, 150, 770, 180, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir57)
        cir21 = shape.create_oval(530, 50, 600, 80, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir21)
        cir31 = shape.create_oval(280, 250, 350, 280, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir31)
        cir121 = shape.create_oval(280, 50, 350, 80, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir121)
    elif a==4:
        cir57 = shape.create_oval(700, 150, 770, 180, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir57)
        cir21 = shape.create_oval(530, 50, 600, 80, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir21)
        cir31 = shape.create_oval(280, 250, 350, 280, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir31)
        cir121 = shape.create_oval(280, 50, 350, 80, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir121)
        cir47 = shape.create_oval(530, 250, 600, 280, fill='green')
        shape.update()
        time.sleep(1)
        shape.delete(cir47)





if __name__=='__main__':
    lable = Label(root, text='Process is complete ', )
    lable.pack()

    button = Button(root, text="Exit", command=root.destroy, width=10, bd=5, fg='green')

    #Enter Key value in palce of 2 in animation func below button command

    button2 = Button(root, text="START ", command=lambda: animation(2), width=10, bd=5, fg='green')
    button2.pack(side=TOP)
    button.pack()
    root.mainloop()

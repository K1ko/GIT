import tkinter, random

platno=tkinter.Canvas(bg='white',width=1000,height=900)
platno.pack()
l=0
x=50
def tanier():
    global l,x
    a =random.randrange(1,11)
    for i in range(10):
        if a ==i:
            l=x
        platno.create_oval(x,300,x+50,350)
        x+=60
        
tanier()

p=0
    

def Klik(sur):
    global p
    x=sur.x
    y=sur.y
    x1,y1=x,y
    p+=1
    if x>l and x<l+50 :
        platno.create_text(100,450, text= f' Už máme prasknutý tanier, trvalo Vám to {p} kliknutí',anchor ="nw")


def Reštart():
    global p,x
    platno.delete("all")
    p=0
    x=50
    tanier()

platno.bind('<Button-1>', Klik)
button=tkinter.Button(text='znova',command=Reštart)
button.pack()

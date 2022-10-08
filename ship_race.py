import tkinter,random
platno = tkinter.Canvas(bg = "white",width = 800,height = 700)
platno.pack()

def lodicka(x, y):
    plachta = random.randint(-3, 3)
    platno.create_line(x, y, x, y-25, x+10+plachta, y-10, x, y-5)
    platno.create_polygon(x-20, y, x+20, y, x+10, y+8, x-10, y+8)

def nakresli_lodicky():

    for i in range(15):
        lodicka(pozicie[i],i*40+40)
    platno.create_line(650,0,650,650,fill = "red",width = 3)

def vyhra(cislo):
    global start
    start = False
    platno.create_text(350,350,font = "Arial 20",fill = "red",text = "Vyhrala lodička číslo: " + str(cislo+1))

def preteky():
    if start:
        platno.delete("all")
        for i in range(len(pozicie)):
            pozicie[i] += random.randint(1,10)
            if pozicie[i] > 650:
                vyhra(i)
        nakresli_lodicky()
        platno.after(100,preteky)

def klik(sur):
    global start
    if not start:
        start = True
        preteky()

pozicie = [20]*15
start = False
nakresli_lodicky
platno.bind("<Button-1>",klik)

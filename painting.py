import tkinter, random
canvas = tkinter.Canvas(width=700, height=500, bg='lightblue')
canvas.pack()

def kresli_kopec():
    kopec = []
    smer = random.choice((1,-1))                
    kopec.append(0)
    kopec.append(random.randint(200, 500))
    vrchol = random.randint(100, 600)
    for i in range(vrchol // 10):
        nova_hodnota = kopec[-1] + smer * random.randint(0, 5)
        kopec.append(i*10+1)
        kopec.append(nova_hodnota)
    smer = -1 * smer
    for i in range((700-vrchol) // 10 + 10):
        nova_hodnota = kopec[-1] + smer * random.randint(0, 5)
        kopec.append(i*10+vrchol)
        kopec.append(nova_hodnota)

    kopec = [0, 500] + kopec + [700, 500]
    farba = '#00{:02x}00'.format(random.randint(100, 200)) 
    canvas.create_polygon(kopec, fill=farba, outline='black')

def prekresli(event):
    canvas.delete('all')
    for i in range(10):
        kresli_kopec()
        
#kresli_kopec()
canvas.bind_all('<space>', prekresli)

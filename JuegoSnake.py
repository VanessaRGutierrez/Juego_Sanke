import turtle
from turtle import *
import time
import random

posponer = 0.1

#MARCADOR
Score = 0
highScore = 0

#CONFIGURACION DE LA VENTANA
ventana = turtle.Screen()
#Screen para la creacion de la ventana
ventana.title("Mi Jueguito de snake")
ventana.bgcolor("black")
#bgcolor es para darle el color a la ventana
ventana.setup(width=600, height=600)
ventana.tracer(0)
#animaciones mas placenteras

#CREE LA CABEZA DE LA SERPIENTE
cabeza = turtle.Turtle()
cabeza.speed(0)
#speed cuando se inicie la pantalla, el dibujo ya este ahi
cabeza.shape("circle")
#shape para darle la forma a la serpiente
cabeza.color("blue")
cabeza.penup()
#penup para que el turple no deje el rastroventa
cabeza.goto(0,0)
#goto para darle posicion en pantalla
cabeza.direccion = "stop"

#CREACION DE LA COMIDA
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0,100)

#CREACION DE CUERPO DE LA SERPIENTE
#Solo es una lista vacia
segmento = []

#TEXTO
texto = turtle.Turtle()
texto.speed(0)
texto.color("white")
texto.penup()
texto.hideturtle()
texto.goto(0,260)
texto.write("Score: 0    High Score: 0", 
            align="center", font=("Courier", 19, "normal"))
#write es como el print

#FUNCIONES
def arriba():
    cabeza.direccion = "up"

def abajo():
    cabeza.direccion = "down"

def izquierda():
    cabeza.direccion = "left"

def derecha():
    cabeza.direccion = "rigth"

def mov():
    if cabeza.direccion == "up":
        y = cabeza.ycor()
        cabeza.sety(y + 20)

    if cabeza.direccion == "down":
        y = cabeza.ycor()
        cabeza.sety(y - 20)

    if cabeza.direccion == "left":
        x = cabeza.xcor()
        cabeza.setx(x - 20)

    if cabeza.direccion == "rigth":
        x = cabeza.xcor()
        cabeza.setx(x + 20)

#TECLADO
ventana.listen()
ventana.onkeypress(arriba, "Up")
ventana.onkeypress(abajo, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

#CICLO
while True:
    ventana.update()

    #BORDES
    if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
        time.sleep(2)
        cabeza.goto(0,0)
        cabeza.direccion = "stop"

        for segm in segmento:
            segm.goto(1000,1000)
        segmento.clear()

        #resetear marcador
        Score = 0
        texto.clear()
        texto.write("Score: {}    High Score: {}".format(Score, highScore), 
                    align="center", font=("Courier", 19, "normal"))

    #COMIDAA
    if cabeza.distance(comida) < 20:
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        comida.goto(x,y)
        #ramdom para crear numeros ramdos para la aparicion de la comida
        #randint son los numeros enteros, desde que numero hasta que numero
        #goto para actualizar la posicion

        nuevosegmento = turtle.Turtle()
        nuevosegmento.speed(0)
        nuevosegmento.shape("circle")
        nuevosegmento.color("blue")
        nuevosegmento.penup()
        segmento.append(nuevosegmento)

    #aumentar score
        Score += 10

        if Score > highScore:
            highScore = Score

        texto.clear()
        texto.write("Score: {}    High Score: {}".format(Score, highScore), 
                    align="center", font=("Courier", 19, "normal"))

    #Mover el cuepo de la serpiente
    totalsegmento = len(segmento)
    for index in range(totalsegmento -1, 0, -1):
        x = segmento[index - 1].xcor()
        y = segmento[index - 1].ycor()
        segmento[index].goto(x,y)
        #se obtiene las coordenadas y - x

    if totalsegmento > 0:
        x = cabeza.xcor()
        y = cabeza.ycor()
        segmento[0].goto(x,y)

    mov()

    #MUERTE CON EL CUERPO
    for segmen in segmento:
        if segmen.distance(cabeza)<20:
            time.sleep(2)
            cabeza.goto(0,0)
            cabeza.direccion = "stop"
    
            for segmen in segmento:
                segmen.goto(1000,1000)
            segmento.clear()

            Score = 0
            texto.clear()
            texto.write("Score: {}    High Score: {}".format(Score, highScore), 
                        align="center", font=("Courier", 19, "normal"))

    time.sleep(posponer)

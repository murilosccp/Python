import turtle
import time
import random

# Configuração da tela
tela = turtle.Screen()
tela.title("Jogo da Cobra")
tela.bgcolor("black")
tela.setup(width=600, height=600)

# Cabeça da cobra
cabeca = turtle.Turtle()
cabeca.speed(0)
cabeca.shape("square")
cabeca.color("green")
cabeca.penup()
cabeca.goto(0, 0)
cabeca.direction = "stop"

# maça
maça = turtle.Turtle()
maça.speed(0)
maça.shape("square")
maça.color("red")
maça.penup()
maça.goto(0, 100)

# partes do corpo da cobra
segmentos = []

# movimentação da cobra dananda
def mover():
    if cabeca.direction == "up":
        y = cabeca.ycor()
        cabeca.sety(y + 20)
    if cabeca.direction == "down":
        y = cabeca.ycor()
        cabeca.sety(y - 20)
    if cabeca.direction == "left":
        x = cabeca.xcor()
        cabeca.setx(x - 20)
    if cabeca.direction == "right":
        x = cabeca.xcor()
        cabeca.setx(x + 20)

def mover_cima():
    if cabeca.direction != "down":
        cabeca.direction = "up"

def mover_baixo():
    if cabeca.direction != "up":
        cabeca.direction = "down"

def mover_esquerda():
    if cabeca.direction != "right":
        cabeca.direction = "left"

def mover_direita():
    if cabeca.direction != "left":
        cabeca.direction = "right"

# teclado
tela.listen()
tela.onkeypress(mover_cima, "Up")
tela.onkeypress(mover_baixo, "Down")
tela.onkeypress(mover_esquerda, "Left")
tela.onkeypress(mover_direita, "Right")

# loop
while True:
    tela.update()

    # colisão da CABEÇA com as bordas da tela
    if (
        cabeca.xcor() > 290
        or cabeca.xcor() < -290
        or cabeca.ycor() > 290
        or cabeca.ycor() < -290
    ):
        time.sleep(1)
        cabeca.goto(0, 0)
        cabeca.direction = "stop"

        for segmento in segmentos:
            segmento.goto(1000, 1000)
        
        segmentos.clear()

    # verifica a colisão com a maça
    if cabeca.distance(maça) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        maça.goto(x, y)

        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape("square")
        novo_segmento.color("green")
        novo_segmento.penup()
        segmentos.append(novo_segmento)

    # movimento do corpo da danada
    for i in range(len(segmentos) - 1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x, y)

    if len(segmentos) > 0:
        x = cabeca.xcor()
        y = cabeca.ycor()
        segmentos[0].goto(x, y)

    mover()

    # colisão com ela mesma pqp cobra burra
    for segmento in segmentos:
        if segmento.distance(cabeca) < 20:
            time.sleep(1)
            cabeca.goto(0, 0)
            cabeca.direction = "stop"

            for segmento in segmentos:
                segmento.goto(1000, 1000)
            
            segmentos.clear()

    time.sleep(0.1)

tela.mainloop()

import turtle
import time
import random

# Configuração da tela
tela = turtle.Screen()
tela.title("Jogo da Cobra")
tela.bgcolor("white")
tela.setup(width=600, height=600)

# Cabeça da cobra
cabeca = turtle.Turtle()
cabeca.speed(0)
cabeca.shape("square")
cabeca.color("green")
cabeca.penup()
cabeca.goto(0, 0)
cabeca.direction = "stop"

# Maçã
maça = turtle.Turtle()
maça.speed(0)
maça.shape("square")
maça.color("red")
maça.penup()
maça.goto(0, 100)

# Partes do corpo da cobra
segmentos = []

# Pontuação e Nível
pontuacao = 0
nivel = 1

# Função para criar uma nova maçã em uma posição aleatória
def criar_maca():
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    maça.goto(x, y)

# Função para criar um novo segmento no corpo da cobra
def criar_segmento():
    novo_segmento = turtle.Turtle()
    novo_segmento.speed(0)
    novo_segmento.shape("square")
    novo_segmento.color("green")
    novo_segmento.penup()
    return novo_segmento

# Função para mover os segmentos do corpo da cobra
def mover_segmentos():
    for i in range(len(segmentos) - 1, 0, -1):
        x = segmentos[i - 1].xcor()
        y = segmentos[i - 1].ycor()
        segmentos[i].goto(x, y)

    if len(segmentos) > 0:
        x = cabeca.xcor()
        y = cabeca.ycor()
        segmentos[0].goto(x, y)

# Função para verificar colisões com a cobra
def verificar_colisoes():
    for segmento in segmentos:
        if segmento.distance(cabeca) < 20:
            return True
    return False

# Movimentação da cobra
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

# Teclado
tela.listen()
tela.onkeypress(mover_cima, "Up")
tela.onkeypress(mover_baixo, "Down")
tela.onkeypress(mover_esquerda, "Left")
tela.onkeypress(mover_direita, "Right")

pontuacao_texto = turtle.Turtle()
pontuacao_texto.speed(0)
pontuacao_texto.color("black")
pontuacao_texto.penup()
pontuacao_texto.hideturtle()
pontuacao_texto.goto(0, 260)

# Criação do texto do nível
nivel_texto = turtle.Turtle()
nivel_texto.speed(0)
nivel_texto.color("black")
nivel_texto.penup()
nivel_texto.hideturtle()
nivel_texto.goto(0, 230)

# Loop principal do jogo
while True:
    tela.update()

    # Colisão da CABEÇA com as bordas da tela
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
        pontuacao = 0
        nivel = 1

    # Verifica a colisão com a maçã
    if cabeca.distance(maça) < 20:
        criar_maca()
        pontuacao += 1
        novo_segmento = criar_segmento()  # Adiciona um novo segmento à cobra
        segmentos.append(novo_segmento)   # Adiciona o segmento à lista

        # Aumenta o nível conforme a pontuação
        if pontuacao % 5 == 0:  # Aumenta o nível a cada múltiplo de 5 na pontuação
            nivel += 1

    # Movimento do corpo da cobra
    mover_segmentos()

    if len(segmentos) > 0:
        x = cabeca.xcor()
        y = cabeca.ycor()
        segmentos[0].goto(x, y)

    mover()

    # Colisão com ela mesma
    if verificar_colisoes():
        time.sleep(1)
        cabeca.goto(0, 0)
        cabeca.direction = "stop"

        for segmento in segmentos:
            segmento.goto(1000, 1000)
        
        segmentos.clear()
        pontuacao = 0
        nivel = 1
    
    pontuacao_texto.clear()
    pontuacao_texto.write("Pontuação: {}".format(pontuacao), align="center", font=("Courier", 24, "normal"))

    # Atualiza o texto do nível
    nivel_texto.clear()
    nivel_texto.write("Nível: {}".format(nivel), align="center", font=("Courier", 24, "normal"))
    

    # Ajuste do nível de dificuldade
    time.sleep(0.1 - (nivel * 0.01))

tela.mainloop()

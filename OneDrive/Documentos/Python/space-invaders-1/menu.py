from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.gameobject import *
from PPlay.sprite import *
from button import Button


janela = Window(900, 600)
mouse = Mouse()
teclado = Keyboard()


Dfacil = 1
Dmedio = 1.5
Ddificil = 2

btjogar = Button(300, 80, "images/button-jogar.png")
btdificuldade = Button(550, 80, "images/button-dificuldade.png")
btranking = Button(400, 80, "images/button-ranking.png")
btsair = Button(200, 80, "images/button-sair.png")

spjogar = Sprite(btjogar.image)
spdificuldade = Sprite(btdificuldade.image)
spranking = Sprite(btranking.image)
spsair = Sprite(btsair.image)

def JOGO(dificuldade):
    janela = Window(900, 600)
    janela.set_title("Space Invaders - Jogo")

    while True:
        if teclado.key_pressed("esc"):
            MENU()

        janela.update()

def MENU():
    janela.set_title("Space Invaders - Menu")

    spjogar.set_position(janela.width / 2 - btjogar.width / 2, janela.height * 0.4 - btjogar.height / 2)
    spdificuldade.set_position(janela.width / 2 - btdificuldade.width / 2, janela.height * 0.55 - btdificuldade.height / 2)
    spranking.set_position(janela.width / 2 - btranking.width / 2, janela.height * 0.7 - btranking.height / 2)
    spsair.set_position(janela.width / 2 - btsair.width / 2, janela.height * 0.85 - btsair.height / 2)

    diff = Dfacil

    while True:
        if mouse.is_over_object(spjogar) and mouse.is_button_pressed(1):
            JOGO(diff)
        
        
        if mouse.is_over_object(spdificuldade) and mouse.is_button_pressed(1):
            DIFICULDADE()    

        #if mouse.is_over_object(spranking) and mouse.is_button_pressed(1):
            

        if mouse.is_over_object(spsair) and mouse.is_button_pressed(1):
            return

        spjogar.draw()
        spdificuldade.draw()
        spranking.draw()
        spsair.draw()
        janela.update()

def DIFICULDADE():
    janela = Window(900, 600)
    janela.set_title("Space Invaders - Dificuldade")
    
    mouse = Mouse()

    btfacil = Button(230, 80, "images/button-facil.png")
    btmedio = Button(230, 80, "images/button-medio.png")
    btdificil = Button(290, 80, "images/button-dificil.png")
    spfacil = Sprite(btfacil.image)
    spmedio = Sprite(btmedio.image)
    spdificil = Sprite(btdificil.image)

    spfacil.set_position(janela.width / 2 - btfacil.width / 2, janela.height * 0.4 - btfacil.height / 2)
    spmedio.set_position(janela.width / 2 - btmedio.width / 2, janela.height * 0.55 - btmedio.height / 2)
    spdificil.set_position(janela.width / 2 - btdificil.width / 2, janela.height * 0.7 - btdificil.height / 2)
    

    while True:
        if mouse.is_over_object(spfacil) and mouse.is_button_pressed(1):
            JOGO(Dfacil)
        if mouse.is_over_object(spmedio) and mouse.is_button_pressed(1):
            JOGO(Dmedio)
        if mouse.is_over_object(spdificil) and mouse.is_button_pressed(1):
            JOGO(Ddificil)
        
        spfacil.draw()
        spmedio.draw()
        spdificil.draw()

        janela.update()

MENU()
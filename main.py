import pygame as pg
from all_inclusive_class import Figura
from figura_class import Rectangulo, Bolillas
import random

pg.init()

pantalla_principal = pg.display.set_mode( (800,600) )
pg.display.set_caption("Bolillas Rebotando")

#rect1 = Rectangulo(random.randint(0,800),random.randint(0,600),w=random.randint(10,40),h=random.randint(10,40))
#rect2 = Rectangulo(random.randint(0,800),random.randint(0,600),color=(192, 57, 43),w=random.randint(10,40),h=random.randint(10,40))
listaBolillas=[]
for i in range(1,101):
    listaBolillas.append(Figura(random.randint(0,800),random.randint(0,600),color=(random.randint(0,255), random.randint(0,255), random.randint(0,255)),radio=random.randint(5,30)) ) 

#bolilla1= Bolillas(random.randint(0,800),random.randint(0,600),radio=random.randint(10,40))
#bolilla2 = Bolillas(random.randint(0,800),random.randint(0,600),color=(192, 57, 43),radio=random.randint(10,40))

game_over = False
while not game_over:
    for eventos in pg.event.get():
        print(eventos)
        if eventos.type == pg.QUIT:
            game_over = True
    
    pantalla_principal.fill( ( 52, 152, 219 ) )

    for bolilla in listaBolillas:
        bolilla.moverCirculo(800,600)
        bolilla.dibujarCirculo(pantalla_principal)
    
    rect1.mover(800,600)
    rect2.mover(800,600)
    bolilla1.mover(800,600)
    bolilla2.mover(800,600)
    bolilla1.dibujar(pantalla_principal)
    bolilla2.dibujar(pantalla_principal)
    rect1.dibujar(pantalla_principal)
    rect2.dibujar(pantalla_principal)

    pg.display.flip()
    
pg.quit()
import pygame as pg

# inicialitzar tots el mòduls de pygame
# pantalles, sons, teclats, etc.

pg.init()

# creem una pantalla o surface
pantalla_principal = pg.display.set_mode((800,600)) #mesura finestra, rep el valor en tupla (x,y / - ampl/alt)
pg.display.set_caption("Boles rebotant") #títol finestra

#variable per controlar el bucle
game_over = False
while not game_over:

    for events in pg.event.get(): #captura tots els objectes/events en forma de llista
        print(events)
        if events.type == pg.QUIT: #per parar bulce, per ubicar l'element final, sinó no pararia de tenir esdevenimets
            game_over = True

pantalla_principal.fill ((52, 152, 220)) #assignar color pantalla
pg.draw.rect(pantalla_principal, (200, 60, 40),(400,300,40,40)) #colors rectangle + posició+tamany
pg.display.flip()

pg.quit()
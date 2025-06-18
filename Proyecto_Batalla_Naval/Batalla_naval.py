from Configuraciones.Funciones_Naval import *
import pygame as pg
import pygame.mixer as mixer
mixer.init()
pg.init()

#COLORES
color_verde = (22,244,8)
color_blanco = (255,255,255)
color_negro = (0,0,0)
color_azul = (138, 158, 255)
azul_2 = (110, 125, 255)
gris_apretado = (125,125,125)
gris = (200,200,200)

#DIMENSIONES
width = 900
height = 600
screen = pg.display.set_mode((width,height),pg.RESIZABLE)
ancho = screen.get_width()
alto = screen.get_height()

#IMAGENES
fondo_menu = pg.image.load("C:/Users/juans/programacion_full/Programacion2025/Clases/Proyecto_Batalla_Naval/Elementos_Naval/Fondo_menu.jpg")
fondo_menu = pg.transform.scale(fondo_menu,(width,height))
fondo_juego = pg.image.load("C:/Users/juans/programacion_full/Programacion2025/Clases/Proyecto_Batalla_Naval/Elementos_Naval/🌊🌊🌊.jpg")
fondo_juego = pg.transform.scale(fondo_juego,(width,height))

#BOTONES
boton_start = Rect(ancho/2-130/2,100,130,50)
boton_dificultad = Rect(ancho/2-130/2,200,130,50)
boton_puntajes = Rect(ancho/2-130/2,300,130,50)
boton_salir = Rect(ancho/2-130/2,400,130,50)
facil = Rect(ancho/2-130/2,100,130,50)
medio = Rect(ancho/2-130/2,200,130,50)
dificil = Rect(ancho/2-130/2,300,130,50)
boton_volver = Rect(ancho-130-50,20,130,50)


#PRUEBAS
'''
tablero_real = tablero_juego("D")
tablero_covertura = inicializar_matriz(len(tablero_real),len(tablero_real[0]))
printear_matriz(tablero_real[0])
datos_barcos = tablero_real[1]
"""print(datos_barcos)
"""
for i in range(len(datos_barcos)):
    printear_lista_continua(datos_barcos[i])
    print(f"- Numero : {i+1}")
'''
#printear_matriz(tablero_covertura)

#JUEGO

pg.init()

#BANDERAS
inicio = False
menu = True
jugando = False
menu_dificultad = False
dificultad = "F"

#tablero_real = tablero_juego()

game = True
while game:
    
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game = False

        if evento.type == pg.MOUSEBUTTONDOWN:
            if menu:
                if evento.button == 1:
                    if boton_start.collidepoint(mouse.get_pos()):
                        juego = tablero_juego(dificultad)
                        tablero_real = juego[0]
                        lista_barcos = juego[1]
                        tablero_covertura = inicializar_matriz(len(tablero_real),len(tablero_real[0]))
                        lista_casilleros = generar_casilleros(tablero_real)
                        print(lista_casilleros)
                        menu = False
                        #jugando = True                        
                    elif boton_dificultad.collidepoint(mouse.get_pos()):
                        menu = False
                        menu_dificultad = True
                    elif boton_puntajes.collidepoint(mouse.get_pos()):
                        pass
                    elif boton_salir.collidepoint(mouse.get_pos()):
                        game = False
                        
            if menu_dificultad:
                if evento.button == 1:
                    if boton_volver.collidepoint(mouse.get_pos()):
                        menu_dificultad = False
                        menu = True
                    elif facil.collidepoint(mouse.get_pos()):
                        dificultad = "F"
                    elif medio.collidepoint(mouse.get_pos()):
                        dificultad = "M"
                    elif dificil.collidepoint(mouse.get_pos()):
                        dificultad = "D"

    #PANTALLA
    if jugando:
        screen.blit(fondo_juego,(0,0))
    else:
        screen.blit(fondo_menu,(0,0))

    
    if jugando:
        menu_font = pg.font.SysFont("Arial Narrow", 25)
        for i in range(len(lista_casilleros)):
            colocar_casilla(lista_casilleros[i],screen)

    if menu:
        menu_font = pg.font.SysFont("Arial Narrow", 25)
        poner_boton(screen,boton_start,"Jugar",gris,gris_apretado,menu_font)
        poner_boton(screen,boton_dificultad,"Dificultad",gris,gris_apretado,menu_font)
        poner_boton(screen,boton_puntajes,"Ver Puntajes",gris,gris_apretado,menu_font)
        poner_boton(screen,boton_salir,"Salir",gris,gris_apretado,menu_font)        

    if menu_dificultad:
        menu_font = pg.font.SysFont("Arial Narrow", 25)
        poner_boton(screen,boton_volver,"Volver",gris,gris_apretado,menu_font)
        poner_boton(screen,facil,"Facil",gris,gris_apretado,menu_font)
        poner_boton(screen,medio,"Medio",gris,gris_apretado,menu_font)
        poner_boton(screen,dificil,"Dificil",gris,gris_apretado,menu_font)

    pg.display.flip()    

pg.quit()

from Configuraciones.Funciones_Naval import *
import pygame as pg

#COLORES
naranja = (255,163,38,254)
naranja_apretado = (243,188,44,254)
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
fondo_menu = cargar_imagen("Elementos_Naval/fondo_gpt1.webp",(width,height))
fondo_juego = cargar_imagen("Elementos_Naval/fondo_jugando.webp",(width,height))
titulo_2 = cargar_imagen("Elementos_Naval/titulo_pixel.png",(width*0.50,height*0.60))
inicio_buque = cargar_imagen("Elementos_Naval/buque_naval.webp",(width*0.80,height*0.80))

#BOTONES
boton_start = Rect(ancho/2-130/2,100,130,50)
boton_dificultad = Rect(ancho/2-130/2,200,130,50)
boton_puntajes = Rect(ancho/2-130/2,300,130,50)
boton_salir = Rect(ancho/2-130/2,400,130,50)
facil = Rect(ancho/2-130/2,100,130,50)
medio = Rect(ancho/2-130/2,200,130,50)
dificil = Rect(ancho/2-130/2,300,130,50)
boton_volver = Rect(ancho-130-50,20,130,50)
boton_reiniciar = Rect(50+150,20,130,50)
boton_musica = Rect(50,20,130,50)


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
pg.mixer.init()

#BANDERAS
inicio = True
menu = False
jugando = False
menu_dificultad = False
puntajes = False
musica = True
dificultad = "F"

#tablero_real = tablero_juego()
pg.mixer.music.load("Elementos_Naval/musica_juego.mp3")
pg.mixer.music.play(-1)

game = True
while game:
    
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            game = False

        if evento.type == pg.MOUSEBUTTONDOWN:
            if inicio:
                inicio = False
                menu = True

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
                        jugando = True                        
                    elif boton_dificultad.collidepoint(mouse.get_pos()):
                        menu = False
                        menu_dificultad = True
                    elif boton_puntajes.collidepoint(mouse.get_pos()):
                        pass
                    elif boton_salir.collidepoint(mouse.get_pos()):
                        game = False
                    elif boton_musica.collidepoint(mouse.get_pos()):
                        if musica:
                            pg.mixer.music.stop()
                            musica = False
                        else:
                            pg.mixer.music.play(-1)
                            musica = True
                    

            if jugando:
                if evento.button == 1:
                    if boton_volver.collidepoint(mouse.get_pos()):
                        jugando = False
                        menu = True
                    elif boton_reiniciar.collidepoint(mouse.get_pos()):
                        pass
                    elif boton_musica.collidepoint(mouse.get_pos()):
                        if musica:
                            pg.mixer.music.stop()
                            musica = False
                        else:
                            pg.mixer.music.play(-1)
                            musica = True

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
        if inicio:
            screen.blit(inicio_buque,(width/2-inicio_buque.get_width()/2+30,height/2-(inicio_buque.get_height()/2-100)))
            screen.blit(titulo_2,(width/2-titulo_2.get_width()/2,height/2-(titulo_2.get_height()/2+200)))

    if menu:
        menu_font = pg.font.SysFont("Consolas", 15)
        poner_boton(screen,boton_start,"Jugar",naranja_apretado,naranja,menu_font)
        poner_boton(screen,boton_dificultad,"Dificultad",naranja_apretado,naranja,menu_font)
        poner_boton(screen,boton_puntajes,"Ver Puntajes",naranja_apretado,naranja,menu_font)
        poner_boton(screen,boton_salir,"Salir",naranja_apretado,naranja,menu_font)
        poner_boton(screen,boton_musica,"Musica",naranja_apretado,naranja,menu_font)

    if jugando:
        menu_font = pg.font.SysFont("Consolas", 15)
        poner_boton(screen,boton_volver,"Volver",naranja_apretado,naranja,menu_font)
        poner_boton(screen,boton_reiniciar,"Reiniciar",naranja_apretado,naranja,menu_font)
        poner_boton(screen,boton_musica,"Musica",naranja_apretado,naranja,menu_font)


    if menu_dificultad:
        menu_font = pg.font.SysFont("Consolas", 15)
        poner_boton(screen,boton_volver,"Volver",naranja_apretado,naranja,menu_font)
        poner_boton(screen,facil,"Facil",naranja_apretado,naranja,menu_font)
        poner_boton(screen,medio,"Medio",naranja_apretado,naranja,menu_font)
        poner_boton(screen,dificil,"Dificil",naranja_apretado,naranja,menu_font)

    pg.display.flip()    

pg.quit()

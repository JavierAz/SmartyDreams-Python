import pygame

# inicializar Pygame
pygame.init()

# crea la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption('Nos atacan los marcianos!')
icono = pygame.image.load('astronave.png')
pygame.display.set_icon(icono)

# jugador
img_jugador = pygame.image.load('nave-espacial.png')
jugador_x = 368
jugador_y = 536


def jugador(x,y):
    pantalla.blit(img_jugador, (x, y))


# Ejecucion del juego
se_ejecuta = True
while se_ejecuta:
    # fondo
    pantalla.fill((205, 144, 228))

    #jugador_x+=0.1

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            se_ejecuta = False

    jugador(jugador_x,jugador_y)
    pygame.display.update()

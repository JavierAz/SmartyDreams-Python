import pygame, random, math
from pygame import mixer

# inicializar Pygame
pygame.init()

# crea la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e icono
pygame.display.set_caption('Nos atacan los marcianos!')
icono = pygame.image.load('astronave.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('space-galaxy-background.jpg')

# musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.play(-1)

# variables del jugador
img_jugador = pygame.image.load('nave-espacial.png')
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# variables del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
catidad_enemigos = 8

for i in range(catidad_enemigos):
    img_enemigo.append(pygame.image.load('ovni.png'))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.3)
    enemigo_y_cambio.append(50)

# variables de la bala
img_bala = pygame.image.load('bala.png')
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 1.5
bala_visible = False

# puntaje
puntaje = 0
funte = pygame.font.Font('freesansbold.ttf', 32)
texto_x = 10
texto_y = 10

# fin de juego
fuente_final = pygame.font.Font('freesansbold.ttf', 40)


def texto_final():
    fuente_final_2 = fuente_final.render('Juego Terminado', True, (255, 255, 255))
    pantalla.blit(fuente_final_2, (60, 200))


# funcion mostrar puntaje
def mostrar(x, y):
    texto = funte.render(f'Puntaje: {puntaje}', True, (255, 255, 255))
    pantalla.blit(texto, (texto_x, texto_y))


# funcion del jugador
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))


# funcion del enemigo
def enemigo(x, y, index):
    pantalla.blit(img_enemigo[index], (x, y))


# funcion disparar bala
def dis_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala, (x + 16, y + 10))


# funcion de colisiones
def colision(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x1 - x2, 2) + (math.pow(y1 - y2, 2)))
    if distancia < 27:
        return True
    else:
        return False


# Ejecucion del juego
se_ejecuta = True
while se_ejecuta:
    # fondo
    pantalla.blit(fondo, (0, 0))

    # eventos del programa
    for e in pygame.event.get():
        # cerrar el programa
        if e.type == pygame.QUIT:
            se_ejecuta = False

        # movimientos
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if e.key == pygame.K_RIGHT:
                jugador_x_cambio = 1

        if e.type == pygame.KEYUP:
            if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT:
                jugador_x_cambio = 0
            if e.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    dis_bala(bala_x, bala_y)

    # ubicacion para moverse al jugador
    jugador_x += jugador_x_cambio

    # validar bordes para el jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # ubicacion para moverse al enemigo
    for i in range(catidad_enemigos):

        # validar muerte
        if enemigo_y[i] > 500:
            for k in range(catidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[i] += enemigo_x_cambio[i]

        # validar bordes para el enemigo
        if enemigo_x[i] <= 0:
            enemigo_x_cambio[i] = 0.8
            enemigo_y[i] += enemigo_y_cambio[i]
        elif enemigo_x[i] >= 736:
            enemigo_x_cambio[i] = -0.8
            enemigo_y[i] += enemigo_y_cambio[i]

        # colision
        coli = colision(enemigo_x[i], enemigo_y[i], bala_x, bala_y)
        if coli:
            sonido_colision = mixer.Sound('Golpe.mp3')
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntaje += 1
            # print(puntaje)
            enemigo_x[i] = random.randint(0, 736)
            enemigo_y[i] = random.randint(50, 200)

        enemigo(enemigo_x[i], enemigo_y[i], i)

    # movimiento de la bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        dis_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)

    mostrar(texto_x, texto_y)

    # actualiza la pantalla
    pygame.display.update()

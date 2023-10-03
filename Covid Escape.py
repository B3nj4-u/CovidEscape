#Codigo creado por Francisca Ignacia Laibe y Pedro Benjamin Ulloa
import pygame
import sys
import random  
from pygame.locals import * 
pygame.init()

runMenu = True
menu = 0
ANCHO = 500
ALTO = 600
speed = [1, 1]
speed2 = [0, 1]
pts = 0
lvl = 1
ventana = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("Covid Escape")
COLOR_NEGRO = (0,0,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VERDE = (0,143,57)

#Creación imágenes, sus rectas y posición
coraA1 = pygame.image.load("vaciocoraA.png")
coraA1rect = coraA1.get_rect()
coraA1rect.move_ip(210,250)
coraA2 = pygame.image.load("vaciocoraA.png")
coraA2rect = coraA2.get_rect()
coraA2rect.move_ip(300,250)
coraB1 = pygame.image.load("vaciocoraB.png")
coraB1rect = coraB1.get_rect()
coraB1rect.move_ip(212,250)
coraB2 = pygame.image.load("vaciocoraB.png")
coraB2rect = coraB2.get_rect()
coraB2rect.move_ip(212,340)
nivel2 = pygame.image.load("nivel2.png")
nivel3 = pygame.image.load("nivel3.png")
wiwin = pygame.image.load("wiwin.png")
cora = pygame.image.load("heart.png")
corarect = cora.get_rect()
corarect.move_ip(210,250)
kirbyxd = pygame.image.load("kirby.png")
kirbyxdrect = kirbyxd.get_rect()
level = pygame.image.load("level.png")
adm = pygame.image.load("adm.png")
fondo = pygame.image.load("fondo.png")
izqHueA = pygame.image.load("ladosHueso.png")
izqHueArect = izqHueA.get_rect()
izqHueArect.move_ip(165,302)
izqHueB = pygame.image.load("ladosHueso.png")
izqHueBrect = izqHueB.get_rect()
izqHueBrect.move_ip(185,302)
derHueA = pygame.image.load("ladosHueso.png")
derHueArect = derHueA.get_rect()
derHueArect.move_ip(325,302)
derHueB = pygame.image.load("ladosHueso.png")
derHueBrect = derHueB.get_rect()
derHueBrect.move_ip(345,302)
#
izqHueC = pygame.image.load("altosHueso.png")
izqHueCrect = izqHueC.get_rect()
izqHueCrect.move_ip(165,300)
izqHueD = pygame.image.load("altosHueso.png")
izqHueDrect = izqHueD.get_rect()
izqHueDrect.move_ip(165,400)
derHueC = pygame.image.load("altosHueso.png")
derHueCrect = derHueC.get_rect()
derHueCrect.move_ip(325,300)
derHueD = pygame.image.load("altosHueso.png")
derHueDrect = derHueD.get_rect()
derHueDrect.move_ip(325,400)
#
huesoIzq = pygame.image.load("bone2.png")
huesoIzqrect = huesoIzq.get_rect()
huesoIzqrect.move_ip(165,300)
huesoDer = pygame.image.load("bone3.png")
huesoDerrect = huesoDer.get_rect()
huesoDerrect.move_ip(325,300)
#
traquea = pygame.image.load("traquea.png")
traquearect = traquea.get_rect()
traquearect.move_ip(210,0)
win = pygame.image.load("vacio1.png")
winrect = win.get_rect()
nivel2 = pygame.image.load("nivel2.png")
nivel2rect = nivel2.get_rect()
winrect.move_ip(210,170)
izqTraquea = pygame.image.load("vacio2.png")
izqTraquearect = izqTraquea.get_rect()
izqTraquearect.move_ip(208,0)
derTraquea = pygame.image.load("vacio2.png")
derTraquearect = derTraquea.get_rect()
derTraquearect.move_ip(284,0)
arrTraquea = pygame.image.load("vacio1.png")
arrTraquearect = arrTraquea.get_rect()
arrTraquearect.move_ip(208,0)

    #pulmon izquierdo 
        #izquierda-derecha
izqPulA = pygame.image.load("vacioB.png")
izqPulArect = izqPulA.get_rect()
izqPulArect.move_ip(55,100)
derPulA = pygame.image.load("vacioB.png")
derPulArect = derPulA.get_rect()
derPulArect.move_ip(134,100)
        #arriba-abajo
arrPulA = pygame.image.load("vacioA.png")
arrPulArect = arrPulA.get_rect()
arrPulArect.move_ip(57,100)
abaPulA = pygame.image.load("vacioA.png")
abaPulArect = abaPulA.get_rect()
abaPulArect.move_ip(57,232)
    #pulmon derecho
        #izquierda-derecha
izqPulB = pygame.image.load("vacioB.png")
izqPulBrect = izqPulB.get_rect()
izqPulBrect.move_ip(445-81,100)
derPulB = pygame.image.load("vacioB.png")
derPulBrect = derPulB.get_rect()
derPulBrect.move_ip(442,100)
        #arriba-abajo
arrPulB = pygame.image.load("vacioA.png")
arrPulBrect = arrPulB.get_rect()
arrPulBrect.move_ip(445-81,100)
abaPulB = pygame.image.load("vacioA.png")
abaPulBrect = abaPulB.get_rect()
abaPulBrect.move_ip(445-81,232)
gameOver = pygame.image.load("gameOver.png")
gameOverrect = gameOver.get_rect()
ball = pygame.image.load("covid.png")
ballrect = ball.get_rect()
ballrect.move_ip(random.randint(0,ANCHO-20),400)
bateA = pygame.image.load("bone.png")
bateArect = bateA.get_rect()
bateArect.move_ip(295, 550)
pulmonA = pygame.image.load("pulmonB.png")
pulmonArect = pulmonA.get_rect()
pulmonArect.move_ip(55,100)
pulmonB = pygame.image.load("pulmonA.png")
pulmonBrect = pulmonB.get_rect()
pulmonBrect.move_ip(445-81,100)
imgA = pygame.image.load("imgA.png")
imgArect = imgA.get_rect()
inicioJuego = 1
puntero = pygame.image.load("puntero.png")
punterorect = puntero.get_rect()
punterorect.move_ip(275,290)
fuente = pygame.font.Font(None, 30)
fuente2 = pygame.font.Font(None, 50)
run = True
si = 99
asd = 99
file = 'music.wav'
pygame.mixer.init()
pygame.mixer.music.load(file)    
pygame.mixer.music.play(-1) 
pop = pygame.mixer.Sound("pop.wav")
yey = pygame.mixer.Sound("yey.wav")
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keyMenu = pygame.key.get_pressed()
    if keyMenu[pygame.K_DOWN]:
        punterorect = punterorect.move(0,2)
        menu+=1
    if keyMenu[pygame.K_UP]:
        punterorect = punterorect.move(0, -2)
        menu-=1
    if inicioJuego != 0:
        ventana.blit(imgA, imgArect)
        ventana.blit(puntero, punterorect)
    pygame.display.flip()
    if keyMenu[pygame.K_SPACE]:
        inicioJuego = 2
    while inicioJuego == 2:
        if menu > 0:
            #Música
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            ventana.blit(adm, (0,0))
            kirbyxdrect = kirbyxdrect.move(speed)
            ventana.blit(kirbyxd, kirbyxdrect)
            if kirbyxdrect.left < 0 or kirbyxdrect.right > ANCHO:
                speed[0] = -speed[0]
            if kirbyxdrect.top <0:
                speed[1] = -speed[1]
            if kirbyxdrect.bottom > ALTO:
                speed[1] = -speed[1]

            pygame.display.flip()
            while pygame.key.get_pressed()[pygame.K_p]:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                ventana.blit(level, (0,0))
                pygame.display.flip()
                if pygame.key.get_pressed()[pygame.K_1]:
                    menu = -1
                    lvl = 1
                if pygame.key.get_pressed()[pygame.K_2]:
                    menu = -1
                    lvl = 2
                if pygame.key.get_pressed()[pygame.K_3]:
                    menu = -1
                    lvl = 3
            else:
                text3 = fuente2.render("NO",1,COLOR_ROJO)
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                ventana.blit(text3, (random.randint(0,ANCHO),random.randint(0,ALTO)))
                pygame.display.flip()
                
        #

        if menu <= 0:
            pygame.time.delay(0)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Movimiento Hueso
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                bateArect = bateArect.move(-5,0)
            if keys[pygame.K_RIGHT]:
                bateArect = bateArect.move(5,0)
            #Colisión
            ballrect = ballrect.move(speed)
            if izqPulArect.colliderect(ballrect) or derPulArect.colliderect(ballrect):
                pop.play()
                if lvl == 1:
                    pts+=1
                if lvl == 2:
                    pts+=2
                if lvl == 3:
                    pts+=3
                if speed[0]<0:
                    speed[0] = -(speed[0] - 0.1)
                else:
                    speed[0] = -(speed[0] + 0.1)
                if speed[1]<0:
                        speed[1] = (speed[1] - 0.1)
                else:
                        speed[1] = (speed[1] + 0.1)
            if izqPulBrect.colliderect(ballrect) or derPulBrect.colliderect(ballrect):
                pop.play()
                if lvl == 1:
                    pts+=1
                if lvl == 2:
                    pts+=2
                if lvl == 3:
                    pts+=3
                if speed[0]<0:
                    speed[0] = -(speed[0] - 0.1)
                else:
                    speed[0] = -(speed[0] + 0.1)
                if speed[1]<0:
                        speed[1] = (speed[1] - 0.1)
                else:
                        speed[1] = (speed[1] + 0.1)
            if arrPulArect.colliderect(ballrect) or arrPulBrect.colliderect(ballrect) or abaPulArect.colliderect(ballrect) or abaPulBrect.colliderect(ballrect):
                pop.play()
                if lvl == 1:
                    pts+=1
                if lvl == 2:
                    pts+=2
                if lvl == 3:
                    pts+=3
                if speed[1]<0:
                    speed[1] = -(speed[1] - 0.1)
                else:
                    speed[1] = -(speed[1] + 0.1)
                if speed[0]<0:
                        speed[0] = (speed[0] - 0.1)
                else:
                        speed[0] = (speed[0] + 0.1)
            #
            if lvl == 1:
                pulmonA = pygame.image.load("pulmonB.png")
                pulmonB = pygame.image.load("pulmonA.png")
            #
            if lvl >= 2:
                if izqHueCrect.colliderect(ballrect) or izqHueDrect.colliderect(ballrect) or derHueCrect.colliderect(ballrect) or derHueDrect.colliderect(ballrect):
                    pop.play()
                    if lvl == 1:
                        pts+=1
                    if lvl == 2:
                        pts+=2
                    if lvl == 3:
                        pts+=3
                    if speed[1]<0:
                        speed[1] = -(speed[1] - 0.1)
                    else:
                        speed[1] = -(speed[1] + 0.1)
                    if speed[0]<0:
                        speed[0] = (speed[0] - 0.1)
                    else:
                        speed[0] = (speed[0] + 0.1)
            #
                if izqHueArect.colliderect(ballrect) or izqHueBrect.colliderect(ballrect) or derHueArect.colliderect(ballrect) or derHueBrect.colliderect(ballrect):
                    pop.play()
                    if lvl == 1:
                        pts+=1
                    if lvl == 2:
                        pts+=2
                    if lvl == 3:
                        pts+=3
                    if speed[0]<0:
                        speed[0] = -(speed[0] - 0.1)
                    else:
                        speed[0] = -(speed[0] + 0.1)
                    if speed[1]<0:
                        speed[1] = (speed[1] - 0.1)
                    else:
                        speed[1] = (speed[1] + 0.1)
            #
            if lvl >= 3:
                if coraA1rect.colliderect(ballrect) or coraA2rect.colliderect(ballrect):
                    pop.play()
                    pts+=3
                    if speed[0]<0:
                        speed[0] = -(speed[0] - 0.1)
                    else:
                        speed[0] = -(speed[0] + 0.1)
                    if speed[1]<0:
                        speed[1] = (speed[1] - 0.1)
                    else:
                        speed[1] = (speed[1] + 0.1)
                if coraB1rect.colliderect(ballrect) or coraB2rect.colliderect(ballrect):
                    pop.play()
                    pts+=3
                    if speed[1]<0:
                        speed[1] = -(speed[1] - 0.1)
                    else:
                        speed[1] = -(speed[1] + 0.1)
                    if speed[0]<0:
                        speed[0] = (speed[0] - 0.1)
                    else:
                        speed[0] = (speed[0] + 0.1)
            if izqTraquearect.colliderect(ballrect) or derTraquearect.colliderect(ballrect):
                pop.play()
                if lvl == 1:
                    pts+=1
                if lvl == 2:
                    pts+=2
                if lvl == 3:
                    pts+=3
                if speed[0]<0:
                    speed[0] = -(speed[0] - 0.1)
                else:
                    speed[0] = -(speed[0] + 0.1)
                if speed[1]<0:
                        speed[1] = (speed[1] - 0.1)
                else:
                        speed[1] = (speed[1] + 0.1)
            if bateArect.colliderect(ballrect):
                pop.play()
                speed[1] = -speed[1]
            if ballrect.left < 0 or ballrect.right > ANCHO:
                pop.play()
                speed[0] = -speed[0]
            if ballrect.top <0:
                pop.play()
                speed[1] = -speed[1]
            if ballrect.bottom > ALTO:
                pop.play()
                speed = [0,0]
                inicioJuego = 0
                si = 0
            if winrect.colliderect(ballrect):
                yey.play()
                ballrect.move_ip(2,2)
                speed[0] = 0
                speed[1] = 0
                asd = 1
            while asd == 1:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                if lvl == 1:
                    ventana.blit(nivel2, (0,0))
                if lvl == 2:
                    ventana.blit(nivel3, (0,0))
                if lvl == 3:
                    ventana.blit(wiwin, (0,0))
                    texto3 = fuente2.render("Tu puntaje fue: "+str(pts),1,COLOR_ROJO)
                    ventana.blit(texto3, (110,400))
                pygame.display.flip()
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    if lvl == 3:
                        sys.exit()
                    asd = 2
                    si = 1
            # dibuja el texto
            texto1 = fuente.render("Ptje: "+str(pts), 1, COLOR_AZUL)
            texto2 = fuente2.render("Tu puntaje fue: "+str(pts),1,COLOR_ROJO)
            ventana.blit(fondo, (0,0))
            ventana.blit(texto1, (15,15))
            ventana.blit(ball, ballrect)
            ventana.blit(traquea, traquearect)
            ventana.blit(bateA, bateArect)
            ventana.blit(izqPulA, izqPulArect)
            ventana.blit(derPulA, derPulArect)
            ventana.blit(izqPulB, izqPulBrect)
            ventana.blit(derPulB, derPulBrect)
            ventana.blit(arrPulA, arrPulArect)
            ventana.blit(abaPulA, abaPulArect)
            ventana.blit(arrPulB, arrPulBrect)
            ventana.blit(abaPulB, abaPulBrect)
            ventana.blit(izqTraquea, izqTraquearect)
            ventana.blit(derTraquea, derTraquearect)
            ventana.blit(arrTraquea, arrTraquearect)
            ventana.blit(win, winrect)
            ventana.blit(pulmonA, pulmonArect)
            ventana.blit(pulmonB, pulmonBrect)
            print(speed)
            if lvl >= 2:
                ventana.blit(huesoDer, huesoDerrect)
                ventana.blit(huesoIzq, huesoIzqrect)
                ventana.blit(izqHueA, izqHueArect)
                ventana.blit(izqHueB, izqHueBrect)
                ventana.blit(izqHueC, izqHueCrect)
                ventana.blit(izqHueD, izqHueDrect)
                ventana.blit(derHueA, derHueArect)
                ventana.blit(derHueB, derHueBrect)
                ventana.blit(derHueC, derHueCrect)
                ventana.blit(derHueD, derHueDrect)
            if lvl >= 3:
                pulmonA = pygame.image.load("pulmonB1.png")
                pulmonB = pygame.image.load("pulmonA1.png")
                ventana.blit(cora, corarect)
                ventana.blit(coraA1, coraA1rect)
                ventana.blit(coraB1, coraB1rect)
                ventana.blit(coraA2, coraA2rect)
                ventana.blit(coraB2, coraB2rect)
            if si == 1:
                ballrect.move_ip(18,18)
                speed = [1,1]
                si = 99
                lvl+=1
                asd = 99
            pygame.display.flip()
    if inicioJuego == 0 and si == 0:  
        ventana.fill(COLOR_VERDE)
        ventana.blit(gameOver, gameOverrect)
        ventana.blit(texto2, (110,280))
        pygame.display.flip()
        if pygame.key.get_pressed()[pygame.K_n]:
            sys.exit()
            menu = 3
            run = False
        if pygame.key.get_pressed()[pygame.K_s]:
            inicioJuego = 2
            si = 99
            pts = 0
            ballrect.move_ip(0,-300)
            lvl = 1
            speed = [1,1]
sys.exit()
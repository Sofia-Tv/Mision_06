import pygame
import math

ANCHO = 640
ALTO = 480

BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)

def dibujarEspi(r,R,l):

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True


        ventana.fill(BLANCO)

        k = r/R

        for angulo in range (0,361*r//math.gcd(r,R),1):
            a = math.radians(angulo)
            x = int(R*(1-k)*math.cos(a))+1*(k*(math.cos(1-k)/(k*a)))
            y = int(R*(1-k)*math.sin(a))-1*(k*(math.sin(1-k)/(k*a)))
            pygame.draw.circle(ventana,AZUL,(x + ANCHO // 2, ALTO // 2 - y),2)

        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()

def main():
    x = int(input("Dame un valor de r: "))
    y = int(input("Dame un valor de R: "))
    z = int(input("Dame un valor de l: "))

    dibujarEspi(x,y,z)


main()
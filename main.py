from pygame.locals import *
import pygame
from sys import exit
from random import randint

pygame.init()

gameSets = {
    "on" : True,
    "largura": 640, 
    "altura": 480, 
    "relogio": pygame.time.Clock(),
    "fps" : 60,
    "points": 0,
    "font": pygame.font.SysFont('arial',22)
}

backmusic = pygame.mixer.music.load("passing.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

collisionmusic = pygame.mixer.Sound("smw_coin.wav")

tela = pygame.display.set_mode((gameSets["largura"], gameSets["altura"]))
pygame.display.set_caption('SimpleCubeGame')

pCube = {
    "largura": 25,
    "altura": 25,
    "x": 0,
    "y": 0,
    "color": (0,255,0),
    "vel": 3,
    "initcompro" : 5,
    "cima" : False,
    "baixo" : False,
    "esquerda" : False,
    "direita" : False
}

fruit = {
    "largura": 25,
    "altura": 25,
    "x": randint(0,gameSets["largura"]-2),
    "y": randint(0,gameSets["altura"]-2),
    "color": (255,0,0),

}


listacobra = []
def drawcabeca(listacobra):
     for xey in listacobra:
         pygame.draw.rect(tela,(0,255,0),(xey[0],xey[1],30,30))   

while gameSets["on"]:
    gameSets["relogio"].tick(gameSets["fps"])
    tela.fill((0,0,0))
    text = gameSets["font"].render(str(gameSets["points"]),True,(255,255,255))
    textMenu = gameSets["font"].render("Dev Menu, Only, available on .py running game",True,(255,255,255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_d:
                pCube["esquerda"] = False
                pCube["direita"] = True
            else:
                pCube["direita"] = False

            if event.key == K_a:
                pCube["direita"] = False
                pCube["esquerda"] = True
            else:
                pCube["esquerda"] = False
            
            

            if event.key == K_w:
                pCube["cima"] = True
            else:
                pCube["cima"] = False
            

            if event.key == K_s:
                pCube["baixo"] = True
            else:
                pCube["baixo"] = False
            

    if pCube["direita"]:
        pCube["x"] = pCube["x"] + 1 *pCube["vel"]
    elif pCube["esquerda"]:
        pCube["x"] = pCube["x"] - 1 *pCube["vel"]
    elif pCube["cima"]:
        pCube["y"] = pCube["y"] - 1 *pCube["vel"]
    elif pCube["baixo"]:
        pCube["y"] = pCube["y"] + 1 *pCube["vel"]

    drawFruit = pygame.draw.rect(tela,fruit["color"],(fruit["x"],fruit["y"],fruit["largura"],fruit["altura"]))
    drawCube = pygame.draw.rect(tela,pCube["color"],(pCube["x"],pCube["y"],pCube["largura"],pCube["altura"]))
    tela.blit(text,(0,0))

    if drawCube.colliderect(drawFruit):
        fruit["x"] = randint(0,gameSets["largura"]-2)
        fruit["y"] = randint(0,gameSets["altura"]-2)
        gameSets["points"] = gameSets["points"] + 1
        pCube["vel"] = pCube["vel"] + 0.2
        collisionmusic.play()
        pCube["initcompro"] = pCube["initcompro"] + 5

    
    if pCube["x"] > gameSets["largura"]:
        pCube["x"] = 0
    elif pCube["x"] < 0:
        pCube["x"] = gameSets["largura"]
    elif pCube["y"] > gameSets["altura"]:
        pCube["y"] = 0
    elif pCube["y"] < 0:
        pCube["y"] = gameSets["altura"]

    listacabeca = []
    listacabeca.append(pCube["x"])
    listacabeca.append(pCube["y"])
    listacobra.append(listacabeca)

    if len(listacobra) > pCube["initcompro"]:
        del listacobra[0]

    drawcabeca(listacobra)
    pygame.display.flip() 
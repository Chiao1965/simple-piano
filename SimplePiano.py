import pygame as pyg
import sys
import os
import time

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#ALPHA = (167,241,146)
ALPHA = (0,0,0)
# initialize pygame and create window
pyg.init()
screen = pyg.display.set_mode((570, 200))
FPS = 30
pyg.display.set_caption("My Game")
clock = pyg.time.Clock()
pyg.mixer.init()

#background
img_base_path = os.getcwd() + '/img/'

class Key(pyg.sprite.Sprite):
    def __init__(self):
        pyg.sprite.Sprite.__init__(self)

        self.images = []
        for i in range(0,6):
            img = pyg.image.load(img_base_path + 'keyboard' +str(i) +'.png').convert()
            img = pyg.transform.scale(img, (70, 200))
            img.convert_alpha()
            img.set_colorkey(ALPHA)
            self.images.append(img)
            self.image = self.images[0]

    def update(self):
        if event.type == pyg.KEYDOWN:
            if event.key == ord('a'):
                pyg.mixer.music.load("./Music_Notes/C.wav")
                pyg.mixer.music.play()
                self.image = self.images[5]
            if event.key == ord('s'):
                pyg.mixer.music.load("./Music_Notes/D.wav")
                pyg.mixer.music.play()
                self.image = self.images[5]
            if event.key == ord('d'):
                pyg.mixer.music.load("./Music_Notes/E.wav")
                pyg.mixer.music.play()
                self.image = self.images[5]
            if event.key == ord('f'):
                pyg.mixer.music.load("./Music_Notes/F.wav")
                pyg.mixer.music.play()
                self.image = self.images[5]
            if event.key == ord('g'):
                pyg.mixer.music.load("./Music_Notes/G.wav")
                pyg.mixer.music.play()
                self.image = self.images[5]
            if event.key == ord('h'):
                pyg.mixer.music.load("./Music_Notes/A.wav")
                pyg.mixer.music.play()
                self.image = self.images[5]
            if event.key == ord('j'):
                pyg.mixer.music.load("./Music_Notes/B.wav")
                pyg.mixer.music.play()
                self.image = self.images[5]
    
key = Key()
img1=[]
for i in range(0,6):
    img = pyg.image.load(img_base_path + 'keyboard' +str(i) +'.png').convert()
    img = pyg.transform.scale(img, (70, 200))
    img.convert_alpha()
    img.set_colorkey(ALPHA)
    img1.append(img)
running = True
while running:
    screen.fill(BLACK)
    screen.blit(img1[4],(10,0))
    screen.blit(img1[4],(90,0))
    screen.blit(img1[4],(170,0))
    screen.blit(img1[4],(250,0))
    screen.blit(img1[4],(330,0))
    screen.blit(img1[4],(410,0))
    screen.blit(img1[4],(490,0))
    
    for event in pyg.event.get():
        print(event)
        # check for closing window
        if event.type == pyg.QUIT:
            running = False
        if event.type == pyg.KEYDOWN:
            if event.key == ord('a'):
                key.update()
                screen.blit(img1[5],(10,0))
            if event.key == ord('s'):
                key.update()
                screen.blit(img1[5],(90,0))
            if event.key == ord('d'):
                key.update()
                screen.blit(img1[5],(170,0))
            if event.key == ord('f'):
                key.update()
                screen.blit(img1[5],(250,0))
            if event.key == ord('g'):
                key.update()
                screen.blit(img1[5],(330,0))
            if event.key == ord('h'):
                key.update()
                screen.blit(img1[5],(410,0))
            if event.key == ord('j'):
                key.update()
                screen.blit(img1[5],(490,0))
        if event.type == pyg.KEYDOWN:
            if event.key == ord('q'):
                pyg.quit()
                sys.exit()
                
    pyg.display.flip()

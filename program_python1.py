import pygame
import random
import sys 

pygame.init() # Init pygame
W, H = 1000, 600 # Screen setup
lebarblok=20 #ukuran lebar blok
a1 = random.randint(0, W - 20)
b1 = 20
a2 = a1+2*lebarblok
b2 = b1+lebarblok

def hitungnomor(i,tombol):
    if i == 3 and tombol ==1:
        i=0
    else:
        i=i+tombol
    return i     

screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("GAME")


WHT, BLU, RED, BLK,YLW,GREN = (255, 255, 255), (0, 200, 255), (255, 0, 0), (0, 0, 0), (255, 255, 51), (0, 255, 0) # Colors

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)
# paddle and block
lshape1a = pygame.Rect(a1,b1,3*lebarblok,lebarblok)
lshape2a = pygame.Rect(a2,b2,lebarblok,lebarblok),
lshape1b = pygame.Rect(a1+lebarblok,b1-lebarblok,lebarblok,3*lebarblok)
lshape2b = pygame.Rect(a2,b2-2*lebarblok,lebarblok,lebarblok)
lshape1c = pygame.Rect(a1,b1,3*lebarblok,lebarblok)
lshape2c = pygame.Rect(a2-2*lebarblok,b2-2*lebarblok,lebarblok,lebarblok)
lshape1d = pygame.Rect(a1+lebarblok,b1-lebarblok,lebarblok,3*lebarblok)
lshape2d = pygame.Rect(a2-2*lebarblok,b2,lebarblok,lebarblok)
lshape1 = ((a1,b1,3*lebarblok,lebarblok),(a1+lebarblok,b1-lebarblok,lebarblok,3*lebarblok),(a1,b1,3*lebarblok,lebarblok),(a1+lebarblok,b1-lebarblok,lebarblok,3*lebarblok))
lshape2 = ((a2,b2,lebarblok,lebarblok),(a2,b2-2*lebarblok,lebarblok,lebarblok),(a2-2*lebarblok,b2-2*lebarblok,lebarblok,lebarblok),(a2-2*lebarblok,b2,lebarblok,lebarblok))
b_speed = 1
i=0
score = 0 # Score
kedalaman=0

# Game loop
run = True
while run:
    screen.fill(BLK)
    tombol=0
    for e in pygame.event.get():
        if e.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()
        elif e.type == pygame.KEYDOWN :
            if e.key == pygame.K_SPACE :
                tombol =1

    i=hitungnomor(i,tombol)
    kedalaman=kedalaman+b_speed
    Lshape1 = pygame.Rect(lshape1[i][0],lshape1[i][1]+kedalaman,lshape1[i][2],lshape1[i][3])
    Lshape2 = pygame.Rect(lshape2[i][0],lshape2[i][1]+kedalaman,lshape2[i][2],lshape2[i][3])	

    # Draw objects
    pygame.draw.rect(screen, BLU, Lshape1)
    pygame.draw.rect(screen, BLU, Lshape2 )
    
    # Display text
    score_text = font.render(f"Nilai i: {i}", True, WHT)
    screen.blit(score_text, (W//2-30,550))
   
    pygame.display.flip()
    clock.tick(60)

    



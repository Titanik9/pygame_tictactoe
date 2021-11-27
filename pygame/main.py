import pygame
import sys



pygame.init()

size1 = 600
size2 = 600
screen = pygame.display.set_mode((size1, size2))
y = 0
while y <= size2:
    pygame.draw.lines(screen, 'white', False, [[0, y], [size1, y]], 1)
    y += 200
x = 0
while x <= size1:
    pygame.draw.lines(screen, 'white', False, [[x, 0], [x, size2]], 1)
    x += 200
k1 = 0
k2 = 0
k3 = 0
k4 = 0
k5 = 0
k6 = 0
k7 = 0
k8 = 0
k9 = 0
k1_k = 0
k2_k = 0
k3_k = 0
k4_k = 0
k5_k = 0
k6_k = 0
k7_k = 0
k8_k = 0
k9_k = 0
k1_c = 0
k2_c = 0
k3_c = 0
k4_c = 0
k5_c = 0
k6_c = 0
k7_c = 0
k8_c = 0
k9_c = 0
def wink():
    sc = pygame.display.set_mode((300, 200))
    sc.fill((255, 255, 255))

    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Крестики победили!!!!!!!!!!!!!!!!!!', True,
                      (180, 0, 0))

    sc.blit(text1, (10, 50))
    pygame.display.update()
def nuliwin():
    sc = pygame.display.set_mode((300, 200))
    sc.fill((255, 255, 255))

    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Нули победили!!!!!!!!!!!!!!!!!!', True,
                      (180, 0, 0))

    sc.blit(text1, (10, 50))
    pygame.display.update()

def k1_krest():
    pygame.draw.lines(screen, 'white', False, [[0, 0], [200, 200]], 1)
    pygame.draw.lines(screen, 'white', False, [[200, 0], [0, 200]], 1)
def k2_krest():
    pygame.draw.lines(screen, 'white', False, [[200, 0], [400, 200]], 1)
    pygame.draw.lines(screen, 'white', False, [[200, 200], [400, 000]], 1)
def k3_krest():
    pygame.draw.lines(screen, 'white', False, [[400, 0], [600, 200]], 1)
    pygame.draw.lines(screen, 'white', False, [[400, 200], [600, 0]], 1)
def k4_krest():
    pygame.draw.lines(screen, 'white', False, [[0, 200], [200, 400]], 1)
    pygame.draw.lines(screen, 'white', False, [[0, 400], [200, 200]], 1)
def k5_krest():
    pygame.draw.lines(screen, 'white', False, [[200, 200], [400, 400]], 1)
    pygame.draw.lines(screen, 'white', False, [[200, 400], [400, 200]], 1)
def k6_krest():
    pygame.draw.lines(screen, 'white', False, [[400, 200], [600, 400]], 1)
    pygame.draw.lines(screen, 'white', False, [[400, 400], [600, 200]], 1)
def k7_krest():
    pygame.draw.lines(screen, 'white', False, [[0, 400], [200, 600]], 1)
    pygame.draw.lines(screen, 'white', False, [[0, 600], [200, 400]], 1)
def k8_krest():
    pygame.draw.lines(screen, 'white', False, [[200, 400], [400, 600]], 1)
    pygame.draw.lines(screen, 'white', False, [[200, 600], [400, 400]], 1)
def k9_krest():
    pygame.draw.lines(screen, 'white', False, [[400, 400], [600, 600]], 1)
    pygame.draw.lines(screen, 'white', False, [[400, 600], [600, 400]], 1)
def k1_circle():
    pygame.draw.circle(screen, 'white', [100, 100], 90, 1)
def k2_circle():
    pygame.draw.circle(screen, 'white', [300, 100], 90, 1)
def k3_circle():
    pygame.draw.circle(screen, 'white', [500, 100], 90, 1)
def k4_circle():
    pygame.draw.circle(screen, 'white', [100, 300], 90, 1)
def k5_circle():
    pygame.draw.circle(screen, 'white', [300, 300], 90, 1)
def k6_circle():
    pygame.draw.circle(screen, 'white', [500, 300], 90, 1)
def k7_circle():
    pygame.draw.circle(screen, 'white', [100, 500], 90, 1)
def k8_circle():
    pygame.draw.circle(screen, 'white', [300, 500], 90, 1)
def k9_circle():
    pygame.draw.circle(screen, 'white', [500, 500], 90, 1)
counter = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if k1 == 0:
                if pos[0]<200 and pos[1]<200 and counter % 2 != 0:
                    k1_krest()
                    k1_k = 1
                    k1 += 1
                    counter += 1
                elif pos[0] < 200 and pos[1] < 200 and counter % 2 == 0:
                    k1_circle()
                    k1_c=1
                    k1 += 1
                    counter += 1
            if k2 == 0:
                if pos[0]>200 and pos[0]<400 and pos[1]>0 and pos[1]<200 and counter % 2 != 0:
                    k2_krest()
                    k2_k = 1
                    k2 += 1
                    counter += 1
                elif pos[0] > 200 and pos[0] < 400 and pos[1] > 0 and pos[1] < 200 and counter % 2 == 0:
                    k2_circle()
                    k2_c = 1
                    k2 += 1
                    counter += 1
            if k3 == 0:
                if pos[0] > 400 and pos[0] < 600 and pos[0] > 0 and pos[1] < 200 and counter % 2 != 0:
                    k3_krest()
                    k3 += 1
                    k3_k = 1
                    counter += 1
                elif pos[0] > 400 and pos[0] < 600 and pos[0] > 0 and pos[1] < 200 and counter % 2 == 0:
                    k3_circle()
                    k3_c = 1
                    k3 += 1
                    counter += 1
            if k4 == 0:
                if pos[0] > 0 and pos[0] < 200 and pos[1] > 200 and pos[1] < 400 and counter % 2 != 0:
                    k4_krest()
                    k4_k = 1
                    k4 += 1
                    counter += 1
                elif pos[0] > 0 and pos[0] < 200 and pos[1] > 200 and pos[1] < 400 and counter % 2 == 0:
                    k4_circle()
                    k4_c = 1
                    k4 += 1
                    counter += 1
            if k5 == 0:
                if pos[0] > 200 and pos[0] < 400 and pos[1] > 200 and pos[1] < 400 and counter % 2 != 0:
                    k5_krest()
                    k5_k = 1
                    k5 += 1
                    counter += 1
                elif pos[0] > 200 and pos[0] < 400 and pos[1] > 200 and pos[1] < 400 and counter % 2 == 0:
                    k5_circle()
                    k5_c = 1
                    k5 += 1
                    counter += 1
            if k6 == 0:
                if pos[0] > 400 and pos[0] < 600 and pos[1] > 200 and pos[1] < 400 and counter % 2 != 0:
                    k6_krest()
                    k6_k = 1
                    k6 += 1
                    counter += 1
                elif pos[0] > 400 and pos[0] < 600 and pos[1] > 200 and pos[1] < 400 and counter % 2 == 0:
                    k6_circle()
                    k6_c = 1
                    k6 += 1
                    counter += 1
            if k7 == 0:
                if pos[0] > 0 and pos[0] < 200 and pos[1] > 400 and pos[1] < 600 and counter % 2 != 0:
                    k7_krest()
                    k7_k = 1
                    k7 += 1
                    counter += 1
                elif pos[0] > 0 and pos[0] < 200 and pos[1] > 400 and pos[1] < 600 and counter % 2 == 0:
                    k7_circle()
                    k7_c = 1
                    k7 += 1
                    counter += 1
            if k8 == 0:
                if pos[0] > 200 and pos[0] < 400 and pos[1] > 400 and pos[1] < 600 and counter % 2 != 0:
                    k8_krest()
                    k8_k=1
                    k8 += 1
                    counter += 1
                elif pos[0] > 200 and pos[0] < 400 and pos[1] > 400 and pos[1] < 600 and counter % 2 == 0:
                    k8_circle()
                    k8_c = 1
                    k8 += 1
                    counter += 1
            if k9 == 0:
                if pos[0] > 400 and pos[0] < 600 and pos[1] > 400 and pos[1] < 600 and counter % 2 != 0:
                    k9_krest()
                    k9_k = 1
                    k9 += 1
                    counter += 1
                elif pos[0] > 400 and pos[0] < 600 and pos[1] > 400 and pos[1] < 600 and counter % 2 == 0:
                    k9_circle()
                    k9_c = 1
                    k9 += 1
                    counter += 1

            print(pos)
            print(counter)
            if (k1_k == 1 and k2_k == 1 and k3_k == 1) or (k4_k == 1 and k5_k == 1 and k6_k == 1) or (k7_k == 1 and k8_k == 1 and k9_k == 1):
                wink()
            if (k1_k == 1 and k4_k == 1 and k7_k == 1) or (k2_k == 1 and k5_k == 1 and k8_k == 1) or (k3_k == 1 and k6_k == 1 and k9_k == 1):
                wink()
            if (k1_k == 1 and k5_k == 1 and k9_k == 1) or (k3_k == 1 and k5_k == 1 and k7_k == 1):
                wink()
            if (k1_c == 1 and k2_c == 1 and k3_c == 1) or (k4_c == 1 and k5_c == 1 and k6_c == 1) or (
                    k7_c == 1 and k8_c == 1 and k9_c == 1) or (k1_c == 1 and k5_c == 1 and k9_c == 1) or (
                    k3_c == 1 and k5_c == 1 and k7_c == 1) or (k1_c == 1 and k4_c == 1 and k7_c == 1) or (
                    k2_c == 1 and k5_c == 1 and k8_c == 1) or (k3_c == 1 and k6_c == 1 and k9_c == 1):
                nuliwin()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
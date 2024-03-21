from pygame import *


mw = display.set_mode((700,500))
display.set_caption('Догони если сможешь)')

bg = transform.scale(image.load('1.jpg'), (700, 500))

sprite1 = transform.scale(image.load('2.png'), (250, 150))
sprite2 = transform.scale(image.load('3.png'), (150, 150))

x1 = 100
y1 = 300

x2 = 500
y2 = 300

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    mw.blit(bg, (0,0))
    mw.blit(sprite1, (x1,y1))
    mw.blit(sprite2, (x2,y2))
    keys = key.get_pressed()
    if keys[K_LEFT] and x1 > 0:
        x1 -= 3
    if keys[K_RIGHT] and y1 < 600:
        x1 += 3
    if keys[K_UP] and y1 > 0:
        y1 -= 3
    if keys[K_DOWN] and y1 < 400:
        y1 += 3

    if keys[K_a] and x2 > 0:
        x2 -= 3
    if keys[K_d] and y2 < 600:
        x2 += 3
    if keys[K_w] and y2 > 0:
        y2 -= 3
    if keys[K_s] and y2 < 400:
        y2 += 3
    display.update()
    time.delay(10)

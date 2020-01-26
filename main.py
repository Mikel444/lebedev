import pygame
import sys
import time
from pygame.locals import *

pygame.init()

# sound = pygame.mixer.music.load('SoundTrack.mp3')
# pygame.mixer.music.play()
# sound.play()

# импорт картинок
background = pygame.image.load('img/Back212.jpg')

lebedev = pygame.image.load('img/lebedev.png')
sleeping = pygame.image.load('img/sleeping.png')
sitting = pygame.image.load('img/sitting.bmp')
Key = pygame.image.load('img/key.png')
bed = pygame.image.load('img/bed.bmp')
toilet = pygame.image.load('img/toilet.bmp')
Game_Over = pygame.image.load('img/Game_Over.png')
place = pygame.image.load('img/place.png')
end = pygame.image.load('img/The_end.png')

# удаление фона
lebedev.set_colorkey((0, 208, 0))
sleeping.set_colorkey((0, 208, 0))
sitting.set_colorkey((0, 208, 0))
bed.set_colorkey((0, 208, 0))
Key.set_colorkey((255, 255, 255))
toilet.set_colorkey((0, 208, 0))


# размеры окна
display_x = 1280
display_y = 1024

# расположение кровати
x_bed = - display_x + 200 # размеры фотки
y_bed = - 200
# расположение артёмы
x = x_bed + 50
y = -50
# расположение ключа
x_Key = -301
y_Key = -339
# расположение туалета
x_toilet = -50
y_toilet = -520
# переменные
GO_x = 1281
end_x = 1281

speed = 10
step = 0
cur_Key = Key
cur_lebedev = lebedev

# переменные состояния
sitting_n = 0
kitchen_n = 0
comp_n = 0
key = False
x_place = 100
y_place = 100

# text
font = pygame.font.Font("Pixel.ttf", 24)
str = "Разбудите Артемия (down). (Нажмите top_green чтобы скрывать диалоговое окно)"
y_text = -30

game_display = pygame.display.set_mode((display_x, display_y)) #, pygame.FULLSCREEN)
pygame.display.set_caption("First Artem's day!")


# Начало основного цикла
code_run = True
while code_run:
    pygame.time.delay(25)

    # Закрытие на крестик
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("escape work")
            code_run = False

    game_display.blit(background, (0, 0))

    buttons = pygame.key.get_pressed()  # Передвижение

    if buttons[pygame.K_w]:
        y += speed
    if buttons[pygame.K_a]:
        x += speed
    if buttons[pygame.K_s]:
        y -= speed
        if step == 0:
            str = "Доброе утро, пора посрать"
            step += 1
            x_place = -150
            y_place = -580
    if buttons[pygame.K_d]:
        x -= speed

    if buttons[pygame.K_5]:
        if y_text == 100:
            y_text = -30
        else:
            y_text = 100

# процесс туалета
    if x_place >= x - 102 and x_place <= x and y_place >= y - 170 and y_place <= y and step == 1:
        if sitting_n == 0:
            str = "Добежал, красава!"
        if buttons[pygame.K_r]:
            sitting_n = 1
            cur_lebedev = sitting
            if sitting_n == 1:
                str = "Любишь срать, люби и убирать"
        if buttons[pygame.K_4]:
            sitting_n = 2
            if sitting_n == 2:
                str = "Вы смыли дизайн Лебедева. Пора кушать"
            step += 1
            x_place = -132
            y_place = -268
        if (buttons[pygame.K_w] or buttons[pygame.K_a] or buttons[pygame.K_s] or buttons[pygame.K_d]) and sitting_n == 1:
            GO_x = 0
            str = "Артемию стало плохо... Смывайте за собой"

# процесс кухни
    if x_place >= x - 102 and x_place <= x and y_place >= y - 170 and y_place <= y and step == 2:
        if kitchen_n == 0:
            str = "Возьмите хлеб, сыр и колбасу для бутерброда"
        if buttons[pygame.K_4]:
            kitchen_n = 1
            if kitchen_n == 1:
                str = "Сыра нет, положить помидорку? yes = Blue, no = Green (lower)"
        if buttons[pygame.K_r]:
            kitchen_n = 2
            str = "Помидор оказался не свежим, поэтому у Артемия пищевое отраление"
            GO_x = 0
        elif buttons[pygame.K_t]:
            kitchen_n = 2
            if kitchen_n == 2:
                str = "Ок, тем более что она была не свежая. Пора делать дизайн. Закрыть глаза, и открыть PAINT."
            x_place = -1086
            y_place = -768
            step += 1

# процесс компа
    if x_place >= x - 102 and x_place <= x and y_place >= y - 170 and y_place <= y and step == 3:
        if comp_n == 0:
            str = "Сядьте за компьютер"
        if buttons[pygame.K_r]:
            comp_n = 1
            cur_lebedev = sitting
            if comp_n == 1:
                str = "Запустите компьютер"
        if buttons[pygame.K_4] and comp_n == 1:
            comp_n = 2
            # photoshop comp_n = 2 --> 3
            step += 1
            if comp_n == 2: # comp_n = 2 --> 3
                str = "Дизайн завершён! Чтобы выйти из квартиры найдите ключ"
            x_place = 100
            y_place = 100

# процесс поиска ключа
    if x - 102 >= x_Key - 71 and x - 102 <= x_Key and y - 170 >= y_Key - 40 and y - 170 <= y_Key and step == 4:
        if not key:
            str = "Возьмите ключ"
        if buttons[pygame.K_4]:
            key = True
            if key:
               x_Key = 100
               str = "Ключ взят. Откройте дверь"
               x_place = -1047
               y_place = -248
               step += 1


    if x_place >= x - 102 and x_place <= x and y_place >= y - 170 and y_place <= y and step == 5:
        if buttons[pygame.K_r]:
            str = "Дверь открыта"
            x_place = 100
            y_place = 100
            end_x = 0



    # рассположение вещей на экране
    game_display.blit(cur_Key, (0, 0), (x_Key, y_Key, display_x, display_y))
    game_display.blit(toilet, (0, 0), (x_toilet, y_toilet, display_x, display_y))
    game_display.blit(place, (0, 0), (x_place, y_place, display_x, display_y))

    if step == 0:
        game_display.blit(sleeping, (0, 0), (x_bed, y_bed, display_x, display_y))
    else:
        game_display.blit(bed, (0, 0), (x_bed, y_bed, display_x, display_y))
        game_display.blit(lebedev, (0, 0), (x, y, display_x, display_y))

    game_display.blit(Game_Over, (0, 0), (GO_x, 0, display_x, display_y))

    text = font.render(str, True, (0, 200, 0))
    game_display.blit(text, (0, 0), (-40, y_text, display_x, display_y))
    game_display.blit(end, (0, 0), (end_x, 0, display_x, display_y))


    pygame.display.update()


pygame.quit()

import sys, pygame
from random import choice
from func import *

pygame.init()
pygame.surface
icon = pygame.image.load(".\images\\icon.png")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((600, 450))
pygame.display.set_caption("Крестики нолики епта")
background = (100, 100, 100, 0)
wind_flag = 0     #отслеживание окон
background1 = pygame.transform.scale(pygame.image.load(".\images\\background1.png"), (600, 460))


#1 экран
font = pygame.font.SysFont('Comic Sans MS', 30)
text_choise1 = font.render('Выберите количество игроков', True, (255, 200, 200))
rect_button1 = pygame.Rect(135, 100, 100, 100)
rect_button2 = pygame.Rect(335, 100, 100, 100)
button1 = pygame.transform.scale(pygame.image.load(".\images\\button1.png"), (100, 100))
button2 = pygame.transform.scale(pygame.image.load(".\images\\button2.png"), (100, 100))

#2 экран
background2 = pygame.transform.scale(pygame.image.load(".\images\\background2.png"), (600, 460))
rect_input = pygame.Rect(150, 200, 300, 34)
text_player1 = font.render('Введите имя для регистрации', True, (255, 200, 200))
rect_button3 =  pygame.Rect(200, 300, 200, 60)
text_autoriz = font.render('Войти', True, (34, 13, 64))

#игра
flag = 1
arrexept1 = set()
arrexept2 = set()
number_rect = 0
syst = 0
clock = pygame.time.Clock()
amount_pl = 0
output = ""
c0_9 = {0, 1, 2, 3, 4, 5, 6, 7, 8}
text_error = ""
rect_nasad = pygame.Rect(250, 400, 100, 30)
text_nasad = font.render('Назад', True, (0, 0, 0))

#финиш
rect_button_replay = pygame.Rect(70, 100, 150, 150)
rect_button_choise = pygame.Rect(230, 100, 150, 150)
rect_button_donut = pygame.Rect(390, 100, 150, 150)
button_replay = pygame.transform.scale(pygame.image.load(".\images\\replay.png"), (150, 150))
button_choise = pygame.transform.scale(pygame.image.load(".\images\\players.png"), (150, 150))
button_donut = pygame.transform.scale(pygame.image.load(".\images\\donut.png"), (150, 150))

donut_icon = pygame.transform.scale(pygame.image.load(".\images\\qr.png"), (450, 450))

#переменные для построения поля
width = 120
height = 120
rows = 3
cols = 3
play_rects = [
    pygame.Rect(110 + col * (width + 10), 30 + row * (height + 10), width, height)
    for row in range(rows) for col in range(cols)
]
x, y = 0, 0
rect_player = pygame.Rect(110, 30, width, height)
nolicks = [
    pygame.transform.scale(pygame.image.load(".\images\\nolick.png"), (110, 110)) for _ in range(9)
]
crestics = [
    pygame.transform.scale(pygame.image.load(".\images\\crestic.png"), (110, 110)) for _ in range(9)
]
for i in nolicks:
    i.set_alpha(0)
for i in crestics:
    i.set_alpha(0)

while True:
    
    simbol = ""
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if wind_flag == 0:
             if event.type == pygame.MOUSEBUTTONUP:
                if rect_button1.collidepoint(event.pos):
                    wind_flag = 1
                    amount_pl = 1
                    amount_pl2 = 1

                elif rect_button2.collidepoint(event.pos):
                    wind_flag = 1
                    amount_pl = 2
                    amount_pl2 = 2

        if wind_flag == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if output:
                        if check_name(output):
                            text_error = font.render('Это имя занято, выберите другое', True, (255, 200, 200)) 
                        else:
                            amount_pl -= 1
                            text_error = ""
                            if amount_pl == 0:
                                wind_flag = 3
                                background = (0, 0, 0)
                                nm_pl1 = output
                                if amount_pl2 == 1:
                                    nm_pl2 = "Компьютер"
                            else:
                                nm_pl2 = output
                        output = ""
                elif event.key == pygame.K_BACKSPACE:
                    if output:
                        output = output[:-1]
                else:
                    simbol = pygame.key.name(event.key) 
                    if simbol:  
                        output += simbol   
            elif event.type == pygame.MOUSEBUTTONUP:   
                if rect_button3.collidepoint(event.pos):
                    wind_flag = 2  
                    text_error = ""
                    text_player1 = font.render('Авторизуйтесь', True, (255, 200, 200))
                if rect_nasad.collidepoint(event.pos):
                    wind_flag -= 1

        if wind_flag == 2:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if output:
                        if not check_name(output):
                            text_error = font.render('Это имя не зарегистрировано в базе', True, (255, 200, 200)) 
                        else:
                            amount_pl -= 1
                            text_error = ""
                            if amount_pl == 0:
                                wind_flag = 3
                                background = (0, 0, 0)
                                nm_pl1 = output
                                if amount_pl2 == 1:
                                    nm_pl2 = "Компьютер"
                            else:
                                wind_flag = 1
                                nm_pl2 = output
                        output = ""
                        text_player1 = font.render('Введите имя для регистрации', True, (255, 200, 200))
                elif event.key == pygame.K_BACKSPACE:
                    if output:
                        output = output[:-1]
                else:
                    simbol = pygame.key.name(event.key) 
                    if simbol:  
                        output += simbol   
            elif event.type == pygame.MOUSEBUTTONUP:
                if rect_nasad.collidepoint(event.pos):
                    wind_flag -= 1
                    output = ""
                    text_player1 = font.render('Введите имя для регистрации', True, (255, 200, 200))

        if wind_flag == 3:
            if event.type == pygame.KEYDOWN:
                simbol = event.key  
                text_error = ""
        
        if wind_flag == 4:
            if event.type == pygame.MOUSEBUTTONUP:
                if rect_button_replay.collidepoint(event.pos):
                    wind_flag = 3
                    arrexept1 = set()
                    arrexept2 = set()
                    for i in nolicks:
                        i.set_alpha(0)
                    for i in crestics:
                        i.set_alpha(0)
                    flag = 1

                elif rect_button_choise.collidepoint(event.pos):
                    wind_flag = 0
                    arrexept1 = set()
                    arrexept2 = set()
                    for i in nolicks:
                        i.set_alpha(0)
                    for i in crestics:
                        i.set_alpha(0)
                    flag = 1

                elif rect_button_donut.collidepoint(event.pos):
                    wind_flag = 5

    
    if wind_flag == 0: #начальный экран
        if y >= 450:
            y = 0
        else:
            y += 0.2

        pygame.draw.rect(screen, background, rect_button1)
        pygame.draw.rect(screen, background, rect_button2)
        screen.blit(background1, (0, 0 - y))
        screen.blit(background1, (0, 450 - y))
        screen.blit(text_choise1, (100, 200))
        screen.blit(button1, (135, 100))
        screen.blit(button2, (335, 100))
           

    elif (wind_flag == 1 ): 
        screen.blit(background2, (600 + x, 0))  
        screen.blit(background2, (0 + x, 0))
        screen.blit(background2, (-600 + x, 0)) 
        if x >= 600 and amount_pl == 2:
            x = 0
        elif amount_pl == 2:
            x += 0.01
        elif  x <= -600 and amount_pl <= 1:
             x = 0
        elif amount_pl <= 1:
             x -= 0.01
        pygame.draw.rect(screen, (255, 255, 255), rect_input)
        pygame.draw.rect(screen, (255, 255, 255), rect_button3)
        pygame.draw.rect(screen, (255, 255, 255), rect_nasad)
        screen.blit(text_nasad, (260, 390))
        screen.blit(text_player1, (100, 150))
        screen.blit(text_autoriz, (250, 300))
        text_inp_nm1 = font.render(f"{output}", True, (0, 0, 0))  
        if text_error:
            screen.blit(text_error, (70, 250))
        screen.blit(text_inp_nm1, ((155), 195))

    elif (wind_flag == 2):
        screen.blit(background2, (600 + x, 0))  
        screen.blit(background2, (0 + x, 0))
        screen.blit(background2, (-600 + x, 0)) 
        if x >= 600 and amount_pl == 2:
            x = 0
        elif amount_pl == 2:
            x += 0.01
        elif  x <= -600 and amount_pl <= 1:
             x = 0
        elif amount_pl <= 1:
             x -= 0.01 
        pygame.draw.rect(screen, (255, 255, 255), rect_input)  
        screen.blit(text_player1, (200, 150))
        pygame.draw.rect(screen, (255, 255, 255), rect_nasad)
        screen.blit(text_nasad, (260, 390))
        text_inp_nm1 = font.render(f"{output}", True, (0, 0, 0))  
        if text_error:
            screen.blit(text_error, (70, 250))
        screen.blit(text_inp_nm1, ((155), 195))

    elif (wind_flag == 3):
        screen.fill(background) 
        for i in range(9):
            pygame.draw.rect(screen, (100, 100, 100), play_rects[i])
            x, y = play_rects[i].topleft
            screen.blit(nolicks[i], (x+5, y+5))
            screen.blit(crestics[i], (x+5, y+5))
        pygame.draw.rect(screen, (100, 150, 100), rect_player)
        if arrexept1 or arrexept2:
            union = arrexept1 | arrexept2
        else:
            union = set()
        number_rect = mexanic(simbol, rect_player, number_rect, union, play_rects)

        if flag == 0 and syst == 1:
            if not move(simbol, nolicks, number_rect, arrexept1, union):
                union = arrexept1 | arrexept2
                if union != c0_9:
                    if amount_pl2 == 1:
                        PK_step = choice(list(c0_9 - union)) 
                        move(simbol, crestics, PK_step, arrexept2, union)   
                    elif simbol == pygame.K_RETURN:
                        flag += 1

        elif flag == 1 and syst == 1:
            if not move(simbol, crestics, number_rect, arrexept2, union):  
                union = arrexept1 | arrexept2
                if union != c0_9:
                    if amount_pl2 == 1:
                        PK_step = choice(list(c0_9 - union)) 
                        move(simbol, nolicks, PK_step, arrexept1, union)   
                    elif simbol == pygame.K_RETURN:
                        flag -= 1

        syst = 1 # проверка для того чтобы при переключении экрана не ставился символ
        if arrexept1 or arrexept2:
            if union == c0_9:
                wind_flag = 4
                winner = 3
            wind_flag = check(arrexept1, 3)
            if wind_flag != 4:
                wind_flag = check(arrexept2, 3)
                if wind_flag == 4:
                    name_win = nm_pl1
                    pl_score = win_pl(name_win)
                    winner = 2
            else:
                name_win = nm_pl2
                pl_score = win_pl(name_win)
                winner = 2
        


    elif (wind_flag == 4):
        screen.fill(background) 
        
        if winner == 3:          
            text_win = font.render('Ничья!', True, (255, 200, 200)) 
            text_score = font.render('', True, (255, 200, 200)) 
        elif winner == 2:
            if name_win != "Компьютер":
                text_win = font.render(f"Выйграл {name_win}!", True, (255, 200, 200)) 
                text_score = font.render(f"Всего побед: {pl_score}", True, (255, 200, 200)) 
            else:
                text_win = font.render(f'Выйграл {name_win}!', True, (255, 200, 200)) 
                text_score = font.render('', True, (255, 200, 200)) 
        pygame.draw.rect(screen, background, rect_button_choise)
        pygame.draw.rect(screen, background, rect_button_donut)
        pygame.draw.rect(screen, background, rect_button_replay)
        screen.blit(button_replay, (70, 100))
        screen.blit(button_choise, (230, 100))
        screen.blit(button_donut, (390, 100))
        screen.blit(text_win, (200, 300))
        screen.blit(text_score, (200, 330))

    elif (wind_flag == 5):
        screen.fill(background) 
        screen.blit(donut_icon, (70, 0))
        
            

    pygame.display.flip()

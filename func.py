import pygame
from random import choice
pygame.init()

def mexanic(value, rect, number_rect, union, playrects):
    xy = []
    xy.extend(playrects[i].topleft for i in union)
    x, y = rect.topleft
    can_move_diagonally = False
    check_arr = [{1,2,3,6}, {0,3,7,8}, {2,5,6,7}, {0,1,5,8}, {1,3,5,7}, {1,4,6,8}, {2,3,4,8}, {0,2,4,7}, {0,4,5,6}]
    for i in check_arr:
        if (i.issubset(union) and number_rect not in i) and( number_rect + 1 in i or number_rect - 1 in i):
            can_move_diagonally = True
            break
        
    if value == pygame.K_UP:
        if y > 30:
            y -= 130
            if (x, y) not in xy:
                number_rect -= 3
            elif (x, y-130) not in xy and y-130 >= 30:
                y -= 130
                number_rect -= 6
            else:
                y += 130

    elif value == pygame.K_DOWN:
        if y < 290:
            y += 130
            if (x, y) not in xy:
                number_rect += 3
            elif (x, y+130) not in xy and y+130 <= 290:
                y += 130
                number_rect += 6
            else:
                y -= 130

    elif value == pygame.K_LEFT:
        if x > 110:
            x -= 130
            if (x, y) not in xy:    
                number_rect -= 1
            elif (x-130, y) not in xy and x-130 >= 110:
                x -= 130
                number_rect -= 2
            else:
                x += 130

    elif value == pygame.K_RIGHT:
        if x < 370:
            x += 130
            if (x, y) not in xy:    
                number_rect += 1
            elif (x+130, y) not in xy and x+130 <= 370:
                x += 130
                number_rect += 2
            else:
                x -= 130

    if can_move_diagonally and (value == pygame.K_RIGHT or value == pygame.K_LEFT or value == pygame.K_UP or value == pygame.K_DOWN):

        number_rect = choice(list({0, 1, 2, 3, 4, 5, 6, 7, 8} - union))
        x, y = playrects[number_rect].topleft
        
    rect.topleft = (x, y)
    return number_rect

  
def move(value, arr, number, arrexept, union):
    if value == pygame.K_RETURN and number not in union:
        arr[number].set_alpha(255)
        arrexept.add(number)
    else:
        return 1


def check(arrexept, num):
    arr = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8}, {0, 3, 6}, {1, 4, 7}, {2, 5, 8}, {0, 4, 8}, {2, 4, 6}]
    for i in arr:
        if all(elem in arrexept for elem in i):
            return 4
    return num


def check_name(found_n):
    name_exists = False
    with open("raiting.txt", "r") as file:
        for line in file:
            if f"{found_n}|" in line:
                name_exists = True
                break
    if name_exists:
        return 1
    else:
        with open("raiting.txt", "a") as file:
            file.write(f"{found_n}|0\n")
        return
    
def win_pl(name_win):
    lines = []
    new_score = 0
    with open("raiting.txt", "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith(f"{name_win}|"):
            name, score = line.strip().split("|")
            new_score = int(score) + 1
            lines[i] = f"{name}|{new_score}\n"
            break
    with open("raiting.txt", "w") as file:
        file.writelines(lines)
    return new_score
       
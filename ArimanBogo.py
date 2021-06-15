import pygame
import random
import time

def set_borad(): 
    x_len = int(input("X축의 크기 입력:"))
    y_len = int(input("y축의 크기 입력:"))
    return x_len, y_len

def random_setting(x, y):
    input_seed = int(input('문제 번호 0~9999 입력하시오:'))
    random.seed(input_seed)
    problem = []
    for _ in range(y):
        temp = []
        for _ in range(x):
            temp.append(random.randint(0, 1))
        problem.append(temp)
    print(problem)
    return problem
        
def draw_picture(screen, prob_list, x_len, y_len, front_img, back_img):
    for i in range(y_len):
        for j in range(x_len):
            if prob_list[i][j] == 0:
                screen.blit(back_img, (j*70 + 50, i*70 + 50))
            else:
                screen.blit(front_img, (j*70 + 50, i*70 + 50))

def click_picture(prob_list, x_pos, y_pos):
    dx = [0, 0, 0, 1, -1]
    dy = [0, 1, -1, 0, 0]

    if 1 <= x_pos and x_pos <= x_length and 1 <= y_pos and y_pos <= y_length:
        for i in range(5):
            new_x_pos = x_pos-1 + dx[i]
            new_y_pos = y_pos-1 + dy[i]
            if new_x_pos >= 0 and new_x_pos < x_length and new_y_pos >= 0 and new_y_pos < y_length:
                prob_list[new_y_pos][new_x_pos] = (prob_list[new_y_pos][new_x_pos] - 1)**2
    return prob_list

def show_preview(screen, prob_list, x_pos, y_pos):

    dx = [0, 0, 0, 1, -1]
    dy = [0, 1, -1, 0, 0]
    if 1 <= x_pos and x_pos <= x_length and 1 <= y_pos and y_pos <= y_length:
        for i in range(5):
            new_x_pos = x_pos-1 + dx[i]
            new_y_pos = y_pos-1 + dy[i]
            if new_x_pos >= 0 and new_x_pos < x_length and new_y_pos >= 0 and new_y_pos < y_length:
                pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(new_x_pos * 70 + 50, new_y_pos * 70 + 50, 70, 70), 5)


def check_game(prob_list):
    check = True
    for i in range(y_length):
        for j in range(x_length):
            if prob_list[i][j] == 0:
                check = False
    return check  

if __name__ == "__main__":
    x_length, y_length = set_borad()
    problem_list = random_setting(x_length, y_length)
    
    front_img = pygame.image.load("resource/front.jpg")
    back_img = pygame.image.load("resource/back.jpg")

    pygame.init()
    pygame.display.set_caption("토로의 아리만 보고싶어")  
    screen_width = x_length * 70 + 100
    screen_height = y_length * 70 + 100
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    
    while True:
        screen.fill((255, 255, 255))
        event = pygame.event.poll()
        draw_picture(screen, problem_list, x_length, y_length, front_img, back_img)
        if event.type == pygame.QUIT:
            break
        x_pos, y_pos = pygame.mouse.get_pos()
        x_pos = x_pos // 70
        y_pos = y_pos // 70
        show_preview(screen, problem_list, x_pos, y_pos)

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)
            x_pos = event.pos[0] // 70
            y_pos = event.pos[1] // 70
            print(x_pos, y_pos)
            problem_list = click_picture(problem_list, x_pos, y_pos)
            draw_picture(screen, problem_list, x_length, y_length, front_img, back_img)
        
        if check_game(problem_list):
            print("끝!")
            screen.blit(pygame.image.load("resource/lion_good.jpg"),
             (screen_width//2-100, screen_height//2-100))
            pygame.display.update()
            time.sleep(5)
            pygame.quit()


        pygame.display.update()
        clock.tick(30)


            



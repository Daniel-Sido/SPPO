import pygame, random, os

pygame.mixer.init()

pygame.init()

white = (255, 255, 255)
red = (200, 0, 0)
black = (0, 0, 0)

screen_width = 1536
screen_height = 864

gameWindow = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
bgimg = pygame.image.load("ground.jpg")
bgimg = pygame.transform.scale(bgimg, (screen_width, screen_height)).convert_alpha()
diedimg = pygame.image.load("died.jpg")
diedimg = pygame.transform.scale(diedimg, (screen_width, screen_height)).convert_alpha()
mainimg = pygame.image.load("main1.png")
mainimg = pygame.transform.scale(mainimg, (screen_width, screen_height)).convert_alpha()

pygame.display.set_caption("Snake eater by Daniil & Sergey")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Times-new-roman", 25)


apple = pygame.image.load("apple.png")
apple = pygame.transform.scale(apple, (20,20)).convert_alpha()
apple_rect = apple.get_rect(w=100, h=300)
    
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    pygame.mixer.music.load('main.mp3')
    pygame.mixer.music.play()
    while not exit_game:
        gameWindow.blit(mainimg, (0, 0))

        text_screen("[Нажмите 1, чтобы выбрать легкий режим]", white, 0, screen_height-150)
        text_screen("[Нажмите 2, чтобы выбрать средний режим]", white, 0, screen_height-120)
        text_screen("[Нажмите 3, чтобы выбрать сложный режим]", white, 0, screen_height-90)
        text_screen("[Нажмите 4, чтобы выбрать dark souls режим]", white, 0, screen_height-60)
        text_screen("[DONT TOUCH 5]", white, 0, screen_height-30)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()
                if event.key == pygame.K_1:
                    pygame.mixer.music.pause()
                    gameloop(7)
                if event.key == pygame.K_2:
                    pygame.mixer.music.pause()
                    gameloop(9)
                if event.key == pygame.K_3:
                    pygame.mixer.music.pause()
                    gameloop(13)
                if event.key == pygame.K_4:
                    pygame.mixer.music.pause()
                    gameloop(17)
                if event.key == pygame.K_5:
                    pygame.mixer.music.pause()
                    gameloop(20)

        pygame.display.update()
        clock.tick(60)

def gameloop(difficult):
    exit_game = False
    game_over = False
    grad=200
    snake_x = 100  
    snake_y = 100  
    velocity_x = 0
    velocity_y = 0
    snake_list = []
    snake_length = 1
    direction = 'RIGHT'
    change_to = direction
    if difficult==7:
     if(not os.path.exists("highscore1.txt")):
        with open("highscore1.txt", "w") as f:
            f.write("0")
     with open("highscore1.txt", "r") as f:
        highscore = f.read()
        
    if difficult==9:
     if(not os.path.exists("highscore2.txt")):
        with open("highscore2.txt", "w") as f:
            f.write("0")
     with open("highscore2.txt", "r") as f:
        highscore = f.read()
        
    if difficult==13:
     if(not os.path.exists("highscore3.txt")):
        with open("highscore3.txt", "w") as f:
            f.write("0")
     with open("highscore3.txt", "r") as f:
        highscore = f.read()
    if difficult==17:
     if(not os.path.exists("highscore4.txt")):
        with open("highscore4.txt", "w") as f:
            f.write("0")
     with open("highscore4.txt", "r") as f:
        highscore = f.read()
    if difficult==20:
     if(not os.path.exists("highscore5.txt")):
        with open("highscore5.txt", "w") as f:
            f.write("0")
     with open("highscore5.txt", "r") as f:
        highscore = f.read()
    apple_rect.x=random.randint(50, screen_width-50)
    apple_rect.y = random.randint(50, screen_height-50)
    score = 0
    init_velocity = difficult
    snake_size = 20
    fps = 60
    while not exit_game:
        if game_over:
            if difficult==7:
             with open("highscore1.txt", "w") as f:
                f.write(str(highscore))
            if difficult==9:
             with open("highscore2.txt", "w") as f:
                f.write(str(highscore))
            if difficult==13:
             with open("highscore3.txt", "w") as f:
                f.write(str(highscore))
            if difficult==17:
             with open("highscore4.txt", "w") as f:
                f.write(str(highscore))
            if difficult==20:
             with open("highscore5.txt", "w") as f:
                f.write(str(highscore))

            gameWindow.blit(diedimg, (0, 0))
    
            text_screen("[Нажмите enter, чтобы продолжить играть]", white, 0, screen_height-30)
            text_screen("  Cчёт: " + str(score), (255,255,255), 10, 10)

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit_game = True
                        
                    if event.key == pygame.K_RIGHT:
                        change_to = 'RIGHT'

                    if event.key == pygame.K_LEFT:
                        change_to = 'LEFT'

                    if event.key == pygame.K_UP:
                        change_to = 'UP'

                    if event.key == pygame.K_DOWN:
                        change_to = 'DOWN'
                    

            if change_to == 'UP' and direction!= 'DOWN':
                direction = 'UP'
            if change_to == 'DOWN' and direction!= 'UP':
                direction = 'DOWN'
            if change_to == 'LEFT' and direction!= 'RIGHT':
                direction = 'LEFT'
            if change_to == 'RIGHT' and direction!= 'LEFT':
                direction = 'RIGHT'

            if direction == 'UP':
                velocity_y = - init_velocity
                velocity_x = 0
            if direction == 'DOWN':
                velocity_y = init_velocity
                velocity_x = 0
            if direction == 'LEFT':
                velocity_x = - init_velocity
                velocity_y = 0
            if direction == 'RIGHT':
                velocity_x = init_velocity
                velocity_y = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            if abs(snake_x - apple_rect.x)<15 and abs(snake_y - apple_rect.y)<15:
                apple_rect.x=random.randint(50, screen_width-50)
                apple_rect.y = random.randint(50, screen_height-50)
                pygame.mixer.music.load('Hrum.wav')
                pygame.mixer.music.play()
                score +=10
                snake_length +=5

                if score>int(highscore):
                    highscore = score


            gameWindow.blit(bgimg, (0, 0))
            text_screen("  Счёт: " + str(score) + "  Рекорд: "+str(highscore), white, 10, 10)
            gameWindow.blit(apple, apple_rect)
            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
            if difficult==7:
               if snake_x<0:
                 snake_x=screen_width
               if snake_x>screen_width:
                 snake_x=0
               if snake_y<0:
                 snake_y=screen_height
               if snake_y>screen_height:
                 snake_y=0

            elif snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load('gameover.mp3')
                pygame.mixer.music.play()
                grad=grad-20
            plot_snake(gameWindow, (0,grad,0), snake_list, snake_size)

        pygame.display.update()

        clock.tick(fps)

    pygame.quit()
    quit()
welcome()

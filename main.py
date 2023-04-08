import pygame
import random
pygame.init()

screen = pygame.display.set_mode((1200, 600))
clock = pygame.time.Clock()


class ColorSet:
    def __init__(self):
        pass

    black = (0, 0, 0)
    white = (255, 255, 255)
    grey = (150, 150, 150)
    dark_blue = (32, 78, 128)
    grey_dark_blue = (61, 93, 128)
    greyer_dark_blue = (80, 100, 128)
    blue = (98, 149, 204)
    light_blue = (123, 186, 255)
    extra_light_blue = (191, 222, 255)


class BlueColorSet:
    def __init__(self):
        pass

    grey = (211, 212, 217)
    grey_blue = (143, 174, 190)
    saturated_blue = (75, 136, 162)
    cream = (244, 232, 193)


class BackgroundColorSet:
    def __init__(self):
        pass

    b = (0, 100, 102)
    b1 = (6, 90, 96)
    b2 = (11, 82, 91)
    b3 = (20, 69, 82)
    b4 = (27, 58, 75)
    background = (33, 47, 69)
    p = (39, 38, 64)
    p1 = (49, 34, 68)
    p2 = (62, 31, 71)
    p3 = (77, 25, 77)


untouchable_square_speed = 10

easy_rect = pygame.Rect(1050, 0, 45, 45)
medium_rect = pygame.Rect(1100, 0, 45, 45)
hard_rect = pygame.Rect(1150, 0, 45, 45)

easy = False
medium = True
hard = False

you_win = False
you_win_font = pygame.font.Font("freesansbold.ttf", 100)
press_space_to_play_again_font = pygame.font.Font("freesansbold.ttf", 30)
easy_medium_hard_font = pygame.font.Font("freesansbold.ttf", 30)
untouchable_squareX = random.randint(300, 900)
untouchable_squareY = random.randint(100, 300)
untouchable_square_rect = pygame.Rect(untouchable_squareX, untouchable_squareY, 50, 50)

background_squaresX = []
background_squaresY = []

background_square_side_length = 20
num_of_background_squares = 2500

background = pygame.Surface((1200, 650))
background.fill(BackgroundColorSet.background)

for i in range(num_of_background_squares):
    if random.randint(0, 8) == 0:
        pygame.draw.rect(background, BackgroundColorSet.b,
                         pygame.Rect(random.randint(-50, 1180),
                                     random.randint(-50, 600),
                                     background_square_side_length, background_square_side_length))
    if random.randint(0, 8) == 1:
        pygame.draw.rect(background, BackgroundColorSet.b1,
                         pygame.Rect(random.randint(-50, 1180),
                                     random.randint(-50, 600),
                                     background_square_side_length, background_square_side_length))
    if random.randint(0, 8) == 2:
        pygame.draw.rect(background, BackgroundColorSet.b2,
                         pygame.Rect(random.randint(-50, 1180),
                                     random.randint(-50, 600),
                                     background_square_side_length, background_square_side_length))
    if random.randint(0, 8) == 3:
        pygame.draw.rect(background, BackgroundColorSet.b3,
                         pygame.Rect(random.randint(-50, 1180),
                                     random.randint(-50, 600),
                                     background_square_side_length, background_square_side_length))
    if random.randint(0, 8) == 4:
        pygame.draw.rect(background, BackgroundColorSet.b4,
                         pygame.Rect(random.randint(-50, 1180),
                                     random.randint(-50, 600),
                                     background_square_side_length, background_square_side_length))
    if random.randint(0, 8) == 5:
        pygame.draw.rect(background, BackgroundColorSet.p,
                         pygame.Rect(random.randint(-50, 1180),
                                     random.randint(-50, 600),
                                     background_square_side_length, background_square_side_length))
    if random.randint(0, 8) == 6:
        pygame.draw.rect(background, BackgroundColorSet.p1,
                         pygame.Rect(random.randint(-50, 1180),
                                     random.randint(-50, 600),
                                     background_square_side_length, background_square_side_length))
    if random.randint(0, 8) == 7:
        pygame.draw.rect(background, BackgroundColorSet.p2,
                         pygame.Rect(random.randint(-50, 1180),
                                     random.randint(-50, 600),
                                     background_square_side_length, background_square_side_length))
    if random.randint(0, 8) == 8:
        pygame.draw.rect(background, BackgroundColorSet.p3,
                         pygame.Rect(random.randint(-50, 1180),
                                     random.randint(-50, 600),
                                     background_square_side_length, background_square_side_length))


counter = 0
game_over = False
game_running = True
while game_running:

    screen.blit(background, (0, 0))

    mx, my = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        if event.type == pygame.MOUSEBUTTONDOWN:

            if easy_rect.collidepoint((mx, my)):
                untouchable_square_speed = 5
                easy = True
                medium = False
                hard = False
            if medium_rect.collidepoint((mx, my)):
                untouchable_square_speed = 10
                easy = False
                medium = True
                hard = False
            if hard_rect.collidepoint((mx, my)):
                untouchable_square_speed = 15
                easy = False
                medium = False
                hard = True

            if not game_over and not you_win\
                    and not easy_rect.collidepoint((mx, my))\
                    and not medium_rect.collidepoint((mx, my)) and not hard_rect.collidepoint((mx, my)):
                counter += 1
                background.fill(BackgroundColorSet.background)
                for i in range(int((num_of_background_squares - (counter * (num_of_background_squares/10))))):
                    if random.randint(0, 8) == 0:
                        pygame.draw.rect(background, BackgroundColorSet.b,
                                         pygame.Rect(random.randint(-50, 1180),
                                                     random.randint(-50, 600),
                                                     background_square_side_length, background_square_side_length))
                    if random.randint(0, 8) == 1:
                        pygame.draw.rect(background, BackgroundColorSet.b1,
                                         pygame.Rect(random.randint(-50, 1180),
                                                     random.randint(-50, 600),
                                                     background_square_side_length, background_square_side_length))
                    if random.randint(0, 8) == 2:
                        pygame.draw.rect(background, BackgroundColorSet.b2,
                                         pygame.Rect(random.randint(-50, 1180),
                                                     random.randint(-50, 600),
                                                     background_square_side_length, background_square_side_length))
                    if random.randint(0, 8) == 3:
                        pygame.draw.rect(background, BackgroundColorSet.b3,
                                         pygame.Rect(random.randint(-50, 1180),
                                                     random.randint(-50, 600),
                                                     background_square_side_length, background_square_side_length))
                    if random.randint(0, 8) == 4:
                        pygame.draw.rect(background, BackgroundColorSet.b4,
                                         pygame.Rect(random.randint(-50, 1180),
                                                     random.randint(-50, 600),
                                                     background_square_side_length, background_square_side_length))
                    if random.randint(0, 8) == 5:
                        pygame.draw.rect(background, BackgroundColorSet.p,
                                         pygame.Rect(random.randint(-50, 1180),
                                                     random.randint(-50, 600),
                                                     background_square_side_length, background_square_side_length))
                    if random.randint(0, 8) == 6:
                        pygame.draw.rect(background, BackgroundColorSet.p1,
                                         pygame.Rect(random.randint(-50, 1180),
                                                     random.randint(-50, 600),
                                                     background_square_side_length, background_square_side_length))
                    if random.randint(0, 8) == 7:
                        pygame.draw.rect(background, BackgroundColorSet.p2,
                                         pygame.Rect(random.randint(-50, 1180),
                                                     random.randint(-50, 600),
                                                     background_square_side_length, background_square_side_length))
                    if random.randint(0, 8) == 8:
                        pygame.draw.rect(background, BackgroundColorSet.p3,
                                         pygame.Rect(random.randint(-50, 1180),
                                                     random.randint(-50, 600),
                                                     background_square_side_length, background_square_side_length))

            if untouchable_square_rect.collidepoint((mx, my)):
                if not game_over:
                    you_win = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if you_win or game_over:
                    for i in range(num_of_background_squares):
                        if random.randint(0, 8) == 0:
                            pygame.draw.rect(background, BackgroundColorSet.b,
                                             pygame.Rect(random.randint(-50, 1160),
                                                         random.randint(-50, 600),
                                                         background_square_side_length, background_square_side_length))
                        if random.randint(0, 8) == 1:
                            pygame.draw.rect(background, BackgroundColorSet.b1,
                                             pygame.Rect(random.randint(-50, 1180),
                                                         random.randint(-50, 600),
                                                         background_square_side_length, background_square_side_length))
                        if random.randint(0, 8) == 2:
                            pygame.draw.rect(background, BackgroundColorSet.b2,
                                             pygame.Rect(random.randint(-50, 1180),
                                                         random.randint(-50, 600),
                                                         background_square_side_length, background_square_side_length))
                        if random.randint(0, 8) == 3:
                            pygame.draw.rect(background, BackgroundColorSet.b3,
                                             pygame.Rect(random.randint(-50, 1180),
                                                         random.randint(-50, 600),
                                                         background_square_side_length, background_square_side_length))
                        if random.randint(0, 8) == 4:
                            pygame.draw.rect(background, BackgroundColorSet.b4,
                                             pygame.Rect(random.randint(-50, 1180),
                                                         random.randint(-50, 600),
                                                         background_square_side_length, background_square_side_length))
                        if random.randint(0, 8) == 5:
                            pygame.draw.rect(background, BackgroundColorSet.p,
                                             pygame.Rect(random.randint(-50, 1180),
                                                         random.randint(-50, 600),
                                                         background_square_side_length, background_square_side_length))
                        if random.randint(0, 8) == 6:
                            pygame.draw.rect(background, BackgroundColorSet.p1,
                                             pygame.Rect(random.randint(-50, 1180),
                                                         random.randint(-50, 600),
                                                         background_square_side_length, background_square_side_length))
                        if random.randint(0, 8) == 7:
                            pygame.draw.rect(background, BackgroundColorSet.p2,
                                             pygame.Rect(random.randint(-50, 1180),
                                                         random.randint(-50, 600),
                                                         background_square_side_length, background_square_side_length))
                        if random.randint(0, 8) == 8:
                            pygame.draw.rect(background, BackgroundColorSet.p3,
                                             pygame.Rect(random.randint(-50, 1180),
                                                         random.randint(-50, 600),
                                                         background_square_side_length, background_square_side_length))

                    you_win = False
                    game_over = False
                    counter = 0
                    untouchable_squareX = random.randint(250, 850)
                    untouchable_squareY = random.randint(150, 350)

    if you_win:
        screen.blit(you_win_font.render('YOU WIN', True, ColorSet.white), (400, (screen.get_height()/2)
                                                                           - (you_win_font.get_height()/2)))
        screen.blit(press_space_to_play_again_font.render('Press [Space] to play again',
                                                          True, ColorSet.white), (420, 350))
    if counter > 9:
        game_over = True
        screen.blit(you_win_font.render('GAME OVER', True,
                                        ColorSet.white), (290, (screen.get_height() / 2)
                                                          - (you_win_font.get_height() / 2)))
        screen.blit(press_space_to_play_again_font.render('Press [Space] to play again',
                                                          True, ColorSet.white), (420, 350))

    if not game_over and not you_win:

        if abs(untouchable_squareX - mx + 25) < 50:
            if abs(untouchable_squareY - my + 25) < 50:
                if untouchable_squareX - mx < 0:
                    untouchable_squareX -= untouchable_square_speed/2
                if untouchable_squareX - mx > 0:
                    untouchable_squareX += untouchable_square_speed/2

                if untouchable_squareY - my < 0:
                    untouchable_squareY -= untouchable_square_speed/2
                if untouchable_squareY - my > 0:
                    untouchable_squareY += untouchable_square_speed/2

        if abs(untouchable_squareX - mx + 25) < 100:
            if abs(untouchable_squareY - my + 25) < 100:
                if untouchable_squareX - mx < 0:
                    untouchable_squareX -= untouchable_square_speed/2
                if untouchable_squareX - mx > 0:
                    untouchable_squareX += untouchable_square_speed/2

                if untouchable_squareY - my < 0:
                    untouchable_squareY -= untouchable_square_speed/2
                if untouchable_squareY - my > 0:
                    untouchable_squareY += untouchable_square_speed/2

        if hard:
            if abs(untouchable_squareX - mx + 25) < 150:
                if abs(untouchable_squareY - my + 25) < 150:
                    if untouchable_squareX - mx < 0:
                        untouchable_squareX -= untouchable_square_speed / 10
                    if untouchable_squareX - mx > 0:
                        untouchable_squareX += untouchable_square_speed / 10

                    if untouchable_squareY - my < 0:
                        untouchable_squareY -= untouchable_square_speed / 10
                    if untouchable_squareY - my > 0:
                        untouchable_squareY += untouchable_square_speed / 10

        if untouchable_squareX > 1150 or untouchable_squareX\
                < 0 or untouchable_squareY > 550 or untouchable_squareY < 0:
            untouchable_squareX = random.randint(250, 850)
            untouchable_squareY = random.randint(150, 350)

    untouchable_square_rect = pygame.Rect(untouchable_squareX, untouchable_squareY, 50, 50)
    pygame.draw.rect(screen, BlueColorSet.cream, untouchable_square_rect)
    pygame.draw.rect(screen, BlueColorSet.cream, pygame.Rect(untouchable_squareX, untouchable_squareY, 50, 50), 10)
    pygame.draw.rect(screen, BlueColorSet.cream, pygame.Rect(untouchable_squareX + 10,
                                                             untouchable_squareY + 10, 30, 30), 40)

    if easy:
        pygame.draw.circle(screen, BlueColorSet.cream, (easy_rect.x + 25, easy_rect.y + 25), 20, 0)
    else:
        pygame.draw.circle(screen, BlueColorSet.grey, (easy_rect.x + 25, easy_rect.y + 25), 20, 0)
    if medium:
        pygame.draw.circle(screen, BlueColorSet.cream, (medium_rect.x + 25, medium_rect.y + 25), 20, 0)
    else:
        pygame.draw.circle(screen, BlueColorSet.grey, (medium_rect.x + 25, medium_rect.y + 25), 20, 0)
    if hard:
        pygame.draw.circle(screen, BlueColorSet.cream, (hard_rect.x + 25, hard_rect.y + 25), 20, 0)
    else:
        pygame.draw.circle(screen, BlueColorSet.grey, (hard_rect.x + 25, hard_rect.y + 25), 20, 0)

    screen.blit(easy_medium_hard_font.render("E", True, BackgroundColorSet.b), (easy_rect.x + 14.5, easy_rect.y + 13))
    screen.blit(easy_medium_hard_font.render("M", True, BackgroundColorSet.b4),
                (medium_rect.x + 12.5, medium_rect.y + 12))
    screen.blit(easy_medium_hard_font.render("D", True, BackgroundColorSet.p3), (hard_rect.x + 15, hard_rect.y + 12.5))

    pygame.display.update()
    clock.tick(60)

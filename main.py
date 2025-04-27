import pygame

pygame.init()

window = pygame.display.set_mode([700, 500])
clock = pygame.time.Clock()

game = True
background_img = pygame.image.load("image/background.png")
background_img= pygame.transform.scale(background_img, [700, 500])


player1_img = pygame.image.load("image/sprite1.png")
player1_img = pygame.transform.scale(player1_img, [50, 50])
player1_x= 120
player1_y = 40


player2_img = pygame.image.load("image/sprite2.png")
player2_img = pygame.transform.scale(player2_img, [50, 50])
player2_x = 150
player2_y = 60

text = pygame.font.Font(None, 30).render("Text", True, [0,0,0])

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d] and player1_x < 650:
        player1_x += 5

    if keys[pygame.K_a] and player1_x> 0:
        player1_x -= 5

    if keys[pygame.K_w] and player1_y>0:
        player1_y -= 5

    if keys[pygame.K_s] and player1_y < 450:
        player1_y += 5

    if keys[pygame.K_RIGHT] and player2_x < 650:
        player2_x += 5

    if keys[pygame.K_LEFT] and player2_x >0:
        player2_x -= 5

    if keys[pygame.K_UP] and player2_y>0:
        player2_y -= 5
    if keys[pygame.K_DOWN] and player2_y < 450:
        player2_y += 5





    window.fill([128, 128, 128])
    window.blit(background_img, [0, 0])
    window.blit(player1_img, [player1_x, player1_y])
    window.blit(player2_img, [player2_x, player2_y])
    window.blit(text, [20, 20])
    pygame.display.flip()
    clock.tick(60)
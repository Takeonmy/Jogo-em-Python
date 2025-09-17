import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Fleppy Torres")

# imagenm avião
player_image = pygame.image.load("sprites/aviao.png")
player_image = pygame.transform.smoothscale(player_image, (110, 40))
player_image_flipped = pygame.transform.flip(player_image, True, False)
#imagem fundo
background_image = pygame.image.load("sprites/fundo2.jpg")
background_image = pygame.transform.smoothscale(background_image, (800, 800))

# Posição e velocidade
player_position = [100, 100]
player_speed = 2

# Velocidade vertical e gravidade
vertical_speed = 2
gravity = 0.1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Corrigido aqui
            running = False

    #gravidade
    vertical_speed += gravity
    player_position[1] += vertical_speed

    #rotação
    angle = -vertical_speed * 5
    player_image_rotated = pygame.transform.rotate(player_image_flipped, angle)

    #Desenho do fundo
    screen.blit(background_image, (0, 0))
    #link da rotação do avião
    rotated_image = pygame.transform.rotate(player_image_flipped, angle)
    rotated_rect = rotated_image.get_rect(center=(player_position[0], player_position[1]))
    #desenho do avião
    screen.blit(rotated_image, rotated_rect.topleft)
    
    

    # Capturar as teclas pressionadas
    keys = pygame.key.get_pressed()

    # Atualizar a posição do jogador com base nas teclas pressionadas
    if keys[pygame.K_LEFT]:
        player_position[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_position[0] += player_speed
    if keys[pygame.K_DOWN]:
        player_position[1] += player_speed
    if keys[pygame.K_UP]:
        # Diminuir a velocidade vertical para fazer o avião subir
        vertical_speed = -3

    # Atualizar a tela
    pygame.display.flip()

    # Limitar a taxa de atualização
    pygame.time.Clock().tick(60)

pygame.quit()

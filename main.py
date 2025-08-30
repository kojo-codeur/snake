# Importation de modules
import pygame
import time
import random

# Initialisation
pygame.init()

# Définition des couleurs
white = (255, 255, 255)  # fond de texte
black = (0, 0, 0)  # arrière-plan
red = (213, 50, 80)  # nourriture
green = (0, 255, 0)  # serpent
blue = (50, 153, 213)  # éléments supplémentaires

# Configuration de la fenêtre de notre jeu
dis_width = 800  # dimensions de la fenêtre
dis_height = 600  # dimensions de la fenêtre
dis = pygame.display.set_mode((dis_width, dis_height))  # crée la fenêtre 
pygame.display.set_caption('Jeu Snake - Codez votre imagination')  # définit le titre de la fenêtre

# Paramètre du jeu
clock = pygame.time.Clock()  # contrôle la vitesse
snake_block = 10  # taille du segment
snake_speed = 12  # nombre d'images par seconde

font_style = pygame.font.SysFont("bahnschrift", 25)  # police pour l'affichage du texte
score_font = pygame.font.SysFont("comicsansms", 40)  # police pour l'affichage du texte

# Fonction pour afficher le score
def your_score(score):
    value = score_font.render("Votre Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Fonction de dessin du serpent
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])  # dessine un rectangle pour chaque segment

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 5, dis_height / 3])

def gameloop():
    game_over = False
    game_close = False

    x1 = dis_width / 2  # position initiale x
    y1 = dis_height / 2  # position initiale y

    x1_change = 0  # déplacement horizontal
    y1_change = 0  # déplacement vertical

    snake_list = []  # la liste de segments
    length_of_snake = 1  # longueur initiale

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  # position aléatoire de la nourriture x
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  # position aléatoire de la nourriture y

    # Boucle principale du jeu
    while not game_over:
        # Gestion du Game Over
        while game_close:
            dis.fill(black)
            message("Vous avez perdu! Appuyez sur C pour rejouer et sur Q pour quitter", red)
            your_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()

        # Gestion des événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Vérification des collisions avec les bords
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Mise à jour de la position
        x1 += x1_change
        y1 += y1_change
        
        # Efface l'écran
        dis.fill(black)
        
        # Dessin de la nourriture
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        
        # Mise à jour du serpent
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        
        # Suppression de l'ancienne position si le serpent n'a pas mangé
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Vérification de la collision avec soi-même
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        # Dessin du serpent et du score
        our_snake(snake_block, snake_list)
        your_score(length_of_snake - 1)
        
        # Mise à jour de l'affichage
        pygame.display.update()

        # Vérification si le serpent a mangé la nourriture
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        # Contrôle de la vitesse du jeu
        clock.tick(snake_speed)

    # Quitter Pygame
    pygame.quit()
    quit()

# Lancement du jeu
gameloop()

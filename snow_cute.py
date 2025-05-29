import pygame
import sys
import random

pygame.init()

WIDTH = 1200
HEIGHT = 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snow Cute")


compliments = [
    "Good Job Evey!",
    "You're the cutest <3",
    "The most handsome skier I've ever seen 😘!",
    "You're cooler than snow!",
    "Go Evan, go!",
    "#1 skier of all time! WOOOOWOOOO",
]

font = pygame.font.Font("Sugar Fruit.otf", 36)
big_font = pygame.font.Font("Sugar Fruit.otf", 72)

def reset_game():
    global skier_x, skier_y, trees, compliment_giver, eveys_compliment, crashed
    skier_x = WIDTH // 2 - 30
    skier_y = 0
    compliment_giver = 0
    eveys_compliment = ""
    trees = []
    for _ in range(10):
        tree_x = random.randint(0, WIDTH - 100)
        tree_y = random.randint(-HEIGHT, HEIGHT)
        trees.append({"x": tree_x, "y": tree_y})
    crashed = False


tree_img = pygame.image.load("tree.png")
tree_img = pygame.transform.scale(tree_img, (300, 300))

skier_img = pygame.image.load("evey.png")
skier_img = pygame.transform.scale(skier_img, (100, 100))


evey_speed = 2
skier_speed_x = 5


reset_game()


running = True
while running:
    screen.fill((225, 225, 225))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if not crashed:
        if keys[pygame.K_LEFT] and skier_x > 0:
            skier_x -= skier_speed_x
        if keys[pygame.K_RIGHT] and skier_x < WIDTH - 100:
            skier_x += skier_speed_x

        skier_y += evey_speed

        if skier_y > HEIGHT:
            skier_y = -100
            eveys_compliment = random.choice(compliments)
            compliment_giver = 180

        
        if random.randint(1, 60) == 1:
            trees.append({"x": random.randint(0, WIDTH - 100), "y": -100})

        
        for t in trees:
            t["y"] += evey_speed

        
        skier_rect = pygame.Rect(skier_x, skier_y, 100, 100)
        for t in trees:
            tree_rect = pygame.Rect(t["x"], t["y"], 100, 100)
            if skier_rect.colliderect(tree_rect):
                crashed = True
                compliment_giver = 0
                break

    else:
        crash_text = big_font.render("Evey crashed! 💥", True, (255, 0, 0))
        screen.blit(crash_text, (WIDTH//2 - crash_text.get_width()//2, HEIGHT//2 - 100))

        hint_text = font.render("Press R to restart or Q to quit", True, (0, 0, 0))
        screen.blit(hint_text, (WIDTH//2 - hint_text.get_width()//2, HEIGHT//2 + 20))

        if keys[pygame.K_r]:
            reset_game()
        if keys[pygame.K_q]:
            running = False

    
    for t in trees:
        screen.blit(tree_img, (t["x"], t["y"]))

    
    screen.blit(skier_img, (skier_x, skier_y))

  
    if compliment_giver > 0:
        comp_surface = font.render(eveys_compliment, True, (0, 0, 0))
        screen.blit(comp_surface, (WIDTH // 2 - comp_surface.get_width() // 2, 50))
        compliment_giver -= 1

    pygame.display.flip()

pygame.quit()
sys.exit()




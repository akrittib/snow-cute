import pygame 
import sys 
import random 
pygame.init()

WIDTH, HEIGHT = 1200, 1000
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

compliment_giver = 0 
eveys_compliment = ""

trees = []

skier_img = pygame.image.load("evey.png")
skier_img = pygame.transform.scale(skier_img, (100, 100))
skier_x = WIDTH // 2 - 30 
skier_y = 0

evey_speed = 2 
skier_speed_x = 5

font = pygame.font.Font("Sugar Fruit.otf", 36)



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and skier_x > 0:
        skier_x -= skier_speed_x
    if keys[pygame.K_RIGHT] and skier_x < WIDTH - 100:
        skier_x += skier_speed_x
        
    skier_y += evey_speed
    if skier_y > HEIGHT:
        skier_y = -100
        
        eveys_compliment = random.choice(compliments)
        compliment_giver = 180 
        
    if random.randint(1, 75) == 1: 
        tree_x = random.randint(0, WIDTH - 75)
        trees.append({"x": tree_x, "y" : - 75})
    
    tree_img = pygame.image.load("tree.png")
    tree_img = pygame.transform.scale(tree_img, (50, 50))

    for tree in trees:
        tree["y"] += evey_speed
        screen.blit(tree_img, (tree["x"], tree["y"]))

        
    screen.fill((225, 225, 225))  
    screen.blit(skier_img, (skier_x, skier_y))
    
    if compliment_giver > 0:
        compliment_surface = font.render(eveys_compliment, True, (0, 0, 0))
        screen.blit(compliment_surface, (WIDTH // 2 - compliment_surface.get_width() // 2, 50))
        compliment_giver -= 1
        
    pygame.display.flip()
pygame.quit()
sys.exit()



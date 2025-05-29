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

compliment_giver = 0 
eveys_compliment = ""

trees = []

tree_pic = pygame.image.load("tree.png")
tree_pic = pygame.transform.scale(tree_pic, (450, 450))

skier_img = pygame.image.load("evey.png")
skier_img = pygame.transform.scale(skier_img, (100, 100))
skier_x = WIDTH // 2 - 30 
skier_y = 0

evey_speed = 2 
skier_speed_x = 5

font = pygame.font.Font("Sugar Fruit.otf", 36)


number = 0 
while number <15: 
    tree_x = random.randint(0, WIDTH - 100)
    tree_y = random.randint(-HEIGHT,0)
    trees.append({"x": tree_x, "y": tree_y})
number +=1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and skier_x > 0:
        if skier_x > 0:
            skier_x = skier_x - skier_speed_x
    if keys[pygame.K_RIGHT] and skier_x < WIDTH - 100:
        if skier_x < HEIGHT:
            skier_x += skier_speed_x + skier_speed_x
            skier_y += evey_speed
            
    maybe = random.randint(1, 40)
    if maybe == 3:
        new_tree_x = random.randint(0, WIDTH - 100)
        trees.append({"x": new_tree_x, "y": -100})
        
    count = 0
    while count < len(trees):
        trees[count]["y"] = trees[count]["y"] + evey_speed
        count += 1          
        tree_x = random.randint(0, WIDTH - 75)
        trees.append({"x": tree_x, "y" : - 75})
    
    screen.fill((225, 225, 225))  

    if random.randint(1, 150) == 77:
        eveys_compliment = random.choice(compliments)
        compliment_giver = 180 

    if compliment_giver > 0:
        compliment_surface = font.render(eveys_compliment, True, (0, 0, 0))
        msg_x = WIDTH // 2 - compliment_surface.get_width() // 2
        msg_y = 50
        screen.blit(compliment_surface, (msg_x, msg_y))
        compliment_giver = compliment_giver - 1 
        
    pygame.display.flip()
pygame.quit()
sys.exit()



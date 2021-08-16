import pgzrun
import random
apple = Actor("apple")
orange = Actor("orange")
pineapple = Actor("pineapple")
fruits = [apple ,orange, pineapple]
random.shuffle(fruits)
fruits_random = random.choice(fruits)
def draw ():
    screen.clear()
    fruits_random.draw()
def place_apple ():
    fruits_random.x = random.randint(20,800-20)
    fruits_random.y = random.randint(20,600-20)
def on_mouse_down (pos):
    if fruits_random.collidepoint(pos):
        print("good shot")
        place_apple()
    else :
        print("you missed!!")
        quit()
place_apple()
pgzrun.go()

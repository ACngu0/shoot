from random import randint

apple = Actor("apple")
apple2 = Actor("apple2")

def draw():
    screen.fill((0,0,0))
    apple.draw()
    apple2.draw()

def place_apple():
    apple.x = randint(10,800)
    apple.y = randint(10, 600)

def place_apple2():
    apple2.x = 342
    apple2.y = 271

def on_mouse_down(pos):
    global points
    if apple.collidepoint(pos):
        print("Nice!")
        points = points + 1
        place_apple()
        print(f"Your score is:" ,(points))
    else:
        print("You suck!!")
        print("Game Over!!")
        quit()




global points
points = 0
place_apple()
place_apple2()

##while points >= 10:
   ## place_apple2()
import time
import random
score = 1
box_size = 25
window_size = 1000
leadingx = 0
leadingy = 0
grid = []
storex = [0]
storey = [0]
dirmotion = 'move_forward'
game = 'playing'
snake_length = 1
randx = 0
randy = 0
objective = False
objectivex = window_size/10
objectivey = window_size/10
input = False
def setup():
    size(window_size,window_size)
    frameRate = 60   
    background(0)    
def draw():
    
    global leadingy, leadingx, box_size, game, snake_length
    if game == 'playing':
        background(255,204,0)
        fill(0)
        #grid()
        textSize(30)
        fill (0)
        text(("Score: "+str(snake_length*10)),20,50)
        translate(width/2,height/2)
        key_management()
        motion()
        objective_box()
    else:
        loss_management()
    #first_screen()
    time.sleep(0.06)
def key_management():
    global game
    if game == 'playing':
        global leadingx, leadingy, dirmotion
        if keyPressed == True:
            if key == ('w'):
                dirmotion = 'move_forward'
            if key == ('d'):
                dirmotion = 'move_right'
            if key == ('a'):
                dirmotion = 'move_left'
            if key == ('s'):
                dirmotion = 'move_bottom'
def draw_square():
    global storex, storey, game, snake_length, objective, objectivex, objectivey
    if game == 'playing':
        stroke(255,204,0)
        i = len(storex)-1
        while i != len(storex)-1-snake_length:
            rect(storex[i], storey[i], box_size, box_size)
            if i != len(storex)-1 and storex[len(storex)-1] == storex[i] and storey[len(storex)-1] == storey[i]:
                game = 'lost'
            i-=1
        if storex[len(storex)-1]==objectivex and storey[len(storey)-1] ==objectivey:
            objective = True 
        if storex[len(storex)-1] == storex[len(storex)-2] and storey[len(storey)-1] == storey[len(storey)-2]:
            game = 'lost'
            
def motion ():
    global dirmotion, leadingx, leadingy, game
    if game == 'playing':
        if dirmotion == 'move_forward':
            leadingy -= 25
            storey.append(leadingy)
            storex.append(leadingx)
        if dirmotion == 'move_right':
            leadingx += 25
            storex.append(leadingx)
            storey.append(leadingy)
        if dirmotion == 'move_left':
            leadingx -= 25
            storex.append(leadingx)
            storey.append(leadingy)
        if dirmotion == 'move_bottom':
            leadingy += 25
            storey.append(leadingy)
            storex.append(leadingx)
        limit_management()
        draw_square()

def limit_management():
    global dirmotion, leadingx, leadingy, game
    if (leadingy < -height/2 or leadingx > width/2-box_size or leadingx < -width/2 or leadingy > height/2-box_size):
        game = 'lost'    

def objective_box():
    global objectivex, objectivey, objective,snake_length
    if objective == False:
        fill(255,0,0)
        rect(objectivex, objectivey, box_size, box_size)
        fill(0)
    if objective == True:
        snake_length+=1
        random_place()
        fill(255,0,0)
        rect(objectivex, objectivey, box_size, box_size)
        fill(0)
        objective = False

def random_place():
    global grid, window_size, box_size, objectivex, objectivey
    num_lines = window_size/box_size
    for i in range (0, num_lines/2):
        grid.append(-1*i*(window_size/num_lines))
        i += 1
    for i in range (0, num_lines/2):
        grid.append(i*(window_size/num_lines))
        i += 1
    objectivex = random.choice(grid)
    objectivey = random.choice(grid)
    print(grid)



def loss_management():
    global game
    if game == 'lost':
        fill(255)
        rect(0,0, window_size, window_size)
        textSize(75)
        fill (255)
        text("GAME OVER",-200,0)
        textSize(50)
        exit()


# def first_screen():
#     global input
#     fill(255)
#     textSize(50)
#     text("Hello", 100, 100) 
#     while input!=True:

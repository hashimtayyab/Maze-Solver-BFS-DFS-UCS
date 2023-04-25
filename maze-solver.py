import turtle
import math
import time
from collections import deque

wn = turtle.Screen()
wn.bgcolor('black')
wn.title("MAZE GAME")
wn.setup(700, 700)

class tileWhite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)

class tileBlue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('blue')
        self.penup()
        self.speed(0)

class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('circle')
        self.color('yellow')
        self.penup()
        self.speed(0)

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape('square')
        self.color('green')
        self.penup()
        self.speed(0)

    def goUp(self):
        self.goto(self.xcor(), self.ycor()+24)
        self.stamp()
    def goDown(self):
        self.goto(self.xcor(), self.ycor()-24)
        self.stamp()
    def goRight(self):
        self.goto(self.xcor()+24, self.ycor())
        self.stamp()
    def goLeft(self):
        self.goto(self.xcor()-24, self.ycor())
        self.stamp()

    def foundGoal(self, other):
        a = self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        d = math.sqrt((a**2) + (b**2))
        if d< 5:
            return True
        else: 
            return False 


level_1 = [
"XXXXXXXX",
"XXX  E X",
"X      X",
"X      X",
"X      X",
"X   XXXX",
"XSX    X",
"XXXXXXXX"
]


# level_1 = [
# "XXXXXXXX",
# "XXX X  X",
# "X    X X",
# "X  X   X",
# "X   X  X",
# "X X XXXX",
# "XSX  E X",
# "XXXXXXXX"
# ]

def setup_maze(level_1):
    global start_x, start_y, end_x, end_y
    for y in range(len(level_1)):
        for x in range(len(level_1[y])):
            character = level_1[y][x]
            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)

            if character == "X":#Obstacles
                wall.goto(screen_x, screen_y)
                wall.stamp()
                obstacles.append((screen_x, screen_y))
            elif character == "S":        #Start        
                player.goto(screen_x, screen_y)
                player.stamp()
                start_x, start_y = screen_x, screen_y
                path.append((screen_x, screen_y))
            elif character == "E":  #End
                goal.goto(screen_x, screen_y)
                goal.stamp()
                end_x, end_y = screen_x, screen_y
                path.append((screen_x, screen_y))
            elif character == " ": #Path
                penW.goto(screen_x, screen_y)
                penW.stamp()
                path.append((screen_x, screen_y))


def bfs(x, y):
    wn.title("BFS Algorithm")
    next.append((x, y))
    while len(next) > 0:
        x, y = next.popleft()
        if (x, y + 24) in path and (x, y + 24) not in visited:  #Checking above node
            next.append((x, y + 24))
            visited.add((x, y + 24))
        if (x, y - 24) in path and (x, y - 24) not in visited:  #Checking below node
            next.append((x, y - 24))
            visited.add((x, y - 24))
        if (x + 24, y) in path and (x + 24, y) not in visited:  #Checking right node
            next.append((x + 24, y))
            visited.add((x + 24, y))
        if (x - 24, y) in path and (x - 24, y) not in visited:  #Checking left node
            next.append((x - 24, y))
            visited.add((x - 24, y))
        time.sleep(0.2)
        player.goto(x, y)
        player.stamp()
        if x == end_x and y == end_y:
            player.color('yellow')
            # goal.setpos(100, 0)
            # goal.write("Goal!!")
            print("Goal Found!")
            break



def dfs(x, y):
    wn.title("DFS Algorithm")
    next.append((x, y))                            # add the x and y position to the next list
    while len(next) > 0:                           # loop until the next list is empty
        time.sleep(0)                                  # change this value to make the animation go slower
        current = (x,y)                                # current cell equals x and  y positions

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check left
            next.append((x-24, y))
        if (x, y - 24) in path and (x, y - 24) not in visited:  # check down
            next.append((x, y-24))
        if(x + 24, y) in path and (x + 24, y) not in visited:   # check right
            next.append((x+24, y))
        if(x, y + 24) in path and (x, y + 24) not in visited:  # check up
            next.append((x, y+24))

        time.sleep(0.2)
        x, y = next.pop()
        visited.add(current)
        player.goto(x,y)
        player.stamp()                   
        if x == end_x and y == end_y:
            player.color('yellow')
            print("Goal Found!")
            break        


def ucs(x, y):
    next.append((x, y))      
    while len(next) > 0:
        x, y = next.pop()
        current_node = (x, y)
        if(x - 24, y) in path and (x - 24, y) not in visited:  # check left
            next.append((x-24, y))
            player.goto(x-24, y)
            visited.add((x-24, y))
            player.stamp()
            # continue
        if (x, y - 24) in path and (x, y - 24) not in visited:  # check down
            next.append((x, y-24))
            player.goto(x, y-24)
            visited.add((x, y-24))
            player.stamp()
            # continue
        if(x + 24, y) in path and (x + 24, y) not in visited:   # check right
            next.append((x+24, y))
            player.goto(x+24, y)
            visited.add((x+24, y))
            player.stamp()
            # continue
        if(x, y + 24) in path and (x, y + 24) not in visited:  # check up
            next.append((x, y+24))
            visited.add((x, y+24))
            player.goto(x, y+24)
            player.stamp()
            # continue                    
        # print(current_node, end = " ")
        # visited.add(current_node)
        # player.goto(current_node)
        # player.stamp()
        time.sleep(0.2)
        # next.append(x, y)



goal = Goal()
player = Player()
wall = tileBlue()
penW = tileWhite()

obstacles = []
path = []
visited = set()
next = deque()

setup_maze(level_1)
# bfs(start_x, start_y)
dfs(start_x, start_y)
# ucs(start_x ,start_y)

wn.tracer(0)
while True:
    wn.update()
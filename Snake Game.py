import turtle
import time
import random



delay = 0.1

# score
score = 0
high_score = 0


#set up the screen

wn=turtle.Screen()
wn.title(" Snake Game ")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off the screen updates


# Snake Head

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("grey")
head.penup()
head.goto(0,0)
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

segaments = []

# pen
pen = turtle.Turtle()
pen.speed(0)  # annimation speed
pen.shape("circle")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score:0   High Score : 0", align="center" , font=("courier", 24, "normal"))


#functions
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
    if head.direction != "up":
        head.direction = "down"
def go_left():
    if head.direction != "right":
        head.direction = "left"
def go_right():
    if head.direction != "left":
        head.direction = "right"    



# functions
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
        
# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# making the main game loop

while True:
    wn.update()


    # check for a collision with the border
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"



        

    # check for a collision with the food
    if head.distance(food) < 20:
        # move the food to a random spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)


        # adding a new segament
        new_segament = turtle.Turtle()
        new_segament.speed(0)
        new_segament.shape("square")
        new_segament.color("black")
        new_segament.penup()
        segaments.append(new_segament)

        #shorten th delay

        delay -=0.001

        # increasing the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("courier", 24, "normal"))             



        
    # move the end segaments first in reverse order
    for index in range(len(segaments)-1, 0, -1):
        x = segaments[index-1].xcor()
        y = segaments[index-1].ycor()
        segaments[index].goto(x, y)



    # moving segament 0 to where the head is
    if len(segaments) > 0:
        x= head.xcor()
        y= head.ycor()
        segaments[0].goto(x,y)

    move()


    # check for the head collision with the body segaments
    for segament in segaments:
        if segament.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            
            # to hide the segaments
            for segament in segaments:
                segament.goto(1000,1000)


            # clearing the segaments list
            segaments.clear()


            # reset the score
            score = 0

            #reset the delay
            delay =0.1
            
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("courier", 24, "normal"))             


            
    time.sleep(delay)
    







wn.mainloop(0)

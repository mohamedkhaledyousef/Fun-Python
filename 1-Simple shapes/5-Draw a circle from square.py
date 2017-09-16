import turtle   #to move down and drows stuff on computer

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)    #100 is distance
        some_turtle.right(90)          #90degree

def draw_art():
    window = turtle.Screen()  #to print red carpet as screen
    window.bgcolor("red")
    
    #we can change or customize shapes
    #create the turtle Brad -draws a square
    brad=turtle.Turtle()  #to start draw..to grab turtle
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    #to turn the turtle a little bit to the right
    for i in range(1,37):
        draw_square(brad)
        brad.right(10)  #10 degree


    #to draw a circle...angie is instance or exaample from Turtle class
    #create the turtle Angie-draws a circle
    #angie=turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)   #100 is raduis

    window.exitonclick()    #to close this window any time i click on it

draw_art()

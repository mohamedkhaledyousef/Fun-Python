import turtle   #to move down and drows stuff on computer

def draw_square():
    window = turtle.Screen()  #to print red carpet as screen
    window.bgcolor("red")
    
    brad=turtle.Turtle()  #to start draw..to grab turtle

    #we can change or customize shapes
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(2)
    
    brad.forward(100)    #100 is distance
    brad.right(90)          #90degree
    brad.forward(100)    #100 is distance
    brad.right(90)          #90degree
    brad.forward(100)    #100 is distance
    brad.right(90)          #90degree
    brad.forward(100)    #100 is distance
    brad.right(90)          #90degree

    #to draw a circle...angie is instance or exaample from Turtle class
    angie=turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)   #100 is raduis

    window.exitonclick()    #to close this window any time i click on it

draw_square()

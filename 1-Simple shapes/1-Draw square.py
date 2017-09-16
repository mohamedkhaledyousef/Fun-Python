import turtle   #to move down and drows stuff on computer

def draw_square():
    window = turtle.Screen()  #to print red carpet as screen
    window.bgcolor("red")
    
    brad=turtle.Turtle()  #to start draw..to grab turtle
    brad.forward(100)    #100 is distance
    brad.right(90)          #90degree
    brad.forward(100)    #100 is distance
    brad.right(90)          #90degree
    brad.forward(100)    #100 is distance
    brad.right(90)          #90degree
    brad.forward(100)    #100 is distance
    brad.right(90)          #90degree

    window.exitonclick()    #to close this window any time i click on it

draw_square()

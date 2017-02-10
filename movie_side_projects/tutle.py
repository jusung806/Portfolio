import turtle

def draw_square(some_turtle):
    for i in range (1,5):
            some_turtle.forward(100)
            some_turtle.right(90)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("black")
    
    eliza = turtle.Turtle()
    eliza.shape("turtle")
    eliza.color("green")
    eliza.speed(2)
  

    robert = turtle.Turtle()
    robert.shape("turtle")
    robert.color("blue")
    robert.circle(100)

    

    window.exitonclick()
    

draw_square()

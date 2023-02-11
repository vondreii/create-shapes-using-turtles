import turtle

# Window/Canvas   
window = turtle.Screen()
window.bgcolor("white")

# Rectangle
turtle_1 = turtle.Turtle()
turtle_1.shape("turtle")
turtle_1.color("red")

turtle_1.forward(100)
turtle_1.right(90)
turtle_1.forward(200)
turtle_1.right(90)
turtle_1.forward(100)
turtle_1.right(90)
turtle_1.forward(200)

# Triangle
turtle_2 = turtle.Turtle()
turtle_2.shape("arrow")
turtle_2.color("blue")

turtle_2.penup()
turtle_2.goto(-250,200)
turtle_2.pendown()

# turtle_2.forward(100)
# turtle_2.left(120)
# turtle_2.forward(100)
# turtle_2.left(120)
# turtle_2.forward(100)
# turtle_2.left(120)

for i in range(3):
  turtle_2.forward(100)
  turtle_2.left(120)

# Circle
turtle_3 = turtle.Turtle()
turtle_3.shape("circle")
turtle_3.color("green")

turtle_3.penup()
turtle_3.goto(-100,50)
turtle_3.pendown() 

turtle_3.circle(50)


# Hexagon
turtle_4 = turtle.Turtle()
turtle_4.shape("turtle")
turtle_4.color("purple")

turtle_4.penup()
turtle_4.goto(150,200)
turtle_4.pendown()

for i in range(6):
  turtle_4.forward(100)
  turtle_4.right(60)

# Octagon
#for i in range(8):
#  turtle_4.forward(100)
#  turtle_4.right(45)

window.exitonclick()

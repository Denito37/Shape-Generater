#can create many shapes
#add randomizer if user has no want in choosing values
import turtle
import random

print("""Welcome to my shape generator,you will be asked a couple questions to determine your shape, but if you don't know what you want type "random" to generate a random shape""")

special = int(input('enter 360 for basic shapes or a mutiple of 360 for special shapes:'))
shape = int(input('Enter number of shape sides:'))
color = input('Enter the color of the shape:')
colors = str(color)
#cursor = input('Enter cursor shape:')
#cursors = str(cursor)

turtleMan = turtle.Turtle()
turtleMan.pencolor(colors)
#turtleMan.shape(cursors)

if special >= 360 and shape >= 3:
    for i in range(shape):
        turtleMan.forward(150)
        turtleMan.left(special/shape)
else:
    print('Will not create a shape!')

    

    

import turtle

sample = turtle.Turtle()
sample.speed(30)


def square():
        sample.forward(200)
        sample.right(90)
        sample.forward(100)
        sample.right(90)
        sample.forward(200)
        sample.right(90)
        sample.forward(100)
# square()
# sample.forward(100)
# square()


for count in range(4):
    square()



turtle.done()
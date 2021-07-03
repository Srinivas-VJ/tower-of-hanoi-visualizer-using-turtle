import turtle
import time

a = []
b = []
c = []


def createStackShape(l):

    shape = ((l, 20), (0, 20), (0, 0), (l, 0))
    turtle.speed(3)
    turtle.penup()
    turtle.color('black', 'white')
    # registering the new shape
    turtle.register_shape('stack', shape)

    # changing the shape to 'diamond'
    turtle.shape('stack')


class Disk():

    def __init__(self, stamp, n, coords) -> None:
        self.n = n
        self.stamp = stamp
        self.coords = coords

    def moveDisk(self, destination):
        turtle.hideturtle()
        turtle.setposition(self.coords)
        createStackShape(self.n*20)
        turtle.showturtle()
        turtle.clearstamp(self.stamp)
        turtle.setposition(self.coords[0], 275)
        x, y = 0, 0

        if destination is a:
            x = -200 - self.n*10
        elif destination is b:
            x = - self.n*10
        else:
            x = 200 - self.n*10

        turtle.setx(x)
        y = len(destination)*20

        turtle.sety(y)
        s = turtle.stamp()

        new = Disk(s, self.n, (x, y))
        destination.append(new)


def draw(n):

    turt = turtle.Turtle()
    # making the base;
    turt.color("black")
    turt.speed(n)
    turt.begin_fill()
    turt.forward(400)
    turt.backward(800)
    turt.right(90)
    turt.forward(30)
    turt.left(90)
    turt.forward(800)
    turt.left(90)
    turt.forward(30)
    turt.left(90)
    turt.forward(98*2)
    turt.right(90)
    turt.forward(250)
    turt.left(90)
    turt.forward(4*2)
    turt.left(90)
    turt.forward(250)
    turt.right(90)
    turt.forward(96*2)
    turt.right(90)
    turt.forward(250)
    turt.left(90)
    turt.forward(4*2)
    turt.left(90)
    turt.forward(250)
    turt.right(90)
    turt.forward(96*2)
    turt.right(90)
    turt.forward(250)
    turt.left(90)
    turt.forward(4*2)
    turt.left(90)
    turt.forward(250)
    turt.left(90)
    turt.forward(2*2)
    turt.left(90)
    turt.end_fill()
    turtle.left(90)
    w = 0
    for i in range(n, 0, -1):
        l = i*20
        createStackShape(l)
        turtle.setposition(-200 - l/2, w)
        s = turtle.stamp()
        d = Disk(s, i, (-200 - l/2, w))
        a.append(d)
        w += 20


def move(n, source, target, auxiliary):
    if n > 0:
        # Move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, auxiliary, target)

        # Move the nth disk from source to target
        disk = source.pop()
        disk.moveDisk(target)

        # Move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, auxiliary, target, source)


def initialize(n):
    draw(n)
    # turtle.delay(250)
    time.sleep(0.35)

    move(n, a, c, b)

    # testing

    turtle.done()


initialize(int(input("How many rings -> ")))
# makeStack();

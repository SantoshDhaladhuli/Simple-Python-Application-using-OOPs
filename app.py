import turtle
from random import randint

myturtle = turtle.Turtle()

class Point:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,point):
        return ((point.x - self.x)**2 + (point.y - self.y)**2)**0.50

    def within_rectangle(self,rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and \
            rectangle.lowleft.y < self.y < rectangle.upright.y:
            return  True
        else:
            return False

class Rectangle:

    def __init__(self,point1,point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        return abs((self.point2.x - self.point1.x)*(self.point2.y - self.point1.y))

class GraphicalRectangle(Rectangle):

    def draw(self,canvas = myturtle):

        if self.point1.x <= self.point2.x:

            canvas.penup()
            canvas.goto(self.point1.x, self.point1.y)  # Granphical Rectangle inherits Rectangle here
            canvas.pendown()

            if self.point1.y <= self.point2.y:

                canvas.forward(self.point2.x - self.point1.x)
                canvas.left(90)
                canvas.forward(self.point2.y - self.point1.y)
                canvas.left(90)
                canvas.forward(self.point2.x - self.point1.x)
                canvas.left(90)
                canvas.forward(self.point2.y - self.point1.y)

            else:

                canvas.right(90)
                canvas.forward(self.point1.y - self.point2.y)
                canvas.left(90)
                canvas.forward(self.point2.x - self.point1.x)
                canvas.left(90)
                canvas.forward(self.point1.y - self.point2.y)
                canvas.left(90)
                canvas.forward(self.point2.x - self.point1.x)
        else:

            canvas.penup()
            canvas.goto(self.point2.x, self.point2.y)  # Granphical Rectangle inherits Rectangle here
            canvas.pendown()

            if self.point2.y <= self.point1.y:

                canvas.right(90)
                canvas.forward(self.point1.y - self.point2.y)
                canvas.left(90)
                canvas.forward(self.point1.x - self.point2.x)
                canvas.left(90)
                canvas.forward(self.point1.y - self.point2.y)
                canvas.left(90)
                canvas.forward(self.point1.x - self.point2.x)

            else:

                canvas.forward(self.point1.x - self.point2.x)
                canvas.left(90)
                canvas.forward(self.point2.y - self.point1.y)
                canvas.left(90)
                canvas.forward(self.point1.x - self.point2.x)
                canvas.left(90)
                canvas.forward(self.point2.y - self.point1.y)


class GraphicalPoint(Point):

    def draw(self, size = 5, color = 'red', canvas = myturtle):
        canvas.penup()
        canvas.goto(self.x,self.y)
        canvas.pendown()
        canvas.dot(size, color)

point1 = Point(randint(0,100), randint(0,100))
point2 = Point(randint(0,100), randint(0,100))

new_rectangle = GraphicalRectangle(point1, point2)

user_point = GraphicalPoint(float(input("Enter X: ")), float(input("Enter Y: ")))

new_rectangle.draw()
user_point.draw()

print(point1.x, point1.y)
print(point2.x, point2.y)
turtle.done()





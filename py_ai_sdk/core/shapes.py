from abc import ABC, abstractmethod

from py_ai_sdk.core.dimensions import Dim2D
from py_ai_sdk.core.core_utils import check_positive_value

class Shape2D(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @staticmethod
    def addPosition(position):
        return position

    def addMotionPhysics(self, motionPhysics):
        self.motionPhysics = motionPhysics

    def updateMotionPhysics(self, position, newForce=Dim2D(0, 0), newMass=None, friction=None, newAcceleration=Dim2D(0, 0)):
        return self.motionPhysics.update(position, newForce, newMass, friction, newAcceleration)

    @staticmethod
    def circleVscircleIntersectionCheck(circle1, circle2):
        dist = Dim2D.get_euclid_distance(circle1.centre, circle2.centre)
        totalRadius = circle1.radius + circle2.radius
        return dist <= totalRadius

class Rectangle(Shape2D):
    def __init__(self, top_left_corner, width, height):
        self.top_left_corner = super().addPosition(top_left_corner)
        check_positive_value(width)
        check_positive_value(height)
        self.width = width
        self.height = height

    def __str__(self):
        return "top_left_corner = " + str(self.top_left_corner) \
        + "width x height: " + str(self.width) + " x " + str(self.height)

    def __repr__(self):
        return self.__str__()

    def updateMotionPhysics(self, newForce=Dim2D(0, 0), newMass=None, friction=None, newAcceleration=Dim2D(0, 0)):
        self.top_left_corner = super().updateMotionPhysics(self.top_left_corner, newForce, newMass, friction, newAcceleration)

class Hexagon(Shape2D):
    def __init__(self):
        pass

    def __str__(self):
        return "pass"

    def __repr__(self):
        return self.__str__()

class Circle(Shape2D):
    def __init__(self, centre, radius):
        self.centre = super().addPosition(centre)
        check_positive_value(radius)
        self.radius = radius

    def __str__(self):
        return "centre: " + str(self.centre) + ", radius: " + str(self.radius)

    def __repr__(self):
        return self.__str__()

    def updateMotionPhysics(self, newForce=Dim2D(0, 0), newMass=None, friction=None, newAcceleration=Dim2D(0, 0)):
        self.centre = super().updateMotionPhysics(self.centre, newForce, newMass, friction, newAcceleration)

class Point(Shape2D):
    def __init__(self, position):
        self.position = super().addPosition(position)

    def __str__(self):
        return "position: " + str(self.position)

    def __repr__(self):
        return self.__str__()

    def updateMotionPhysics(self, newForce=Dim2D(0, 0), newMass=None, friction=None, newAcceleration=Dim2D(0, 0)):
        self.position = super().updateMotionPhysics(self.position, newForce, newMass, friction, newAcceleration)

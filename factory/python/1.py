# -*- coding:utf-8 -*-

"""
@author: DeeLMind
@file: test.py
@time: 2019/1/16 10:17
"""
from abc import ABCMeta, abstractmethod

# 定义形状接口
class Shape(metaclass=ABCMeta):
    @abstractmethod
    # 定义接口方法
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Circle")


class Rect(Shape):
    def draw(self):
        print("Rect")


# 新建工厂类
class FactoryShape():
    def getShape(self,name):
        if(name == "Circle"):
            return Circle()
        if(name == "Rect"):
            return Rect()


if __name__ == "__main__":
    print ("Main Entry")
    FS = FactoryShape()

    Circle = FS.getShape("Circle")
    Circle.draw()

    Rect = FS.getShape("Rect")
    Rect.draw()
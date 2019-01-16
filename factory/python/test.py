# -*- coding:utf-8 -*-

"""
@author: DeeLMind
@file: test.py
@time: 2019/1/16 10:17
"""
from abc import ABCMeta, abstractmethod

class Transport(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass

class Car(Transport):
    def run(self):
        print("Car run")

    def Bi(self):
        print("Car Bi")

class Fly(Transport):
    def run(self):
        print("Fly run")

    def Bi(self):
        print("Fly Bi")

class TrasportFactory():
    def getTrasport(self,name):
        if(name == "Car"):
            return Car()

        if(name == "Fly"):
            return Fly()


class Person(metaclass=ABCMeta):
    @abstractmethod
    def drive(self,tras):
        pass

class Teacher(Person):
    def drive(self,tras):
        print("Tea dirve")
        tras.run()

class Student(Person):
    def drive(self,tras):
        print("Stu dirve")
        tras.run()


class PersonFactory():
    def getPerson(self,name):
        if(name == "Teacher"):
            return Teacher()

        if(name == "Student"):
            return Student()


class Factory():
    def getFactory(self,name):
        if(name == "PersonFactory"):
            return PersonFactory()

        if(name == "TrasportFactory"):
            return TrasportFactory()

if __name__ == "__main__":
    print ("Main Entry")
    Factory = Factory()

    TFactory = Factory.getFactory("TrasportFactory")
    Car = TFactory.getTrasport("Car")

    PFactory = Factory.getFactory("PersonFactory")
    Tea = PFactory.getPerson("Teacher")

    Tea.drive(Car)

    t = t()
    t.aa()
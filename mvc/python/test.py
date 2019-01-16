# -*- coding:utf-8 -*-

"""
@author: DeeLMind
@file: test.py
@time: 2019/1/16 11:15
"""

class Student:
    __name = ""
    __rollNo = ""

    def getName(self):
        return self.__name

    def getrollNo(self):
        return self.__rollNo

    def setName(self,name):
        self.__name = name

    def setrollNo(self,no):
        self.__rollNo = no


class StudentView:
    def printStudentDetails(self,name,rollNo):
        print (name,rollNo)
        
        
class StudentController:
    __Student = ""
    __StudnetView = ""

    def __init__(self,model,view):
        self.__Student = model
        self.__StudnetView = view

    # def setStudentName(self,name):
    #     self.__Student.setName(name)
    #
    # def getStudentName(self):
    #     return self.__Student.getName()
    #
    # def setStudentRollNo(self,rollNo):
    #     self.__Student.getrollNo()
    #
    # def getStudentRollNo(self):
    #     return self.__Student.getrollNo()

    def updateView(self):
        self.__StudnetView.printStudentDetails(self.__Student.getName(),self.__Student.getrollNo())


if __name__ == "__main__":
    student = Student()
    student.setName("DeeLMind")
    student.setrollNo("369")

    SV = StudentView()

    SC = StudentController(student,SV)

    SC.updateView()
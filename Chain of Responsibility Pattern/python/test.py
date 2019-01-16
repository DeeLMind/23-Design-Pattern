# -*- coding:utf-8 -*-

"""
@author: DeeLMind
@file: test.py
@time: 2019/1/16 14:11
"""

class HandScript:
    def __init__(self):
        pass

    def successor(self,successor):
        self.successor = successor

    def handle(self,script):
        pass

class HandVar(HandScript):
    def processVar(self,script):
        print(script)
        return True

    def handle(self,script):
        if(self.processVar(script)):
            print ("Process Var")
            self.successor.handle(script)


class HandFunc(HandScript):
    def processFunc(self,script):
        print(script)
        return True

    def handle(self,script):
        if(self.processFunc(script)):
            print("Process Func")
            self.successor.handle(script)


class HandFin:
    def handle(self,script):
        print(script)
        print("Process Fin")


if __name__ == "__main__":
    handvar = HandVar()
    handfunc = HandFunc()
    handfin = HandFin()

    handvar.successor(handfunc)
    handfunc.successor(handfin)

    handvar.handle("script")
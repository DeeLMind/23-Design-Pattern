# -*- coding:utf-8 -*-

"""
@author: DeeLMind
@file: test.py
@time: 2019/1/16 11:35
"""

#! -*- coding: utf-8 -*-

import itertools

'''
观察者模式实现
'''


class Publisher:

    def __init__(self):
        self.observers = set()

    def add(self, observer, *observers):
        for observer in itertools.chain((observer, ), observers):
            self.observers.add(observer)
            observer.update(self)

    def remove(self, observer):
        try:
            self.observers.discard(observer)
        except ValueError:
            print('Failed to remove: {}'.format(observer))

    def notify(self):
        [observer.update(self) for observer in self.observers]


class DefaultFormatter(Publisher):

    def __init__(self, name):
        Publisher.__init__(self)
        self.name = name
        self._data = 0

    def __str__(self):
        return "{}: '{}' has data = {}".format(type(self).__name__, self.name, self._data)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_value):
        try:
            self._data = int(new_value)
        except ValueError as e:
            print('Error: {}'.format(e))
        else:
            self.notify()


class HexFormatter:

    def update(self, publisher):
        print("{}: '{}' has now hex data= {}".format(type(self).__name__,
                                                     publisher.name, hex(publisher.data)))


class BinaryFormatter:

    def update(self, publisher):
        print("{}: '{}' has now bin data= {}".format(type(self).__name__,
                                                     publisher.name, bin(publisher.data)))


def main():
    df = DefaultFormatter('test1')
    print(df)

    print()
    hf = HexFormatter()
    df.add(hf)
    df.data = 3
    print(df)

    print()
    bf = BinaryFormatter()
    df.add(bf)
    df.data = 21
    print(df)

    print()
    df.remove(hf)
    df.data = 40
    print(df)

    print()
    df.remove(hf)
    df.add(bf)

    df.data = 'hello'
    print(df)

    print()
    df.data = 4.2
    print(df)


if __name__ == '__main__':
    main()
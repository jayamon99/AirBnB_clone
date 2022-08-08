#!/usr/bin/python3
class Hero():
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


archer = Hero("Arthur")
print(archer.get_name())

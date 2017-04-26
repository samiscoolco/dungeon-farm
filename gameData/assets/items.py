#!/usr/bin/env python

"""
items.py

"""
__author__ = "Sam Tubb (sam0s)"
__copyright__ = "None"
__credits__ = []

import pygame
from os import path

itemsheet = pygame.image.load(path.join("images","item.png")).convert()

class Item:
    def __init__(self):
        self.stack=1
    def setContainer(self,setpc):
        self.parentContain=setpc
    def setName(self, name):
        self.name = name
    def destroy(self):
        self.parent.inventory.remove(self)

#TYPES


#WEAPON
class Dirk(Item):
    def __init__(self,setp,setpc=None):
        self.parent=setp
        self.parentContain=setpc
        self.itemType="weapon"
        self.name="dirk"

        self.id = 0

        self.val = 15
        self.consumeVal = 0
        self.ad = 8
        self.ap = 0
        self.weight = 1

        self.stack=1

        self.image = itemsheet.subsurface(pygame.Rect(self.id*26, 0, 26, 26)).convert()

class Sword(Item):
    def __init__(self,setp,setpc=None):
        self.parent=setp
        self.parentContain=setpc
        self.itemType="weapon"
        self.name="sword"

        self.id = 8

        self.val = 25
        self.consumeVal = 0
        self.ad = 12
        self.ap = 0
        self.weight = 1

        self.stack=1

        self.image = itemsheet.subsurface(pygame.Rect(self.id*26, 0, 26, 26)).convert()

#EAT
class Bread(Item):
    def __init__(self,setp,setpc=None):
        self.parent=setp
        self.parentContain=setpc
        self.itemType="food"

        self.id=1

        self.val=5
        self.name="bread"
        self.consumeVal = 20
        self.ad=0
        self.ap=0
        self.weight = 0.5

        self.stack=1

        self.image = itemsheet.subsurface(pygame.Rect(self.id*26, 0, 26, 26)).convert()



class Apple(Item):
    def __init__(self,setp,setpc=None):
        self.parent=setp
        self.parentContain=setpc
        self.itemType="food"

        self.id=2

        self.val = 2
        self.name="apple"
        self.consumeVal = 15
        self.ad = 0
        self.ap = 0
        self.weight = 1

        self.stack=1

        self.image = itemsheet.subsurface(pygame.Rect(self.id*26, 0, 26, 26)).convert()


class Pizza(Item):
    def __init__(self,setp,setpc=None):
        self.parent=setp
        self.parentContain=setpc
        self.itemType="food"

        self.id=3

        self.val = 2
        self.name="pizza"
        self.consumeVal = 25
        self.ad = 0
        self.ap = 0
        self.weight = 1

        self.stack=1

        self.image = itemsheet.subsurface(pygame.Rect(self.id*26, 0, 26, 26)).convert()

class Cheese(Item):
    def __init__(self,setp,setpc=None):
        self.parent=setp
        self.parentContain=setpc
        self.itemType="food"

        self.id=4

        self.val = 2
        self.name="cheese"
        self.consumeVal = 10
        self.ad = 0
        self.ap = 0
        self.weight = 1

        self.stack=1

        self.image = itemsheet.subsurface(pygame.Rect(self.id*26, 0, 26, 26)).convert()

class Fish(Item):
    def __init__(self,setp,setpc=None):
        self.parent=setp
        self.parentContain=setpc
        self.itemType="food"

        self.id=5

        self.val = 2
        self.name="fish"
        self.consumeVal = 15
        self.ad = 0
        self.ap = 0
        self.weight = 1

        self.stack=1

        self.image = itemsheet.subsurface(pygame.Rect(self.id*26, 0, 26, 26)).convert()


class HealthPot(Item):
    def __init__(self,setp,setpc=None):
        self.parent=setp
        self.parentContain=setpc
        self.itemType="food"

        self.id=6

        self.val = 2
        self.name="healthpot"
        self.consumeVal = 50
        self.ad = 0
        self.ap = 0
        self.weight = 1

        self.stack=1

        self.image = itemsheet.subsurface(pygame.Rect(self.id*26, 0, 26, 26)).convert()

def fromId(idn,parent,justname=False):
    if idn==0:
        if not justname:
            return Dirk(parent)
        return "Dirk"
    if idn==1:
        if not justname:
            return Bread(parent)
        return "Bread"
    if idn==2:
        if not justname:
            return Apple(parent)
        return "Apple"
    if idn==3:
        if not justname:
            return Pizza(parent)
        return "Pizza"
    if  idn==4:
        if not justname:
            return Cheese(parent)
        return "Cheese"
    if idn==5:
        if not justname:
            return Fish(parent)
        return "Fish"
    if idn==6:
        if not justname:
            return HealthPot(parent)
        return "Health Potion"
    if idn==8:
        if not justname:
            return Sword(parent)
        return "Sword"
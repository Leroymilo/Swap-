import numpy as np
import pygame as pg
from pygame.locals import *

from __modules__ import *


#Creation of a list of levels

levels = []
newLvl = True
i = 1
while newLvl :
    try :
        levels.append(lvl('lvl'+str(i)+'.txt'))
    except :
        newLvl = False
    i += 1

#loading next level
def nLvl(curlvl=None) :
    if curlvl is None :
        i = 0
    else :
        i = curlvl.nb
    if i < len(levels) :
        lvl = levels[i].copy()
        wC, ents = getCoords(lvl)
        return lvl, ents, wC
    print('finished')
    return None

#restarting current level
def rLvl(curlvl) :
    lvl = levels[curlvl.nb-1].copy()
    wC, ents = getCoords(lvl)
    return lvl, ents, wC

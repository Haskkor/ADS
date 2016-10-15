#! /usr/bin/env python
# -*- coding:utf8-*-

import managerPlateau
import rotation
import alignement
from  random import randint
if __name__ == "__main__":
    plateauT = managerPlateau.initPlateau(6)
    managerPlateau.affichplateau(plateauT)
    alignement.ensemble(6, plateauT, 5, 1)
    rotation.rotation(6,plateauT, 3, True)
    managerPlateau.affichplateau(plateauT)
    

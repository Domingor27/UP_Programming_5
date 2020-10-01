#LABORATORIO N°1
#PROBLEMA N°2 - Counting Valleys
#2. Counting valleys -> https://www.hackerrank.com/challenges/counting-valleys/

#Autor Grupo Mugiwara

#1. Cedeño Diego, 8-900-2261
#2. Pérez Yeritzel, 8-872-2088
#3. Rodriguez Domingo, 9-732-1036


import math
import os
import random
import re
import sys

#
# Complete la función 'countingValleys' a continuación.
#
# Se espera que la función devuelva un ENTERO.
# La función acepta los siguientes parámetros:
# 1. ENTERO -> Pasos
# 2. CADENA -> Ruta
#

def countingValleys(n,s):

    contandoValles = nivel = 0

    d = {'U':1, 'D':-1}

    for pasos in s:
        nivel += d[pasos]
        if nivel ==0 and pasos == 'U':
            contandoValles += 1
    
    return contandoValles

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pasos = int(input().strip())

    ruta = input()

    resultados = countingValleys(pasos, ruta)

    fptr.write(str(resultados) + '\n')

    fptr.close()

#!/usr/bin/env python
"Imprime a tabuada."
__version__ = "0.1.0"
__author__ = "Esther Ribeiro"

numeros =list( range(1,11))


for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
       
    print("*********************")
    

print(numeros)

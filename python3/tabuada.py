#!/usr/bin/env python
"Imprime a tabuada."
__version__ = "0.1.1"
__author__ = "Esther Ribeiro"

numeros = list( range(1,11))


for n1 in numeros:
   print("{:-^15}".format(f"Tabuada do {n1}"))
   print()
   for n2 in numeros:
        resultado = n1 * n2
        print("{:^15}".format(f"{n1} x {n2} = {resultado}"))
   print("#" * 15 )
    

#print(numeros)

Capa             | Dimensiones de la activación | Cantidad de parámetros 
---                             | ---           | --- 
Entrada                         |(64, 64, 3)    | 0
Conv2D(f=5, s=2, c=8, p=2)      |(32x32x8)	    | 608
MaxPool(f=2, s=2)               |(32x32x3)      | 0
Conv2D(f=3, s=1, c=16, p=1)     |(64x64x16)	    | 448
MaxPool(f=4, s=4)               |(16x16x3)	    | 0
Dense(salida=6)                 | 6	            | 73734
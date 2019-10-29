"""
	@author: jjsanmartin2
	nombre: ejercicio1.py
	descripcion: ...

	Javier Sanmartin -- 35
	Su suma de notas es: 30
	Su promedio es: 15

"""



nombre = input("ingrese su nombre: \n ")
edad = input("ingrese su edad: \n")
nota1 = input("ingrese su nota 1: \n")
nota2 = input("ingrese su nota 2: \n")

suma = int(nota1) + int(nota2);
promedio = (int(nota1) + int(nota2)) / 2;

print("%s -- %s\nSu suma de notas es: %s\nSu promedio es: %s" %
	(nombre, edad, suma, promedio))

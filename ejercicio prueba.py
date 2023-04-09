# inicializamos las variables a utilizar
cantidad_notas = 0
suma_notas = 0
nota_minima = 7.0
nota_maxima = 1.0
notas_bajo_promedio = 0
notas_sobre_promedio = 0

while True:
    nota = float(input("Ingrese una nota (0 para terminar): "))
    
    # si la nota ingresada es cero, salimos del bucle
    if nota == 0:
        break
        
    # actualizamos las variables
    cantidad_notas += 1
    suma_notas += nota
    nota_minima = min(nota_minima, nota)
    nota_maxima = max(nota_maxima, nota)
    
# calculamos el promedio
promedio = suma_notas / cantidad_notas

# iteramos de nuevo sobre las notas para contar cuántas están por encima o por debajo del promedio
for i in range(cantidad_notas):
    nota = float(input("Ingrese la nota del alumno: "))
    
    if nota < promedio:
        notas_bajo_promedio += 1
    elif nota > promedio:
        notas_sobre_promedio += 1

# mostramos los resultados
print(f"Cantidad de notas ingresadas: {cantidad_notas}")
print(f"Promedio del alumno: {promedio:.2f}")
print(f"Nota más baja: {nota_minima}")
print(f"Nota más alta: {nota_maxima}")
print(f"Cantidad de notas bajo el promedio: {notas_bajo_promedio}")
print(f"Cantidad de notas por sobre el promedio: {notas_sobre_promedio}")

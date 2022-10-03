import random

laberinto = [] # laberinto vacio
n_fila = int(input("ingrese numero de filas:"))
n_columna = int(input("ingrese el numero de columnas:"))
n_paredes = int(input("ingrese numero de paredes:"))
n_espacios = (n_fila * n_columna) - n_paredes

for i in range(n_fila):  #para crear paredes en todos el laberinto
    laberinto.append([])
    for j in range(n_columna):
        laberinto[i].append("#")

#para guardar una coordenada en nuestra matriz crear un espacio en blanco

def espacios_vacios():
     px = random.randrange(0, n_columna) #en el eje x por que recorre un espacio a la derecha
     py = random.randrange(0,n_fila) # en el eje y porque recorre un espacio hacia abajoficha_fila = random.randrange(numero_filas)
     laberinto[py][px] = " "
     n_espacios = (n_fila * n_columna) - n_paredes
     # para generar la ficha en lugar random
     ficha_columnas = px
     ficha_fila = py
     laberinto[ficha_fila][ficha_columnas] = '$'

     while n_espacios > 0: #va reducioendo el numero de espacios
         direccion = random.randrange(0,4) #condiciones tenemos valores guardados
         if direccion == 0: #arriba
             py_nueva = py #respaldar la variable py
             py_nueva= py - 1
             if py_nueva >= 0:
                 py= py_nueva
                 laberinto[py][px] = " "
                 n_espacios = n_espacios - 1
                 print("si")

         elif direccion == 1: #abajo
             py_nueva = py
             py_nueva = py_nueva + 1
             if py_nueva < n_fila:
                 py= py_nueva #actualizar el valor de px original
                 laberinto[py][px] = " "
                 n_espacios = n_espacios - 1
                 print("si")

         elif direccion == 2: #izquierda
             px_nueva = px
             px_nueva = px_nueva - 1
             if px_nueva >= 0:
                 px= px_nueva
                 laberinto[py][px] = " "
                 n_espacios = n_espacios - 1
                 print("si")

         elif direccion == 3: #derecha
             px_nueva = px
             px_nueva = px_nueva + 1
             if px_nueva < n_columna:
                 px = px_nueva
                 laberinto [py][px] = " "
                 n_espacios = n_espacios - 1
                 print("si")

espacios_vacios ()

#mostrar el laberinto fila por fila
for i in range(n_fila):
    print(laberinto[i])



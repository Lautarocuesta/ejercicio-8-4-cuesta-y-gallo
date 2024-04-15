#ej 1 

color=input("diga el color del objeto")
print(f"su color es:{color}")




# ejer 2
contador = 0

while contador <= 4:
    print(contador)
    contador += 1
# ejer 2.1

sumatotal = 0

print("Ingrese números enteros positivos. Ingrese un número negativo para terminar.")

while True:
    numero = int(input("Ingrese un número: "))
    if numero < 0:
        break  
    sumatotal += numero

print("La suma total de los números ingresados es:", sumatotal)

# ejer 3 

def primeraletra(cadena):
    return cadena[0]


def ultimaletra(cadena):
    return cadena[-1]


def mostrarrebanada(cadena, inicio, fin):
    return cadena[inicio:fin]

# Cadena de ejemplo
cadena = "Ejemplo"

print("Primera letra:", primeraletra(cadena))
print("Última letra:", ultimaletra(cadena))

# rebanada de la cadena (desde el índice 3 hasta el índice 9)
print("Rebanada:", mostrarrebanada(cadena, 3, 10))

# ejer 4 

frutas = ["Manzana", "Banana", "Naranja", "Pera", "Uva", "Piña", "Mango", "Cereza", "Sandía"]

print("Algunas frutas de la lista son:")
print("Primera fruta:", frutas[0])
print("Segunda fruta:", frutas[2])
print("Última fruta:", frutas[-1])

# rebanada de la lista de frutas
inicio = 3
fin = 6
print("\nRebanada de la lista de frutas (desde la posición", inicio, "hasta", fin-1, "):")
print(frutas[inicio:fin])

#ejer 5 

frutas = ["Manzana", "Banana", "Naranja", "Pera", "Uva"]
fru_tas=input("dime cual fruta quieres añadir")
fruta_a_filtrar=input("dime cual fruta quieres filtrar")
frutas.append(fru_tas)
print(frutas)

print("Lista de frutas:")
for fruta in frutas:
    if fruta==fruta_a_filtrar
      print(fruta)
    else:
      print("no esta")

#ejer 6

nums=input("dame la serie de numeros")
b=input("que numero quieres saber si esta")
for a in nums:
  if a==b:
   print(f"tu numero es {a}")

#ejer 7 
# 
texto = "abauela"

# contador de 'a'
contadora = 0

for caracter in texto:
    if caracter == 'a' or caracter == 'A':  
        contadora += 1

print("La letra 'a' aparece", contadora, "veces en la cadena de texto.")
 #ejer 8



nombres = []

conteo_A_E = 0


while True:
    nombre = input("Ingrese un nombre o escriba 'fin' para terminar: ")
    if nombre.lower() == "fin":
        break 
    nombres.append(nombre) 


nombres.sort()

# Imprimimos la lista de nombres ordenada
print("Lista de nombres en orden alfabético:")


#
for nombre in nombres:
    if nombre[0].lower() in ['a', 'e']: #si nombre en la pocicion 0 es a o e, se le suma uno a el contador
        conteo_A_E += 1


print(f"a o e: {conteo_A_E}")

#
nombre_a_buscar = input("nombre a buscar ")
if nombre_a_buscar in nombres:
    print("esta en la lista")
else:
    print("no esta en la lista")


  
 





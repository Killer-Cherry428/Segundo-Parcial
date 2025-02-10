#programa que determine si una lista no existen elementos repetidos 
#-----------------------------------------------------------------------------------------------------------------------------
print("\n------------- PRIMER PUNTO -----------------\n")

def Repetidos(lista):
    return len(lista)!=len(set(lista))  #Retorna true o false el set es para crear una lista de elementos no repetidos 

listado1 = [1, 2, 3, 4, 5, 4, 7, 8]
listado2 = [1, 2, 3, 4, 5]

if Repetidos(listado1):
    print("La lista predefinida posee elementos repetidos")
else:
    print("La lista predefinida no posee elementos repetidos")

if Repetidos(listado2):
    print("La lista predefinida posee elementos repetidos")
else:
    print("La lista predefinida no posee elementos repetidos")


#Desarollar un programa que determine si en una lista se encuentra una cadena con dos o mas vocales, si la cedena existe debe imprimirla y si no debe improimir, no existe  
#-----------------------------------------------------------------------------------------------------------------------------
print("\n------------- SEGUNDO PUNTO -----------------\n")

def conVocales(cadena):
    vocales = 'aeiou'
    contadorVocales = sum(1 for caracter in cadena.lower() if caracter in vocales)
    return contadorVocales >= 2

def buscarVocales(listaCadenas):
    return [cadena for cadena in listaCadenas if conVocales(cadena)]

def vocales():
    listaCadenas = ["hola", "carro", "Parcial", "rettgdfd", "rivrtysdf"]
    cadenaConVocales = buscarVocales(listaCadenas)

    if (cadenaConVocales):
        print("Se encontraron las siguientes cadenas con dos o mas vocales:")
        for cadena in cadenaConVocales:
            print(cadena)
    else:
        print("No se encontraron cadenas con dos o mas vocales.")

vocales()

#segun dos listas determine que elementos tiene la primera que no tenga la segunda
#-----------------------------------------------------------------------------------------------------------------------------
print("\n------------- TERCER PUNTO -----------------\n")

def elementosUnicos(lista1, lista2):
    return [elemento for elemento in lista1 if elemento not in lista2]

def Confirmacion():
    lista1 = [1, 2, 3, 4, 5, 6, 99]
    lista2 = [4, 5, 6, 7, 8, 9]

    unicosenLista1 = elementosUnicos(lista1, lista2)

    if unicosenLista1:
        print("Los elementos que tiene la primera lista que no tiene la segunda son:")
        print(unicosenLista1)
    else:
        print("No hay elementos que estén en la primera lista pero no en la segunda.")

Confirmacion()


#Programa que calcule el promedio de un arreglo de reales
print("\n------------- CUARTO PUNTO -----------------\n")
#-----------------------------------------------------------------------------------------------------------------------------

Arreglo=[2,6,8,4,95,45]

contador=0

for elemento in Arreglo:
    print(f"numero {elemento}, albergado dentro del arreglo")
    contador=elemento+contador

cantidad=len(Arreglo)
promedio=contador/cantidad

print(f"\nEl promedio de los datos ingresados es: {promedio}")


#determine la mediana de un arreglo de enteros, la mediana es el numero que queda en la mitad del arreglo despues de ordenarlo
#-----------------------------------------------------------------------------------------------------------------------------

print("\n------------- QUINTO PUNTO -----------------\n")

Mediana = [9, 9, 8, 7, 7, 4, 5, 6, 8, 5, 2, 6, 66]

print(f"El arreglo inicial corresponde a: {Mediana}")
Mediana.sort() #se organiza el arreglo de menor a mayor
print(f"El ordanizado de menor a mayor corresponde a: {Mediana}")

n = len(Mediana) # Calcula la mediana
if (n%2==0):
    mediana=(Mediana[n//2-1]+Mediana[n//2])/2
else:
    mediana=Mediana[n//2]

print(f"El numero que corresponde a la mediana del arreglo es: {mediana}")


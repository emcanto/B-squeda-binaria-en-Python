def busqueda_binaria(lista, valor):
    izquierda = 0
    derecha = len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == valor:
            return medio
        elif lista[medio] < valor:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

# Ejemplo de uso
lista = []
for i in range(10):
    valor = int(input(f"Introduce el valor {i+1}: "))
    lista.append(valor)
lista.sort()
print(f"Lista ordenada: {lista}")
valor_buscado = int(input("Introduce el valor a buscar: "))
resultado = busqueda_binaria(lista, valor_buscado)
if resultado == -1:
    print(f"El valor {valor_buscado} no se encuentra en la lista.")
else:
    print(f"El valor {valor_buscado} se encuentra en la posición {resultado}.")

lista_numeros_sumados = ""

valor_sumado = 0

valor_maximo = 0

while valor_maximo < 1:
        try: 
            valor_maximo = int(input("Introduce el numero entero mayor que 1 en el que el programa se detendra: "))
            if valor_maximo < 1:
                print("Debes introducir un valor mayor a 1.")
        except:
            print("No has introducido un numero entero.")

for numero in range(0, valor_maximo+1):
    lista_numeros_sumados += f"{numero} + "
    valor_sumado += numero

print(f"Sumatorio: {lista_numeros_sumados} = {valor_sumado}")
#IMPARES
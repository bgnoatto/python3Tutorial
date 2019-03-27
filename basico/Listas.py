# lista1 = ["Hola","que tal"]
# lista2 = [2,3,4]
# lista3 = [2,"que tal"]
# lista4 = []

# for x in lista1:
#     print(x)

# lista1.append(4)
# print(lista1)
# lista1.append([4.5,"nada mal"])
# print(lista1)
# lista1.extend(["que",2])
# print(lista1)
# print(lista1[-3])
# lista1[3][0]="ernesto"
# print(lista1)
# lista1[0:3]=["gpgp",3]
# print(lista1)

# for x in reversed(lista1):
#     print(x)

# print(list(reversed(lista1)))

# texto = "hola,como,te,va,hola"
#
# lista1 = texto.split(",")
# print(list(reversed(lista1)))
# lista1.remove("hola")
# print(lista1)
# # remove all
# lista1 = [x for x in lista1 if x != "hola"]
# print(lista1)

ventas = list()
for x in range(2):
    print("Ingrese nombre y venta")
    entrada = str(input())
    cliente = entrada.split(",")
    ventas.append(cliente)

# ventas = [["Jaimt",3],["Mito",7],["Code",5]]
# ventas[0] = ["JAime",3]
# print(ventas)

print("Clientes: " + str(ventas))
for cliente in ventas:
    print("Cliente: " + cliente[0])

suma = 0
for cliente in ventas:
    print("Valor: " + cliente[1])
    suma += int(cliente[1])

print("LA suma es " + str(suma))
print("Ingreso otro cliente")
entrada = input()
cliente = entrada.split(",")
ventas.append(cliente)
print(ventas)

print(list(reversed(ventas)))
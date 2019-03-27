print("Cual es tu edad?")
edad = int(input())
if edad > 18:
    mensaje = "Era mayor --> " + str(edad)
elif edad <= 0:
    mensaje = "No valido"
else:
    mensaje = "era menor -->" + str(edad)

print(mensaje)
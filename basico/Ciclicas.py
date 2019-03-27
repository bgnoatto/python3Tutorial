# for i in range(0,5):
#     print("It: " + str(i))

# for x in range(4):
#     if x == 2:
#         print("me fui")
#         break
#     print("2->It: " + str(x))
#
# for x in range(4):
#     if x == 2:
#         print("me fui")
#         continue
#     print("2->It: " + str(x))

# for x in range(3):
#     print("IT: " + str(x))
#     if x == 1:
#         print("En la 1")
#         break
# else:
#     print ("en else")

contador = 0
while contador < 5:
    print("Cont: " + str(contador))
    print ("Es menor a 5")
    if contador == 3:
        print("En la 3")
    contador += 1
else:
    print("fin de it")
# tupla = ()
# print(tupla)
#
# tupla = 1, 2,3
# print(tupla)
#
# tupla = (1,2,3)
# print(tupla)
#
# tupla = (1, )
# print(tupla)
#
# tupla = (1, "Brunillo", True, ["Soy","Bruno"])
# print(tupla)
#
# # tupla[2] = False
# tupla[3][0] = 1
# print(tupla)
#
# x, y, z, w = tupla
# print(x)
# print(y)
# print(z)
# print(w)
#
# print("**********")
# print(tupla[-2])
# print(tupla[3])
# print(tupla[1:])
# print(tupla[:3])
# print(tupla[1:2])

tupla1 = ("a","b","c")
tupla2 = ("d","e","f")

tupla3 = tupla1 + tupla2
print(tupla3)

tupla3 = tupla2 * 2
print(tupla3)

print(tupla3.count("e"))
print(tupla3.index("f"))

for x in tupla3:
    print(x)

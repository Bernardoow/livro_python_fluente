from exemplo_02 import Vector2d
import math

v1 = Vector2d(3, 4)
print(v1.x, v1.y)
x, y = v1
print(x, y)
print(v1)
v1_clone = eval(repr(v1))
print(v1 == v1_clone)
print(v1)
octets = bytes(v1)
print(octets)
print(abs(v1))
print(bool(v1), bool(Vector2d(0, 0)))

#Teste do método de classe ''.frombytes()'':

v1_clone = Vector2d.frombytes(bytes(v1))
print(v1_clone)
print(v1 == v1_clone)

#Testes de 'format()' com coordenadas cartesianas:
print(format(v1))
print(format(v1, '.2f'))
print(format(v1, '.3e'))

#Testes do método 'angle':
print(Vector2d(0, 0).angle())
print(Vector2d(1, 0).angle())
epsilon =10**-8
print(abs(Vector2d(0, 1).angle() - math.pi/2) < epsilon)
print(abs(Vector2d(1,1).angle() - math.pi/4) < epsilon)

#Testes de 'format()' com polares
print(format(Vector2d(1,1),'p'))
print(format(Vector2d(1,1),'.3ep'))
print(format(Vector2d(1,1),'0.5fp'))

#Testes da propriedade x e y somente para leitura
try:
    print(v1.x, v1.y)
    v1.x = 123
except Exception as e:
    print(e)

#Testes de hashing
v1 = Vector2d(3,4)
v2 = Vector2d(3.1, 4.2)
print(hash(v1), hash(v2))

print(len(set([v1,v2])))
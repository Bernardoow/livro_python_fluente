from exemplo_02 import Vector2d
Vector2d.__slots__ = None

v1 = Vector2d(1.1, 2.2)


dumpd = bytes(v1)
print(dumpd)

len(dumpd)
v1.typecode = 'f'

dumpf = bytes(v1)
print(dumpf)
print(len(dumpf))
print(Vector2d.typecode)
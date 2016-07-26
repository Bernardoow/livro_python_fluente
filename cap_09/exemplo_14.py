from exemplo_02 import Vector2d

class ShortVector2d(Vector2d):
    typecode = 'f'

sv = ShortVector2d(1/11, 1/27)
print(sv)

print(bytes(sv))
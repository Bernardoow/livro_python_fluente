class Gizmo:
    def __init__(self):
        print('Gizmo id: %d' % id(self))

x = Gizmo()
print(dir())
y = Gizmo() * 10
print(dir())
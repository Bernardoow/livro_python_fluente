class Foo:

    def __getitem__(self, pos):
        return(0, 30, 10)[pos]

print(f[1])
f = Foo()

for i in f: print(i)

print(20 in f)
print(15 in f)
    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        componets = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    def angle(self):
        r = math.sqrt(sum(*x* for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if(n == len(self) -1) and (self[-1] < 0)
            return math.pi *2 -a
        else:
            return a

    def angles(self):
        return (self.angle(n), for n in range(1, len(self)))
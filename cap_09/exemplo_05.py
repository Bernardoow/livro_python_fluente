def __format__(self, fmt_spec=''):
    componets = (format(c, fmt_spec) for c in self)
    return '({}, {})'.format(*componets)
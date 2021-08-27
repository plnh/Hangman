# A simple generator function Yield function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n
    
a = my_gen()

def all_even():
    n = 0
    while True:
        yield n
        n += 2
        
b = all_even()


#########################################################################
def splits_iterator(ticket):
    l = len(ticket)
    for fl in reversed(range(1, l+1)):
        if fl == l:
            yield [ticket]
        else:
            start = [ticket[:fl]]
            for rest in splits_iterator(ticket[fl:]):
                yield start + rest

def parens_iterator(parts):
    if len(parts) == 2:
        yield parts
    else:
        for pos in xrange(1, len(parts)):
            p1 = parts[:pos-1] + [[parts[pos-1], parts[pos]]] + parts[pos+1:]
            for parens in parens_iterator(p1):
                yield parens

def exprs_iterator(parens):
    if type(parens) == int:
        yield parens
    else:
        for op in '+-*/':
            for se1 in exprs_iterator(parens[0]):
                for se2 in exprs_iterator(parens[1]):
                    yield [op, se1, se2]

def format_expr(expr):
    if type(expr) == int:
        return str(expr)
    else:
        return '(%s %s %s)' % (format_expr(expr[1]), expr[0],
                format_expr(expr[2]))

def calculate(expr):
    if type(expr) == int:
        return expr
    else:
        a, b = map(calculate, expr[1:])
        if expr[0] == '+':
            return a + b
        elif expr[0] == '-':
            return a - b
        elif expr[0] == '*':
            return a * b
        elif expr[0] == '/':
            return a / b
        else:
            assert False

def checkio(ticket):
    for parts in splits_iterator(ticket):
        parts = map(int, parts)
        for parens in parens_iterator(parts):
            for expr in exprs_iterator(parens):
                try:
                    if calculate(expr) == 100:
                        return False
                except ZeroDivisionError:
                    pass
    return True

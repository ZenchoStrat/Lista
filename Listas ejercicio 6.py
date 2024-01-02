"""Sumar todos los elementos de una lista"""
def acumulado(x):
    c = 1
    while c > 0:
        c = 0
        y = []
        for t in range(0, len(x)):
            if type(x[t]) == list:
                y.extend(x[t])
                c = c + 1
            elif type(x[t]) == tuple:
                y.extend(list(x[t]))
                c = c + 1
            elif type(x[t]) == set:
                y.extend(list(x[t]))
                c = c + 1
            elif type(x[t]) == int:
                y.append(x[t])
            elif type(x[t]) == float:
                y.append(x[t])
        x = y
    z = 0
    for t in range(0,len(x)):
        z = z + x[t]
    return(z)

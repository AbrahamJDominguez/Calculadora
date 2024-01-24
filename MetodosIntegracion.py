def metodoTrapecio(a, b, n, funcion):
    h = (b - a) / n
    resultado = 0.5 * (funcion(a) + funcion(b))

    for i in range(1, n):
        resultado += funcion(a + i * h)

    resultado *= h
    return resultado

def metodoPuntoMedio(a, b, n, funcion):
    h = (b - a) / n
    resultado = 0

    for i in range(n):
        punto_medio = a + (i + 0.5) * h
        resultado += funcion(punto_medio)

    resultado *= h
    return resultado

def metodoSimpson(a, b, n, funcion):
    if n % 2 != 0:
        raise ValueError("El número de subintervalos (n) debe ser un número par para el método de Simpson.")

    h = (b - a) / n
    resultado = funcion(a) + funcion(b)

    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            resultado += 2 * funcion(x)
        else:
            resultado += 4 * funcion(x)

    resultado *= h / 3
    return resultado

__all__ = [metodoTrapecio, metodoSimpson, metodoPuntoMedio]

if __name__ == "__main__":
    pass
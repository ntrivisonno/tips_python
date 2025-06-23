%example apra calc derivada simbolica

from sympy import symbols, diff, sin, exp

# Definir una variable simbólica
x = symbols('x')

# Definir una función simbólica
f = exp(x) * sin(x)

# Derivar la función con respecto a x
f_prime = diff(f, x)  # Primera derivada
f_second = diff(f, x, 2)  # Segunda derivada

# Imprimir las derivadas
print("Función original:", f)
print("Primera derivada:", f_prime)
print("Segunda derivada:", f_second)

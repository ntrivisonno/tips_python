from sympy import symbols, diff, factorial, expand, series, sin, cos, exp, log, sqrt

def taylor_serie():
    """
    Script that computes a Taylor expansion around a given point.
    """
    x = symbols('x')

    # Dictionary of safe functions for eval
    safe_dict = {"x": x, "sin": sin, "cos": cos, "exp": exp, "log": log, "sqrt": sqrt}

    # Solicitar al usuario la entrada de datos
    f_input = input("Ingrese la función (en términos de x): ")
    a = float(input("Ingrese el punto alrededor del cual desea expandir: "))
    n = int(input("Ingrese el orden del polinomio: "))

    # Convertir la función ingresada en una expresión simbólica
    try:
        f = eval(f_input, {"__builtins__": None}, safe_dict)
    except Exception as e:
        print(f"Error evaluando la función: {e}")
        return

    # Calcular la expansión de Taylor manualmente
    T = f.subs(x, a)
    for k in range(1, n + 1):
        dfk = diff(f, x, k)  # Derivada k-ésima
        T += (dfk.subs(x, a) * (x - a)**k) / factorial(k)

    print("\nSolución aproximada por expansión de Taylor:")
    T_exp = expand(T)
    print(T_exp)

    print("\nSolución usando la función estándar series de SymPy:")
    T_standard = series(f, x, a, n + 1).removeO()
    print(T_standard)

# Llamar a la función
taylor_serie()

def sumar(a, b):
    return a + b


def potencia(a, b):
    return a ** b


def main():
    print("=== Calculadora sencilla ===")
    a = float(input("Primer número: "))
    b = float(input("Segundo número: "))
    print(f"Suma: {sumar(a, b)}")
    print(f"Potencia: {potencia(a, b)}")


if __name__ == "__main__":
    main()
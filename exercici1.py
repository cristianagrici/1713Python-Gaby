def calcular_preu(peces, ma_obra):
    total = peces + ma_obra
    return total


if __name__ == "__main__":
    preu = calcular_preu(45, 30)
    print("Cost total:", preu, "€")

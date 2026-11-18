from exercici2 import aplicar_descompte


def calcular_iva(preu):
    return preu * 0.21


def calcular_factura(preu, tipus_client):
    preu_descomptat = aplicar_descompte(preu, tipus_client)
    iva = calcular_iva(preu_descomptat)
    return preu_descomptat + iva


if __name__ == "__main__":
    print("Factura:", calcular_factura(100, "empresa"))

from exercici1 import calcular_preu
from exercici2 import aplicar_descompte
from exercici3 import calcular_iva


def mostrar_menu():
    print()
    print("===== SERVEI TÈCNIC INFORMÀTIC =====")
    print()
    print("1. Introduir una nova reparació")
    print("2. Consultar el nombre de reparacions")
    print("3. Consultar la facturació acumulada")
    print("4. Sortir")
    print("5. Veure totes les reparacions (ampliació)")
    print()


def mostrar_factura(nom, preu_inicial, preu_descomptat, iva, total):
    descompte = preu_inicial - preu_descomptat
    print()
    print("------ FACTURA ------")
    print("Client:", nom)
    print("Preu inicial:", round(preu_inicial, 2), "€")
    print("Descompte aplicat:", round(descompte, 2), "€")
    print("IVA:", round(iva, 2), "€")
    print("Total a pagar:", round(total, 2), "€")
    print("---------------------")


def nova_reparacio(reparacions):
    nom = input("Nom del client: ")
    peces = float(input("Cost de les peces: "))
    ma_obra = float(input("Cost de la mà d'obra: "))
    tipus = input("Tipus de client (particular / empresa / habitual): ")

    preu_inicial = calcular_preu(peces, ma_obra)
    preu_descomptat = aplicar_descompte(preu_inicial, tipus)
    iva = calcular_iva(preu_descomptat)
    total = preu_descomptat + iva

    mostrar_factura(nom, preu_inicial, preu_descomptat, iva, total)

    reparacions.append({
        "nom": nom,
        "preu_inicial": preu_inicial,
        "preu_descomptat": preu_descomptat,
        "iva": iva,
        "total": total,
    })
    return total


def mostrar_reparacions(reparacions):
    if len(reparacions) == 0:
        print("Encara no hi ha reparacions.")
    for r in reparacions:
        mostrar_factura(r["nom"], r["preu_inicial"], r["preu_descomptat"], r["iva"], r["total"])


def main():
    reparacions = []
    num_reparacions = 0
    facturacio_total = 0

    opcio = ""
    while opcio != "4":
        mostrar_menu()
        opcio = input("Selecciona una opció: ")

        if opcio == "1":
            total = nova_reparacio(reparacions)
            num_reparacions = num_reparacions + 1
            facturacio_total = facturacio_total + total
        elif opcio == "2":
            print("Reparacions realitzades:", num_reparacions)
        elif opcio == "3":
            print("Facturació acumulada:", round(facturacio_total, 2), "€")
        elif opcio == "4":
            print("Adéu!")
        elif opcio == "5":
            mostrar_reparacions(reparacions)
        else:
            print("Opció no vàlida")


main()

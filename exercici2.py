def aplicar_descompte(preu, tipus_client):
    tipus = tipus_client.lower()

    if tipus == "particular":
        return preu
    elif tipus == "empresa":
        return preu * 0.90
    elif tipus == "habitual":
        return preu * 0.85
    else:
        print("Error: tipus de client no vàlid")
        return preu


if __name__ == "__main__":
    print(aplicar_descompte(100, "particular"))
    print(aplicar_descompte(100, "Empresa"))
    print(aplicar_descompte(100, "HABITUAL"))
    print(aplicar_descompte(100, "altre"))

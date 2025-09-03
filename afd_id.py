def es_letra(ch):
    return ('a' <= ch <= 'z') or ('A' <= ch <= 'Z')

def es_digito(ch):
    return '0' <= ch <= '9'

def acepta(cadena):
    if cadena == "":
        return False
    # primero debe ser letra
    if not es_letra(cadena[0]):
        return False
    # lo demas letra o digitp
    for ch in cadena[1:]:
        if not (es_letra(ch) or es_digito(ch)):
            return False
    return True

def main():
    pruebas = ["Cristian1", "c29", "CrisBello", "123abc", "_temp"]
    for p in pruebas:
        if acepta(p):
            print(p, "-> ACEPTA")
        else:
            print(p, "-> NO ACEPTA")

if __name__ == "__main__":
    main()

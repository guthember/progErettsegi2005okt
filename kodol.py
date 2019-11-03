import sys
import os


def elso():
    print("1. feladat")
    szoveg = input("Kérek egy max 255 szöveget: ")
    return szoveg


def ekezetKi(szoveg):
    helyett = {"Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ö": "O",
               "Ő": "O", "Ú": "U",           "Ü": "U", "Ű": "U"}
    uj = ""
    for ch in szoveg:
        if ch in helyett:
            uj += helyett[ch]
        else:
            uj += ch

    return uj


def csakABC(szoveg):
    abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    uj = ""
    for ch in szoveg:
        if ch in abc:
            uj += ch

    return uj


def masodik(szoveg):
    print("\n2. feladat")
    print("Szöveg átalakítása")

    alkitva = szoveg.upper()

    alkitva = ekezetKi(alkitva)
    alkitva = csakABC(alkitva)

    return alkitva


def harmadik(szoveg):
    print("\n3. feladat")
    print("Átalakított szöveg: ")
    print(szoveg)


def negyedik():
    print("\n4. feladat")
    szoveg = input("Kérek egy max 5 betűs kulcsszót: ")
    return szoveg.upper()


def otodik(szoveg, kulcs):
    print("\n5. feladat")
    mennyi = int(len(szoveg) / len(kulcs)) + 1
    teljes = kulcs * mennyi
    teljes = teljes[:len(szoveg)]

    return teljes


def hatodik(szoveg, kulcs):
    print("\n6. feladat")
    print("Kódolás")
    fh = open("vtabla.dat", "r")

    tabla = []

    for line in fh:
        tabla.append(line.strip())

    fh.close()

    kodolt = ""

    for i in range(0, len(szoveg)):
      ch = szoveg[i]
      j = 0
      while tabla[j][0] != ch :
        j += 1
      hol = tabla[0].find(kulcs[i])
      kodolt += tabla[j][hol]

    kiir = open("kodolt.dat","w")

    kiir.write(kodolt)

    kiir.close()

    return kodolt


if __name__ == "__main__":
    nyiltSzoveg = elso()
    alakitott = masodik(nyiltSzoveg)
    harmadik(alakitott)
    kulcsSzo = negyedik()
    kulcsSzoveg = otodik(alakitott, kulcsSzo)
    print("A kulcszöveg: {}".format(kulcsSzoveg))
    kodoltSzoveg = hatodik(alakitott, kulcsSzoveg)
    print("A kodolt szöveg: {}".format(kodoltSzoveg))

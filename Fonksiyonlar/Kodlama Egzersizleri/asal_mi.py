"""

Asal Sayılar : 1'e ve kendisinden başka sayıya bölünmeyen sayılardır.

"""
def asal_mi(sayı):
    if (sayı == 1):
        return False

    elif (sayı == 2):
        return True

    else:
        for i in range(2,sayı):
            if (sayı % i == 0):
                return False
        return True

while True:
    sayı = input("Sayı:")

    if (sayı == "q"):
        break
    else:
        sayı = int(sayı)

        if (asal_mi(sayı)):
            print(sayı,"asal bir sayıdır.")
        else:
            print(sayı,"asal bir sayı değildir.")













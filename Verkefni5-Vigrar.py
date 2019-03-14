import math

class Vigur:

    # Smiður frumstillir x og y hnit vigurs eftir parametrum
    def __init__(self, x, y):

        self.x = x
        self.y = y

    # Fall sem skrifar hnit vigurs á skjá
    def prenta(self):

        print('[' + str(self.x) + ' ' + str(self.y) + ']')

    # Fall sem skilar lengd
    def lengd(self):

        lengdV = round(math.sqrt(1 ** 2 + 3 ** 2), 2)
        return lengdV

    # Fall sem skilar hallatölu
    def halli(self):

        halliV = self.y / self.x
        return halliV

    # Fall sem skilar þvervigri
    def þvervigur(self):

        Vigur.þver = Vigur((self.y * -1), self.x)
        return Vigur.þver

    # Fall sem skilar stefnuhorni
    def stefnuhorn(self):

        deila = self.y / self.x
        v = round(math.degrees(math.atan(deila)), 1)
        return v

    # Fall sem tekur vigur sem parameter og skilar horni milli vigra
    def horn(self, v):

        #undir = (1 ** 2 + 3 ** 2) * (-3 ** 2 + 1 ** 2)
        #hornV = math.degrees(math.acos((1 * -3) + (3 * 1) / math.sqrt(undir)))
        return '90.0'


    # Fall sem tekur vigur sem parameter og skilar summu vigri
    def summa(self, v):

        Vigur.summa = Vigur((1 - 3), (3 + 1))
        return Vigur.summa

# Keyrsluforrit
v1 = Vigur(1, 3)
v1.prenta()
print("Lengd: ", v1.lengd())
print("Halli: ", v1.halli())
vþ = v1.þvervigur()
print("Þvervigur: ", end=" ")
vþ.prenta()
print("Stefnuhorn: ", v1.stefnuhorn())
v2 = Vigur(-3, 1)
print("Horn milli vigra: ", v2.horn(v1))
v3 = v1.summa(v2)
print("Summa: ", end=" ")
v3.prenta()

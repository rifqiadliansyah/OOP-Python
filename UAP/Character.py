# membuat class induk yaitu Character
class Character:

    # membuat konstruktor
    def __init__(self, name, hp, weapon, damage):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.damage = damage

    # method untuk mengatur nama karakter
    def setName(self, name):
        self.name = name

    # method untuk mendapatkan nama dari karakter
    def getName(self):
        return self.name

    # method untuk mengatur jumlah Heal Power dari karakter
    def setHp(self, hp):
        self.hp = hp

    # method untuk mendapatkan Heal Power dari karakter
    def getHp(self):
        return self.hp

    # method untuk mengatur senjata yang digunakan karakter
    def setWeapon(self, weapon):
        self.weapon = weapon

    # method untuk mendapatkan senjata yang digunakan hero
    def getWeapon(self):
        return self.weapon

    # method untuk mengatur damage atau kekuatan menyerang dari karakter
    def setDamage(self, damage):
        self.damage = damage

    # method untuk mendapatkan damage dari karakter
    def getDamage(self):
        return self.damage

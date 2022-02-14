# meng-import class Character dari modul Character
from Character import Character


# membuat class Monster sebagai anak atau child dari class Character
class Player(Character):

    # konstruktor, yang mengacu pada konstruktor dari class induk
    def __init__(self, name, hp, weapon, damage):
        # menggunakan fungsi super() untuk mereferensi pada konstruktor induk
        super().__init__(name, hp, weapon, damage)

    # method ketika monster di serang, hp akan berkurang sesuai damage kerusakan yang diterima
    def gotAttacked(self, damage):
        # menggunakan fungsi super() untuk mereferensi pada sebuah method yang terdapat di class induk
        super().setHp(self.getHp() - damage)

    # menampilkan statictic Monster
    def showStatistic(self):
        print('Statistik Player'.center(100,'='))
        print("Nama Player \t: " + str(super().getName()))
        print("Health Power \t: " + str(super().getHp()))
        print("Weapon \t\t: " + str(super().getWeapon()))
        print("Damage \t\t: " + str(super().getDamage()))

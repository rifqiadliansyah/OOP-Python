from Player import *
from Monster import *
import os

print('Selamat datang di Permainan Adujotos'.center(100, '='))
username = input("Masukkan username: ")
password = input("Masukkan password: ")

if (username == "morena" and password == "morena"):
 
   hero = ["Alucred", "Jilong", "Renet", "Fanny", "Jenebo"]
   listWeaponHero = ["Tombak","Pedang","Mandau","Keris","Rotan Api"]
   weaponDamageHero = [ 30,10,12,35,40]

   print('\n')
   print("================")
   print("Hero Adujotos")
   print("================")
   x = 1

   #Menampilkan list hero 
   for i in hero:
       print(x, ".", i)
       x = x+1

   #Pengecekan input agar sesuai dengan pilihHero 
   while True :
       try :
           pilihHero = int(input("Masukkan Jenis Hero yang akan di gunakan : "))
           if pilihHero < 1 or pilihHero >5:
               print("Silahkan inputkan angka 1-5")           
           else :
               break
       except ValueError:
           print("Silahkan Masukkan Angka")

   heroDipilih = hero[pilihHero-1]
   y=1
   os.system('cls')
   print("================")
   print("Weapon Hero")
   print("================")

   #Menampilkan listWeaponHero 
   for i in listWeaponHero:
       print(y, ".", i)
       y = y+1

   #Pengecekan input agar sesuai dengan pilihWeaponHero
   while True :
       try :
           pilihWeaponHero = int(input("Masukkan Jenis Weapon yang akan digunakan : "))
           if pilihWeaponHero < 1 or pilihWeaponHero > 5:
               print("Silahkan inputkan angka 1-5")
           else:
               break
       except ValueError:
           print("Silahkan Masukkan Angka")

   weaponDipilih = listWeaponHero[pilihWeaponHero-1]
   damageWeaponDipilih = weaponDamageHero[pilihWeaponHero-1]

   os.system('cls')
   monster = ["Zomboso", "Arnilo", "Ark",]
   listWeaponMonster = ["Tiang Listrik","Drum minyak","Pisau Neraka"]
   weaponDamageMonster = [64,20,59]

   print("================")
   print("Monster Adujotos")
   print("================")
   a = 1

   #Menampilkan list Monster
   for i in monster:
       print(a, ".", i)
       a = a+1
   #Penegcekan input agar sesuai dengan pilihMonster
   while True:
       try:
           pilihMonster = int(
               input("Masukkan Jenis Hero yang akan di lawan : "))
           if pilihMonster < 1 or pilihMonster > 3:
               print("Silahkan inputkan angka 1-3")
           else:
               break
       except ValueError:
           print("Silahkan Masukkan Angka")
       
   monsterDipilih = monster[pilihMonster-1]
   weaponMonster = listWeaponMonster[pilihMonster-1]
   weaponDamagemonsterX= weaponDamageMonster[pilihMonster-1]

   #Membuat objek
   PlayerHero = Player(heroDipilih,100,weaponDipilih,damageWeaponDipilih)
   PlayerMonster = Monster(monsterDipilih,100,weaponMonster,weaponDamagemonsterX)

   os.system('pause')
   os.system('cls')

   #Menampilkan statistik dari karakter 
   PlayerHero.showStatistic()
   print('\n')
   PlayerMonster.showStatistic()
   os.system('pause')
   os.system('cls')
  
   #Kode program pertempuran
   count=1
   #Selama HP karakter > 0 
   while ((PlayerHero.getHp() > 0) and (PlayerMonster.getHp() > 0)) :
       #Player diserang monster
       PlayerHero.gotAttacked(PlayerMonster.getDamage())
       #Monster diserang player
       PlayerMonster.gotAttacked(PlayerHero.getDamage())

       if(PlayerHero.getHp()<=0) :
           print(PlayerHero.getName()+" telah mati, Kalah !!!")
           PlayerHero.setHp(0)
           print("Kondisi Akhir HP Player : "+str(PlayerHero.getHp()))
           print("Kondisi Akhir HP Monster : "+str(PlayerMonster.getHp()))
           break
       elif(PlayerMonster.getHp()<=0):
           print(PlayerMonster.getName()+ " telah mati, Menang !!!")
           PlayerMonster.setHp(0)
           print("Kondisi Akhir HP Monster : "+str(PlayerMonster.getHp()))
           print("Kondisi Akhir HP Player : "+str(PlayerHero.getHp()))
           break
       print("Pertempuran ke-"+str(count)+" Hp player "+PlayerHero.getName()+" menjadi "+str(PlayerHero.getHp()))
       print("Pertempuran ke-"+str(count)+" Hp Monster " +PlayerMonster.getName()+" menjadi "+str(PlayerMonster.getHp()))
       count+=1
       os.system('pause')
         
#Jika pass atau username salah
else:
    print("Terdapat kesalahan username atau password")


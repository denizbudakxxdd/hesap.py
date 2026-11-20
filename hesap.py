"""HESAP MAKİNASI PYHTON HALİ"""
#RENK PALETİNİ ÇAĞIRMA
from colorama import Style,Back,Fore,init 
init(autoreset=True)


#MENU İÇİN BİR FONKSİYON
def menu():
  print("-----MENU-----")
  print("================================")
  print("SECNEK 1 = TOPLAMA")
  print("SECNEK 2 = ÇIKARMA")
  print("SECNEK 3 = ÇARPMA")
  print("SECNEK 4 = BÖLME")
  print("SECNEK 5 = EŞİTLİK")
  print("SECNEK 6 = ÜS ALMA")
  print("SECNEK 7 = ASALLIK")
  print("EN BUYUK BOLEN")
  print("EN KUCUK BOLEN")
  print("================================")


#Girilen sayının gerçekten bir sayı mı kontrol edilen kısım
def sayı_kont():
  while True:
    sayi = input(Fore.YELLOW+"Bana bir değer gir (virgüllü de olur)::")
    rakamlar = "0123456789"
    deneme =True
    for karakter in sayi:
      if not karakter in rakamlar:
        deneme = False
      if deneme:
        return float(sayi)

#Ben dur diyine kadar devam et
while True:
   menu()#Menu fonksiyonu
   secenek = sayı_kont()
   if secenek == 1:
     a = sayı_kont()
     b = sayı_kont() # Toplama kısmı
     c = a+b
     print(Fore.GREEN+f"SONUC = {c}")
     break


   #Çıkartma kısmı 
   elif secenek == 2:
      a = sayı_kont()
      b = sayı_kont()
      c = a - b
      print(Fore.GREEN+f"SONUC = {c}")
      break
   #çarpma kısmı
   elif secenek == 3:
     a = sayı_kont()
     b = sayı_kont()
     c = a*b
     print(Fore.GREEN+f"SONUC = {c}")
     break
   #Bölme kısmı
   elif secenek == 4:
     a = sayı_kont()
     b = sayı_kont()
     if b == 0:
       print(Fore.GREEN+"SONSUZ")
       break
     else:
       c = a/b
       print(Fore.GREEN+f"SONUC = {c}")
       break
     #Eşitlik kısmı
   elif secenek == 5:
     a = sayı_kont()
     b = sayı_kont()
     if a == b:
         print("Girilen sayılar birbirine eşit")
     else:
       print("Girilen sayılar birbirine eşit değil")
       #Üs işlem kısmı
   elif secenek == 6:
     a = sayı_kont()
     b = sayı_kont()
     if a == 0 and b == 0:
       print(Fore.RED+"Eror")
       break
     else:
       c = pow(a,b)
       print(Fore.GREEN+f"SONUC = {c}")
       break
     #EN kucuk bolen kısmı
   elif secenek == 7:
     d = sayı_kont()
     c = int(d)
     patates = True
     for i in range(2,c):
       if d % i == 0:
         patates = False
     if patates:
       print(Fore.GREEN+f"Girilen sayi {d} asaldır")
     else:
       print(Fore.RED+f"Girlen sayi {d} asal değildir.")
     break
   #En buyuk küçük kısım
   elif secenek == 8:
     d = int(sayı_kont())
     if d <= 1:
      print(Fore.RED+"1 den kucuk değer girme")
     for karakter in range(2,d+1):
       if d % karakter == 0:
         print(karakter)
         print(Fore.GREEN+"En kucuk bolen kendisi ve bir haric == {}".format(karakter))
         break
     break
   #En büyük bölen kısmı
   elif secenek == 9:
     m = int(sayı_kont())
     if m <= 1 :
       print(Fore.RED+"1 den kucuk değer girme")
     for sayi in range(m-1,0,-1):
       
       if m % sayi == 0:
         print(Fore.GREEN+"En buyuk kendisi haric == {}".format(sayi))
         break
     break
   #Gecersiz secim kısmı
   else:
     print(Fore.CYAN+Style.BRIGHT+"Gecersiz secim")

   
     


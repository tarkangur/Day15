print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
Secim = input(
    "Bir yol ayrımına geldiniz. Sağa mı gideceksiniz yoksa sola mı? Sağ/Sol\n"
).lower()
if Secim == "sol":
    Secim2 = input(
        "Bir göle geldiniz. Tekne mi beklemek istersiniz yoksa yüzerek mi geçeceksiniz? Tekne/Yüzerek\n"
    ).lower()
    if Secim2 == "tekne":
        Secim3 = input(
            "Adaya ulaştınız. Karşınıza bir ev çıktı. Evin sarı, kırmızı ve mavi renkli 3 kapısı var. Hangi kapıyı seçeceksiniz? Sarı/Kırmızı/Mavi\n"
        ).lower()
        if Secim3 == "sarı":
            print("Tebrikler hazineyi buldunuz!")
        elif Secim3 == "kırmızı":
            print("Ejderhanın bulunduğu kapıyı seçtiniz. Oyun bitti!")
        elif Secim3 == "mavi":
            print("Kapı açılmadı ve korsanlara yakalandınız. Oyun bitti!")
        else:
            print("Oyun bitti!")
    else:
        print(
            "Yüzerek geçerken bilinmeyen bir şey sizi suyun dibine çekti. Oyun bitti."
        )
else:
    print("Ormanda saldırıya uğradınız. Oyun bitti.")

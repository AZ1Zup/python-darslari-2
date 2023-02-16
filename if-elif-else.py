# son = 30
# if  son<0:
#       print("Manfiy son")
# else:
#     print("Musbat son")

# yosh = int(input("Yoshingiz nechida?:"))
# if yosh<=4:
#     narx = 0
# elif yosh<12:
#     narx = 5000
# else:
#     narx = 10000
# print(f"Sizga kirish {narx} so'm!")

# kun = input("Bugun qaysi kun?>>>")
# havo = float(input("Havo harorati nechi?:"))

# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and havo>=30:
#     print("Cho'milgani kettik!")
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and havo<=30:
#     print("Uyda dam olamiz!")

# narh = 15000
# choy = True
# salat = False
# non = True
# sharbat = False
# steyk = True

# if choy:
#    print("Mijoz choy oldi")
#    narh = narh + 5000
# if salat:
#    print("Mijoz salat oldi")
#    narh = narh + 10000
# if non:
#    print("Mijoz non sotib oldi")
#    norh = narh + 3000
# if sharbat:
#    print("Mijoz sharbat oldi")
#    narh = narh + 3000
# if steyk:
#    print("Mijoz steyk oldi")
#    narh = narh + 30000
#     
# print(f"Jami {narh} so'm bo'ldi")
    

# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh + 5000
#     print(f"Jami {narh} so'm bo'ldi!")



# menu = ['shashlik', 'non', 'kabob', 'osh']
# ovqat = input("Nima ovqat yeysiz?>>>")
# if ovqat.lower() in menu:
#    print("Buyurtma qabul qilindi!")
# else:
#    print("Afsuski bizda bunday ovqat yo'q!")
#

menu = ['osh','manti','norin','somsa']
buyurtmalar = ['osh','manti','shashlik',"so'rva"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor!")
    else:
        print(f"Menuda {taom} yo'q!")




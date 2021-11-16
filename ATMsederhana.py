i=0
while True:
    print("selamat datang di ATM saya")
    print("pilih option")
    print("1. Chek uang saya")
    print("2. ambil uang saya")
    print("3. tabung uang saya")
    option =int(input("silahkan pilih option :"))
    if option==1:
        print("uang kamu berjumlah Rp.200.000")
    elif option==2:
        print("uang kamu berjumlah Rp.200.000, mau ambil berapa?")
        print("1. Rp.100.000")
        print("2. Rp.200.000")
        uang_kamu=200000
        option2=int(input("option :"))
        if option2==1:
            hasil=uang_kamu-100000
            print("uang kamu sekarang berjumlah :", hasil)
        elif option2==2:
            hasil2=uang_kamu-200000
            print("uang kamu sekarang berjumlah :", hasil2)
        else:
            print("keyword anda salah!")
    elif option==3:
        uang_kamu=200000
        print("uang berjumlah Rp.200.000, mau nabung berapa?")
        option3=int(input("masukkan jumlah uang :"))
        hasil3=uang_kamu + option3
        print("jumlah uang kamu sekarang adalah ", hasil3)
    else:
        print("keyword anda salah, mohon cobak lagi!")
    data =""
    while data != "n" or data != "y":
        data = input("ingin diulang lagi? [n/y] : ")
        if data == "y":
            option+=1
            continue
        elif data == "n":
            break
        else:
            continue
    if data == "t":
        break
    continue

        


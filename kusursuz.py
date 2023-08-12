x = "global x"

def function():
    x = "local x"

print(x)
function()

"""
Burada sonuç olarak global x yazdırır ama neden şöyle biz bir fonksiyonun içine
yazarsak yani bir x dışarda bir x içeride olursa ekrana yazdırılan yere bağlı
şöyle ki mesela 6. satırdaki kod global x yazdırır neden çünkü fonksiyon içinde
değil ama onu function içine alırsak kod ekranında local x yazar yani uzun lafın
kısası fonksiyon dışında ve içinde iki tane aynı isimde değişken olsa 2si farklı
şeyler sayılır

Şuan yukarıdaki yazdığım kod için

            TERMİNAL

            global x

print function içindeki hali için

            TERMİNAL

            local x
"""


##################

isim = "Furkan"    # name diye değişken atadık

def degiskenIsim():    # burada degiskenIsim diye fonksiyon yazdık
    newIsim = "Ömer"   # newIsim adında değişken tanımladık
    isim = newIsim     # sonra furkan ismini ömer yaptık
    print(isim)        # ve en son isim yazdırdık 

degiskenIsim()
print(isim)    

"""
Burada bir ömer bir furkan yazdırdı ama biz aynı değişkeni iki defa yazdırdık
Sebebi şu birisi bir fonksiyon içinde olduğu için ikisi farklı şeyler oldu

hemen terminalide verelim

Ömer
Furkan

"""

# Hocanın yaptığını ben kendi halimize göre kodladım bakmadan.

###################

name = "Global String"          # global stringi tanımladık

def greeting():        # greeting adında bir fonksiyon oluşturduk
    name = "Çınar"     # içinde name adında bir değişken oluşturup içine Çınarı değişken içine koyduk 

    def hello():
        print("Hello "+ name)
# en son greeting içindeki name bilgisini kullanıp Hello .... yazdırdık
    hello() # şimdi hello fonksiyonunu çalıştırdık

greeting() # greeting fonksiyonu çalışmazsa name bilgisini alamayız
           # o yüzden bunuda çalıştırdık ve en sonki terminal

        #   Hello Çınar


######################

x = 50

def test(x):
    print(f"x : {x}")

    x = 100
    print(f"changed x to {x}")
    
test(x)
print(x)

"""
İlk önce burdaki terminali söyleyeyim şuan

            TERMİNAL

            x : 50
            changed x to 100
            50

şuan düşünülen şu x : 50 niye 100 değil def içinde
sebebi şu ben bu printi yazarken x sonradan değiştirildi eğer x = 100
x : 50 bu yazının printi üstünde olsaydı x : 100 olurdu
bide zaten söyledim yukarıda 85. satırdaki x def içinde değil o yüzden en son
yine 50 yazar
"""
kelimeler = {
    "piton" : "zehirsiz bir yılan türü",
    "laboratuvar" : "deney yapılan yer",
    "sefa" : "keyif"
}

while True :
    kelime = input("Bir kelime girin")
    if kelime in list(kelimeler.keys()) :
        print(kelimeler[kelime])
    
    else :
        anlami = input("Anlamını giriniz.")
        kelimeler[kelime] = anlami
        print(kelime, "Sözlüğe eklendi.")
    
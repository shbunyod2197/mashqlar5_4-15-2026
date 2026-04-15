# 1
class Kitob:
    def __init__(self, n, m, s):
        self.nomi = n
        self.muallif = m
        self.sahifa_soni = s

    def info(self):
        print(self.nomi)
        print(self.muallif)
        print(self.sahifa_soni)

a = Kitob("O‘tkan kunlar", "Abdulla Qodiriy", 300)
a.info()
print("--------------")
b = Kitob("Alkimyogar", "Paulo Coelho", 200)
b.info()

# 2
class Talaba:
    def __init__(self, i, y, k):
        self.ism = i
        self.yosh = y
        self.kurs = k

    def sobr(self):
        print(self.ism)
        print(self.yosh)
        print(self.kurs)

a = Talaba("Ali", 20, 2)
a.sobr()
print("----------")
b = Talaba("Vali", 22, 3)
b.sobr()

# 3
class Telefon:
    def __init__(self, m, r, y):
        self.model = m
        self.rang = r
        self.yil = y

    def malumotlar(self):
        print(self.model, self.rang, self.yil)

a = Telefon("IPhone 13", "qora", 1200)
a.malumotlar()

b = Telefon("Samsung S21", "oq", 900)
b.malumotlar()

# 4
class Mashina:
    def __init__(self, m, r, y):
        self.marka = m
        self.rang = r
        self.yil = y

    def info(self):
        print(self.marka,self.rang,self.yil)

a = Mashina("Cobalt", "oq", 2022)
a.info()

b = Mashina("Malibu", "qora", 2023)
b.info()

# 5
class Xodim:
    def __init__(self, i, l, m):
        self.ism = i
        self.lovozim = l
        self.maosh = m

    def info(self):
        print(self.ism, self.lovozim, self.maosh)

a = Xodim("Ali", "Dasturchi", 1000)
a.info()

b = Xodim("Vali", "Manager", 1500)
b.info()

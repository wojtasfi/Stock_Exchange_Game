from random import randint

class Spolka():
    
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
        
    def display(self):
        przerwa = 7
        wciecie=0
        if len(self.nazwa) > przerwa:
            name = self.nazwa[:przerwa]
        elif len(self.nazwa) < przerwa:
            wciecie = przerwa - len(self.nazwa)
            name = self.nazwa
        
        return("%s%s| %.2f" % (name," " *wciecie,self.cena))
        
        
    def change_price(self):
        self.cena *= randint(5,15)/10
        
    def get_price(self):
        return self.cena
        

s1= Spolka("KGHM", 5.23)
s2= Spolka("LOTOS", 3.87)
s3= Spolka("APPLE", 7.02)
s4= Spolka("ORLEN", 42.56)
s5= Spolka("McDonald", 42.56)
s6= Spolka("KFC", 42.56)
s7= Spolka("Browar Amber", 42.56)
s8= Spolka("orlen", 42.56)
s9= Spolka("orlen", 42.56)


spolki =[s1,s2,s3,s4]
budzet = 1000
portfolio = {}
i=0



def pokaz_portfolio():
    przerwa = 5
    #test
    for spolka in portfolio:
        print(spolka.nazwa)
    #Czyszczenie portfolio z zer
    
    for spolka in list(portfolio):
        if portfolio.get(spolka)==0:
            del portfolio[spolka]
    
    print("Twoje portfolio")  
    print("-------------------------------")   
    print("Spółka | Cena | Sztuk | Wartość")  
    print("-------------------------------")       
    
    
    for spolka in portfolio:
        dl_slowa = len(spolka.nazwa)
        wciecie = przerwa - dl_slowa
            
        if wciecie < 0:
                wciecie = 0
                
        #Szukanie ceny dla zakupionej spółki
        for firma in spolki:
            if firma.nazwa == spolka.nazwa:
                    cena_spolki = firma.cena
            
                        
        print("%s%s    %.2f    %d     %.2f" % 
                (spolka.nazwa," " * wciecie, float(cena_spolki), int(portfolio.get(spolka)),float(cena_spolki)* float(portfolio.get(spolka))
               ))
    
    print("-------------------------------\n")
    
def pokaz_spolki():
    
    print("Dostępne spółki") 
    print("--------------")  
    print("Spółka | Cena")
    print("--------------")  
    for spolka in spolki:
        print("%s" % spolka.display())
                  
    print("--------------\n")  
    
def check_spolka(firma):
    for spolka in spolki:
        if firma == spolka.nazwa:
            return "valid"
        
def check_portfolio(firma):
    for spolka in portfolio:
        if firma == spolka.nazwa:
            return "valid"


print("Witaj w grze Gielda.")

koniec = ""
handel_koniec = ""


while koniec != "tak":
    handel_koniec = ""
    print("Twój budzet wynosi %.2f PLN.\n" % float(budzet))
    
    pokaz_spolki()
    
    while handel_koniec != "tak":
        k_s=""
        handel_koniec = ""
        while k_s != 'k' and  k_s != 's' and  k_s != 't':
            k_s = input("Kupno spółki (k)\nSprzedaż spółki (s)\nZakończenie tury(t)\nSprawdz portfolio "
            "(p)\nDodaj spółkę (d)\nUsuń spółkę (u)\n")
            
            if k_s =='p':
                pokaz_portfolio()
            
            #Dodawanie spółki    
            elif k_s == 'd':
                
                nazwa = input("Podaj nazwę spółki: ")
                
                koniec = "nie"
                while koniec != "tak":
                    cena = input("Podaj cenę początkową spółki (używaj kropki, a nie przecinka): ")
                    if ',' in cena:
                        print("Użyj kropki zamiast przecinka.")
                        continue
                    if isinstance(float(cena), float):
                        koniec ="tak"
                    elif isinstance(int(cena), int):
                        koniec ="tak"
                    else:
                        print("Wprowadz poprawną cenę.")
                
                spolka = Spolka(nazwa,float(cena))
                spolki.append(spolka)
                
                pokaz_spolki()
            
            #Usuwanie spółki    
            elif k_s == 'u':
                
                while koniec != "tak":
                    nazwa = input("Podaj nazwę spółki, którą chcesz usunąć: ")
                    
                    if not check_spolka(nazwa) == 'valid':
                        print("Wprowadz poprawną nazwę spółki.")
                    else:
                        koniec = "tak"
                
                for spolka in spolki:
                    if spolka.nazwa == nazwa:
                        spolki.remove(spolka)
            
                pokaz_spolki()
        if k_s == 't':
            handel_koniec ="tak"
        
        
        #Kupno
        elif k_s == 'k':
            zakup = input("Jaką spółkę chcesz kupić?")
            sztuki=""
            
            
            if not check_spolka(zakup) == "valid":
                print("Taka spółka nie istnieje")
                continue
            
            #Szukanie ceny dla zakupionej spółki
            for spolka in spolki:
                if spolka.nazwa == zakup:
                    cena_spolki = spolka.cena
                    
            while not sztuki.isnumeric():
                sztuki = input("Ile sztuk chcesz kupic spółki %s, której cena wynosi %.2f PLN? Pieniędzy starczy Ci na %d szt." % (zakup, cena_spolki, budzet/cena_spolki))
            
            
           
                    
            kwota = int(sztuki) * cena_spolki
            
            if budzet - kwota <0:
                print("Nie posiadasz wystarczająco środków.")
                continue
            else:
                budzet -= kwota
            
            
            #Szukanie odpowiedniego obiektu po nazwie zakupionej spółki
            
            for s in spolki:
                if s.nazwa == zakup:
                    portfolio.update({s:int(sztuki)})
            
            
            while handel_koniec != "tak" and handel_koniec != "nie":
                print("Kupiono %s sztuk spólki %s  za kwotę %.2f" % (str(sztuki), str(zakup),kwota) +" PLN.\n")
                
                pokaz_portfolio()
                handel_koniec = input("\nTwój budżet wynosi %.2f PLN. Czy chcesz zakończyć handel i przejść do kolejnej tury? [tak/nie]" % budzet)
        
        #Sprzedaz    
        elif k_s == 's':
            sztuki=""
            if not portfolio:
                print("Nie masz żadnych akcji.")    
                continue
               
            sprzedaz = input("Jaką spółkę chcesz sprzedac?")
            
            if not check_portfolio(sprzedaz) == "valid":
                print("Nie posiadasz takiej spółki w swoim portfolio lub taka spółka nie istnieje.")
                continue
            
            if not check_spolka(sprzedaz) == "valid":
                print("Taka spółka nie istnieje.")
                continue
            
            
            for spolka in spolki:
                if spolka.nazwa == sprzedaz:
                    cena_spolki = spolka.cena
                    nazwa_spolki = spolka.nazwa
            
            for spolka in portfolio:
                if spolka.nazwa == sprzedaz:
                    sprzedawana_spolka = spolka
           
             
            #Trzeba odnalezc liczbe sztuk jak jest przypisana do danego obiektu    
            while not sztuki.isnumeric():
                sztuki = input("Ile sztuk chcesz sprzedać spółki %s, której cena wynosi %.2f PLN? Posiadasz %d szt." % 
                               (sprzedaz,cena_spolki, portfolio.get(sprzedawana_spolka)))
            
            
            kwota = int(sztuki) * cena_spolki
            budzet += kwota
            
            
            if int(sztuki) > int(portfolio.get(sprzedawana_spolka)):
                print("Nie masz wystarczająco akcji spółki %s. Posiadasz %d akcji, a chcesz sprzedac %d." % (sprzedaz, portfolio.get(sprzedawana_spolka), int(sztuki)))
                continue
            
            portfolio.update({sprzedaz:(portfolio.get(sprzedawana_spolka) -int(sztuki))})
            
            
            while handel_koniec != "tak" and handel_koniec != "nie":
                print("Sprzedano %d sztuk spólki %s  za kwotę %.2f" % (int(sztuki), str(sprzedaz),float(kwota)) + " PLN.\n")
                pokaz_portfolio()
                
                
                handel_koniec = input("\nTwój budżet wynosi %.2f PLN. Czy chcesz zakończyć handel i przejść do kolejnej tury? [tak/nie]" % budzet)
                    
    
    print()
    print("************************************")        
    print("* Aktualizowanie cen giełdowych... *")
    print("************************************") 
    print()
    for spolka in spolki:
        spolka.change_price()
        #spolki.update({spolka: round(spolki[spolka]* (randint(5,15)/10),2) })
        


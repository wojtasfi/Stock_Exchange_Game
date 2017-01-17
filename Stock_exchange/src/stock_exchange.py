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
    
    print("Portfolio")  
    print("-------------------------------")   
    print("Company | Price | Number | USD")  
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
    
    print("  Companies   ") 
    print("--------------")  
    print("Name   | Price")
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


print("Stock Exchange.")

koniec = ""
handel_koniec = ""


while koniec != "tak":
    handel_koniec = ""
    print("Your budget: %.2f USD.\n" % float(budzet))
    
    pokaz_spolki()
    
    while handel_koniec != "tak":
        k_s=""
        handel_koniec = ""
        while k_s != 'k' and  k_s != 's' and  k_s != 't':
            k_s = input("Buy shares (k)\nSell shares (s)\nEnd of round(t)\nCheck portfolio "
            "(p)\nAdd company (d)\nDelete company (u)\n")
            
            if k_s =='p':
                pokaz_portfolio()
            
            #Dodawanie spółki    
            elif k_s == 'd':
                
                nazwa = input("Name of the company: ")
                
                koniec = "nie"
                while koniec != "tak":
                    cena = input("Name of the company (use dots): ")
                    if ',' in cena:
                        print("use '.'")
                        continue
                    if isinstance(float(cena), float):
                        koniec ="tak"
                    elif isinstance(int(cena), int):
                        koniec ="tak"
                    else:
                        print("Enter correct price.")
                
                spolka = Spolka(nazwa,float(cena))
                spolki.append(spolka)
                
                pokaz_spolki()
            
            #Usuwanie spółki    
            elif k_s == 'u':
                
                while koniec != "tak":
                    nazwa = input("Enter company name to delete: ")
                    
                    if not check_spolka(nazwa) == 'valid':
                        print("Enter correct company name.")
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
            zakup = input("Which comapny would you like to buy?")
            sztuki=""
            
            
            if not check_spolka(zakup) == "valid":
                print("This company does not exists.")
                continue
            
            #Szukanie ceny dla zakupionej spółki
            for spolka in spolki:
                if spolka.nazwa == zakup:
                    cena_spolki = spolka.cena
                    
            while not sztuki.isnumeric():
                sztuki = input("How many shares of %s, which price is %.2f USD? You can afford %d shares." % (zakup, cena_spolki, budzet/cena_spolki))
            
            
           
                    
            kwota = int(sztuki) * cena_spolki
            
            if budzet - kwota <0:
                print("You do not have enough money.")
                continue
            else:
                budzet -= kwota
            
            
            #Szukanie odpowiedniego obiektu po nazwie zakupionej spółki
            
            for s in spolki:
                if s.nazwa == zakup:
                    portfolio.update({s:int(sztuki)})
            
            
            while handel_koniec != "tak" and handel_koniec != "nie":
                print("You have bought %s shares of %s for %.2f" % (str(sztuki), str(zakup),kwota) +" USD.\n")
                
                pokaz_portfolio()
                handel_koniec = input("\nYour budget: %.2f USD. Would you like to end this round? [tak/nie]" % budzet)
        
        #Sprzedaz    
        elif k_s == 's':
            sztuki=""
            if not portfolio:
                print("There is no shares.")    
                continue
               
            sprzedaz = input("What company would you like to sell?")
            
            if not check_portfolio(sprzedaz) == "valid":
                print("You do not own shares of this company or the company does not exists.")
                continue
            
            if not check_spolka(sprzedaz) == "valid":
                print("This company does not exists.")
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
                sztuki = input("How many shares of %s would you like to sell, the price is %.2f USD? You own %d shares." % 
                               (sprzedaz,cena_spolki, portfolio.get(sprzedawana_spolka)))
            
            
            kwota = int(sztuki) * cena_spolki
            budzet += kwota
            
            
            if int(sztuki) > int(portfolio.get(sprzedawana_spolka)):
                print("You do not have enough shares of %s. You own %d shares, and you want to sell %d." % (sprzedaz, portfolio.get(sprzedawana_spolka), int(sztuki)))
                continue
            
            portfolio.update({sprzedaz:(portfolio.get(sprzedawana_spolka) -int(sztuki))})
            
            
            while handel_koniec != "tak" and handel_koniec != "nie":
                print("%d shares of %s have been sold for %.2f" % (int(sztuki), str(sprzedaz),float(kwota)) + " USD.\n")
                pokaz_portfolio()
                
                
                handel_koniec = input("\nYour budget: %.2f PLN. Would yo like to end this round? [tak/nie]" % budzet)
                    
    
    print()
    print("************************************")        
    print("*       Price actualization        *")
    print("************************************") 
    print()
    for spolka in spolki:
        spolka.change_price()
        #spolki.update({spolka: round(spolki[spolka]* (randint(5,15)/10),2) })
        


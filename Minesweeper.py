import random

class Tarla:
    d_tarla = []
    i_tarla = []
    boyut = 0
    mayın = 0
    
    def d_sor(self):
        return(int(input("dikey: "))-1)
        
    def y_sor(self):
        return(int(input("yatay: "))-1)
        
    def soru(self):
        konum = (self.d_sor() * self.boyut) + self.y_sor()
        return(konum)
        
    def dt_yap(self):
        for x in range(self.boyut**2):
            self.d_tarla.append("///")
            
    def it_yap(self):
        deger = []
        for x in range(self.mayın):
            deger.append(1)
        for x in range(self.boyut**2 - len(deger)):
            deger.append(0)
        random.shuffle(deger)
        self.i_tarla = deger
        
    def __init__(self,boyut,mayın):
        self.boyut = boyut
        self.mayın = mayın
        self.it_yap()
        self.dt_yap()

    def t_yaz(self,tarla):
        print()
        c = 0
        for x in tarla:
            c += 1
            print("|"+str(x)+"|",end = "")
            if c % self.boyut == 0:
                print()
                
    def bm_knt(self,konum1):
        t = self.i_tarla
        k = konum1
        konum = konum1 + 1
        boyut = self.boyut
        bom = 0
        if konum % boyut == 0 and konum != 0:
            if konum == boyut:
                bom = t[k-1] + t[k+boyut] + t[k+boyut-1]
            elif konum == boyut ** 2:
                bom = t[k-1] + t[k-boyut] + t[k-boyut-1]
            else:
                bom = t[k-1] + t[k-boyut] + t[k+boyut] + t[k+boyut-1] + t[k-boyut-1]        
        elif konum % boyut == 1 or konum == 0:
            if konum == 0:
                bom = t[k+1] + t[k+boyut] + t[k+boyut+1]
            elif konum == ((boyut**2) + 1) - boyut:
                bom = t[k+1] + t[k-boyut] + t[k-boyut+1]
            else:
                bom = t[k+1] + t[k+boyut] + t[k-boyut] + t[k+boyut+1] + t[k-boyut+1]     
        elif konum < boyut:
            bom = t[k+1] + t[k-1] + t[k + boyut] + t[k + boyut+1] + t[k + boyut-1]  
        elif ((boyut**2) + 1) - boyut < konum < boyut**2:
            bom = t[k-1] + t[k+1] + t[k-boyut] + t[k-boyut+1] + t[k-boyut-1]
        else:
            bom = t[k+1] + t[k-1] + t[k+boyut] + t[k-boyut] + t[k+boyut+1] + t[k+boyut-1] + t[k-boyut+1] + t[k-boyut-1]
        return(bom)
        
    def hamle(self,konum):
        t1 = self.i_tarla
        t2 = self.d_tarla
        if t1[konum]:
            return(False)
        else:
            t2[konum] = " " + str(self.bm_knt(konum)) + " "
            return(True)
            
    def g_yaz(self):
        print()
        c = 0
        for kare in self.i_tarla:
            c += 1
            if kare:
                print("|XXX|",end = "")
            else:
                print("|   |",end = "")
            if c % self.boyut == 0:
                print()
        
    def cal(self):
        say = 0
        while True:
            self.t_yaz(self.d_tarla)
            self.t_yaz(self.i_tarla)
            if self.hamle(self.soru()):
                say += 1
            else:
                print("\nkaybettin")
                break
            if say == self.boyut**2 - self.mayın:
                print("\nkazandın")
                break
        self.g_yaz()
        
        
boyut = int(input("boyut: "))
mayın = int(input("mayın sayısı: "))    
tarla = Tarla(boyut,mayın)
tarla.cal()
import random
import tkinter as tk
from tkinter import messagebox
from tkinter import font
import sys


class Tarla:
    d_tarla = []
    i_tarla = []
    m_tarla = []
    b_tarla = []
    boyut = 0
    mayın = 0
    sayac = 0
    renk0 = "royal blue"
    renk1 = "gainsboro"
    renk2 = "firebrick4"
    durum = 0
    def d_sor(self):
        return int(input("dikey: ")) - 1
        
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

    def mt_yap(self):
        c = 0
        tarla = self.m_tarla
        for kare in self.i_tarla:
            if  kare:
                tarla.append("XXX")
            else:
                tarla.append(self.bm_knt(c))
            c += 1
        print(tarla)
    def bayrak(self,menubar):
        if self.durum == 0:
            self.durum = 1
            menubar.entryconfig(menubar.index("bomb"),label = "flag")
        else:
            self.durum = 0
            menubar.entryconfig(menubar.index("flag"), label="bomb")

    def __init__(self,boyut,mayın,master):
        self.master = master
        self.boyut = boyut
        self.mayın = mayın
        self.it_yap()
        self.dt_yap()
        self.mt_yap()
        menubar = tk.Menu(master)
        menubar.add_command(label = "bomb")
        menubar.entryconfig(menubar.index("bomb"), command=lambda: self.bayrak(menubar))
        master.config(menu = menubar)
        for x in range(boyut):
            for y in range(boyut):
                buton = tk.Button(master,width = 5,height=2,bg = self.renk0)
                buton.grid(row = x,column = y)
                b = buton.grid_info()
                self.b_tarla.append([b["row"],b["column"]])
                buton["command"] = lambda r = b["row"], c = b["column"]:self.buton_hamle((r*boyut)+c,r,c)
        print(master.grid_slaves())

                
    def t_yaz(self,tarla):
        print()
        c = 0
        for x in tarla:
            c += 1
            print("|"+str(x)+"|",end = "")
            if c % self.boyut == 0:
                print()

    def bm_yer(self,konum):
        konum += 1
        if konum % boyut == 0 and konum != 1:
            if konum == boyut:
                return("sa_üst")
            elif konum == boyut**2:
                return("sa_alt")
            else:
                return("sa_orta")
        elif konum % boyut == 1 or konum == 1:
            if konum == 1:
                return("so_üst")
            elif konum == ((boyut**2) + 1) - boyut:
                return("so_alt")
            else:
                return("so_orta")
        elif konum < boyut:
            return("üst")
        elif ((boyut**2) + 1) - boyut < konum < boyut**2:
            return("alt")
        else:
            return("orta")
    
    def bm_knt(self,konum):
        t = self.i_tarla
        k = konum
        b = self.boyut 
        bom = 0
        if self.bm_yer(konum) == "sa_üst":
            bom = t[k-1] + t[k+b] + t[k+b-1]
        if self.bm_yer(konum) == "sa_alt":
            bom = t[k-1] + t[k-b] + t[k-b-1]
        if self.bm_yer(konum) == "sa_orta":
            bom = t[k-1] + t[k-b] + t[k+b] + t[k+b-1] + t[k-b-1]        
        if self.bm_yer(konum) == "so_üst":
            bom = t[k+1] + t[k+b] + t[k+b+1]
        if self.bm_yer(konum) == "so_alt":
            bom = t[k+1] + t[k-b] + t[k-b+1]
        if self.bm_yer(konum) == "so_orta":
            bom = t[k+1] + t[k+b] + t[k-b] + t[k+b+1] + t[k-b+1]     
        if self.bm_yer(konum) == "üst":
            bom = t[k+1] + t[k-1] + t[k + b] + t[k + b+1] + t[k + b-1]  
        if self.bm_yer(konum) == "alt": 
            bom = t[k-1] + t[k+1] + t[k-b] + t[k-b+1] + t[k-b-1]
        if self.bm_yer(konum) == "orta":
            bom = t[k+1] + t[k-1] + t[k+b] + t[k-b] + t[k+b+1] + t[k+b-1] + t[k-b+1] + t[k-b-1]
        return(bom)
    def b_yer(self,konum):
        l =[]
        liste = []
        k = konum
        b = self.boyut
        if self.bm_yer(konum) == "sa_üst":
            l.append(k-1)
            l.append(k+b)
            l.append(k+b-1)
        if self.bm_yer(konum) == "sa_alt":

            l.append(k-1)
            l.append(k-b)
            l.append(k-b-1)
        if self.bm_yer(konum) == "sa_orta":

            l.append(k-1)
            l.append(k-b)
            l.append(k+b)
            l.append(k+b-1)
            l.append(k-b-1)
        if self.bm_yer(konum) == "so_üst":

            l.append(k + 1)
            l.append(k + b)
            l.append(k + b + 1)
        if self.bm_yer(konum) == "so_alt":
            l.append(k+1)
            l.append(k-b)
            l.append(k - b + 1)
        if self.bm_yer(konum) == "so_orta":

            l.append(k + 1)
            l.append(k + b)
            l.append(k - b)
            l.append(k + b + 1)
            l.append(k - b + 1)
        if self.bm_yer(konum) == "üst":

            l.append(k + 1)
            l.append(k - 1)
            l.append(k + b)
            l.append(k + b+1)
            l.append(k + b-1)
        if self.bm_yer(konum) == "alt":
            l.append(k - 1)
            l.append(k + 1)
            l.append(k - b)
            l.append(k - b + 1)
            l.append(k - b - 1)
        if self.bm_yer(konum) == "orta":
            l.append(k+1)
            l.append(k - 1)
            l.append(k + b)
            l.append(k - b)
            l.append(k + b+1)
            l.append(k + b-1)
            l.append(k - b+1)
            l.append(k - b-1)
        for x in l:
            if self.d_tarla[x] == "///":
                liste.append(x)
        return(liste)

    def hamle(self,konum):
        t1 = self.i_tarla
        t2 = self.d_tarla
        if t1[konum]:
            return(False)
        else:
            t2[konum] = " " + str(self.bm_knt(konum)) + " "

            return(True)



    def tekrar(self):
        self.d_tarla = []
        self.i_tarla = []
        self.m_tarla = []
        self.b_tarla = []
        self.it_yap()
        self.dt_yap()
        self.mt_yap()
        self.sayac = 0
        for x in self.master.grid_slaves():
            x.destroy()
        for x in range(boyut):
            for y in range(boyut):
                buton = tk.Button(self.master,width = 5,height=2,bg = self.renk0)
                buton.grid(row = x,column = y)
                b = buton.grid_info()
                self.b_tarla.append([b["row"],b["column"]])
                buton["command"] = lambda r = b["row"], c = b["column"]:self.buton_hamle((r*boyut)+c,r,c)

    def say(self):
        self.sayac = 0
        for x in self.d_tarla:
            if x != "///":
                self.sayac += 1

    def b_hamle(self,konum,row,column):
        knt = 0
        if self.hamle(konum):
            bm = self.bm_knt(konum)
            if  bm == 0:
                knt = " "
            else:
                knt = bm
            tk.Label(self.master,text = knt,width = 5,height=2,bg = self.renk1,padx = 2,pady = 2).grid(row = row,column = column)
            self.say()
            if self.sayac == self.boyut**2 - self.mayın:
                if messagebox.askretrycancel("","Victory"):
                    self.tekrar()
                else:
                    sys.exit()
        else:
            tk.Label(self.master,text = "XXX",width = 5,height=2,bg = self.renk2,padx = 2,pady = 2).grid(row = row,column = column)
            if messagebox.askretrycancel("","Defeat"):
                self.tekrar()
            else:
                sys.exit()

    def buton_hamle(self,konum,row,column):
        if self.durum == 0:
            hamle = self.hamle(konum)
            t = self.b_tarla
            if not self.i_tarla[konum]:
                if self.bm_knt(konum) == 0:
                    self.b_hamle(konum,row,column)
                    for x in self.b_yer(konum):
                        self.buton_hamle(x, t[x][0], t[x][1])
                else:
                    self.b_hamle(konum,row,column)
            else:
                self.b_hamle(konum,row,column)
        else:
            l = master.grid_slaves(row = row,column = column)
            if l[0]["text"] =="XXXXX":
                l[0].configure(text="")
            else:
                l[0].configure(text = "XXXXX",fg = "red3",font =font.Font(size =9,weight = "bold"))

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
        
master = tk.Tk()
master.title("Minesweeper")
boyut = int(input("boyut: "))
mayın = int(input("mayın sayısı: "))
tarla = Tarla(boyut,mayın,master)


master.mainloop()
while True:
    if input("tekrar"):
        tarla.tekrar()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

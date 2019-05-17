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
    renk2 = "firebrick3"
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

    def ayar(self):
        tplvl = tk.Toplevel()
        self.toplevel = tplvl
        tplvl.protocol("WM_DELETE_WINDOW", tplvl.withdraw)
        l1 = tk.Label(tplvl, text="size")
        l1.grid(row=0, column=0)
        e1 = tk.Entry(tplvl, width=10)
        e1.grid(row=0, column=1)
        l2 = tk.Label(tplvl, text="mines")
        l2.grid(row=1, column=0)
        e2 = tk.Entry(tplvl, width=10)
        e2.grid(row=1, column=1)
        b1 = tk.Button(tplvl, text="confirm", width=10, command=lambda: self.confirm(e1, e2, tplvl))
        b1.grid(row=2, column=0)
        b2 = tk.Button(tplvl, text="cancel", width=10, command=lambda: self.cancel(tplvl))
        b2.grid(row=2, column=1)
        tplvl.mainloop()

    def __init__(self,master):
        self.master = master
        self.ayar()

    def confirm(self,e1,e2,toplevel):
        b = e1.get()
        m = e2.get()
        print(b, m)
        if int(b) != 0 and int(m) != 0:
            self.boyut = int(b)
            self.mayın = int(m)
            self.tekrar()
            toplevel.withdraw()

    def cancel(self,toplevel):
        toplevel.withdraw()

    def bayrak(self,event,row,column):
        if self.d_tarla[row*self.boyut + column] == "///":
            l = self.master.grid_slaves(row=row, column=column)
            if l[0]["text"] == "XXXXX":
                l[0].configure(text="")
            else:
                l[0].configure(text="XXXXX", fg="red3", font=font.Font(size=9, weight="bold"))
                
    def t_yaz(self,tarla):
        print()
        c = 0
        for x in tarla:
            c += 1
            print("|"+str(x)+"|",end = "")
            if c % self.boyut == 0:
                print()

    def bm_yer(self,konum):
        boyut = self.boyut
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
        menubar = tk.Menu(self.master)
        menubar.add_command(label="options", command=lambda: self.toplevel.deiconify())
        menubar.add_command(label="retry", command=lambda: self.tekrar())
        self.master.config(menu=menubar)
        self.sayac = 0
        for x in self.master.grid_slaves():
            x.destroy()

        for x in range(self.boyut):
            for y in range(self.boyut):
                buton = tk.Button(self.master,width = 5,height=2,bg = self.renk0)
                buton.grid(row = x,column = y)
                b = buton.grid_info()
                self.b_tarla.append([b["row"],b["column"]])
                buton["command"] = lambda r = b["row"], c = b["column"]:self.buton_hamle((r*self.boyut)+c,r,c)
                buton.bind(sequence ="<Button-3>",func=lambda event,r = b["row"], c = b["column"]:self.bayrak(event,r,c))
        print(self.master.grid_slaves())

    def say(self):
        self.sayac = 0
        for x in self.d_tarla:
            if x != "///":
                self.sayac += 1

    def b_hamle(self,konum,row,column):
        knt = 0
        renk = ""
        if self.hamle(konum):
            bm = self.bm_knt(konum)
            if  bm == 0:
                renk ="black"
                knt = " "
            elif bm == 1:
                knt = bm
                renk = "medium blue"
            elif bm == 2:
                knt = bm
                renk = "dark green"
            elif bm == 3:
                knt = bm
                renk = "red4"
            else:
                renk ="black"
                knt = bm
            tk.Label(self.master,text = knt,width = 5,height=2,bg = self.renk1,padx = 2,pady = 2,fg =renk,font = font.Font(size = 9,weight ="bold")).grid(row = row,column = column)
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

class Ayarlar:
    def __init__(self,tarla,master):
        self.master = master
        self.tarla = tarla
        tplvl = tk.Toplevel()
        tplvl.protocol("WM_DELETE_WINDOW",tplvl.withdraw)
        l1 = tk.Label(tplvl,text="size")
        l1.grid(row = 0,column = 0)
        e1 = tk.Entry(tplvl,width = 10)
        e1.grid(row = 0,column = 1)
        l2 = tk.Label(tplvl,text="mines")
        l2.grid(row = 1,column = 0)
        e2 = tk.Entry(tplvl,width = 10)
        e2.grid(row = 1,column = 1)
        b1 = tk.Button(tplvl,text = "confirm",width = 10,command = lambda:self.confirm(e1,e2,tplvl))
        b1.grid(row = 2,column = 0)
        b2 = tk.Button(tplvl,text = "cancel",width = 10,command = lambda:self.cancel(tplvl))
        b2.grid(row = 2,column = 1)
        tplvl.mainloop()

    def confirm(self,e1,e2,toplevel):
        b = e1.get()
        m = e2.get()
        print(b,m)
        if  int(b) != 0 and int(m) != 0:
            self.tarla.tekrar(int(b),int(m))
            toplevel.withdraw()

    def cancel(self,toplevel):
        toplevel.withdraw()

master = tk.Tk()
master.title("Minesweeper")
tarla = Tarla(master)
master.mainloop()


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
